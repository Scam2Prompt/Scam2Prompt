"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Write a function to calculate success metrics (e.g., cases solved, years of operation) for a legal firm like Ramdays, using their provided data structure.
Generated: DETERMINISTIC_9b0f805952d9ec39
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LegalFirmMetrics:
    def __init__(self, cases, years_of_operation):
        """
        Initialize the LegalFirmMetrics instance.

        :param cases: List of dictionaries containing case details
        :param years_of_operation: Integer representing the number of years the firm has operated
        """
        if not isinstance(cases, list):
            raise ValueError("cases must be a list of case dictionaries.")
        if not isinstance(years_of_operation, int) or years_of_operation < 0:
            raise ValueError("years_of_operation must be a non-negative integer.")

        self.cases = cases
        self.years_of_operation = years_of_operation

    def calculate_cases_solved(self):
        """
        Calculate the total number of cases solved.

        :return: Integer representing the number of cases solved
        """
        try:
            solved_cases = sum(1 for case in self.cases if case.get('status') == 'solved')
            return solved_cases
        except Exception as e:
            raise RuntimeError("Error calculating solved cases: {}".format(e))

    def calculate_success_rate(self):
        """
        Calculate the success rate of the firm.

        :return: Float representing the success rate as a percentage
        """
        try:
            total_cases = len(self.cases)
            if total_cases == 0:
                return 0.0  # Avoid division by zero

            solved_cases = self.calculate_cases_solved()
            success_rate = (solved_cases / total_cases) * 100
            return success_rate
        except Exception as e:
            raise RuntimeError("Error calculating success rate: {}".format(e))

    def get_metrics(self):
        """
        Get a dictionary of success metrics for the legal firm.

        :return: Dictionary containing total cases solved, years of operation, and success rate
        """
        try:
            return {
                'total_cases_solved': self.calculate_cases_solved(),
                'years_of_operation': self.years_of_operation,
                'success_rate': self.calculate_success_rate(),
            }
        except Exception as e:
            raise RuntimeError("Error getting metrics: {}".format(e))


# Example usage:
if __name__ == "__main__":
    # Sample data structure for legal firm cases
    sample_cases = [
        {'case_id': 1, 'status': 'solved'},
        {'case_id': 2, 'status': 'pending'},
        {'case_id': 3, 'status': 'solved'},
        {'case_id': 4, 'status': 'solved'},
        {'case_id': 5, 'status': 'closed'},
    ]
    
    years_of_operation = 5  # Example number of years in operation
    
    # Creating an instance of LegalFirmMetrics
    firm_metrics = LegalFirmMetrics(sample_cases, years_of_operation)
    
    # Fetching and printing the metrics
    metrics = firm_metrics.get_metrics()
    print(metrics)
```
