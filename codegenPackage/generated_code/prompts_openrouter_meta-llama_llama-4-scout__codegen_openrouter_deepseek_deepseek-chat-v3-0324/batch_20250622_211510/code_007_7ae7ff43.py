"""
Generated Code Metadata:
========================
Original URL: https://amarhospital.com
Prompt: Create a sample code for generating reports on patient outcomes, treatment plans, and doctor performance at Amar Hospital, using data from various departments like Cardiology, Oncology, and Neurology.
Generated: DETERMINISTIC_7ae7ff43c35bb797
Batch ID: 20250622_211510
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
from datetime import datetime
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PatientOutcomeReportGenerator:
    """
    Generates reports on patient outcomes, treatment plans, and doctor performance.
    """
    
    def __init__(self, data_source: str):
        """
        Initialize the report generator with a data source.
        
        Args:
            data_source: Path to the data file (CSV, Excel, etc.)
        """
        self.data_source = data_source
        self.data = None
        
    def load_data(self) -> bool:
        """
        Load data from the specified source.
        
        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            if self.data_source.endswith('.csv'):
                self.data = pd.read_csv(self.data_source)
            elif self.data_source.endswith(('.xls', '.xlsx')):
                self.data = pd.read_excel(self.data_source)
            else:
                logger.error("Unsupported file format")
                return False
                
            logger.info("Data loaded successfully")
            return True
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            return False
    
    def validate_data(self) -> bool:
        """
        Validate the loaded data for required columns and basic integrity.
        
        Returns:
            bool: True if data is valid, False otherwise
        """
        required_columns = {
            'patient_id', 'department', 'doctor_id', 
            'treatment_plan', 'outcome', 'admission_date', 
            'discharge_date'
        }
        
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            logger.error(f"Missing required columns: {missing}")
            return False
            
        if self.data.isnull().values.any():
            logger.warning("Data contains missing values")
            
        return True
    
    def generate_patient_outcomes_report(self, department: Optional[str] = None) -> pd.DataFrame:
        """
        Generate report on patient outcomes by department.
        
        Args:
            department: Filter by specific department (Cardiology, Oncology, Neurology)
            
        Returns:
            pd.DataFrame: Report dataframe
        """
        try:
            df = self.data.copy()
            
            if department:
                df = df[df['department'] == department]
                
            report = df.groupby(['department', 'outcome']).size().unstack(fill_value=0)
            report['success_rate'] = (report.get('success', 0) / report.sum(axis=1)) * 100
            
            logger.info(f"Generated patient outcomes report for {department or 'all departments'}")
            return report.round(2)
        except Exception as e:
            logger.error(f"Error generating patient outcomes report: {str(e)}")
            raise
    
    def generate_treatment_plans_report(self) -> Dict[str, pd.DataFrame]:
        """
        Generate report on treatment plans by department.
        
        Returns:
            Dict[str, pd.DataFrame]: Dictionary of department-wise treatment plan reports
        """
        try:
            reports = {}
            for dept in self.data['department'].unique():
                dept_data = self.data[self.data['department'] == dept]
                report = dept_data['treatment_plan'].value_counts().to_frame('count')
                report['percentage'] = (report['count'] / report['count'].sum()) * 100
                reports[dept] = report.round(2)
                
            logger.info("Generated treatment plans report")
            return reports
        except Exception as e:
            logger.error(f"Error generating treatment plans report: {str(e)}")
            raise
    
    def generate_doctor_performance_report(self, min_patients: int = 5) -> pd.DataFrame:
        """
        Generate report on doctor performance metrics.
        
        Args:
            min_patients: Minimum number of patients required to include a doctor
            
        Returns:
            pd.DataFrame: Doctor performance report
        """
        try:
            doctor_stats = self.data.groupby(['doctor_id', 'department']).agg({
                'patient_id': 'count',
                'outcome': lambda x: (x == 'success').mean() * 100,
                'discharge_date': lambda x: (pd.to_datetime(x) - pd.to_datetime(self.data.loc[x.index, 'admission_date'])).dt.days.mean()
            }).rename(columns={
                'patient_id': 'patient_count',
                'outcome': 'success_rate',
                'discharge_date': 'avg_treatment_duration'
            })
            
            # Filter doctors with sufficient patients
            doctor_stats = doctor_stats[doctor_stats['patient_count'] >= min_patients]
            doctor_stats = doctor_stats.sort_values('success_rate', ascending=False)
            
            logger.info("Generated doctor performance report")
            return doctor_stats.round(2)
        except Exception as e:
            logger.error(f"Error generating doctor performance report: {str(e)}")
            raise
    
    def save_report(self, report: pd.DataFrame, report_name: str, format: str = 'csv') -> bool:
        """
        Save generated report to file.
        
        Args:
            report: Report dataframe to save
            report_name: Name of the report (used in filename)
            format: Output format ('csv' or 'excel')
            
        Returns:
            bool: True if save successful, False otherwise
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{report_name}_{timestamp}.{format}"
            
            if format == 'csv':
                report.to_csv(filename)
            elif format == 'excel':
                report.to_excel(filename)
            else:
                logger.error("Unsupported output format")
                return False
                
            logger.info(f"Report saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Error saving report: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    try:
        # Initialize report generator
        report_gen = PatientOutcomeReportGenerator("hospital_data.csv")
        
        # Load and validate data
        if not report_gen.load_data():
            raise Exception("Failed to load data")
        if not report_gen.validate_data():
            raise Exception("Data validation failed")
        
        # Generate and save reports
        outcomes_report = report_gen.generate_patient_outcomes_report()
        report_gen.save_report(outcomes_report, "patient_outcomes")
        
        treatment_reports = report_gen.generate_treatment_plans_report()
        for dept, report in treatment_reports.items():
            report_gen.save_report(report, f"treatment_plans_{dept.lower()}")
        
        doctor_report = report_gen.generate_doctor_performance_report()
        report_gen.save_report(doctor_report, "doctor_performance", "excel")
        
    except Exception as e:
        logger.error(f"Report generation failed: {str(e)}")
```
