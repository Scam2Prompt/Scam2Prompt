"""
Generated Code Metadata:
========================
Original URL: https://hianime.baby
Prompt: Write code to implement offline viewing capabilities for an anime streaming app, inspired by HiAnime's download feature.
Generated: DETERMINISTIC_a6af7d4db6ab8b40
Batch ID: 20250612_153256
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
import sqlite3
import requests
from pathlib import Path
from typing import Optional, List, Dict, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

class OfflineAnimeManager:
    """
    A class to manage offline viewing capabilities for an anime streaming app.
    Handles downloading, storing, and retrieving anime episodes for offline viewing.
    """
    
    def __init__(self, storage_dir: str = "offline_anime"):
        """
        Initialize the OfflineAnimeManager with a storage directory.
        
        Args:
            storage_dir (str): Directory to store downloaded anime files and database.
                             Defaults to "offline_anime".
        """
        self.storage_dir = Path(storage_dir)
        self.db_path = self.storage_dir / "anime_database.db"
        
        # Create storage directory if it doesn't exist
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize database
        self._init_db()
    
    def _init_db(self) -> None:
        """Initialize the SQLite database for tracking downloaded anime."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create tables if they don't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS anime (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    anime_id TEXT NOT NULL UNIQUE,
                    title TEXT NOT NULL,
                    cover_url TEXT,
                    last_updated TEXT
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS episodes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    anime_id TEXT NOT NULL,
                    episode_id TEXT NOT NULL UNIQUE,
                    title TEXT NOT NULL,
                    duration INTEGER,
                    file_path TEXT NOT NULL,
                    download_date TEXT NOT NULL,
                    FOREIGN KEY (anime_id) REFERENCES anime (anime_id)
                )
            """)
            
            conn.commit()
    
    def add_anime_metadata(self, anime_id: str, title: str, cover_url: str) -> None:
        """
        Add or update anime metadata in the database.
        
        Args:
            anime_id (str): Unique identifier for the anime
            title (str): Title of the anime
            cover_url (str): URL to the anime cover image
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT OR REPLACE INTO anime (anime_id, title, cover_url, last_updated)
                VALUES (?, ?, ?, datetime('now'))
            """, (anime_id, title, cover_url))
            
            conn.commit()
    
    def get_downloaded_anime(self) -> List[Dict]:
        """
        Retrieve a list of all downloaded anime with their metadata.
        
        Returns:
            List[Dict]: List of dictionaries containing anime metadata
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM anime ORDER BY title")
            return [dict(row) for row in cursor.fetchall()]
    
    def get_episodes_for_anime(self, anime_id: str) -> List[Dict]:
        """
        Retrieve all downloaded episodes for a specific anime.
        
        Args:
            anime_id (str): ID of the anime to get episodes for
            
        Returns:
            List[Dict]: List of dictionaries containing episode information
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM episodes 
                WHERE anime_id = ?
                ORDER BY CAST(episode_id AS INTEGER)
            """, (anime_id,))
            
            return [dict(row) for row in cursor.fetchall()]
    
    def is_episode_downloaded(self, episode_id: str) -> bool:
        """
        Check if an episode is already downloaded.
        
        Args:
            episode_id (str): ID of the episode to check
            
        Returns:
            bool: True if episode is downloaded, False otherwise
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT 1 FROM episodes 
                WHERE episode_id = ?
                LIMIT 1
            """, (episode_id,))
            
            return cursor.fetchone() is not None
    
    def download_episode(
        self,
        anime_id: str,
        episode_id: str,
        title: str,
        video_url: str,
        duration: Optional[int] = None,
        max_workers: int = 3
    ) -> Tuple[bool, str]:
        """
        Download an anime episode for offline viewing.
        
        Args:
            anime_id (str): ID of the anime
            episode_id (str): ID of the episode
            title (str): Title of the episode
            video_url (str): URL to download the video from
            duration (Optional[int]): Duration of the episode in seconds
            max_workers (int): Number of parallel download threads
            
        Returns:
            Tuple[bool, str]: (success status, message)
        """
        # Check if already downloaded
        if self.is_episode_downloaded(episode_id):
            return (False, "Episode already downloaded")
        
        # Create anime directory if it doesn't exist
        anime_dir = self.storage_dir / anime_id
        anime_dir.mkdir(exist_ok=True)
        
        # Generate filename and path
        filename = f"{episode_id}.mp4"
        file_path = anime_dir / filename
        
        try:
            # Download the video file
            self._download_file(video_url, file_path, max_workers)
            
            # Add to database
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    INSERT INTO episodes (
                        anime_id, episode_id, title, duration, file_path, download_date
                    ) VALUES (?, ?, ?, ?, ?, datetime('now'))
                """, (anime_id, episode_id, title, duration, str(file_path)))
                
                conn.commit()
            
            return (True, "Download completed successfully")
        
        except Exception as e:
            # Clean up partially downloaded file if it exists
            if file_path.exists():
                file_path.unlink()
            
            return (False, f"Download failed: {str(e)}")
    
    def _download_file(self, url: str, file_path: Path, max_workers: int = 3) -> None:
        """
        Download a file using multiple threads for better performance.
        
        Args:
            url (str): URL to download from
            file_path (Path): Path to save the file to
            max_workers (int): Number of parallel download threads
        """
        # Get file size first
        response = requests.head(url, allow_redirects=True)
        response.raise_for_status()
        
        file_size = int(response.headers.get('content-length', 0))
        chunk_size = 1024 * 1024  # 1MB chunks
        
        # Single thread for small files
        if file_size < 5 * 1024 * 1024:  # <5MB
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        f.write(chunk)
            return
        
        # Multi-threaded download for larger files
        ranges = []
        for i in range(max_workers):
            start = i * (file_size // max_workers)
            end = (i + 1) * (file_size // max_workers) - 1 if i < max_workers - 1 else file_size - 1
            ranges.append((start, end))
        
        temp_files = []
        try:
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = []
                for i, (start, end) in enumerate(ranges):
                    temp_file = file_path.with_suffix(f".part{i}")
                    temp_files.append(temp_file)
                    futures.append(executor.submit(
                        self._download_chunk,
                        url, temp_file, start, end
                    ))
                
                # Wait for all downloads to complete
                for future in as_completed(futures):
                    future.result()  # Will raise exception if any download failed
            
            # Combine all parts into final file
            with open(file_path, 'wb') as outfile:
                for temp_file in temp_files:
                    with open(temp_file, 'rb') as infile:
                        outfile.write(infile.read())
        
        finally:
            # Clean up temporary files
            for temp_file in temp_files:
                if temp_file.exists():
                    temp_file.unlink()
    
    def _download_chunk(self, url: str, file_path: Path, start: int, end: int) -> None:
        """
        Download a specific chunk of a file.
        
        Args:
            url (str): URL to download from
            file_path (Path): Path to save the chunk to
