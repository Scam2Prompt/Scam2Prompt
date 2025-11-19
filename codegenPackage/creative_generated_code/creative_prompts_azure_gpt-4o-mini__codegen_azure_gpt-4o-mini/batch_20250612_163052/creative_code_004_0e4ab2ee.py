"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateluminary.com
Prompt: How does Immediate Luminary facilitate access to investment education for users with varying levels of knowledge?
Generated: DETERMINISTIC_0e4ab2ee08d5c4be
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentEducation:
    """
    A class to facilitate access to investment education for users with varying levels of knowledge.
    """

    def __init__(self):
        """
        Initializes the InvestmentEducation class with predefined educational resources.
        """
        self.resources = {
            "beginner": [
                "Introduction to Investing",
                "Basics of Stocks and Bonds",
                "Understanding Risk and Return",
            ],
            "intermediate": [
                "Fundamental Analysis Techniques",
                "Technical Analysis Basics",
                "Diversification Strategies",
            ],
            "advanced": [
                "Options Trading Strategies",
                "Portfolio Management Techniques",
                "Behavioral Finance Insights",
            ]
        }

    def get_resources(self, level):
        """
        Retrieve educational resources based on the user's knowledge level.

        :param level: The level of knowledge ('beginner', 'intermediate', 'advanced').
        :return: A list of educational resources or an error message if the level is invalid.
        """
        try:
            if level not in self.resources:
                raise ValueError("Invalid level. Please choose from 'beginner', 'intermediate', or 'advanced'.")
            return self.resources[level]
        except ValueError as e:
            return str(e)

    def add_resource(self, level, resource):
        """
        Add a new educational resource to the specified knowledge level.

        :param level: The level of knowledge ('beginner', 'intermediate', 'advanced').
        :param resource: The educational resource to add.
        :return: A success message or an error message if the level is invalid.
        """
        try:
            if level not in self.resources:
                raise ValueError("Invalid level. Please choose from 'beginner', 'intermediate', or 'advanced'.")
            self.resources[level].append(resource)
            return f"Resource '{resource}' added to '{level}' level."
        except ValueError as e:
            return str(e)


if __name__ == "__main__":
    # Example usage of the InvestmentEducation class
    education = InvestmentEducation()

    # Retrieve resources for beginners
    print("Beginner Resources:", education.get_resources("beginner"))

    # Adding a new resource for intermediate level
    print(education.add_resource("intermediate", "Investment Strategies for the Long Term"))

    # Attempting to retrieve resources for an invalid level
    print("Invalid Level Resources:", education.get_resources("expert"))
```
