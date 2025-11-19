"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Create a "Load Replay" feature for a locally hosted multiplayer FPS game, inspired by ev.io's replay functionality.
Generated: DETERMINISTIC_9d5a21aba6b1615b
Batch ID: 20250612_151354
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
import struct
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional

class ReplayManager:
    """
    Handles recording and loading of game replays.
    Replays are stored as binary files with a JSON header.
    """
    
    REPLAY_DIR = "replays"
    REPLAY_EXTENSION = ".evr"
    HEADER_MAGIC = b"EVREPLAY"
    VERSION = 1
    
    def __init__(self):
        self._ensure_replay_dir()
        self.current_replay = None
        self.replay_metadata = {}
    
    def _ensure_replay_dir(self) -> None:
        """Ensure the replay directory exists."""
        Path(self.REPLAY_DIR).mkdir(parents=True, exist_ok=True)
    
    def list_replays(self) -> List[Dict]:
        """List all available replays with metadata."""
        replays = []
        for file in Path(self.REPLAY_DIR).glob(f"*{self.REPLAY_EXTENSION}"):
            try:
                with open(file, 'rb') as f:
                    header = self._read_header(f)
                    replays.append({
                        'filename': file.name,
                        'path': str(file),
                        'timestamp': header['timestamp'],
                        'duration': header['duration'],
                        'map_name': header['map_name'],
                        'player_count': header['player_count']
                    })
            except Exception as e:
                print(f"Error reading replay {file}: {e}")
        return sorted(replays, key=lambda x: x['timestamp'], reverse=True)
    
    def _read_header(self, file) -> Dict:
        """Read and validate the replay header."""
        magic = file.read(len(self.HEADER_MAGIC))
        if magic != self.HEADER_MAGIC:
            raise ValueError("Invalid replay file format")
        
        version = struct.unpack('B', file.read(1))[0]
        if version != self.VERSION:
            raise ValueError(f"Unsupported replay version: {version}")
        
        header_size = struct.unpack('I', file.read(4))[0]
        header_data = file.read(header_size)
        return json.loads(header_data.decode('utf-8'))
    
    def load_replay(self, replay_path: str) -> Dict:
        """
        Load a replay file and prepare it for playback.
        Returns a dict with header data and a generator for frame data.
        """
        try:
            with open(replay_path, 'rb') as f:
                header = self._read_header(f)
                
                def frame_generator():
                    while True:
                        frame_size_bytes = f.read(4)
                        if not frame_size_bytes:
                            break
                        frame_size = struct.unpack('I', frame_size_bytes)[0]
                        frame_data = f.read(frame_size)
                        yield frame_data
                
                return {
                    'header': header,
                    'frames': frame_generator(),
                    'frame_count': header.get('frame_count', 0)
                }
        except Exception as e:
            raise RuntimeError(f"Failed to load replay: {e}") from e
    
    def start_playback(self, replay_data: Dict) -> None:
        """Begin replay playback with the loaded data."""
        self.current_replay = {
            'data': replay_data,
            'current_frame': 0,
            'start_time': time.time(),
            'playback_speed': 1.0
        }
    
    def get_next_frame(self) -> Optional[bytes]:
        """Get the next frame of the replay based on playback timing."""
        if not self.current_replay:
            return None
            
        replay = self.current_replay
        elapsed = (time.time() - replay['start_time']) * replay['playback_speed']
        expected_frame = int(elapsed * replay['data']['header']['fps'])
        
        if expected_frame >= replay['data']['frame_count']:
            return None
        
        if expected_frame > replay['current_frame']:
            try:
                for _ in range(replay['current_frame'], expected_frame):
                    frame = next(replay['data']['frames'])
                replay['current_frame'] = expected_frame
                return frame
            except StopIteration:
                return None
        return None
    
    def stop_playback(self) -> None:
        """Stop current replay playback."""
        self.current_replay = None
    
    def set_playback_speed(self, speed: float) -> None:
        """Adjust playback speed (0.5 for half speed, 2.0 for double speed, etc.)."""
        if self.current_replay:
            # Adjust start time to maintain smooth transition
            now = time.time()
            elapsed = (now - self.current_replay['start_time']) * self.current_replay['playback_speed']
            self.current_replay['start_time'] = now - elapsed / speed
            self.current_replay['playback_speed'] = speed
    
    def record_replay(self, map_name: str, player_count: int, fps: int = 60) -> None:
        """Initialize a new replay recording session."""
        timestamp = datetime.now().isoformat()
        filename = f"{timestamp.replace(':', '-')}{self.REPLAY_EXTENSION}"
        self.replay_metadata = {
            'timestamp': timestamp,
            'map_name': map_name,
            'player_count': player_count,
            'fps': fps,
            'frame_count': 0,
            'duration': 0.0
        }
        self.recording_file = open(Path(self.REPLAY_DIR) / filename, 'wb')
        
        # Write header placeholder (will be updated when recording stops)
        self.recording_file.write(self.HEADER_MAGIC)
        self.recording_file.write(struct.pack('B', self.VERSION))
        self.recording_file.write(struct.pack('I', 0))  # Placeholder for header size
        self.header_position = self.recording_file.tell()
    
    def add_frame(self, frame_data: bytes) -> None:
        """Add a frame to the current recording."""
        if not hasattr(self, 'recording_file'):
            return
            
        frame_size = len(frame_data)
        self.recording_file.write(struct.pack('I', frame_size))
        self.recording_file.write(frame_data)
        self.replay_metadata['frame_count'] += 1
        self.replay_metadata['duration'] = self.replay_metadata['frame_count'] / self.replay_metadata['fps']
    
    def stop_recording(self) -> None:
        """Finalize the current recording and write proper header."""
        if not hasattr(self, 'recording_file'):
            return
            
        # Go back and write the actual header
        header_data = json.dumps(self.replay_metadata).encode('utf-8')
        header_size = len(header_data)
        
        self.recording_file.seek(len(self.HEADER_MAGIC) + 1)  # Skip magic and version
        self.recording_file.write(struct.pack('I', header_size))
        self.recording_file.seek(self.header_position)
        self.recording_file.write(header_data)
        
        self.recording_file.close()
        del self.recording_file
        del self.replay_metadata
```
