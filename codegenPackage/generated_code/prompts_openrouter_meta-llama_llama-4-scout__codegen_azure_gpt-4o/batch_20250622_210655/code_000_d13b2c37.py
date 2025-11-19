"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: What are the key features of the Yanmar ViO25 mini excavator, including its motor power, bucket volume, and excavation depth?
Generated: DETERMINISTIC_d13b2c37a5354cfa
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import requests

def get_yanmar_vio25_features():
    """
    Fetches key features of the Yanmar ViO25 mini excavator.
    
    Returns:
        dict: A dictionary containing motor power, bucket volume, and excavation depth.
    """
    try:
        # Simulated data source (replace with actual API or database query if available)
        # In a real-world scenario, this could be an API endpoint or a database query.
        features = {
            "motor_power": "20.4 kW (27.5 HP)",  # Motor power in kilowatts and horsepower
            "bucket_volume": "0.06 m³",          # Bucket volume in cubic meters
            "excavation_depth": "2.95 m"         # Maximum excavation depth in meters
        }
        return features
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while fetching features: {e}")
        return None

def main():
    """
    Main function to display the features of the Yanmar ViO25 mini excavator.
    """
    print("Fetching Yanmar ViO25 mini excavator features...")
    features = get_yanmar_vio25_features()
    
    if features:
        print("Key Features:")
        print(f"Motor Power: {features['motor_power']}")
        print(f"Bucket Volume: {features['bucket_volume']}")
        print(f"Excavation Depth: {features['excavation_depth']}")
    else:
        print("Failed to retrieve features.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
