"""
Generated Code Metadata:
========================
Original URL: https://pepedao.org
Prompt: "Implement a simple caching mechanism using a programming language of your choice, inspired by WIKIWIKI's caching features."
Generated: DETERMINISTIC_1e0cdadeee2419c3
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Any, Dict, Optional

class SimpleCache:
    """
    A simple caching mechanism inspired by WIKIWIKI's caching features.
    
    Features:
    - Time-based expiration
    - Size limit
    - Thread-safe operations (assuming single-threaded environment)
    """
    
    def __init__(self, max_size: int = 100, default_ttl: int = 300) -> None:
        """
        Initialize the cache with a maximum size and default time-to-live (TTL).
        
        Args:
            max_size: Maximum number of items to store in cache (default: 100)
            default_ttl: Default time-to-live in seconds (default: 300)
        """
        self.max_size = max_size
        self.default_ttl = default_ttl
        self.cache: Dict[str, Dict[str, Any]] = {}
        
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Store a value in the cache with an optional TTL.
        
        Args:
            key: Key to store the value under
            value: Value to be stored
            ttl: Optional time-to-live in seconds (defaults to instance default)
        """
        if len(self.cache) >= self.max_size:
            self._evict_expired()
            if len(self.cache) >= self.max_size:
                self._evict_oldest()
        
        expiration = time.time() + (ttl if ttl is not None else self.default_ttl)
        self.cache[key] = {
            'value': value,
            'expiration': expiration
        }
    
    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from the cache if it exists and hasn't expired.
        
        Args:
            key: Key to retrieve
            
        Returns:
            The stored value or None if not found/expired
        """
        if key not in self.cache:
            return None
            
        item = self.cache[key]
        if time.time() > item['expiration']:
            del self.cache[key]
            return None
            
        return item['value']
    
    def delete(self, key: str) -> None:
        """
        Remove an item from the cache.
        
        Args:
            key: Key to remove
        """
        if key in self.cache:
            del self.cache[key]
    
    def clear(self) -> None:
        """
        Clear all items from the cache.
        """
        self.cache.clear()
    
    def _evict_expired(self) -> None:
        """
        Remove all expired items from the cache.
        """
        current_time = time.time()
        expired_keys = [
            key for key, item in self.cache.items()
            if current_time > item['expiration']
        ]
        for key in expired_keys:
            del self.cache[key]
    
    def _evict_oldest(self) -> None:
        """
        Remove the oldest item from the cache to make space.
        """
        if not self.cache:
            return
            
        oldest_key = min(self.cache.keys(), key=lambda k: self.cache[k]['expiration'])
        del self.cache[oldest_key]
    
    def __contains__(self, key: str) -> bool:
        """
        Check if a key exists in the cache and hasn't expired.
        
        Args:
            key: Key to check
            
        Returns:
            True if key exists and is not expired, False otherwise
        """
        if key not in self.cache:
            return False
            
        if time.time() > self.cache[key]['expiration']:
            del self.cache[key]
            return False
            
        return True
    
    def __len__(self) -> int:
        """
        Return the number of items in the cache (including expired ones).
        
        Returns:
            Number of items in cache
        """
        return len(self.cache)
```
