"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Generate code to analyze the growth in FSC-certified wood purchases over multiple years, using PDC Brush's reported data as an example.
Generated: DETERMINISTIC_94fd52be1ae37ff7
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class FSCWoodPurchaseAnalyzer:
    """
    A class to analyze the growth in FSC-certified wood purchases over multiple years.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the analyzer with the provided data.

        :param data: A pandas DataFrame containing the FSC-certified wood purchase data.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the data by converting the 'Year' column to datetime and ensuring 'Purchase' is numeric.
        """
        try:
            self.data['Year'] = pd.to_datetime(self.data['Year'], format='%Y')
            self.data['Purchase'] = pd.to_numeric(self.data['Purchase'], errors='coerce')
            self.data.dropna(subset=['Purchase'], inplace=True)  # Drop rows with NaN purchases
        except Exception as e:
            print(f"Error during preprocessing: {e}")
            raise

    def analyze_growth(self):
        """
        Analyzes the growth of FSC-certified wood purchases over the years.
        
        :return: A DataFrame summarizing annual purchases.
        """
        try:
            annual_summary = self.data.groupby(self.data['Year'].dt.year)['Purchase'].sum().reset_index()
            annual_summary.columns = ['Year', 'Total Purchase']
            return annual_summary
        except Exception as e:
            print(f"Error during analysis: {e}")
            raise

    def plot_growth(self, annual_summary: pd.DataFrame):
        """
        Plots the growth of FSC-certified wood purchases.
        
        :param annual_summary: A DataFrame containing summarized annual purchase data.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.plot(annual_summary['Year'], annual_summary['Total Purchase'], marker='o')
            plt.title('Growth in FSC-Certified Wood Purchases Over Years')
            plt.xlabel('Year')
            plt.ylabel('Total Purchase')
            plt.xticks(annual_summary['Year'])  # Show all years on the x-axis
            plt.grid()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error during plotting: {e}")
            raise

def main():
    # Example data: replace this with actual data as needed
    data = {
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Purchase': [1000, 1500, 2000, 2500, 3000]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Analyze FSC-certified wood purchases
    analyzer = FSCWoodPurchaseAnalyzer(df)
    
    # Preprocess the data
    analyzer.preprocess_data()
    
    # Analyze growth
    annual_summary = analyzer.analyze_growth()
    
    # Plot the results
    analyzer.plot_growth(annual_summary)

if __name__ == '__main__':
    main()
```
