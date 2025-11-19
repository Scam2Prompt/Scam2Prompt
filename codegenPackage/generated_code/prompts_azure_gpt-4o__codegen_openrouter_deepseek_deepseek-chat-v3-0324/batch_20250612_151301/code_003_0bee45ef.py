"""
Generated Code Metadata:
========================
Original URL: https://clawback-unicorn-meme.pages.dev
Prompt: Write a function to calculate the clawback boost for $UWU token rewards based on user activity in the Unicorn Meme Market.
Generated: DETERMINISTIC_0bee45efb8ebb160
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_clawback_boost(
    user_activity_score: float,
    last_interaction_days: int,
    total_uwu_held: float,
    base_clawback_rate: float = 0.1,
    max_boost: float = 2.0,
    activity_threshold: float = 50.0,
    decay_rate: float = 0.05
) -> float:
    """
    Calculate the clawback boost for $UWU token rewards based on user activity.
    
    Args:
        user_activity_score: Score representing user's recent activity (0-100)
        last_interaction_days: Days since last interaction with the platform
        total_uwu_held: Total $UWU tokens held by the user
        base_clawback_rate: Base rate for clawback (default: 0.1 or 10%)
        max_boost: Maximum possible boost multiplier (default: 2.0)
        activity_threshold: Minimum activity score to qualify for boost (default: 50)
        decay_rate: Daily decay rate for inactivity (default: 0.05 or 5%)
    
    Returns:
        float: The calculated clawback boost multiplier
        
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if user_activity_score < 0 or user_activity_score > 100:
        raise ValueError("User activity score must be between 0 and 100")
    if last_interaction_days < 0:
        raise ValueError("Days since last interaction cannot be negative")
    if total_uwu_held < 0:
        raise ValueError("Total UWU held cannot be negative")
    if base_clawback_rate <= 0 or base_clawback_rate >= 1:
        raise ValueError("Base clawback rate must be between 0 and 1")
    if max_boost < 1:
        raise ValueError("Max boost must be at least 1")
    if activity_threshold <= 0 or activity_threshold > 100:
        raise ValueError("Activity threshold must be between 0 and 100")
    if decay_rate <= 0 or decay_rate >= 1:
        raise ValueError("Decay rate must be between 0 and 1")

    # Calculate activity-based boost component
    activity_boost = 1.0
    if user_activity_score >= activity_threshold:
        activity_boost = min(
            max_boost,
            1 + (user_activity_score - activity_threshold) / (100 - activity_threshold)
        )

    # Calculate decay factor based on inactivity
    decay_factor = (1 - decay_rate) ** last_interaction_days

    # Calculate holding-based boost component (logarithmic to prevent whale dominance)
    holding_boost = 1 + (base_clawback_rate * min(1, (total_uwu_held ** 0.5) / 1000))

    # Combine all components with appropriate weights
    final_boost = (
        0.5 * activity_boost * decay_factor +
        0.3 * holding_boost +
        0.2  # Base component to ensure minimum boost of 1.0
    )

    # Ensure boost stays within reasonable bounds
    return min(max(final_boost, 1.0), max_boost)
```
