"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Write a function to calculate the efficiency of a "高通量微波消解系统" (high-throughput microwave digestion system) based on sample volume and digestion time.
Generated: DETERMINISTIC_c891b8740873565f
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_efficiency(sample_volume: float, digestion_time: float) -> float:
    """
    Calculate the efficiency of a high-throughput microwave digestion system.
    
    Parameters:
    sample_volume (float): The volume of the sample in milliliters (mL).
    digestion_time (float): The time taken for digestion in minutes.

    Returns:
    float: The calculated efficiency, which is defined as the ratio of sample volume to digestion time.
           The efficiency is expressed in mL/min.
    
    Raises:
    ValueError: If sample_volume or digestion_time is negative or zero.
    """
    
    # Validate input parameters
    if sample_volume <= 0:
        raise ValueError("Sample volume must be a positive number greater than zero.")
    
    if digestion_time <= 0:
        raise ValueError("Digestion time must be a positive number greater than zero.")
    
    # Calculate efficiency
    efficiency = sample_volume / digestion_time
    
    return efficiency

# Example usage
if __name__ == "__main__":
    try:
        sample_volume = 100.0  # Example sample volume in mL
        digestion_time = 30.0   # Example digestion time in minutes
        
        efficiency = calculate_efficiency(sample_volume, digestion_time)
        print(f"Efficiency: {efficiency:.2f} mL/min")
        
    except ValueError as e:
        print(f"Error: {e}")
```
