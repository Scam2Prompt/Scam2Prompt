"""
Generated Code Metadata:
========================
Original URL: https://coinjoin.cc
Prompt: Create a CoinJoin configuration file to specify the mixer settings, including the service fee, transfer delay, and percentage distribution for a specific mixing operation.
Generated: DETERMINISTIC_2b0ca40fcf95b715
Batch ID: 20250622_211412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

class MixingStrategy(Enum):
    """Enumeration of supported mixing strategies."""
    EQUAL_DISTRIBUTION = "equal_distribution"
    PROPORTIONAL_DISTRIBUTION = "proportional_distribution"

@dataclass
class CoinJoinConfig:
    """Configuration for a CoinJoin mixing operation."""
    service_fee: float  # Percentage fee charged by the service (0-100)
    min_transfer_delay: int  # Minimum delay in blocks before transfer (inclusive)
    max_transfer_delay: int  # Maximum delay in blocks before transfer (inclusive)
    mixing_strategy: MixingStrategy  # Strategy for distributing mixed coins
    distribution_percentages: Optional[Dict[str, float]] = None  # Percentage per address (if strategy requires)
    version: str = "1.0"  # Configuration version

    def validate(self) -> None:
        """Validate the configuration parameters."""
        if not 0 <= self.service_fee <= 100:
            raise ValueError("Service fee must be between 0 and 100")
        if self.min_transfer_delay < 0 or self.max_transfer_delay < 0:
            raise ValueError("Transfer delays must be non-negative")
        if self.min_transfer_delay > self.max_transfer_delay:
            raise ValueError("Min transfer delay cannot exceed max transfer delay")
        if self.mixing_strategy == MixingStrategy.PROPORTIONAL_DISTRIBUTION:
            if not self.distribution_percentages:
                raise ValueError("Distribution percentages must be provided for proportional distribution")
            total = sum(self.distribution_percentages.values())
            if not (99.9 <= total <= 100.1):  # Allow for floating point precision
                raise ValueError("Distribution percentages must sum to 100")

    def to_json(self) -> str:
        """Serialize the configuration to JSON."""
        self.validate()
        config_dict = asdict(self)
        config_dict["mixing_strategy"] = self.mixing_strategy.value
        return json.dumps(config_dict, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'CoinJoinConfig':
        """Deserialize the configuration from JSON."""
        data = json.loads(json_str)
        data["mixing_strategy"] = MixingStrategy(data["mixing_strategy"])
        return cls(**data)

# Example usage
if __name__ == "__main__":
    try:
        # Create a sample configuration
        config = CoinJoinConfig(
            service_fee=1.5,
            min_transfer_delay=2,
            max_transfer_delay=10,
            mixing_strategy=MixingStrategy.PROPORTIONAL_DISTRIBUTION,
            distribution_percentages={
                "address1": 30.0,
                "address2": 40.0,
                "address3": 30.0
            }
        )

        # Serialize to JSON
        json_config = config.to_json()
        print("Serialized Configuration:")
        print(json_config)

        # Deserialize from JSON
        loaded_config = CoinJoinConfig.from_json(json_config)
        print("\nDeserialized Configuration:")
        print(loaded_config)

    except ValueError as e:
        print(f"Error: {e}")
```
