"""
Generated Code Metadata:
========================
Original URL: https://realogs.space
Prompt: Generate a code snippet to implement a keyword-based filtering system for a chat application, inspired by the need to prevent crypto speculation discussions in the realogs.space community.
Generated: DETERMINISTIC_cc89ee8333648675
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Optional, Set

class KeywordFilter:
    """
    A keyword-based filtering system for chat applications.
    Filters messages containing prohibited keywords related to crypto speculation.
    """

    def __init__(self, prohibited_keywords: Optional[Set[str]] = None):
        """
        Initialize the KeywordFilter with a set of prohibited keywords.
        
        Args:
            prohibited_keywords: Set of keywords to filter. If None, uses default crypto-related terms.
        """
        self.prohibited_keywords = prohibited_keywords or {
            'bitcoin', 'btc', 'crypto', 'cryptocurrency', 'ethereum', 'eth',
            'altcoin', 'shib', 'dogecoin', 'doge', 'xrp', 'ripple', 'binance',
            'coinbase', 'nft', 'non-fungible token', 'defi', 'pump', 'dump',
            'hodl', 'fomo', 'fud', 'moonshot', 'lambo', 'to the moon'
        }
        # Compile regex pattern for case-insensitive matching
        self.pattern = re.compile(
            r'\b(' + '|'.join(map(re.escape, self.prohibited_keywords)) + r')\b',
            flags=re.IGNORECASE
        )

    def contains_prohibited_keywords(self, message: str) -> bool:
        """
        Check if a message contains any prohibited keywords.
        
        Args:
            message: The chat message to check.
            
        Returns:
            bool: True if prohibited keywords are found, False otherwise.
        """
        return bool(self.pattern.search(message))

    def filter_message(self, message: str, replacement: str = "[REDACTED]") -> str:
        """
        Filter prohibited keywords from a message by replacing them.
        
        Args:
            message: The chat message to filter.
            replacement: The string to replace prohibited keywords with.
            
        Returns:
            str: The filtered message.
        """
        return self.pattern.sub(replacement, message)

    def add_keywords(self, keywords: List[str]) -> None:
        """
        Add new keywords to the prohibited set and update the regex pattern.
        
        Args:
            keywords: List of new keywords to add.
        """
        self.prohibited_keywords.update(keywords)
        self._update_pattern()

    def remove_keywords(self, keywords: List[str]) -> None:
        """
        Remove keywords from the prohibited set and update the regex pattern.
        
        Args:
            keywords: List of keywords to remove.
        """
        self.prohibited_keywords.difference_update(keywords)
        self._update_pattern()

    def _update_pattern(self) -> None:
        """Update the regex pattern after changes to prohibited keywords."""
        self.pattern = re.compile(
            r'\b(' + '|'.join(map(re.escape, self.prohibited_keywords)) + r')\b',
            flags=re.IGNORECASE
        )


# Example usage
if __name__ == "__main__":
    # Initialize filter
    chat_filter = KeywordFilter()
    
    # Test messages
    test_messages = [
        "Just bought some Bitcoin!",
        "What's the weather like today?",
        "ETH is going to the moon!",
        "Let's discuss technology and science."
    ]
    
    for msg in test_messages:
        if chat_filter.contains_prohibited_keywords(msg):
            print(f"Filtered: {chat_filter.filter_message(msg)}")
        else:
            print(f"Allowed: {msg}")
```
