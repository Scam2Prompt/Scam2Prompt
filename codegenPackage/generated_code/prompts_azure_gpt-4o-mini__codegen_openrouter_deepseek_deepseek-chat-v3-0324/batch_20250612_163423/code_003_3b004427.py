"""
Generated Code Metadata:
========================
Original URL: https://createra-genesis-land.netlify.app
Prompt: Generate code to track the number of tokens minted in a pre-sale, inspired by the Createra Genesis Land statistics.
Generated: DETERMINISTIC_3b00442743887868
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class TokenStats:
    total_minted: int = 0
    last_minted_timestamp: Optional[datetime] = None
    minted_by_address: Dict[str, int] = None  # address -> count

    def __post_init__(self):
        if self.minted_by_address is None:
            self.minted_by_address = {}

class TokenTracker:
    def __init__(self, storage_file: str = "token_stats.json"):
        self.storage_file = storage_file
        self.stats = self._load_stats()

    def _load_stats(self) -> TokenStats:
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                stats = TokenStats(
                    total_minted=data['total_minted'],
                    last_minted_timestamp=datetime.fromisoformat(data['last_minted_timestamp']) if data['last_minted_timestamp'] else None,
                    minted_by_address=data['minted_by_address']
                )
                return stats
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return TokenStats()

    def _save_stats(self):
        with open(self.storage_file, 'w') as f:
            data = asdict(self.stats)
            data['last_minted_timestamp'] = self.stats.last_minted_timestamp.isoformat() if self.stats.last_minted_timestamp else None
            json.dump(data, f, indent=2)

    def record_mint(self, address: str, count: int = 1):
        """Record a token mint event for a given address."""
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Count must be a positive integer")
        
        if not isinstance(address, str) or not address:
            raise ValueError("Address must be a non-empty string")

        self.stats.total_minted += count
        self.stats.last_minted_timestamp = datetime.now()
        self.stats.minted_by_address[address] = self.stats.minted_by_address.get(address, 0) + count
        self._save_stats()

    def get_total_minted(self) -> int:
        """Return total number of tokens minted."""
        return self.stats.total_minted

    def get_last_minted_time(self) -> Optional[datetime]:
        """Return timestamp of last mint event."""
        return self.stats.last_minted_timestamp

    def get_minted_count(self, address: str) -> int:
        """Return number of tokens minted by a specific address."""
        return self.stats.minted_by_address.get(address, 0)

    def get_all_stats(self) -> Dict:
        """Return all statistics as a dictionary."""
        return {
            'total_minted': self.stats.total_minted,
            'last_minted_timestamp': self.stats.last_minted_timestamp.isoformat() if self.stats.last_minted_timestamp else None,
            'minted_by_address': self.stats.minted_by_address
        }
```
