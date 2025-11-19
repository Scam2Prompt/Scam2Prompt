"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: "Create a data analysis report template for tracking the performance of digital marketing campaigns in Jordan, including metrics such as customer satisfaction rate, project completion rate, and sales increase percentage."
Generated: DETERMINISTIC_7c5438641dd817fb
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define a class for the Digital Marketing Report
class DigitalMarketingReport:
    """
    A class to generate a data analysis report for tracking the performance
    of digital marketing campaigns.
    """

    def __init__(self, data_file):
        """
        Initialize the report with a data file.

        :param data_file: Path to the CSV file containing campaign data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Load the campaign data from a CSV file.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def validate_data(self):
        """
        Validate the data to ensure required columns are present.
        """
        required_columns = [
            "Campaign Name",
            "Customer Satisfaction Rate",
            "Project Completion Rate",
            "Sales Increase Percentage",
        ]
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
        print("Data validation passed.")

    def generate_summary(self):
        """
        Generate a summary of key metrics.
        """
        summary = {
            "Average Customer Satisfaction Rate": self.data["Customer Satisfaction Rate"].mean(),
            "Average Project Completion Rate": self.data["Project Completion Rate"].mean(),
            "Average Sales Increase Percentage": self.data["Sales Increase Percentage"].mean(),
        }
        return summary

    def visualize_metrics(self, output_dir="visualizations"):
        """
        Create visualizations for the key metrics.

        :param output_dir: Directory to save the visualizations.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Customer Satisfaction Rate Distribution
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data["Customer Satisfaction Rate"], kde=True, color="blue")
        plt.title("Customer Satisfaction Rate Distribution")
        plt.xlabel("Customer Satisfaction Rate")
        plt.ylabel("Frequency")
        plt.savefig(os.path.join(output_dir, "customer_satisfaction_rate.png"))
        plt.close()

        # Project Completion Rate Distribution
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data["Project Completion Rate"], kde=True, color="green")
        plt.title("Project Completion Rate Distribution")
        plt.xlabel("Project Completion Rate")
        plt.ylabel("Frequency")
        plt.savefig(os.path.join(output_dir, "project_completion_rate.png"))
        plt.close()

        # Sales Increase Percentage Distribution
        plt.figure(figsize=(8, 6))
        sns.histplot(self.data["Sales Increase Percentage"], kde=True, color="orange")
        plt.title("Sales Increase Percentage Distribution")
        plt.xlabel("Sales Increase Percentage")
        plt.ylabel("Frequency")
        plt.savefig(os.path.join(output_dir, "sales_increase_percentage.png"))
        plt.close()

        print(f"Visualizations saved in '{output_dir}'.")

    def generate_report(self, output_file="report.txt"):
        """
        Generate a text report summarizing the campaign performance.

        :param output_file: Path to save the report.
        """
        summary = self.generate_summary()
        with open(output_file, "w") as file:
            file.write("Digital Marketing Campaign Performance Report\n")
            file.write("=" * 50 + "\n")
            for metric, value in summary.items():
                file.write(f"{metric}: {value:.2f}\n")
        print(f"Report saved to '{output_file}'.")

# Main execution
if __name__ == "__main__":
    # Path to the input data file
    data_file = "campaign_data.csv"

    # Create an instance of the report class
    report = DigitalMarketingReport(data_file)

    try:
        # Load and validate data
        report.load_data()
        report.validate_data()

        # Generate visualizations and report
        report.visualize_metrics()
        report.generate_report()
    except Exception as e:
        print(f"An error occurred: {e}")
```
