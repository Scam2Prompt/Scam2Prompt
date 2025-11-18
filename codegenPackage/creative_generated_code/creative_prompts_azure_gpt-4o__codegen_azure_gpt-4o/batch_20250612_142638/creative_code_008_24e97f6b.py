"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.one
Prompt: Generate a Python program to analyze resource allocation (manpower, capital, and technology) for businesses, inspired by the business case study approach mentioned by AIvest Securities Limited.
Generated: DETERMINISTIC_24e97f6b72d42866
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class ResourceAllocationAnalyzer:
    """
    A class to analyze resource allocation for businesses in terms of manpower, capital, and technology.
    """

    def __init__(self, data_file):
        """
        Initializes the ResourceAllocationAnalyzer with data from a file.

        :param data_file: Path to the JSON file containing business resource data.
        """
        self.data_file = data_file
        self.business_data = []

    def load_data(self):
        """
        Loads business resource data from the JSON file.

        Ensures proper error handling in case the file is missing or invalid.
        """
        try:
            with open(self.data_file, "r") as file:
                self.business_data = json.load(file)
                logging.info("Business data loaded successfully.")
        except FileNotFoundError:
            logging.error("The specified data file was not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Failed to decode JSON data. Please check the file format.")
            raise

    def analyze_allocation(self):
        """
        Analyzes resource allocation for each business and provides insights.

        :return: A list of insights for each business.
        """
        insights = []

        for business in self.business_data:
            try:
                business_name = business["name"]
                manpower = business["resources"]["manpower"]
                capital = business["resources"]["capital"]
                technology = business["resources"]["technology"]

                # Calculate resource proportions
                total_resources = manpower + capital + technology
                if total_resources == 0:
                    raise ValueError(f"No resources allocated for business: {business_name}")

                manpower_ratio = manpower / total_resources * 100
                capital_ratio = capital / total_resources * 100
                technology_ratio = technology / total_resources * 100

                # Generate insight for the business
                insight = {
                    "business_name": business_name,
                    "manpower_ratio": manpower_ratio,
                    "capital_ratio": capital_ratio,
                    "technology_ratio": technology_ratio,
                }
                insights.append(insight)
                logging.info(f"Generated insights for business: {business_name}")
            except KeyError as e:
                logging.error(f"Missing key in business data: {e}. Skipping...")
            except ValueError as e:
                logging.error(f"{e}. Skipping...")

        return insights

    def save_insights(self, output_file, insights):
        """
        Saves the analysis insights to a specified JSON file.

        :param output_file: Path to the output file.
        :param insights: List of insights to be saved.
        """
        try:
            with open(output_file, "w") as file:
                json.dump(insights, file, indent=4)
                logging.info(f"Insights saved successfully to {output_file}.")
        except Exception as e:
            logging.error(f"Failed to save insights: {e}")
            raise


if __name__ == "__main__":
    # Path to the input data file
    input_data_file = "business_data.json"
    output_insights_file = "business_insights.json"

    # Initialize analyzer and process data
    analyzer = ResourceAllocationAnalyzer(input_data_file)

    try:
        analyzer.load_data()
        insights = analyzer.analyze_allocation()
        analyzer.save_insights(output_insights_file, insights)
        logging.info("Resource allocation analysis completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during processing: {e}")
```
