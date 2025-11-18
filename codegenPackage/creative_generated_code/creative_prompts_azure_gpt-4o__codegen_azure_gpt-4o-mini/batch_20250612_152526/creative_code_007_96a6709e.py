"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebookkeepingdiaries.com
Prompt: Recommend software solutions for small businesses to manage bookkeeping, payroll, and tax preparation, similar to the affordable solutions provided by "The Bookkeeping Diaries."
Generated: DETERMINISTIC_96a6709e5231452c
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# software_recommendations.py

class SoftwareRecommendation:
    """
    A class to represent a software recommendation for small businesses
    to manage bookkeeping, payroll, and tax preparation.
    """

    def __init__(self):
        """
        Initializes the SoftwareRecommendation class with a list of recommendations.
        """
        self.recommendations = []

    def add_recommendation(self, name, description, price, features):
        """
        Adds a software recommendation to the list.

        :param name: Name of the software
        :param description: Brief description of the software
        :param price: Monthly price of the software
        :param features: List of key features offered by the software
        """
        try:
            if not isinstance(name, str) or not isinstance(description, str) or not isinstance(price, (int, float)) or not isinstance(features, list):
                raise ValueError("Invalid input types for software recommendation.")

            software = {
                "name": name,
                "description": description,
                "price": price,
                "features": features
            }
            self.recommendations.append(software)

        except Exception as e:
            print(f"Error adding recommendation: {e}")

    def get_recommendations(self):
        """
        Returns the list of software recommendations.

        :return: List of software recommendations
        """
        return self.recommendations

    def display_recommendations(self):
        """
        Prints out all software recommendations in a user-friendly format.
        """
        if not self.recommendations:
            print("No recommendations available.")
            return
        
        print("Software Recommendations for Small Businesses:")
        for idx, software in enumerate(self.recommendations, start=1):
            print(f"{idx}. {software['name']}")
            print(f"   Description: {software['description']}")
            print(f"   Monthly Price: ${software['price']:.2f}")
            print(f"   Features: {', '.join(software['features'])}\n")


if __name__ == "__main__":
    # Create an instance of SoftwareRecommendation
    software_recommender = SoftwareRecommendation()

    # Adding software recommendations
    software_recommender.add_recommendation(
        name="QuickBooks Online",
        description="A popular accounting software for small businesses.",
        price=25.00,
        features=["Invoice creation", "Expense tracking", "Tax calculation"]
    )

    software_recommender.add_recommendation(
        name="FreshBooks",
        description="User-friendly accounting software for service-based businesses.",
        price=15.00,
        features=["Time tracking", "Automatic invoicing", "Expense management"]
    )

    software_recommender.add_recommendation(
        name="Wave",
        description="Free accounting software with optional paid services.",
        price=0.00,
        features=["Accounting", "Invoicing", "Receipt scanning"]
    )

    # Display all recommendations
    software_recommender.display_recommendations()
```
