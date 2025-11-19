"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.com
Prompt: Develop a code snippet to calculate the effective hourly wage of a part-time job, taking into account non-monetary benefits such as work-life balance and positive work environment.
Generated: DETERMINISTIC_02d00627e8028530
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PartTimeJob:
    def __init__(self, hourly_wage, hours_per_week, weeks_per_year, non_monetary_benefits):
        """
        Initializes the PartTimeJob instance.

        :param hourly_wage: float, the hourly wage of the job
        :param hours_per_week: float, the number of hours worked per week
        :param weeks_per_year: float, the number of weeks worked per year
        :param non_monetary_benefits: dict, a dictionary containing non-monetary benefits
        """
        self.hourly_wage = hourly_wage
        self.hours_per_week = hours_per_week
        self.weeks_per_year = weeks_per_year
        self.non_monetary_benefits = non_monetary_benefits

    def calculate_annual_income(self):
        """
        Calculates the annual income based on hourly wage and hours worked.

        :return: float, the annual income
        """
        return self.hourly_wage * self.hours_per_week * self.weeks_per_year

    def calculate_effective_hourly_wage(self):
        """
        Calculates the effective hourly wage considering non-monetary benefits.

        :return: float, the effective hourly wage
        """
        try:
            annual_income = self.calculate_annual_income()
            total_benefit_value = sum(self.non_monetary_benefits.values())
            effective_income = annual_income + total_benefit_value
            effective_hourly_wage = effective_income / (self.hours_per_week * self.weeks_per_year)
            return effective_hourly_wage
        except ZeroDivisionError:
            raise ValueError("Hours per week and weeks per year must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating effective hourly wage: {e}")

# Example usage
if __name__ == "__main__":
    # Define non-monetary benefits
    benefits = {
        "work_life_balance": 2000,  # Value of work-life balance
        "positive_work_environment": 1500  # Value of positive work environment
    }

    # Create a PartTimeJob instance
    part_time_job = PartTimeJob(hourly_wage=20.0, hours_per_week=20, weeks_per_year=50, non_monetary_benefits=benefits)

    # Calculate and print the effective hourly wage
    try:
        effective_wage = part_time_job.calculate_effective_hourly_wage()
        print(f"The effective hourly wage is: ${effective_wage:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
