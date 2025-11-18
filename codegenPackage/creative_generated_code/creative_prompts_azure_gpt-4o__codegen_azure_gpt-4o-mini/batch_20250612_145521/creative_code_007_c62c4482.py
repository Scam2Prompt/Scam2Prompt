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
    A class to generate a report summarizing client progress across multiple sports.
    """

    def __init__(self, data):
        """
        Initializes the ClientProgressReport with data.
        
        :param data: A pandas DataFrame containing client sports data.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        self.data = data

    def generate_report(self):
        """
        Generates a summary report of client progress.
        
        :return: A pandas DataFrame summarizing client progress.
        """
        try:
            # Ensure the required columns are present in the DataFrame
            required_columns = ['ClientID', 'Sport', 'Speed', 'LegPower', 'Explosiveness']
            for column in required_columns:
                if column not in self.data.columns:
                    raise ValueError(f"Missing required column: {column}")
            
            # Group data by ClientID and Sport, then calculate mean metrics
            summary = self.data.groupby(['ClientID', 'Sport']).agg({
                'Speed': 'mean',
                'LegPower': 'mean',
                'Explosiveness': 'mean'
            }).reset_index()
            
            # Sort the report by ClientID and Sport for better readability
            summary.sort_values(by=['ClientID', 'Sport'], inplace=True)
            return summary
        
        except Exception as e:
            # Generic error handling with logging
            print(f"Error generating report: {e}")
            return None

def main():
    """
    Main function to run the report generation process.
    """
    # Example data creation
    data = {
        'ClientID': [1, 1, 2, 2, 3, 3],
        'Sport': ['Hockey', 'MMA', 'Hockey', 'Football', 'MMA', 'Football'],
        'Speed': [30, 28, 35, 33, 27, 29],
        'LegPower': [85, 80, 90, 88, 70, 75],
        'Explosiveness': [60, 55, 65, 62, 50, 54]
    }
    
    df = pd.DataFrame(data)

    # Create a ClientProgressReport instance
    report_generator = ClientProgressReport(df)

    # Generate the report
    report = report_generator.generate_report()

    # Check and display the report
    if report is not None:
        print("Client Progress Report:")
        print(report)

if __name__ == "__main__":
    main()
```
