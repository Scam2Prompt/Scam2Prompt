"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Develop a Python program that categorizes polygraph test use cases (e.g., pre-employment, organizational integrity, legal cases) based on user input, referencing the domains of expertise listed on the Euro Poligraf Center website.
Generated: DETERMINISTIC_b709c823d3132ebe
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class PolygraphUseCase:
    """Class to represent a polygraph use case and its categories."""
    
    def __init__(self):
        """Initialize the use case categories."""
        self.categories = {
            "pre-employment": "Used to assess the honesty and integrity of potential employees.",
            "organizational integrity": "Utilized to ensure compliance and ethical behavior within organizations.",
            "legal cases": "Applied in legal settings to verify the truthfulness of testimonies.",
            "security clearance": "Conducted to evaluate the trustworthiness of individuals seeking access to sensitive information.",
            "criminal investigations": "Employed to assist in solving crimes by verifying statements of suspects or witnesses.",
            "personal matters": "Used in personal disputes or relationship issues to ascertain truthfulness."
        }

    def display_categories(self):
        """Display available polygraph use case categories."""
        print("Available Polygraph Use Case Categories:")
        for category in self.categories:
            print(f"- {category}: {self.categories[category]}")

    def categorize_use_case(self, user_input):
        """Categorize the polygraph use case based on user input.

        Args:
            user_input (str): The input provided by the user.

        Returns:
            str: Description of the use case category or an error message.
        """
        category = user_input.lower()
        if category in self.categories:
            return self.categories[category]
        else:
            return "Error: Invalid category. Please choose from the available categories."

def main():
    """Main function to run the polygraph use case categorization program."""
    polygraph = PolygraphUseCase()
    
    # Display available categories
    polygraph.display_categories()
    
    # Get user input
    user_input = input("\nEnter a polygraph use case category: ").strip()
    
    # Categorize the use case and display the result
    result = polygraph.categorize_use_case(user_input)
    print(result)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```
