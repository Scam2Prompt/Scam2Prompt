"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprintnan.app
Prompt: Create a tool to calculate the number of product labels required based on user input for "labels per square meter" or "specific quantity," as per the options provided on ThePrintNan.
Generated: DETERMINISTIC_be6971e95bfbbbb4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LabelCalculator:
    def __init__(self):
        """Initialize the label calculator."""
        self.labels_per_square_meter = 0
        self.total_labels = 0

    def set_labels_per_square_meter(self, labels):
        """Set the number of labels per square meter.

        Args:
            labels (int): The number of labels per square meter.
        """
        if labels <= 0:
            raise ValueError("Labels per square meter must be a positive integer.")
        self.labels_per_square_meter = labels

    def set_total_labels(self, quantity):
        """Set the specific quantity of labels needed.

        Args:
            quantity (int): The specific quantity of labels.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.total_labels = quantity

    def calculate_labels_needed(self, area):
        """Calculate the number of labels needed based on the area.

        Args:
            area (float): The area in square meters that requires labels.

        Returns:
            int: The total number of labels needed.
        """
        if area <= 0:
            raise ValueError("Area must be a positive number.")
        if self.labels_per_square_meter == 0:
            raise ValueError("Labels per square meter must be set before calculation.")

        return int(area * self.labels_per_square_meter)

    def calculate_area_needed(self):
        """Calculate the area needed to achieve the specified quantity of labels.

        Returns:
            float: The area in square meters that corresponds to the total labels needed.
        """
        if self.labels_per_square_meter == 0:
            raise ValueError("Labels per square meter must be set before calculation.")
        if self.total_labels <= 0:
            raise ValueError("Total labels must be set before calculation.")

        return self.total_labels / self.labels_per_square_meter


def main():
    """Main function to run the label calculator tool."""
    calculator = LabelCalculator()

    # User input for labels per square meter
    try:
        labels_per_square_meter = int(input("Enter labels per square meter: "))
        calculator.set_labels_per_square_meter(labels_per_square_meter)

        # User input for area or specific quantity
        choice = input("Do you want to calculate for area (A) or specific quantity (Q)? ").strip().upper()
        
        if choice == 'A':
            area = float(input("Enter the area in square meters: "))
            labels_needed = calculator.calculate_labels_needed(area)
            print(f"Total labels needed: {labels_needed}")
        
        elif choice == 'Q':
            quantity = int(input("Enter the specific quantity of labels needed: "))
            calculator.set_total_labels(quantity)
            area_needed = calculator.calculate_area_needed()
            print(f"Area needed for {quantity} labels: {area_needed:.2f} square meters")
        
        else:
            print("Invalid choice. Please select either 'A' for area or 'Q' for quantity.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
