"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Build a Python tool to calculate and display the environmental impact of Everyworld's contributions based on user engagement metrics and token distribution data.
Generated: DETERMINISTIC_b90fc51784e46cb8
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class EnvironmentalImpactCalculator:
    """
    A tool to calculate and display the environmental impact of Everyworld's contributions
    based on user engagement metrics and token distribution data.
    """

    def __init__(self, engagement_data, token_data):
        """
        Initialize the calculator with engagement and token distribution data.

        :param engagement_data: Dict containing user engagement metrics.
        :param token_data: Dict containing token distribution data.
        """
        self.engagement_data = engagement_data
        self.token_data = token_data

    def calculate_impact(self):
        """
        Calculate the environmental impact based on the provided data.

        :return: Dict containing calculated environmental impact metrics.
        """
        try:
            # Metric 1: Calculate engagement-based impact
            total_engagement = sum(self.engagement_data.values())
            engagement_impact = total_engagement * 0.1  # Example coefficient

            # Metric 2: Calculate token-based impact
            total_tokens = sum(self.token_data.values())
            token_impact = total_tokens * 0.05  # Example coefficient

            # Combine metrics to calculate total impact
            total_impact = engagement_impact + token_impact

            # Return a dictionary of calculated impact metrics
            return {
                "engagement_impact": round(engagement_impact, 2),
                "token_impact": round(token_impact, 2),
                "total_impact": round(total_impact, 2),
            }
        except Exception as e:
            # Handle unexpected errors during calculation
            print(f"Error during impact calculation: {e}")
            return {}

    def display_impact(self):
        """
        Display the environmental impact in a user-friendly format.
        """
        impact_metrics = self.calculate_impact()
        if not impact_metrics:
            print("Unable to display impact due to calculation errors.")
            return

        print("Environmental Impact Metrics:")
        print(f"- Engagement Impact: {impact_metrics['engagement_impact']}")
        print(f"- Token Impact: {impact_metrics['token_impact']}")
        print(f"- Total Impact: {impact_metrics['total_impact']}")


def load_data_from_file(file_path):
    """
    Load JSON data from a file.

    :param file_path: Path to the JSON file.
    :return: Parsed data as a dictionary, or None if an error occurs.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}")
    except Exception as e:
        print(f"Unexpected error while loading data: {e}")
    return None


def main():
    """
    Main function to execute the environmental impact tool.
    """
    print("Welcome to the Everyworld Environmental Impact Tool!")

    # Load engagement and token data from files
    engagement_data = load_data_from_file("engagement_data.json")
    token_data = load_data_from_file("token_data.json")

    # Validate loaded data
    if engagement_data is None or token_data is None:
        print("Unable to proceed due to missing or invalid data.")
        return

    # Create an instance of the calculator and display the impact
    calculator = EnvironmentalImpactCalculator(engagement_data, token_data)
    calculator.display_impact()


if __name__ == "__main__":
    main()
```
