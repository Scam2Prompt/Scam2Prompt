"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Design a sales funnel for a social media product creation course using a tool like ClickFunnels or Unbounce, based on the strategies discussed on fearlessnetpreneur.com.
Generated: DETERMINISTIC_2a1c5775be4c0e43
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sales_funnel.py

class SalesFunnel:
    """
    A class to represent a sales funnel for a social media product creation course.
    """

    def __init__(self, course_name, target_audience):
        """
        Initializes the SalesFunnel with course name and target audience.

        :param course_name: str - The name of the course
        :param target_audience: str - The target audience for the course
        """
        self.course_name = course_name
        self.target_audience = target_audience
        self.stages = {
            "Awareness": [],
            "Interest": [],
            "Decision": [],
            "Action": []
        }

    def add_lead(self, stage, lead_info):
        """
        Adds a lead to a specific stage of the sales funnel.

        :param stage: str - The stage to which the lead is added
        :param lead_info: dict - Information about the lead
        :raises ValueError: If the stage is not valid
        """
        if stage not in self.stages:
            raise ValueError(f"Invalid stage: {stage}. Valid stages are: {list(self.stages.keys())}")

        self.stages[stage].append(lead_info)

    def get_leads(self, stage):
        """
        Retrieves leads from a specific stage of the sales funnel.

        :param stage: str - The stage from which to retrieve leads
        :raises ValueError: If the stage is not valid
        :return: list - List of leads in the specified stage
        """
        if stage not in self.stages:
            raise ValueError(f"Invalid stage: {stage}. Valid stages are: {list(self.stages.keys())}")

        return self.stages[stage]

    def display_funnel(self):
        """
        Displays the current state of the sales funnel.
        """
        print(f"Sales Funnel for '{self.course_name}' targeting '{self.target_audience}':")
        for stage, leads in self.stages.items():
            print(f"{stage} Stage: {len(leads)} leads")

# Example usage
if __name__ == "__main__":
    try:
        funnel = SalesFunnel("Social Media Product Creation", "Aspiring Entrepreneurs")
        
        # Adding leads to different stages
        funnel.add_lead("Awareness", {"name": "John Doe", "email": "john@example.com"})
        funnel.add_lead("Interest", {"name": "Jane Smith", "email": "jane@example.com"})
        funnel.add_lead("Decision", {"name": "Alice Johnson", "email": "alice@example.com"})
        funnel.add_lead("Action", {"name": "Bob Brown", "email": "bob@example.com"})
        
        # Display the funnel
        funnel.display_funnel()
        
        # Retrieve leads from a specific stage
        interest_leads = funnel.get_leads("Interest")
        print(f"Interest Stage Leads: {interest_leads}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
