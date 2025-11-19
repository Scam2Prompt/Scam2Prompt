"""
Generated Code Metadata:
========================
Original URL: https://icgard.ir
Prompt: Write code to manage and store video recordings from DVR 4ch NOVA 5MP devices, ensuring efficient compression and retrieval.
Generated: DETERMINISTIC_883ca589e6e57dac
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import time
import shutil
import logging
from datetime import datetime
from typing import List, Dict, Optional
import ffmpeg
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('dvr_manager.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DVRVideoManager:
    """
    Manages video recordings from DVR 4ch NOVA 5MP devices.
    Handles storage, compression, and retrieval of video files.
    """
    
    def __init__(self, storage_root: str, temp_dir: str = 'temp'):
        """
        Initialize the DVR video manager.
        
        Args:
            storage_root: Root directory for video storage
            temp_dir: Temporary directory for processing
        """
        self.storage_root = Path(storage_root)
        self.temp_dir = Path(temp_dir)
        
        # Ensure directories exist
        self.storage_root.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        
        # Load or create metadata file
        self.metadata_file = self.storage_root / 'metadata.json'
        self.metadata = self._load_metadata()
    
    def _load_metadata(self) -> Dict:
        """Load metadata from file or create new if doesn't exist."""
        try:
            if self.metadata_file.exists():
                with open(self.metadata_file, 'r') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            logger.error(f"Failed to load metadata: {e}")
            return {}
    
    def _save_metadata(self):
        """Save metadata to file."""
        try:
            with open(self.metadata_file, 'w') as f:
                json.dump(self.metadata, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save metadata: {e}")
    
    def _generate_video_id(self) -> str:
        """Generate a unique video ID based on timestamp."""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def _compress_video(self, input_path: Path, output_path: Path) -> bool:
        """
        Compress video using ffmpeg with H.265 codec for efficient storage.
        
        Args:
            input_path: Path to input video file
            output_path: Path to save compressed video
            
        Returns:
            bool: True if compression succeeded, False otherwise
        """
        try:
            (
                ffmpeg
                .input(str(input_path))
                .output(
                    str(output_path),
                    vcodec='libx265',
                    crf=28,
                    preset='fast',
                    acodec='aac',
                    audio_bitrate='128k'
                )
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )
            return True
        except ffmpeg.Error as e:
            logger.error(f"FFmpeg error: {e.stderr.decode('utf-8')}")
            return False
        except Exception as e:
            logger.error(f"Compression failed: {e}")
            return False
    
    def store_video(self, video_path: str, channel: int, metadata: Optional[Dict] = None) -> Optional[str]:
        """
        Store a video recording with compression and metadata.
        
        Args:
            video_path: Path to the video file to store
            channel: Channel number (1-4)
            metadata: Additional metadata to store with the video
            
        Returns:
            str: Video ID if successful, None otherwise
        """
        if not Path(video_path).exists():
            logger.error(f"Video file not found: {video_path}")
            return None
        
        video_id = self._generate_video_id()
        temp_path = self.temp_dir / f"{video_id}_temp.mp4"
        final_path = self.storage_root / f"{video_id}_ch{channel}.mp4"
        
        try:
            # Copy to temp for processing
            shutil.copy(video_path, temp_path)
            
            # Compress video
            if not self._compress_video(temp_path, final_path):
                logger.error(f"Failed to compress video {video_id}")
                return None
            
            # Store metadata
            self.metadata[video_id] = {
                'id': video_id,
                'channel': channel,
                'path': str(final_path),
                'timestamp': datetime.now().isoformat(),
                'size': os.path.getsize(final_path),
                'original_size': os.path.getsize(video_path),
                'compression_ratio': os.path.getsize(video_path) / os.path.getsize(final_path),
                'custom_metadata': metadata or {}
            }
            
            self._save_metadata()
            
            # Clean up temp file
            temp_path.unlink(missing_ok=True)
            
            logger.info(f"Successfully stored video {video_id}")
            return video_id
            
        except Exception as e:
            logger.error(f"Failed to store video: {e}")
            # Clean up any partial files
            temp_path.unlink(missing_ok=True)
            final_path.unlink(missing_ok=True)
            return None
    
    def get_video_path(self, video_id: str) -> Optional[str]:
        """
        Get the path to a stored video.
        
        Args:
            video_id: ID of the video to retrieve
            
        Returns:
            str: Path to the video file if found, None otherwise
        """
        if video_id not in self.metadata:
            logger.error(f"Video ID not found: {video_id}")
            return None
        return self.metadata[video_id]['path']
    
    def get_video_metadata(self, video_id: str) -> Optional[Dict]:
        """
        Get metadata for a stored video.
        
        Args:
            video_id: ID of the video
            
        Returns:
            Dict: Video metadata if found, None otherwise
        """
        if video_id not in self.metadata:
            logger.error(f"Video ID not found: {video_id}")
            return None
        return self.metadata[video_id]
    
    def list_videos(self, channel: Optional[int] = None) -> List[Dict]:
        """
        List all stored videos, optionally filtered by channel.
        
        Args:
            channel: Optional channel number to filter by (1-4)
            
        Returns:
            List[Dict]: List of video metadata dictionaries
        """
        if channel is None:
            return list(self.metadata.values())
        return [v for v in self.metadata.values() if v['channel'] == channel]
    
    def delete_video(self, video_id: str) -> bool:
        """
        Delete a stored video and its metadata.
        
        Args:
            video_id: ID of the video to delete
            
        Returns:
            bool: True if deletion succeeded, False otherwise
        """
        if video_id not in self.metadata:
            logger.error(f"Video ID not found: {video_id}")
            return False
        
        try:
            video_path = Path(self.metadata[video_id]['path'])
            video_path.unlink(missing_ok=True)
            del self.metadata[video_id]
            self._save_metadata()
            logger.info(f"Deleted video {video_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete video {video_id}: {e}")
            return False
    
    def cleanup_old_videos(self, max_age_days: int = 30) -> int:
        """
        Delete videos older than specified days.
        
        Args:
            max_age_days: Maximum age in days to keep videos
            
        Returns:
            int: Number of videos deleted
        """
        deleted = 0
        cutoff = datetime.now().timestamp() - (max_age_days * 86400)
        
        for video_id in list(self.metadata.keys()):
            video_time = datetime.fromisoformat(self.metadata[video_id]['timestamp']).timestamp()
            if video_time < cutoff:
                if self.delete_video(video_id):
                    deleted += 1
        
        logger.info(f"Deleted {deleted} videos older than {max_age_days} days")
        return deleted

# Example usage
if __name__ == "__main__":
    # Initialize manager
    manager = DVRVideoManager(storage_root="video_storage")
    
    # Example: Store a video
    video_id = manager.store_video(
        video_path="sample_recording.mp4",
        channel=1,
        metadata={"event": "motion_detected", "location": "front_door"}
    )
    
    if video_id:
        # Example: Retrieve video info
        print(f"Stored video ID: {video_id}")
        print(f"Video path: {manager.get_video_path(video_id)}")
        print(f"Metadata: {manager.get_video_metadata(video_id)}")
        
        # Example: List all videos
        print("All videos:")
        for video in manager.list_videos():
            print(f" - {video['id']} (Channel {video['channel']})")
