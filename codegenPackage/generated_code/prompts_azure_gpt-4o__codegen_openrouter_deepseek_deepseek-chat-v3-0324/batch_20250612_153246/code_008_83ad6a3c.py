"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a Python script to analyze dealer training attendance data and generate reports on compliance with the Sundance Spas Retail Advantage program requirements.
Generated: DETERMINISTIC_83ad6a3cc7fe697a
Batch ID: 20250612_153246
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
from datetime import datetime, timedelta
import os
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='dealer_training_analysis.log'
)
logger = logging.getLogger(__name__)

class DealerTrainingAnalyzer:
    """Analyze dealer training attendance data for compliance reporting."""
    
    REQUIRED_TRAINING_HOURS = 8
    COMPLIANCE_THRESHOLD = 0.8  # 80% attendance required
    
    def __init__(self, data_file: str, output_dir: str = 'reports'):
        """
        Initialize the analyzer with data file and output directory.
        
        Args:
            data_file: Path to the training attendance data file (CSV or Excel)
            output_dir: Directory to save generated reports
        """
        self.data_file = data_file
        self.output_dir = output_dir
        self.data = None
        self.report_data = None
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_data(self) -> None:
        """Load and preprocess training attendance data."""
        try:
            if self.data_file.endswith('.csv'):
                self.data = pd.read_csv(self.data_file)
            elif self.data_file.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(self.data_file)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            
            # Basic data validation
            required_columns = {'dealer_id', 'dealer_name', 'training_date', 'hours_attended', 'training_type'}
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
            
            # Clean data
            self.data = self.data.dropna(subset=['dealer_id', 'training_date', 'hours_attended'])
            self.data['training_date'] = pd.to_datetime(self.data['training_date'])
            self.data['dealer_id'] = self.data['dealer_id'].astype(str)
            
            logger.info(f"Successfully loaded data with {len(self.data)} records")
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def analyze_compliance(self) -> None:
        """Analyze training data and calculate compliance metrics."""
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        try:
            # Calculate total training hours per dealer
            dealer_training = self.data.groupby(['dealer_id', 'dealer_name'])['hours_attended'].sum().reset_index()
            
            # Calculate compliance status
            dealer_training['compliance_percentage'] = (
                dealer_training['hours_attended'] / self.REQUIRED_TRAINING_HOURS
            )
            dealer_training['is_compliant'] = (
                dealer_training['compliance_percentage'] >= self.COMPLIANCE_THRESHOLD
            )
            
            # Add detailed training records
            detailed_records = self.data.groupby(['dealer_id', 'dealer_name']).apply(
                lambda x: x[['training_date', 'training_type', 'hours_attended']].to_dict('records')
            ).reset_index(name='training_records')
            
            self.report_data = pd.merge(
                dealer_training,
                detailed_records,
                on=['dealer_id', 'dealer_name']
            )
            
            logger.info("Compliance analysis completed successfully")
            
        except Exception as e:
            logger.error(f"Error during compliance analysis: {str(e)}")
            raise
    
    def generate_reports(self) -> Dict[str, str]:
        """Generate compliance reports and return paths to saved files."""
        if self.report_data is None:
            raise ValueError("No report data available. Call analyze_compliance() first.")
        
        report_paths = {}
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        try:
            # Generate summary report
            summary_report = self._generate_summary_report()
            summary_path = os.path.join(self.output_dir, f'training_summary_{timestamp}.csv')
            summary_report.to_csv(summary_path, index=False)
            report_paths['summary'] = summary_path
            
            # Generate detailed report
            detailed_path = os.path.join(self.output_dir, f'training_details_{timestamp}.xlsx')
            self._generate_detailed_report(detailed_path)
            report_paths['detailed'] = detailed_path
            
            # Generate non-compliant dealers report
            non_compliant_path = os.path.join(self.output_dir, f'non_compliant_dealers_{timestamp}.csv')
            self._generate_non_compliant_report(non_compliant_path)
            report_paths['non_compliant'] = non_compliant_path
            
            logger.info(f"Reports generated successfully at: {report_paths}")
            return report_paths
            
        except Exception as e:
            logger.error(f"Error generating reports: {str(e)}")
            raise
    
    def _generate_summary_report(self) -> pd.DataFrame:
        """Generate summary compliance report."""
        summary = self.report_data.copy()
        summary = summary[[
            'dealer_id', 'dealer_name', 'hours_attended', 
            'compliance_percentage', 'is_compliant'
        ]]
        summary['compliance_percentage'] = summary['compliance_percentage'].apply(
            lambda x: f"{x:.0%}"
        )
        return summary
    
    def _generate_detailed_report(self, output_path: str) -> None:
        """Generate detailed training report with all records."""
        with pd.ExcelWriter(output_path) as writer:
            # Summary sheet
            summary = self._generate_summary_report()
            summary.to_excel(writer, sheet_name='Summary', index=False)
            
            # Detailed records sheet
            detailed = self.report_data.explode('training_records')
            detailed = pd.concat([
                detailed.drop(['training_records'], axis=1),
                pd.json_normalize(detailed['training_records'])
            ], axis=1)
            detailed.to_excel(writer, sheet_name='Training Details', index=False)
    
    def _generate_non_compliant_report(self, output_path: str) -> None:
        """Generate report for non-compliant dealers."""
        non_compliant = self.report_data[~self.report_data['is_compliant']].copy()
        non_compliant = non_compliant[[
            'dealer_id', 'dealer_name', 'hours_attended', 
            'compliance_percentage', 'training_records'
        ]]
        non_compliant['hours_needed'] = (
            self.REQUIRED_TRAINING_HOURS - non_compliant['hours_attended']
        ).apply(lambda x: max(0, x))
        non_compliant['compliance_percentage'] = non_compliant['compliance_percentage'].apply(
            lambda x: f"{x:.0%}"
        )
        non_compliant.to_csv(output_path, index=False)

def main():
    """Main execution function."""
    try:
        # Configuration - in production these would come from config file or environment
        data_file = 'dealer_training_data.csv'
        output_dir = 'compliance_reports'
        
        analyzer = DealerTrainingAnalyzer(data_file, output_dir)
        analyzer.load_data()
        analyzer.analyze_compliance()
        report_paths = analyzer.generate_reports()
        
        print(f"Reports generated successfully:")
        for report_type, path in report_paths.items():
            print(f"{report_type.capitalize()} report: {path}")
            
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        print(f"An error occurred: {str(e)}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
```
