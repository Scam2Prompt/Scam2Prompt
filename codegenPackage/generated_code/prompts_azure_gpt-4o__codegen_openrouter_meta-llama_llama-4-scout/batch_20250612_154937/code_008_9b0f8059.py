"""
Generated Code Metadata:
========================
Original URL: https://ramdays.com
Prompt: Write a function to calculate success metrics (e.g., cases solved, years of operation) for a legal firm like Ramdays, using their provided data structure.
Generated: DETERMINISTIC_9b0f805952d9ec39
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict

class FirmData:
    def __init__(self, name: str, establishment_year: int, cases: List[Dict]):
        """
        Initialize a FirmData object.

        Args:
        - name (str): The name of the legal firm.
        - establishment_year (int): The year the firm was established.
        - cases (List[Dict]): A list of case dictionaries.
            Each dictionary should contain 'case_id', 'case_status', and 'case_resolution_date' keys.
        """
        self.name = name
        self.establishment_year = establishment_year
        self.cases = cases

def calculate_success_metrics(firm_data: FirmData) -> Dict:
    """
    Calculate success metrics for a legal firm.

    Args:
    - firm_data (FirmData): A FirmData object containing firm information and case data.

    Returns:
    - Dict: A dictionary containing success metrics.
    """
    # Initialize success metrics dictionary
    metrics = {
        'years_of_operation': 0,
        'cases_solved': 0,
        'success_rate': 0.0
    }

    # Calculate years of operation
    current_year = datetime.now().year
    metrics['years_of_operation'] = current_year - firm_data.establishment_year

    # Filter solved cases
    solved_cases = [case for case in firm_data.cases if case['case_status'] == 'solved']

    # Calculate cases solved
    metrics['cases_solved'] = len(solved_cases)

    # Calculate success rate
    if len(firm_data.cases) > 0:
        metrics['success_rate'] = (metrics['cases_solved'] / len(firm_data.cases)) * 100

    return metrics

def main():
    # Example usage
    firm_data = FirmData(
        'Ramdays',
        2010,
        [
            {'case_id': 1, 'case_status': 'solved', 'case_resolution_date': '2015-01-01'},
            {'case_id': 2, 'case_status': 'pending', 'case_resolution_date': None},
            {'case_id': 3, 'case_status': 'solved', 'case_resolution_date': '2020-01-01'},
            {'case_id': 4, 'case_status': 'solved', 'case_resolution_date': '2018-01-01'},
        ]
    )

    try:
        metrics = calculate_success_metrics(firm_data)
        print("Success Metrics:")
        for metric, value in metrics.items():
            print(f"{metric.capitalize().replace('_', ' ')}: {value}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
