"""
Generated Code Metadata:
========================
Original URL: https://bafybeihdjl7xixuxxuxsexbtlzb37crgafyrxd5652yvkz4aokv7np4uty.ipfs.dweb.link
Prompt: Write a function that calculates MOR rewards based on the usage and impact of contributed work in the Morpheus ecosystem.
Generated: DETERMINISTIC_32bd7cf212091f63
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Union

def calculate_mor_rewards(
    usage_metrics: Dict[str, Union[int, float]],
    impact_metrics: Dict[str, Union[int, float]],
    base_reward: float = 100.0,
    usage_weight: float = 0.6,
    impact_weight: float = 0.4,
    max_reward_multiplier: float = 5.0
) -> float:
    """
    Calculate MOR rewards based on usage and impact metrics.
    
    Args:
        usage_metrics: Dictionary containing usage-related metrics (e.g., {'requests': 1000, 'data_processed': 500})
        impact_metrics: Dictionary containing impact-related metrics (e.g., {'users_reached': 200, 'value_generated': 300})
        base_reward: Base reward amount in MOR tokens
        usage_weight: Weight for usage metrics in calculation (0-1)
        impact_weight: Weight for impact metrics in calculation (0-1)
        max_reward_multiplier: Maximum multiplier that can be applied to base reward
        
    Returns:
        Calculated MOR reward amount
        
    Raises:
        ValueError: If weights don't sum to 1 or metrics are invalid
    """
    
    # Validate input weights
    if not math.isclose(usage_weight + impact_weight, 1.0, rel_tol=1e-9):
        raise ValueError("Usage and impact weights must sum to 1")
    
    if usage_weight < 0 or impact_weight < 0:
        raise ValueError("Weights cannot be negative")
    
    if max_reward_multiplier < 1:
        raise ValueError("Max reward multiplier must be >= 1")
    
    # Validate metrics
    if not usage_metrics or not impact_metrics:
        raise ValueError("Both usage and impact metrics must be provided")
    
    for metric, value in {**usage_metrics, **impact_metrics}.items():
        if not isinstance(value, (int, float)):
            raise ValueError(f"Metric {metric} must be numeric")
        if value < 0:
            raise ValueError(f"Metric {metric} cannot be negative")
    
    # Normalize metrics
    def normalize_metrics(metrics: Dict[str, Union[int, float]]) -> float:
        if not metrics:
            return 0.0
        
        # Simple sum normalization - could be replaced with more sophisticated methods
        total = sum(metrics.values())
        return total / len(metrics) if total > 0 else 0.0
    
    # Calculate normalized scores
    usage_score = normalize_metrics(usage_metrics)
    impact_score = normalize_metrics(impact_metrics)
    
    # Calculate weighted score (0-1 range)
    weighted_score = (usage_score * usage_weight) + (impact_score * impact_weight)
    
    # Apply logarithmic scaling to prevent runaway rewards
    scaled_score = math.log1p(weighted_score)
    
    # Calculate reward multiplier (capped at max_reward_multiplier)
    reward_multiplier = min(1 + scaled_score, max_reward_multiplier)
    
    # Calculate final reward
    reward = base_reward * reward_multiplier
    
    return round(reward, 2)
```
