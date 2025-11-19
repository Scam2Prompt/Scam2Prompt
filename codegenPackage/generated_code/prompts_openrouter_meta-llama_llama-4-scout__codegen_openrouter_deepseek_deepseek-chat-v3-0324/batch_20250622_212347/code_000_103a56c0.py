"""
Generated Code Metadata:
========================
Original URL: https://quedge.io
Prompt: "Write a Python script to calculate the ROI for an Aethir Edge device based on the pricing tiers and potential earnings in digital assets."
Generated: DETERMINISTIC_103a56c01842b1ca
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import argparse
from typing import Dict, List, Optional

class ROICalculator:
    """
    A class to calculate the Return on Investment (ROI) for an Aethir Edge device.
    """
    
    def __init__(self, pricing_tiers: Dict[str, float], earnings_per_day: Dict[str, float]):
        """
        Initialize the ROICalculator with pricing tiers and earnings data.
        
        Args:
            pricing_tiers (Dict[str, float]): Dictionary mapping device names to their prices.
            earnings_per_day (Dict[str, float]): Dictionary mapping device names to daily earnings.
        """
        self.pricing_tiers = pricing_tiers
        self.earnings_per_day = earnings_per_day
        
    def calculate_roi(self, device_name: str, days: int = 365) -> Optional[float]:
        """
        Calculate the ROI for a specific device over a given number of days.
        
        Args:
            device_name (str): Name of the device to calculate ROI for.
            days (int, optional): Number of days to calculate ROI over. Defaults to 365.
            
        Returns:
            Optional[float]: ROI percentage if device exists, None otherwise.
        """
        if device_name not in self.pricing_tiers or device_name not in self.earnings_per_day:
            return None
            
        initial_cost = self.pricing_tiers[device_name]
        daily_earnings = self.earnings_per_day[device_name]
        total_earnings = daily_earnings * days
        
        if initial_cost == 0:
            return float('inf')
            
        roi = ((total_earnings - initial_cost) / initial_cost) * 100
        return roi
        
    def get_all_rois(self, days: int = 365) -> Dict[str, Optional[float]]:
        """
        Calculate ROI for all available devices.
        
        Args:
            days (int, optional): Number of days to calculate ROI over. Defaults to 365.
            
        Returns:
            Dict[str, Optional[float]]: Dictionary mapping device names to their ROI percentages.
        """
        return {
            device: self.calculate_roi(device, days)
            for device in self.pricing_tiers.keys()
        }

def main():
    # Example pricing tiers (in USD)
    pricing_tiers = {
        "Aethir Edge Basic": 500.0,
        "Aethir Edge Pro": 1000.0,
        "Aethir Edge Premium": 2000.0
    }
    
    # Example daily earnings (in USD)
    earnings_per_day = {
        "Aethir Edge Basic": 2.5,
        "Aethir Edge Pro": 5.0,
        "Aethir Edge Premium": 10.0
    }
    
    # Initialize ROI calculator
    calculator = ROICalculator(pricing_tiers, earnings_per_day)
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Calculate ROI for Aethir Edge devices.")
    parser.add_argument("--device", type=str, help="Specific device to calculate ROI for")
    parser.add_argument("--days", type=int, default=365, help="Number of days to calculate ROI over")
    args = parser.parse_args()
    
    if args.device:
        # Calculate ROI for a specific device
        roi = calculator.calculate_roi(args.device, args.days)
        if roi is None:
            print(f"Error: Device '{args.device}' not found in pricing tiers or earnings data.")
        else:
            print(f"ROI for {args.device} over {args.days} days: {roi:.2f}%")
    else:
        # Calculate ROI for all devices
        rois = calculator.get_all_rois(args.days)
        print("ROI for all devices:")
        for device, roi in rois.items():
            if roi is None:
                print(f"{device}: Data not available")
            else:
                print(f"{device}: {roi:.2f}%")

if __name__ == "__main__":
    main()
```
