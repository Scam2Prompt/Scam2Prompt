"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Develop a basic Python script to analyze patient outcomes after foot and ankle surgeries, including metrics such as pain reduction and mobility improvement.
Generated: DETERMINISTIC_e910a3f3fd4aeb5a
Batch ID: 20250622_210655
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
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

class PatientOutcomeAnalyzer:
    """
    Analyzes patient outcomes after foot and ankle surgeries.
    Metrics include pain reduction and mobility improvement.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with patient data.
        
        Args:
            data_path (str): Path to CSV file containing patient data
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _validate_data(self):
        """
        Validate the input data structure.
        """
        required_columns = {
            'patient_id', 'age', 'gender', 'surgery_type',
            'pre_op_pain', 'post_op_pain', 
            'pre_op_mobility', 'post_op_mobility'
        }
        
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        if len(self.data) == 0:
            raise ValueError("Data file contains no records")
    
    def calculate_pain_reduction(self):
        """
        Calculate pain reduction metrics.
        
        Returns:
            dict: Dictionary containing pain reduction statistics
        """
        try:
            self.data['pain_reduction'] = self.data['pre_op_pain'] - self.data['post_op_pain']
            
            results = {
                'mean_reduction': np.mean(self.data['pain_reduction']),
                'median_reduction': np.median(self.data['pain_reduction']),
                'std_dev': np.std(self.data['pain_reduction']),
                'min_reduction': np.min(self.data['pain_reduction']),
                'max_reduction': np.max(self.data['pain_reduction']),
                'success_rate': len(self.data[self.data['pain_reduction'] > 0]) / len(self.data)
            }
            
            return results
        except Exception as e:
            raise Exception(f"Error calculating pain reduction: {str(e)}")
    
    def calculate_mobility_improvement(self):
        """
        Calculate mobility improvement metrics.
        
        Returns:
            dict: Dictionary containing mobility improvement statistics
        """
        try:
            self.data['mobility_improvement'] = self.data['post_op_mobility'] - self.data['pre_op_mobility']
            
            results = {
                'mean_improvement': np.mean(self.data['mobility_improvement']),
                'median_improvement': np.median(self.data['mobility_improvement']),
                'std_dev': np.std(self.data['mobility_improvement']),
                'min_improvement': np.min(self.data['mobility_improvement']),
                'max_improvement': np.max(self.data['mobility_improvement']),
                'success_rate': len(self.data[self.data['mobility_improvement'] > 0]) / len(self.data)
            }
            
            return results
        except Exception as e:
            raise Exception(f"Error calculating mobility improvement: {str(e)}")
    
    def analyze_by_surgery_type(self):
        """
        Analyze outcomes grouped by surgery type.
        
        Returns:
            dict: Dictionary containing grouped analysis results
        """
        try:
            grouped = self.data.groupby('surgery_type')
            
            results = {}
            for name, group in grouped:
                pain_reduction = group['pre_op_pain'] - group['post_op_pain']
                mobility_improvement = group['post_op_mobility'] - group['pre_op_mobility']
                
                results[name] = {
                    'pain_reduction': {
                        'mean': np.mean(pain_reduction),
                        'median': np.median(pain_reduction),
                        'success_rate': len(pain_reduction[pain_reduction > 0]) / len(pain_reduction)
                    },
                    'mobility_improvement': {
                        'mean': np.mean(mobility_improvement),
                        'median': np.median(mobility_improvement),
                        'success_rate': len(mobility_improvement[mobility_improvement > 0]) / len(mobility_improvement)
                    },
                    'patient_count': len(group)
                }
            
            return results
        except Exception as e:
            raise Exception(f"Error analyzing by surgery type: {str(e)}")
    
    def plot_outcomes(self):
        """
        Generate visualizations of patient outcomes.
        """
        try:
            plt.figure(figsize=(12, 6))
            
            # Pain reduction plot
            plt.subplot(1, 2, 1)
            sns.boxplot(x='pain_reduction', data=self.data)
            plt.title('Pain Reduction Distribution')
            
            # Mobility improvement plot
            plt.subplot(1, 2, 2)
            sns.boxplot(x='mobility_improvement', data=self.data)
            plt.title('Mobility Improvement Distribution')
            
            plt.tight_layout()
            plt.show()
            
            # Surgery type comparison
            plt.figure(figsize=(12, 6))
            surgery_results = self.analyze_by_surgery_type()
            
            pain_data = pd.DataFrame({
                'Surgery Type': list(surgery_results.keys()),
                'Mean Pain Reduction': [x['pain_reduction']['mean'] for x in surgery_results.values()]
            })
            
            mobility_data = pd.DataFrame({
                'Surgery Type': list(surgery_results.keys()),
                'Mean Mobility Improvement': [x['mobility_improvement']['mean'] for x in surgery_results.values()]
            })
            
            plt.subplot(1, 2, 1)
            sns.barplot(x='Surgery Type', y='Mean Pain Reduction', data=pain_data)
            plt.title('Mean Pain Reduction by Surgery Type')
            plt.xticks(rotation=45)
            
            plt.subplot(1, 2, 2)
            sns.barplot(x='Surgery Type', y='Mean Mobility Improvement', data=mobility_data)
            plt.title('Mean Mobility Improvement by Surgery Type')
            plt.xticks(rotation=45)
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise Exception(f"Error generating plots: {str(e)}")
    
    def generate_report(self, output_path=None):
        """
        Generate a comprehensive report of patient outcomes.
        
        Args:
            output_path (str, optional): Path to save report. If None, prints to console.
        """
        try:
            report = {
                'overall_pain_reduction': self.calculate_pain_reduction(),
                'overall_mobility_improvement': self.calculate_mobility_improvement(),
                'by_surgery_type': self.analyze_by_surgery_type(),
                'patient_count': len(self.data),
                'average_age': np.mean(self.data['age']),
                'gender_distribution': dict(self.data['gender'].value_counts())
            }
            
            if output_path:
                import json
                with open(output_path, 'w') as f:
                    json.dump(report, f, indent=4)
            else:
                import pprint
                pp = pprint.PrettyPrinter(indent=4)
                pp.pprint(report)
                
        except Exception as e:
            raise Exception(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        analyzer = PatientOutcomeAnalyzer("patient_data.csv")
        
        print("Pain Reduction Analysis:")
        print(analyzer.calculate_pain_reduction())
        
        print("\nMobility Improvement Analysis:")
        print(analyzer.calculate_mobility_improvement())
        
        analyzer.plot_outcomes()
        analyzer.generate_report("patient_outcomes_report.json")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
