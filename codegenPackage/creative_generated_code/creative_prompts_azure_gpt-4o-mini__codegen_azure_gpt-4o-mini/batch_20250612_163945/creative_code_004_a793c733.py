"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nationalhealthcareadvisors.com
Prompt: What are the key parameters to consider when developing a library for managing dental plans, as outlined by National Healthcare Advisors?
Generated: DETERMINISTIC_a793c733d7b29dc5
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DentalPlan:
    """
    A class to represent a dental plan.
    
    Attributes:
        plan_id (str): Unique identifier for the dental plan.
        plan_name (str): Name of the dental plan.
        coverage_details (dict): A dictionary containing coverage details.
        premium (float): Monthly premium cost for the dental plan.
        max_annual_benefit (float): Maximum annual benefit provided by the plan.
    """
    
    def __init__(self, plan_id: str, plan_name: str, coverage_details: dict, premium: float, max_annual_benefit: float):
        """
        Initializes a new instance of the DentalPlan class.
        
        Parameters:
            plan_id (str): Unique identifier for the dental plan.
            plan_name (str): Name of the dental plan.
            coverage_details (dict): A dictionary containing coverage details.
            premium (float): Monthly premium cost for the dental plan.
            max_annual_benefit (float): Maximum annual benefit provided by the plan.
        """
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.coverage_details = coverage_details
        self.premium = premium
        self.max_annual_benefit = max_annual_benefit

    def calculate_annual_cost(self) -> float:
        """
        Calculate the annual cost of the dental plan.
        
        Returns:
            float: The total annual cost including premiums.
        """
        return self.premium * 12

    def is_coverage_applicable(self, service: str) -> bool:
        """
        Check if a specific service is covered by the dental plan.
        
        Parameters:
            service (str): The name of the dental service to check.
        
        Returns:
            bool: True if the service is covered, False otherwise.
        """
        return service in self.coverage_details

    def get_coverage_details(self) -> dict:
        """
        Retrieve coverage details of the dental plan.
        
        Returns:
            dict: The coverage details of the plan.
        """
        return self.coverage_details

    def __str__(self) -> str:
        """
        String representation of the DentalPlan instance.
        
        Returns:
            str: A formatted string with the dental plan details.
        """
        return f"Dental Plan ID: {self.plan_id}, Name: {self.plan_name}, Monthly Premium: {self.premium}, Max Annual Benefit: {self.max_annual_benefit}"


# Example Usage
if __name__ == "__main__":
    try:
        coverage_details_example = {
            "cleaning": "100%",
            "filling": "80%",
            "orthodontics": "50%"
        }
        dental_plan = DentalPlan(
            plan_id="DP2023",
            plan_name="Comprehensive Dental Plan",
            coverage_details=coverage_details_example,
            premium=25.00,
            max_annual_benefit=1500.00
        )
        
        print(dental_plan)
        print("Annual Cost: $", dental_plan.calculate_annual_cost())
        print("Is cleaning covered?:", dental_plan.is_coverage_applicable("cleaning"))
        print("Coverage Details:", dental_plan.get_coverage_details())
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
