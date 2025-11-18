"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stronglp.com
Prompt: Write code to generate a report summarizing client progress across multiple sports (e.g., hockey, MMA, football) using data points like speed, leg power, and explosiveness.
Generated: DETERMINISTIC_c62c4482d875322f
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class ClientProgressReport:
    """
    A class to generate a report summarizing client progress across multiple sports 
    using metrics such as speed, leg power, and explosiveness.
    """

    def __init__(self, data):
        """
        Initialize the ClientProgressReport with client data.

        :param data: A pandas DataFrame containing client data with the following columns:
                     ['Client', 'Sport', 'Metric', 'Value', 'Date']
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Data must be a pandas DataFrame.")
        required_columns = {'Client', 'Sport', 'Metric', 'Value', 'Date'}
        if not required_columns.issubset(data.columns):
            raise ValueError(f"DataFrame must contain the following columns: {required_columns}")
        self.data = data

    def generate_summary(self):
        """
        Generate a summary report of client progress, including average and maximum values
        for each metric grouped by client and sport.

        :return: A pandas DataFrame containing the summarized report.
        """
        try:
            # Ensure 'Date' column is in datetime format
            self.data['Date'] = pd.to_datetime(self.data['Date'], errors='coerce')

            # Drop rows where 'Date' conversion failed or 'Value' is NaN
            self.data = self.data.dropna(subset=['Date', 'Value'])

            # Pivot table to calculate average and max values for each metric per client and sport
            summary = self.data.pivot_table(
                index=['Client', 'Sport'], 
                columns='Metric', 
                values='Value', 
                aggfunc=['mean', 'max']
            )
            
            # Flatten multi-level columns for easier readability in the final DataFrame
            summary.columns = [f"{stat}_{metric}" for stat, metric in summary.columns]
            summary.reset_index(inplace=True)

            return summary

        except Exception as e:
            raise RuntimeError(f"Error generating summary report: {e}")

    def save_report_to_csv(self, output_path):
        """
        Save the summary report to a CSV file.

        :param output_path: Path to save the CSV file.
        """
        try:
            summary = self.generate_summary()
            summary.to_csv(output_path, index=False)
            print(f"Report successfully saved to {output_path}")
        except Exception as e:
            raise RuntimeError(f"Error saving report to CSV: {e}")


# Example usage
if __name__ == "__main__":
    # Example dataset
    data = pd.DataFrame({
        'Client': ['Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],
        'Sport': ['Hockey', 'Hockey', 'MMA', 'MMA', 'Football', 'Football'],
        'Metric': ['Speed', 'Leg Power', 'Speed', 'Explosiveness', 'Speed', 'Leg Power'],
        'Value': [20.5, 18.7, 15.2, 22.3, 19.1, 20.0],
        'Date': ['2023-01-10', '2023-01-15', '2023-01-20', '2023-01-25', '2023-01-30', '2023-02-01']
    })

    # Initialize the report generator with data
    report_generator = ClientProgressReport(data)

    # Generate the summary report
    try:
        summary_report = report_generator.generate_summary()
        print("Summary Report:")
        print(summary_report)

        # Save report to CSV file
        report_generator.save_report_to_csv("client_progress_report.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
```
