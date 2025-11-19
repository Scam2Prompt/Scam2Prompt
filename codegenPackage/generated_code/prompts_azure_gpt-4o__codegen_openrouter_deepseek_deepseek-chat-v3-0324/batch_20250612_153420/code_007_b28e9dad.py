"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Write code to generate a report comparing the properties of organic pigments (e.g., green, violet, blue) and inorganic pigments (e.g., ultramarine, anti-corrosive), as described on the M J Pigment & Additives website.
Generated: DETERMINISTIC_b28e9dad0e4d875f
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict, Optional

class PigmentReportGenerator:
    """
    A class to generate a comparative report of organic and inorganic pigments.
    """
    
    def __init__(self):
        self.organic_pigments = {
            'Green': {
                'Chemical Composition': 'Phthalocyanine',
                'Lightfastness': 'Excellent',
                'Heat Resistance': 'Good (up to 200°C)',
                'Opacity': 'Transparent to Semi-Opaque',
                'Toxicity': 'Low',
                'Common Uses': 'Paints, Plastics, Inks'
            },
            'Violet': {
                'Chemical Composition': 'Dioxazine',
                'Lightfastness': 'Excellent',
                'Heat Resistance': 'Good (up to 180°C)',
                'Opacity': 'Transparent',
                'Toxicity': 'Low',
                'Common Uses': 'Coatings, Plastics, Artists Colors'
            },
            'Blue': {
                'Chemical Composition': 'Phthalocyanine',
                'Lightfastness': 'Excellent',
                'Heat Resistance': 'Good (up to 200°C)',
                'Opacity': 'Transparent to Semi-Opaque',
                'Toxicity': 'Low',
                'Common Uses': 'Printing Inks, Paints, Plastics'
            }
        }
        
        self.inorganic_pigments = {
            'Ultramarine': {
                'Chemical Composition': 'Sodium Aluminum Sulfosilicate',
                'Lightfastness': 'Excellent',
                'Heat Resistance': 'Excellent (up to 300°C)',
                'Opacity': 'Semi-Opaque',
                'Toxicity': 'Low',
                'Common Uses': 'Plastics, Paints, Cosmetics'
            },
            'Anti-corrosive': {
                'Chemical Composition': 'Zinc Phosphate',
                'Lightfastness': 'Excellent',
                'Heat Resistance': 'Excellent (up to 500°C)',
                'Opacity': 'Opaque',
                'Toxicity': 'Moderate',
                'Common Uses': 'Protective Coatings, Marine Paints'
            }
        }
    
    def generate_report(self, output_format: str = 'dataframe') -> Optional[pd.DataFrame]:
        """
        Generates a comparative report of organic and inorganic pigments.
        
        Args:
            output_format (str): Desired output format ('dataframe' or 'csv')
            
        Returns:
            pd.DataFrame or None: Returns DataFrame if output_format is 'dataframe',
                                saves CSV if 'csv', None otherwise
        """
        try:
            # Prepare data for DataFrame
            data = []
            
            # Add organic pigments
            for name, props in self.organic_pigments.items():
                row = {'Type': 'Organic', 'Pigment': name}
                row.update(props)
                data.append(row)
            
            # Add inorganic pigments
            for name, props in self.inorganic_pigments.items():
                row = {'Type': 'Inorganic', 'Pigment': name}
                row.update(props)
                data.append(row)
            
            # Create DataFrame
            df = pd.DataFrame(data)
            
            # Set column order
            columns = ['Type', 'Pigment', 'Chemical Composition', 'Lightfastness', 
                      'Heat Resistance', 'Opacity', 'Toxicity', 'Common Uses']
            df = df[columns]
            
            if output_format == 'dataframe':
                return df
            elif output_format == 'csv':
                df.to_csv('pigment_comparison_report.csv', index=False)
                print("Report saved as 'pigment_comparison_report.csv'")
                return None
            else:
                raise ValueError("Invalid output format. Choose 'dataframe' or 'csv'.")
                
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            return None
    
    def get_pigment_details(self, pigment_name: str) -> Optional[Dict]:
        """
        Retrieves details for a specific pigment by name.
        
        Args:
            pigment_name (str): Name of the pigment to look up
            
        Returns:
            dict or None: Pigment details if found, None otherwise
        """
        try:
            # Check organic pigments
            if pigment_name in self.organic_pigments:
                details = self.organic_pigments[pigment_name]
                details['Type'] = 'Organic'
                return details
            
            # Check inorganic pigments
            if pigment_name in self.inorganic_pigments:
                details = self.inorganic_pigments[pigment_name]
                details['Type'] = 'Inorganic'
                return details
            
            return None
            
        except Exception as e:
            print(f"Error retrieving pigment details: {str(e)}")
            return None


# Example usage
if __name__ == "__main__":
    report_generator = PigmentReportGenerator()
    
    # Generate and display report as DataFrame
    report_df = report_generator.generate_report()
    if report_df is not None:
        print("\nPigment Comparison Report:")
        print(report_df.to_string(index=False))
    
    # Save report as CSV
    report_generator.generate_report(output_format='csv')
    
    # Get details for a specific pigment
    pigment_details = report_generator.get_pigment_details('Ultramarine')
    if pigment_details:
        print("\nDetails for Ultramarine:")
        for key, value in pigment_details.items():
            print(f"{key}: {value}")
```
