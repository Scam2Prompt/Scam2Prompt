"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: What are some best practices for establishing industry-academia linkages based on the strategies mentioned by ORIC at Kinnaird College?
Generated: DETERMINISTIC_f341776d0b683453
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class IndustryAcademiaLinkage:
    """
    A class to represent best practices for establishing industry-academia linkages.
    """

    def __init__(self):
        """
        Initializes the best practices list.
        """
        self.best_practices = []

    def add_practice(self, practice: str):
        """
        Adds a best practice to the list.

        Args:
            practice (str): A description of the best practice.
        """
        if not isinstance(practice, str) or not practice:
            raise ValueError("Practice must be a non-empty string.")
        self.best_practices.append(practice)

    def get_practices(self):
        """
        Returns the list of best practices.

        Returns:
            list: A list of best practices for industry-academia linkages.
        """
        return self.best_practices

    def display_practices(self):
        """
        Displays the best practices in a formatted manner.
        """
        if not self.best_practices:
            print("No best practices available.")
            return
        
        print("Best Practices for Industry-Academia Linkages:")
        for idx, practice in enumerate(self.best_practices, start=1):
            print(f"{idx}. {practice}")

def main():
    """
    Main function to demonstrate the usage of the IndustryAcademiaLinkage class.
    """
    try:
        linkage = IndustryAcademiaLinkage()
        
        # Adding best practices
        linkage.add_practice("Establish regular communication channels between industry and academia.")
        linkage.add_practice("Organize joint workshops and seminars to share knowledge.")
        linkage.add_practice("Create internship and co-op programs for students.")
        linkage.add_practice("Encourage collaborative research projects.")
        linkage.add_practice("Develop advisory boards with industry representatives.")
        
        # Displaying the best practices
        linkage.display_practices()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
