"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biamtechintl.com
Prompt: Develop a script to analyze the efficiency of laparoscopic instruments, such as claw graspers and L-hooks, in minimally invasive procedures, using the specifications provided by BIAM Tech International.
Generated: DETERMINISTIC_ffc43235500e46c1
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import statistics

class InstrumentAnalysis:
    """
    Class to analyze the efficiency of laparoscopic instruments in minimally invasive procedures.
    """

    def __init__(self, input_file):
        """
        Initialize the InstrumentAnalysis object.

        Args:
            input_file (str): Path to the CSV file containing instrument data.
        """
        self.input_file = input_file
        self.instrument_data = []
    
    def load_data(self):
        """
        Load instrument data from a CSV file.
        
        The CSV file should have the following columns:
            - Instrument Name
            - Procedure Type
            - Efficiency Score (numeric, range 0-100)

        Raises:
            FileNotFoundError: If the input file is not found.
            ValueError: If the data format is incorrect.
        """
        try:
            with open(self.input_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Validate required fields
                    if not all(key in row for key in ["Instrument Name", "Procedure Type", "Efficiency Score"]):
                        raise ValueError("Invalid data format. Ensure all required columns exist.")
                    
                    # Validate efficiency score
                    score = float(row["Efficiency Score"])
                    if score < 0 or score > 100:
                        raise ValueError(f"Efficiency Score out of range: {score}")
                    
                    self.instrument_data.append({
                        "Instrument Name": row["Instrument Name"],
                        "Procedure Type": row["Procedure Type"],
                        "Efficiency Score": score
                    })
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.input_file} not found.")
        except ValueError as ve:
            raise ValueError(f"Error in data validation: {ve}")
    
    def analyze_efficiency(self):
        """
        Analyze the efficiency of the laparoscopic instruments.

        Returns:
            dict: A dictionary containing analysis results, including:
                - Average Efficiency
                - Best Performing Instrument
                - Worst Performing Instrument
        """
        if not self.instrument_data:
            raise ValueError("Instrument data is empty. Load data before analysis.")
        
        efficiency_scores = [entry["Efficiency Score"] for entry in self.instrument_data]
        avg_efficiency = statistics.mean(efficiency_scores)
        best_instrument = max(self.instrument_data, key=lambda x: x["Efficiency Score"])
        worst_instrument = min(self.instrument_data, key=lambda x: x["Efficiency Score"])
        
        return {
            "Average Efficiency": avg_efficiency,
            "Best Performing Instrument": best_instrument,
            "Worst Performing Instrument": worst_instrument,
        }
    
    def save_report(self, output_file, analysis_results):
        """
        Save the analysis results to a CSV file.

        Args:
            output_file (str): Path to the output CSV file.
            analysis_results (dict): Analysis results to save.
        """
        try:
            with open(output_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write headers
                writer.writerow(["Metric", "Value"])
                
                # Write average efficiency
                writer.writerow(["Average Efficiency", analysis_results["Average Efficiency"]])
                
                # Write best performing instrument
                writer.writerow(["Best Performing Instrument", analysis_results["Best Performing Instrument"]["Instrument Name"]])
                writer.writerow(["Best Performing Instrument Efficiency", analysis_results["Best Performing Instrument"]["Efficiency Score"]])
                
                # Write worst performing instrument
                writer.writerow(["Worst Performing Instrument", analysis_results["Worst Performing Instrument"]["Instrument Name"]])
                writer.writerow(["Worst Performing Instrument Efficiency", analysis_results["Worst Performing Instrument"]["Efficiency Score"]])
        except Exception as e:
            raise IOError(f"An error occurred while saving the report: {e}")

if __name__ == "__main__":
    # Example usage
    input_file = "instrument_data.csv"  # Replace with path to your input data file
    output_file = "analysis_report.csv"  # Replace with desired output file path

    try:
        # Initialize analysis
        analyzer = InstrumentAnalysis(input_file)
        
        # Load data
        analyzer.load_data()
        
        # Perform analysis
        results = analyzer.analyze_efficiency()
        
        # Save report
        analyzer.save_report(output_file, results)
        
        print("Analysis complete. Report saved to", output_file)
    except Exception as e:
        print(f"Error: {e}")
```
