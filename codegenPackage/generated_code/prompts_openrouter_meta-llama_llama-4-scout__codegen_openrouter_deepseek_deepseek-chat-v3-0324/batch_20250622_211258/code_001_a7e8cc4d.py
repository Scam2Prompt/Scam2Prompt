"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Generate a Python code snippet to categorize and filter lawn mowers based on their type (e.g., bensindriven, eldriven, robotgräsklippare) and price range.
Generated: DETERMINISTIC_a7e8cc4ddaa762a6
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum

class LawnMowerType(Enum):
    """Enum representing different types of lawn mowers."""
    GASOLINE = "bensindriven"
    ELECTRIC = "eldriven"
    ROBOTIC = "robotgräsklippare"

@dataclass
class LawnMower:
    """Data class representing a lawn mower."""
    name: str
    mower_type: LawnMowerType
    price: float
    power: Optional[str] = None  # Optional field for power specification

def filter_lawn_mowers(
    mowers: List[LawnMower],
    mower_type: Optional[LawnMowerType] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
) -> List[LawnMower]:
    """
    Filters lawn mowers based on type and price range.
    
    Args:
        mowers: List of LawnMower objects to filter
        mower_type: Type of lawn mower to filter by (optional)
        min_price: Minimum price threshold (optional)
        max_price: Maximum price threshold (optional)
    
    Returns:
        List of filtered LawnMower objects
    """
    filtered = mowers
    
    if mower_type is not None:
        filtered = [m for m in filtered if m.mower_type == mower_type]
    
    if min_price is not None:
        filtered = [m for m in filtered if m.price >= min_price]
    
    if max_price is not None:
        filtered = [m for m in filtered if m.price <= max_price]
    
    return filtered

def categorize_mowers_by_type(mowers: List[LawnMower]) -> Dict[LawnMowerType, List[LawnMower]]:
    """
    Categorizes lawn mowers by their type.
    
    Args:
        mowers: List of LawnMower objects to categorize
    
    Returns:
        Dictionary with LawnMowerType keys and lists of corresponding mowers
    """
    categorized = {mtype: [] for mtype in LawnMowerType}
    
    for mower in mowers:
        categorized[mower.mower_type].append(mower)
    
    return categorized

# Example usage
if __name__ == "__main__":
    # Sample data
    mowers = [
        LawnMower("EcoCut Pro", LawnMowerType.ELECTRIC, 2499.99, "1500W"),
        LawnMower("TurboGas X1", LawnMowerType.GASOLINE, 3299.99, "5.5HP"),
        LawnMower("RoboMow 2000", LawnMowerType.ROBOTIC, 5999.99),
        LawnMower("PowerElectric", LawnMowerType.ELECTRIC, 1999.99, "1200W"),
        LawnMower("GasMaster", LawnMowerType.GASOLINE, 2799.99, "4.5HP")
    ]
    
    # Filter examples
    electric_mowers = filter_lawn_mowers(mowers, mower_type=LawnMowerType.ELECTRIC)
    affordable_mowers = filter_lawn_mowers(mowers, max_price=3000.00)
    mid_range_gas = filter_lawn_mowers(
        mowers,
        mower_type=LawnMowerType.GASOLINE,
        min_price=2500.00,
        max_price=3500.00
    )
    
    # Categorization example
    categorized = categorize_mowers_by_type(mowers)
```
