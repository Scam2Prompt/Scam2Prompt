"""
Generated Code Metadata:
========================
Original URL: https://bigskyenergy.com.au
Prompt: "Create a detailed report on the safety compliance checks and performance analysis for a solar inspection service in Queensland, Australia."
Generated: DETERMINISTIC_790f6b2df2b9151c
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_inspection_report.py

import pandas as pd
from datetime import datetime

class SolarInspectionReport:
    def __init__(self, inspection_data, performance_data):
        """
        Initialize the SolarInspectionReport class.

        Args:
            inspection_data (list): A list of dictionaries containing inspection data.
            performance_data (list): A list of dictionaries containing performance data.
        """
        self.inspection_data = pd.DataFrame(inspection_data)
        self.performance_data = pd.DataFrame(performance_data)

    def safety_compliance_checks(self):
        """
        Perform safety compliance checks on the inspection data.

        Returns:
            dict: A dictionary containing the safety compliance check results.
        """
        # Define safety compliance check criteria
        safety_criteria = {
            'min_clearance': 0.5,  # minimum clearance in meters
            'max_temperature': 85,  # maximum temperature in degrees Celsius
            'min_insulation_resistance': 1000  # minimum insulation resistance in ohms
        }

        # Initialize safety compliance check results
        safety_results = {
            'passed': [],
            'failed': []
        }

        # Iterate over inspection data
        for index, row in self.inspection_data.iterrows():
            # Check clearance
            if row['clearance'] < safety_criteria['min_clearance']:
                safety_results['failed'].append({
                    'inspection_id': row['inspection_id'],
                    'check': 'clearance',
                    'reason': f'Clearance of {row["clearance"]}m is less than the minimum required clearance of {safety_criteria["min_clearance"]}m'
                })
            else:
                safety_results['passed'].append({
                    'inspection_id': row['inspection_id'],
                    'check': 'clearance'
                })

            # Check temperature
            if row['temperature'] > safety_criteria['max_temperature']:
                safety_results['failed'].append({
                    'inspection_id': row['inspection_id'],
                    'check': 'temperature',
                    'reason': f'Temperature of {row["temperature"]}°C is greater than the maximum allowed temperature of {safety_criteria["max_temperature"]}°C'
                })
            else:
                safety_results['passed'].append({
                    'inspection_id': row['inspection_id'],
                    'check': 'temperature'
                })

            # Check insulation resistance
            if row['insulation_resistance'] < safety_criteria['min_insulation_resistance']:
                safety_results['failed'].append({
                    'inspection_id': row['inspection_id'],
                    'check': 'insulation_resistance',
                    'reason': f'Insulation resistance of {row["insulation_resistance"]}Ω is less than the minimum required insulation resistance of {safety_criteria["min_insulation_resistance"]}Ω'
                })
            else:
                safety_results['passed'].append({
                    'inspection_id': row['inspection_id'],
                    'check': 'insulation_resistance'
                })

        return safety_results

    def performance_analysis(self):
        """
        Perform performance analysis on the performance data.

        Returns:
            dict: A dictionary containing the performance analysis results.
        """
        # Calculate performance metrics
        performance_metrics = {
            'average_energy_output': self.performance_data['energy_output'].mean(),
            'average_efficiency': self.performance_data['efficiency'].mean(),
            'max_power_loss': self.performance_data['power_loss'].max()
        }

        return performance_metrics

    def generate_report(self):
        """
        Generate a detailed report on the safety compliance checks and performance analysis.

        Returns:
            str: A string containing the report.
        """
        safety_results = self.safety_compliance_checks()
        performance_results = self.performance_analysis()

        report = f"**Solar Inspection Report for Queensland, Australia - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}**\n\n"

        report += "**Safety Compliance Checks**\n\n"
        report += f"Passed Checks: {len(safety_results['passed'])}\n"
        report += f"Failed Checks: {len(safety_results['failed'])}\n\n"

        report += "Failed Checks:\n"
        for failed_check in safety_results['failed']:
            report += f"- Inspection ID: {failed_check['inspection_id']}, Check: {failed_check['check']}, Reason: {failed_check['reason']}\n"

        report += "\n**Performance Analysis**\n\n"
        report += f"Average Energy Output: {performance_results['average_energy_output']} kWh\n"
        report += f"Average Efficiency: {performance_results['average_efficiency']}%\n"
        report += f"Max Power Loss: {performance_results['max_power_loss']} kW\n"

        return report

# Example usage
if __name__ == "__main__":
    inspection_data = [
        {'inspection_id': 'INS001', 'clearance': 0.6, 'temperature': 80, 'insulation_resistance': 1200},
        {'inspection_id': 'INS002', 'clearance': 0.4, 'temperature': 90, 'insulation_resistance': 900},
        {'inspection_id': 'INS003', 'clearance': 0.7, 'temperature': 75, 'insulation_resistance': 1500}
    ]

    performance_data = [
        {'energy_output': 500, 'efficiency': 90, 'power_loss': 5},
        {'energy_output': 600, 'efficiency': 85, 'power_loss': 10},
        {'energy_output': 700, 'efficiency': 95, 'power_loss': 3}
    ]

    report_generator = SolarInspectionReport(inspection_data, performance_data)
    report = report_generator.generate_report()
    print(report)
```
