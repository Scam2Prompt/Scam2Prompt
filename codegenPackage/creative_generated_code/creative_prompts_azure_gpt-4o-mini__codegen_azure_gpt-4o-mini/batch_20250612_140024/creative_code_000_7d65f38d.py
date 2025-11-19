"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnalkhedmad.com
Prompt: Generate code to create a product comparison table for different iPhone models, including screen sizes and features like MagSafe compatibility.
Generated: DETERMINISTIC_7d65f38de11f0eaf
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class iPhoneModel:
    def __init__(self, model_name, screen_size, magsafe_compatible, camera_quality):
        """
        Initialize an iPhone model with its specifications.

        Args:
            model_name (str): The name of the iPhone model.
            screen_size (float): The screen size of the iPhone model in inches.
            magsafe_compatible (bool): Indicates if the model is MagSafe compatible.
            camera_quality (str): Description of the camera quality.
        """
        self.model_name = model_name
        self.screen_size = screen_size
        self.magsafe_compatible = magsafe_compatible
        self.camera_quality = camera_quality

    def to_dict(self):
        """
        Convert the iPhone model details to a dictionary for easier data manipulation.

        Returns:
            dict: A dictionary representation of the iPhone model.
        """
        return {
            "Model": self.model_name,
            "Screen Size (inches)": self.screen_size,
            "MagSafe Compatible": "Yes" if self.magsafe_compatible else "No",
            "Camera Quality": self.camera_quality
        }


def create_comparison_table(models):
    """
    Create a comparison table for different iPhone models.

    Args:
        models (list of iPhoneModel): A list of iPhoneModel instances.

    Returns:
        DataFrame: A pandas DataFrame containing the comparison table.
    """
    # Convert each model to a dictionary and create a DataFrame
    try:
        comparison_data = [model.to_dict() for model in models]
        comparison_table = pd.DataFrame(comparison_data)
        return comparison_table
    except Exception as e:
        print(f"Error creating comparison table: {e}")
        return None


def main():
    """
    Main function to create and display the iPhone comparison table.
    """
    # List of iPhone models with their specifications
    iphone_models = [
        iPhoneModel("iPhone 13", 6.1, True, "Dual 12MP cameras"),
        iPhoneModel("iPhone 13 Pro", 6.1, True, "Triple 12MP cameras with ProRAW"),
        iPhoneModel("iPhone 13 Mini", 5.4, True, "Dual 12MP cameras"),
        iPhoneModel("iPhone SE (3rd Gen)", 4.7, False, "Single 12MP camera"),
        iPhoneModel("iPhone 14", 6.1, True, "Dual 12MP cameras"),
        iPhoneModel("iPhone 14 Pro", 6.1, True, "Triple 48MP + 12MP + 12MP cameras")
    ]

    # Create the comparison table
    comparison_table = create_comparison_table(iphone_models)

    # Display the comparison table
    if comparison_table is not None:
        print(comparison_table)


if __name__ == "__main__":
    main()
```
