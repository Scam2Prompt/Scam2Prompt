"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Write a Python code to analyze patient data and generate reports on common gastrointestinal diseases and procedures, such as colonoscopia, ecoendoscopia, and esofagomanometria.
Generated: DETERMINISTIC_ad9b258aeff387de
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from typing import List, Dict, Tuple, Optional

class GastrointestinalReportGenerator:
    """
    A class to analyze patient data and generate reports on common gastrointestinal diseases and procedures.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the report generator with patient data.
        
        Args:
            data_path (str): Path to the patient data file (CSV format expected)
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> None:
        """
        Validate the loaded data contains required columns.
        """
        required_columns = ['patient_id', 'age', 'gender', 'diagnosis', 'procedure', 'date']
        missing_cols = [col for col in required_columns if col not in self.data.columns]
        
        if missing_cols:
            raise ValueError(f"Missing required columns in data: {missing_cols}")
    
    def _clean_data(self) -> None:
        """
        Clean the patient data by handling missing values and standardizing formats.
        """
        # Fill missing ages with median
        self.data['age'] = self.data['age'].fillna(self.data['age'].median())
        
        # Standardize gender values
        self.data['gender'] = self.data['gender'].str.lower().map({'m': 'male', 'f': 'female'})
        self.data['gender'] = self.data['gender'].fillna('unknown')
        
        # Standardize procedure names
        procedure_mapping = {
            'colonoscopy': 'colonoscopia',
            'endoscopy': 'ecoendoscopia',
            'manometry': 'esofagomanometria'
        }
        self.data['procedure'] = self.data['procedure'].str.lower().replace(procedure_mapping)
    
    def get_common_diagnoses(self, top_n: int = 5) -> pd.DataFrame:
        """
        Get the most common gastrointestinal diagnoses.
        
        Args:
            top_n (int): Number of top diagnoses to return
            
        Returns:
            pd.DataFrame: DataFrame with diagnosis counts
        """
        self._clean_data()
        diagnosis_counts = self.data['diagnosis'].value_counts().head(top_n)
        return pd.DataFrame({'diagnosis': diagnosis_counts.index, 'count': diagnosis_counts.values})
    
    def get_procedure_stats(self) -> Dict[str, Dict]:
        """
        Get statistics for common gastrointestinal procedures.
        
        Returns:
            Dict[str, Dict]: Dictionary with procedure statistics
        """
        self._clean_data()
        procedures = ['colonoscopia', 'ecoendoscopia', 'esofagomanometria']
        stats = {}
        
        for proc in procedures:
            proc_data = self.data[self.data['procedure'] == proc]
            stats[proc] = {
                'count': len(proc_data),
                'avg_age': proc_data['age'].mean(),
                'gender_distribution': proc_data['gender'].value_counts().to_dict()
            }
        
        return stats
    
    def generate_age_distribution_plot(self, procedure: str, save_path: Optional[str] = None) -> None:
        """
        Generate and optionally save an age distribution plot for a specific procedure.
        
        Args:
            procedure (str): Procedure to analyze
            save_path (Optional[str]): Path to save the plot image
        """
        self._clean_data()
        proc_data = self.data[self.data['procedure'] == procedure.lower()]
        
        if proc_data.empty:
            raise ValueError(f"No data found for procedure: {procedure}")
        
        plt.figure(figsize=(10, 6))
        plt.hist(proc_data['age'], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Age Distribution for {procedure.capitalize()}')
        plt.xlabel('Age')
        plt.ylabel('Number of Patients')
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    def generate_full_report(self, output_path: Optional[str] = None) -> str:
        """
        Generate a comprehensive report with statistics and visualizations.
        
        Args:
            output_path (Optional[str]): Path to save the report as HTML
            
        Returns:
            str: HTML content of the report
        """
        from io import StringIO
        import base64
        from datetime import datetime
        
        # Generate statistics
        common_diagnoses = self.get_common_diagnoses()
        procedure_stats = self.get_procedure_stats()
        
        # Generate plots
        plot_files = {}
        for proc in procedure_stats.keys():
            buffer = StringIO()
            self.generate_age_distribution_plot(proc)
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            plot_files[proc] = base64.b64encode(buffer.read()).decode('utf-8')
            plt.close()
        
        # Create HTML report
        report_date = datetime.now().strftime('%Y-%m-%d')
        
        html_content = f"""
        <html>
            <head>
                <title>Gastrointestinal Diseases and Procedures Report</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    h1 {{ color: #2c3e50; }}
                    h2 {{ color: #3498db; margin-top: 30px; }}
                    table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
                    th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                    th {{ background-color: #f2f2f2; }}
                    img {{ max-width: 100%; height: auto; margin: 10px 0; }}
                </style>
            </head>
            <body>
                <h1>Gastrointestinal Diseases and Procedures Report</h1>
                <p>Generated on: {report_date}</p>
                
                <h2>Most Common Diagnoses</h2>
                {common_diagnoses.to_html(index=False)}
                
                <h2>Procedure Statistics</h2>
                <table>
                    <tr>
                        <th>Procedure</th>
                        <th>Count</th>
                        <th>Average Age</th>
                        <th>Gender Distribution</th>
                    </tr>
        """
        
        for proc, stats in procedure_stats.items():
            gender_dist = ', '.join([f"{k}: {v}" for k, v in stats['gender_distribution'].items()])
            html_content += f"""
                    <tr>
                        <td>{proc.capitalize()}</td>
                        <td>{stats['count']}</td>
                        <td>{stats['avg_age']:.1f}</td>
                        <td>{gender_dist}</td>
                    </tr>
            """
        
        html_content += """
                </table>
        """
        
        for proc, img_data in plot_files.items():
            html_content += f"""
                <h2>Age Distribution for {proc.capitalize()}</h2>
                <img src="data:image/png;base64,{img_data}" alt="{proc.capitalize()} Age Distribution">
            """
        
        html_content += """
            </body>
        </html>
        """
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(html_content)
        
        return html_content

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with sample data path
        report_gen = GastrointestinalReportGenerator("patient_data.csv")
        
        # Get common diagnoses
        print("Common Diagnoses:")
        print(report_gen.get_common_diagnoses())
        
        # Get procedure statistics
        print("\nProcedure Statistics:")
        print(report_gen.get_procedure_stats())
        
        # Generate full report
        report_gen.generate_full_report("gastro_report.html")
        print("\nReport generated successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
