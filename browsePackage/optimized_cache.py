#!/usr/bin/env python3
"""Optimized HTML file cache with subfolder organization"""

import os
import hashlib
from typing import Optional, Tuple
from pathlib import Path

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class OptimizedHTMLCache:
    def __init__(self, cache_type="static", levels=2, chars_per_level=2):
        """
        Initialize optimized HTML cache with subfolder organization
        
        Args:
            cache_type: "static" or "dynamic" 
            levels: Number of subfolder levels (default 2)
            chars_per_level: Characters per subfolder level (default 2)
            
        Example structure:
            cache/static/ab/cd/abcd1234567890_https__example.com.html
            cache/static/12/34/12345678901234_https__github.com.html
        """
        self.cache_type = cache_type
        self.levels = levels
        self.chars_per_level = chars_per_level
        
        # Set up cache directory
        self.cache_root = os.path.join(CURRENT_DIR, "cache", cache_type)
        os.makedirs(self.cache_root, exist_ok=True)
    
    def _url_to_hash(self, url: str) -> str:
        """Convert URL to hash for filename"""
        return hashlib.sha256(url.encode('utf-8')).hexdigest()
    
    def _url_to_safe_filename(self, url: str) -> str:
        """Convert URL to filesystem-safe filename"""
        # Replace problematic characters
        safe_url = url.replace("://", "__").replace("/", "_").replace("?", "_").replace("&", "_")
        # Limit length to avoid filesystem limits
        if len(safe_url) > 100:
            safe_url = safe_url[:100]
        return safe_url
    
    def _get_cache_path(self, url: str) -> Tuple[str, str]:
        """
        Get the cache file path for a URL
        
        Returns:
            Tuple of (directory_path, file_path)
        """
        url_hash = self._url_to_hash(url)
        safe_filename = self._url_to_safe_filename(url)
        
        # Create subfolder structure based on hash
        subfolder_parts = []
        for i in range(self.levels):
            start_idx = i * self.chars_per_level
            end_idx = start_idx + self.chars_per_level
            subfolder_parts.append(url_hash[start_idx:end_idx])
        
        # Build directory path
        dir_path = os.path.join(self.cache_root, *subfolder_parts)
        
        # Build filename: hash_prefix + safe_url + .html
        hash_prefix = url_hash[:12]  # First 12 chars of hash
        filename = f"{hash_prefix}_{safe_filename}.html"
        file_path = os.path.join(dir_path, filename)
        
        return dir_path, file_path
    
    def get_cached_content(self, url: str) -> Optional[str]:
        """
        Get cached content for a URL
        
        Returns:
            Content string or None if not cached
        """
        try:
            dir_path, file_path = self._get_cache_path(url)
            
            if os.path.exists(file_path):
                with open(file_path, "r", encoding='utf-8') as f:
                    return f.read()
            return None
            
        except Exception as e:
            print(f"Error reading cache for {url}: {e}")
            return None
    
    def cache_content(self, url: str, content: str) -> bool:
        """
        Cache content for a URL
        
        Args:
            url: The URL
            content: HTML content to cache
            
        Returns:
            True if successfully cached, False otherwise
        """
        try:
            dir_path, file_path = self._get_cache_path(url)
            
            # Create directory if it doesn't exist
            os.makedirs(dir_path, exist_ok=True)
            
            # Write content to file
            with open(file_path, "w", encoding='utf-8') as f:
                f.write(content)
            
            return True
            
        except Exception as e:
            print(f"Error caching content for {url}: {e}")
            return False
    
    def is_cached(self, url: str) -> bool:
        """Check if URL is cached"""
        _, file_path = self._get_cache_path(url)
        return os.path.exists(file_path)
    
    def remove_cached_content(self, url: str) -> bool:
        """Remove cached content for a URL"""
        try:
            _, file_path = self._get_cache_path(url)
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            return False
        except Exception as e:
            print(f"Error removing cache for {url}: {e}")
            return False
    
    def get_cache_stats(self) -> dict:
        """Get cache statistics"""
        total_files = 0
        total_size_bytes = 0
        folder_count = 0
        
        try:
            for root, dirs, files in os.walk(self.cache_root):
                folder_count += len(dirs)
                for file in files:
                    if file.endswith('.html'):
                        file_path = os.path.join(root, file)
                        total_files += 1
                        total_size_bytes += os.path.getsize(file_path)
        
        except Exception as e:
            print(f"Error getting cache stats: {e}")
        
        return {
            'cache_type': self.cache_type,
            'total_files': total_files,
            'total_folders': folder_count,
            'total_size_bytes': total_size_bytes,
            'total_size_mb': round(total_size_bytes / (1024 * 1024), 2),
            'avg_file_size_kb': round(total_size_bytes / total_files / 1024, 2) if total_files > 0 else 0
        }
    
    def cleanup_empty_folders(self):
        """Remove empty folders from cache"""
        removed_count = 0
        try:
            # Walk from deepest to shallowest to remove empty folders
            for root, dirs, files in os.walk(self.cache_root, topdown=False):
                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    try:
                        os.rmdir(dir_path)  # Only removes if empty
                        removed_count += 1
                    except OSError:
                        pass  # Directory not empty, that's fine
        except Exception as e:
            print(f"Error during cleanup: {e}")
        
        return removed_count


def demonstrate_cache_structure():
    """Demonstrate how the cache structure works"""
    print("🗂️  Cache Structure Demonstration")
    print("=" * 50)
    
    cache = OptimizedHTMLCache("static")
    
    # Test URLs
    test_urls = [
        "https://example.com",
        "https://github.com/user/repo",
        "https://stackoverflow.com/questions/123",
        "https://docs.python.org/3/library/os.html",
        "https://malicious-site.com/phishing-page"
    ]
    
    print("URL -> Cache Path Mapping:")
    for url in test_urls:
        dir_path, file_path = cache._get_cache_path(url)
        rel_path = os.path.relpath(file_path, CURRENT_DIR)
        print(f"  {url}")
        print(f"    -> {rel_path}")
        print()


def main():
    """Test the optimized cache"""
    print("🚀 Testing Optimized HTML Cache")
    print("=" * 50)
    
    # Test both static and dynamic caches
    static_cache = OptimizedHTMLCache("static")
    dynamic_cache = OptimizedHTMLCache("dynamic")
    
    test_url = "https://example.com/test"
    test_content = "<html><body><h1>Test Content</h1><p>This is a test.</p></body></html>"
    
    # Test caching
    print(f"Caching content for: {test_url}")
    success = static_cache.cache_content(test_url, test_content)
    print(f"Cache success: {success}")
    
    # Test retrieval
    print("Retrieving cached content...")
    cached_content = static_cache.get_cached_content(test_url)
    print(f"Retrieved: {'Yes' if cached_content else 'No'}")
    print(f"Content length: {len(cached_content) if cached_content else 0}")
    
    # Test stats
    print("\nCache Stats:")
    stats = static_cache.get_cache_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Demonstrate structure
    print("\n" + "="*50)
    demonstrate_cache_structure()


if __name__ == "__main__":
    main() 