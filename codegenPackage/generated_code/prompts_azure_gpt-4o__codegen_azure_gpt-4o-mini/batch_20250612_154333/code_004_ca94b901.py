"""
Generated Code Metadata:
========================
Original URL: https://ethx-ai.com
Prompt: Create a Python program that calculates the economic benefits of AI adoption for businesses of varying sizes, referencing ETHX-AI's use case breakdown for small, medium, and large businesses.
Generated: DETERMINISTIC_ca94b9017a1465bd
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Business:
    def __init__(self, size, revenue, ai_investment):
        """
        Initialize a Business instance.

        :param size: Size of the business ('small', 'medium', 'large')
        :param revenue: Annual revenue of the business
        :param ai_investment: Investment in AI technologies
        """
        self.size = size
        self.revenue = revenue
        self.ai_investment = ai_investment
        self.ai_benefits = self.calculate_ai_benefits()

    def calculate_ai_benefits(self):
        """
        Calculate the economic benefits of AI adoption based on business size.

        :return: Estimated economic benefits from AI adoption
        """
        benefits_percentage = {
            'small': 0.1,  # 10% increase in efficiency
            'medium': 0.15,  # 15% increase in efficiency
            'large': 0.2  # 20% increase in efficiency
        }

        if self.size not in benefits_percentage:
            raise ValueError("Invalid business size. Choose from 'small', 'medium', or 'large'.")

        # Calculate benefits based on revenue and investment
        benefits = self.revenue * benefits_percentage[self.size] - self.ai_investment
        return max(benefits, 0)  # Ensure benefits are not negative

    def report(self):
        """
        Generate a report of the business's AI adoption benefits.

        :return: A dictionary containing the business size, revenue, investment, and benefits
        """
        return {
            'size': self.size,
            'revenue': self.revenue,
            'ai_investment': self.ai_investment,
            'ai_benefits': self.ai_benefits
        }


def main():
    """
    Main function to execute the program.
    """
    # Sample data for businesses
    businesses_data = [
        {'size': 'small', 'revenue': 500000, 'ai_investment': 30000},
        {'size': 'medium', 'revenue': 2000000, 'ai_investment': 150000},
        {'size': 'large', 'revenue': 10000000, 'ai_investment': 500000}
    ]

    results = []

    for data in businesses_data:
        try:
            business = Business(data['size'], data['revenue'], data['ai_investment'])
            results.append(business.report())
        except ValueError as e:
            print(f"Error processing business data: {e}")

    # Output results in JSON format
    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
```
