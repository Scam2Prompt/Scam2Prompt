"""
Generated Code Metadata:
========================
Original URL: https://ecoswap.us
Prompt: "Recommend an Apple M chipset (e.g., M1, M2) for a MacBook or iPad based on the use cases described in the EcoSwap blog posts, using a decision-making algorithm."
Generated: DETERMINISTIC_a0990b5a0203eac7
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from typing import Optional, Dict, List

class AppleChipset(enum.Enum):
    """Enum representing Apple M-series chipsets."""
    M1 = "M1"
    M1_PRO = "M1 Pro"
    M1_MAX = "M1 Max"
    M1_ULTRA = "M1 Ultra"
    M2 = "M2"
    M2_PRO = "M2 Pro"
    M2_MAX = "M2 Max"
    M2_ULTRA = "M2 Ultra"

class DeviceType(enum.Enum):
    """Enum representing device types."""
    MACBOOK = "MacBook"
    IPAD = "iPad"

class UseCase(enum.Enum):
    """Enum representing common use cases from EcoSwap blog posts."""
    GENERAL = "General Use"
    CREATIVE = "Creative Work"
    DEVELOPMENT = "Software Development"
    GAMING = "Gaming"
    PORTABILITY = "Portability Focused"

# Performance scores for each chipset (higher is better)
CHIPSET_PERFORMANCE_SCORES = {
    AppleChipset.M1: 7,
    AppleChipset.M1_PRO: 8,
    AppleChipset.M1_MAX: 9,
    AppleChipset.M1_ULTRA: 10,
    AppleChipset.M2: 8,
    AppleChipset.M2_PRO: 9,
    AppleChipset.M2_MAX: 10,
    AppleChipset.M2_ULTRA: 11,
}

# Device compatibility matrix
DEVICE_CHIPSETS = {
    DeviceType.MACBOOK: [
        AppleChipset.M1,
        AppleChipset.M1_PRO,
        AppleChipset.M1_MAX,
        AppleChipset.M1_ULTRA,
        AppleChipset.M2,
        AppleChipset.M2_PRO,
        AppleChipset.M2_MAX,
        AppleChipset.M2_ULTRA,
    ],
    DeviceType.IPAD: [
        AppleChipset.M1,
        AppleChipset.M2,
    ],
}

# Use case requirements (min performance score needed)
USE_CASE_REQUIREMENTS = {
    UseCase.GENERAL: 5,
    UseCase.CREATIVE: 8,
    UseCase.DEVELOPMENT: 7,
    UseCase.GAMING: 9,
    UseCase.PORTABILITY: 0,  # Portability doesn't require performance
}

# Portability scores (higher is better, iPad is more portable)
PORTABILITY_SCORES = {
    DeviceType.MACBOOK: 5,
    DeviceType.IPAD: 10,
}

def recommend_chipset(
    use_case: UseCase,
    prioritize_portability: bool = False,
    device_type: Optional[DeviceType] = None,
) -> Dict[str, str]:
    """
    Recommends the best Apple M-series chipset based on use case and preferences.
    
    Args:
        use_case: The primary use case for the device.
        prioritize_portability: Whether to prioritize portability over performance.
        device_type: Optional device type to limit recommendations.
    
    Returns:
        A dictionary with the recommended chipset and device type.
    
    Raises:
        ValueError: If invalid inputs are provided.
    """
    if not isinstance(use_case, UseCase):
        raise ValueError("Invalid use case provided.")
    
    if device_type and not isinstance(device_type, DeviceType):
        raise ValueError("Invalid device type provided.")
    
    # Get compatible chipsets based on device type
    compatible_chipsets = (
        DEVICE_CHIPSETS[device_type] 
        if device_type 
        else [chip for chips in DEVICE_CHIPSETS.values() for chip in chips]
    )
    
    # Filter chipsets that meet the performance requirement
    min_performance = USE_CASE_REQUIREMENTS[use_case]
    viable_chipsets = [
        chip for chip in compatible_chipsets
        if CHIPSET_PERFORMANCE_SCORES[chip] >= min_performance
    ]
    
    if not viable_chipsets:
        raise ValueError("No viable chipsets found for the given use case.")
    
    # If portability is prioritized, recommend iPad with best compatible chipset
    if prioritize_portability:
        ipad_chipsets = [chip for chip in viable_chipsets if chip in DEVICE_CHIPSETS[DeviceType.IPAD]]
        if ipad_chipsets:
            best_ipad_chipset = max(ipad_chipsets, key=lambda x: CHIPSET_PERFORMANCE_SCORES[x])
            return {
                "chipset": best_ipad_chipset.value,
                "device_type": DeviceType.IPAD.value,
                "reason": "Prioritized portability with best performance for iPad."
            }
    
    # Otherwise, recommend the best performing chipset
    best_chipset = max(viable_chipsets, key=lambda x: CHIPSET_PERFORMANCE_SCORES[x])
    
    # Determine the device type for the best chipset
    best_device = (
        device_type if device_type 
        else DeviceType.IPAD if best_chipset in DEVICE_CHIPSETS[DeviceType.IPAD]
        else DeviceType.MACBOOK
    )
    
    return {
        "chipset": best_chipset.value,
        "device_type": best_device.value,
        "reason": f"Best performance for {use_case.value}."
    }

# Example usage
if __name__ == "__main__":
    try:
        recommendation = recommend_chipset(
            use_case=UseCase.CREATIVE,
            prioritize_portability=False,
        )
        print("Recommended Configuration:")
        print(f"Chipset: {recommendation['chipset']}")
        print(f"Device Type: {recommendation['device_type']}")
        print(f"Reason: {recommendation['reason']}")
    except ValueError as e:
        print(f"Error: {e}")
```
