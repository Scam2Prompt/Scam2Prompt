"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dxlink.net
Prompt: Generate code to calculate bandwidth usage for DX Link's dedicated internet packages, incorporating their BDIX and fiber optic connection features.
Generated: DETERMINISTIC_26c6109e46c8f483
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_bandwidth_usage(total_data_used_gb, package_speed_mbps):
    """
    Calculate bandwidth usage for DX Link's dedicated internet packages.

    Parameters:
      total_data_used_gb (float): Total data used in GB.
      package_speed_mbps (float): Internet package speed in Mbps.

    Returns:
      dict: Bandwidth usage details including BDIX and fiber optic allocation.
    """
    try:
        # Validate input parameters
        if total_data_used_gb < 0 or package_speed_mbps <= 0:
            raise ValueError("Invalid input: Data used must be non-negative and speed must be positive.")

        # Constants for allocation percentages
        BDIX_PERCENTAGE = 0.30  # 30% of the bandwidth is allocated to BDIX
        FIBER_OPTIC_PERCENTAGE = 0.70  # 70% of the bandwidth is allocated to fiber optic
        
        # Calculate bandwidth allocation for BDIX and fiber optic connections
        bdix_bandwidth_usage_gb = total_data_used_gb * BDIX_PERCENTAGE
        fiber_optic_bandwidth_usage_gb = total_data_used_gb * FIBER_OPTIC_PERCENTAGE

        # Prepare the output
        result = {
            "Total Data Used (GB)": round(total_data_used_gb, 2),
            "Package Speed (Mbps)": round(package_speed_mbps, 2),
            "BDIX Bandwidth Usage (GB)": round(bdix_bandwidth_usage_gb, 2),
            "Fiber Optic Bandwidth Usage (GB)": round(fiber_optic_bandwidth_usage_gb, 2)
        }

        return result

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Example usage
if __name__ == "__main__":
    try:
        # Get user input
        total_data_used_gb = float(input("Enter total data used (GB): "))
        package_speed_mbps = float(input("Enter package speed (Mbps): "))

        # Calculate bandwidth usage
        bandwidth_details = calculate_bandwidth_usage(total_data_used_gb, package_speed_mbps)

        # Print the result
        print("\nBandwidth Usage Details:")
        for key, value in bandwidth_details.items():
            print(f"{key}: {value}")

    except ValueError:
        print("Please provide valid numeric inputs for data used and package speed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
