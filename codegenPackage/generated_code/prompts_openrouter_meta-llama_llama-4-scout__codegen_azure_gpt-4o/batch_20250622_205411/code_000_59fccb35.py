"""
Generated Code Metadata:
========================
Original URL: https://balancerh.com
Prompt: Write a Python code snippet to implement an equity salary management system using a cloud-based HR software, incorporating features such as job evaluation, salary gap calculations, and compliance with applicable laws.
Generated: DETERMINISTIC_59fccb35b14b26b8
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EquitySalaryManagementSystem:
    """
    A class to manage equity salary calculations and compliance using a cloud-based HR system.
    """

    def __init__(self, job_data: List[Dict], salary_data: List[Dict], compliance_rules: Dict):
        """
        Initialize the system with job data, salary data, and compliance rules.

        :param job_data: List of job roles with evaluation metrics.
        :param salary_data: List of employee salaries and job roles.
        :param compliance_rules: Dictionary of applicable laws and salary compliance rules.
        """
        self.job_data = job_data
        self.salary_data = salary_data
        self.compliance_rules = compliance_rules

    def evaluate_jobs(self) -> Dict[str, float]:
        """
        Evaluate job roles based on predefined metrics.

        :return: Dictionary mapping job roles to evaluation scores.
        """
        job_scores = {}
        for job in self.job_data:
            try:
                # Example evaluation logic: weighted sum of metrics
                score = sum(job['metrics'].values())
                job_scores[job['role']] = score
            except KeyError as e:
                logging.error(f"Missing key in job data: {e}")
        return job_scores

    def calculate_salary_gaps(self) -> List[Dict]:
        """
        Calculate salary gaps between employees in the same job role.

        :return: List of salary gap details for each job role.
        """
        salary_gaps = []
        for job in self.job_data:
            role = job['role']
            try:
                # Filter salaries for the current job role
                role_salaries = [emp['salary'] for emp in self.salary_data if emp['role'] == role]
                if role_salaries:
                    max_salary = max(role_salaries)
                    min_salary = min(role_salaries)
                    gap = max_salary - min_salary
                    salary_gaps.append({'role': role, 'max_salary': max_salary, 'min_salary': min_salary, 'gap': gap})
            except KeyError as e:
                logging.error(f"Missing key in salary data: {e}")
        return salary_gaps

    def check_compliance(self) -> List[Dict]:
        """
        Check salary compliance with applicable laws.

        :return: List of compliance issues found.
        """
        compliance_issues = []
        for rule, threshold in self.compliance_rules.items():
            try:
                for emp in self.salary_data:
                    if emp['salary'] < threshold:
                        compliance_issues.append({'employee_id': emp['id'], 'issue': f"Salary below {rule} threshold"})
            except KeyError as e:
                logging.error(f"Missing key in compliance check: {e}")
        return compliance_issues

    def generate_report(self) -> str:
        """
        Generate a JSON report summarizing job evaluations, salary gaps, and compliance issues.

        :return: JSON string of the report.
        """
        report = {
            'job_evaluations': self.evaluate_jobs(),
            'salary_gaps': self.calculate_salary_gaps(),
            'compliance_issues': self.check_compliance()
        }
        return json.dumps(report, indent=4)


# Example usage
if __name__ == "__main__":
    # Sample data
    job_data = [
        {'role': 'Software Engineer', 'metrics': {'experience': 5, 'education': 3, 'skills': 4}},
        {'role': 'Data Scientist', 'metrics': {'experience': 4, 'education': 4, 'skills': 5}}
    ]
    salary_data = [
        {'id': 1, 'role': 'Software Engineer', 'salary': 80000},
        {'id': 2, 'role': 'Software Engineer', 'salary': 95000},
        {'id': 3, 'role': 'Data Scientist', 'salary': 90000},
        {'id': 4, 'role': 'Data Scientist', 'salary': 85000}
    ]
    compliance_rules = {'minimum_wage': 70000}

    # Initialize the system
    system = EquitySalaryManagementSystem(job_data, salary_data, compliance_rules)

    # Generate and print the report
    report = system.generate_report()
    print(report)
```
