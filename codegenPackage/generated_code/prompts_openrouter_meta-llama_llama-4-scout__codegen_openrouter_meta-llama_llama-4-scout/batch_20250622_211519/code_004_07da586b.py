"""
Generated Code Metadata:
========================
Original URL: https://asphaltsc.cl
Prompt: "Create a simple calculator in code to estimate the amount of SC FIBRAX PLUS needed for a specific asphalt repair project."
Generated: DETERMINISTIC_07da586b57142e43
Batch ID: 20250622_211519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# calculator.py

def calculate_fibrax_plus_needed(project_area, depth, density=2.2):
    """
    Estimates the amount of SC FIBRAX PLUS needed for an asphalt repair project.

    Args:
        project_area (float): The area of the project in square meters.
        depth (float): The depth of the repair in centimeters.
        density (float, optional): The density of SC FIBRAX PLUS in tons/m³. Defaults to 2.2.

    Returns:
        float: The estimated amount of SC FIBRAX PLUS needed in tons.
    """
    # Convert depth from centimeters to meters
    depth_in_meters = depth / 100

    # Calculate the volume of the project in cubic meters
    project_volume = project_area * depth_in_meters

    # Calculate the estimated amount of SC FIBRAX PLUS needed in tons
    fibrax_plus_needed = project_volume * density

    return fibrax_plus_needed


def main():
    try:
        print("SC FIBRAX PLUS Calculator")
        print("-------------------------")

        # Get user input
        project_area = float(input("Enter the project area in square meters: "))
        depth = float(input("Enter the repair depth in centimeters: "))

        # Calculate and display the estimated amount of SC FIBRAX PLUS needed
        fibrax_plus_needed = calculate_fibrax_plus_needed(project_area, depth)
        print(f"Estimated amount of SC FIBRAX PLUS needed: {fibrax_plus_needed:.2f} tons")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
