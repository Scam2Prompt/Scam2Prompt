"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strive.serwerdwg.pl
Prompt: What are effective methods for building a recruitment strategy tailored to the engineering sector?
Generated: DETERMINISTIC_3dd35dc53163c953
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RecruitmentStrategy:
    """
    A class to represent a recruitment strategy tailored to the engineering sector.
    """

    def __init__(self):
        """
        Initializes an empty list to hold recruitment methods.
        """
        self.methods = []

    def add_method(self, method: str):
        """
        Adds a recruitment method to the list.
        
        Parameters:
        method (str): The recruitment method to be added.
        """
        if not isinstance(method, str) or not method.strip():
            raise ValueError("Method must be a non-empty string.")
        self.methods.append(method.strip())

    def remove_method(self, method: str):
        """
        Removes a recruitment method from the list if it exists.
        
        Parameters:
        method (str): The recruitment method to be removed.
        
        Raises:
        ValueError: If the method does not exist in the list.
        """
        try:
            self.methods.remove(method)
        except ValueError:
            raise ValueError(f"Method '{method}' not found in the recruitment strategy.")

    def get_methods(self):
        """
        Returns the list of recruitment methods.
        
        Returns:
        list: A list containing all recruitment methods.
        """
        return self.methods

    def display_methods(self):
        """
        Displays all recruitment methods in a formatted way.
        """
        if not self.methods:
            print("No recruitment methods have been added.")
            return
        print("Recruitment Methods for Engineering Sector:")
        for method in self.methods:
            print(f"- {method}")

def main():
    """
    Main function to demonstrate the usage of RecruitmentStrategy class.
    """
    try:
        strategy = RecruitmentStrategy()

        # Adding recruitment methods
        strategy.add_method("Leverage social media platforms.")
        strategy.add_method("Attend engineering job fairs.")
        strategy.add_method("Partner with universities and colleges.")
        strategy.add_method("Implement employee referral programs.")
        strategy.add_method("Utilize specialized recruitment agencies.")
        
        # Display current methods
        strategy.display_methods()

        # Example of removing a method
        strategy.remove_method("Utilize specialized recruitment agencies.")
        
        # Display methods after removal
        print("\nAfter removal:")
        strategy.display_methods()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
