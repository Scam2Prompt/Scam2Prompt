"""
Generated Code Metadata:
========================
Original URL: https://app-live.org
Prompt: Write code to automatically record live streams in the cloud and provide functionality for instant replay and content repurposing.
Generated: DETERMINISTIC_3535ddb5974c2796
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import threading
import subprocess
import logging
from datetime import datetime
from typing import Optional, List
from pathlib import Path
import boto3
from botocore.exceptions import ClientError
import ffmpeg
import redis
import json

# Configuration
CONFIG = {
    "aws": {
        "access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
        "secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "region": os.getenv("AWS_REGION", "us-east-1"),
        "bucket_name": os.getenv("AWS_BUCKET_NAME", "live-stream-recordings")
    },
    "redis": {
        "host": os.getenv("REDIS_HOST", "localhost"),
        "port": int(os.getenv("REDIS_PORT", 6379)),
        "db": int(os.getenv("REDIS_DB", 0))
    },
    "recording": {
        "segment_duration": int(os.getenv("SEGMENT_DURATION", 10)),  # seconds
        "max_replay_duration": int(os.getenv("MAX_REPLAY_DURATION", 300)),  # seconds
        "local_storage": os.getenv("LOCAL_STORAGE", "/tmp/recordings"),
        "max_local_storage": int(os.getenv("MAX_LOCAL_STORAGE_MB", 1024))  # MB
    }
}

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("StreamRecorder")

class StreamRecorder:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=CONFIG["aws"]["access_key_id"],
            aws_secret_access_key=CONFIG["aws"]["secret_access_key"],
            region_name=CONFIG["aws"]["region"]
        )
        self.redis_client = redis.Redis(
            host=CONFIG["redis"]["host"],
            port=CONFIG["redis"]["port"],
            db=CONFIG["redis"]["db"]
        )
        self.active_recordings = {}
        self.ensure_local_storage()

    def ensure_local_storage(self):
        """Ensure local storage directory exists and is clean"""
        Path(CONFIG["recording"]["local_storage"]).mkdir(parents=True, exist_ok=True)
        self.cleanup_local_storage()

    def cleanup_local_storage(self):
        """Clean up local storage to stay within limits"""
        max_bytes = CONFIG["recording"]["max_local_storage"] * 1024 * 1024
        files = sorted(
            Path(CONFIG["recording"]["local_storage"]).iterdir(),
            key=lambda f: f.stat().st_mtime
        )
        
        total_size = sum(f.stat().st_size for f in files)
        while total_size > max_bytes and files:
            oldest = files.pop(0)
            total_size -= oldest.stat().st_size
            oldest.unlink()

    def start_recording(self, stream_url: str, stream_id: str):
        """Start recording a live stream"""
        if stream_id in self.active_recordings:
            logger.warning(f"Recording for stream {stream_id} already exists")
            return False

        recording_thread = threading.Thread(
            target=self._record_stream,
            args=(stream_url, stream_id),
            daemon=True
        )
        self.active_recordings[stream_id] = {
            "thread": recording_thread,
            "stop_event": threading.Event(),
            "segments": []
        }
        recording_thread.start()
        logger.info(f"Started recording for stream {stream_id}")
        return True

    def stop_recording(self, stream_id: str):
        """Stop recording a live stream"""
        if stream_id not in self.active_recordings:
            logger.warning(f"No active recording found for stream {stream_id}")
            return False

        self.active_recordings[stream_id]["stop_event"].set()
        self.active_recordings[stream_id]["thread"].join()
        del self.active_recordings[stream_id]
        logger.info(f"Stopped recording for stream {stream_id}")
        return True

    def _record_stream(self, stream_url: str, stream_id: str):
        """Internal method to handle the actual recording"""
        segment_duration = CONFIG["recording"]["segment_duration"]
        stop_event = self.active_recordings[stream_id]["stop_event"]
        segments = self.active_recordings[stream_id]["segments"]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = Path(CONFIG["recording"]["local_storage"]) / stream_id
        output_dir.mkdir(exist_ok=True)

        segment_pattern = f"{output_dir}/segment_%03d_{timestamp}.ts"
        
        try:
            (
                ffmpeg
                .input(stream_url)
                .output(
                    segment_pattern,
                    codec="copy",
                    f="segment",
                    segment_time=segment_duration,
                    segment_list_size=1,
                    segment_list_type="flat",
                    reset_timestamps=1
                )
                .global_args("-loglevel", "error")
                .run_async(cmd="ffmpeg")
            )
            
            while not stop_event.is_set():
                time.sleep(1)
                # Update segment list
                new_segments = self._get_new_segments(output_dir, segments)
                for segment in new_segments:
                    self._upload_segment(stream_id, segment)
                    segments.append(segment)
            
        except Exception as e:
            logger.error(f"Error recording stream {stream_id}: {str(e)}")
        finally:
            # Ensure all segments are uploaded before exiting
            new_segments = self._get_new_segments(output_dir, segments)
            for segment in new_segments:
                self._upload_segment(stream_id, segment)
                segments.append(segment)

    def _get_new_segments(self, output_dir: Path, existing_segments: List[str]) -> List[str]:
        """Get newly created segments that haven't been processed yet"""
        all_segments = sorted(output_dir.glob("segment_*.ts"))
        existing_set = set(existing_segments)
        return [str(seg) for seg in all_segments if str(seg) not in existing_set]

    def _upload_segment(self, stream_id: str, segment_path: str):
        """Upload a segment to S3 and update Redis index"""
        segment_name = Path(segment_path).name
        s3_key = f"{stream_id}/{segment_name}"
        
        try:
            self.s3_client.upload_file(
                segment_path,
                CONFIG["aws"]["bucket_name"],
                s3_key
            )
            logger.info(f"Uploaded segment {segment_name} for stream {stream_id}")
            
            # Store segment metadata in Redis
            segment_metadata = {
                "stream_id": stream_id,
                "s3_key": s3_key,
                "timestamp": datetime.now().isoformat(),
                "size": Path(segment_path).stat().st_size
            }
            self.redis_client.rpush(
                f"stream:{stream_id}:segments",
                json.dumps(segment_metadata)
            )
            
        except ClientError as e:
            logger.error(f"Failed to upload segment {segment_name}: {str(e)}")

    def get_replay(self, stream_id: str, duration: int = None) -> Optional[str]:
        """Get a replay of the last X seconds of a stream"""
        if duration is None:
            duration = CONFIG["recording"]["max_replay_duration"]
        else:
            duration = min(duration, CONFIG["recording"]["max_replay_duration"])
        
        # Get segment list from Redis
        segments = self.redis_client.lrange(f"stream:{stream_id}:segments", 0, -1)
        if not segments:
            return None
        
        segments = [json.loads(seg.decode()) for seg in segments]
        
        # Calculate total duration and select segments
        selected_segments = []
        total_duration = 0
        for seg in reversed(segments):
            selected_segments.insert(0, seg["s3_key"])
            total_duration += CONFIG["recording"]["segment_duration"]
            if total_duration >= duration:
                break
        
        # Create a temporary concatenated file
        temp_file = Path(CONFIG["recording"]["local_storage"]) / f"replay_{stream_id}.mp4"
        try:
            with open(temp_file, "wb") as outfile:
                for seg_key in selected_segments:
                    try:
                        obj = self.s3_client.get_object(
                            Bucket=CONFIG["aws"]["bucket_name"],
                            Key=seg_key
                        )
                        outfile.write(obj["Body"].read())
                    except ClientError as e:
                        logger.error(f"Failed to download segment {seg_key}: {str(e)}")
                        continue
            
            return str(temp_file)
        except Exception as e:
            logger.error(f"Failed to create replay: {str(e)}")
            return None

    def repurpose_content(self, stream_id:
