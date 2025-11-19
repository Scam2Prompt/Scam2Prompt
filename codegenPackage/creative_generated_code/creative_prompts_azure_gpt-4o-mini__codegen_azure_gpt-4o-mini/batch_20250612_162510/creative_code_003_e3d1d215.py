"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axos-management.com
Prompt: Generate a sample contract for an influencer partnership that includes elements of communication and performance tracking, based on the full-service influencer management described on axos-management.com.
Generated: DETERMINISTIC_e3d1d215dfce0bcf
Batch ID: 20250612_162510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InfluencerPartnershipContract:
    """
    Class to represent an influencer partnership contract.
    """

    def __init__(self, influencer_name, brand_name, start_date, end_date):
        """
        Initializes the contract with the influencer and brand information,
        along with the contract duration.

        :param influencer_name: Name of the influencer
        :param brand_name: Name of the brand
        :param start_date: Start date of the contract (YYYY-MM-DD)
        :param end_date: End date of the contract (YYYY-MM-DD)
        """
        self.influencer_name = influencer_name
        self.brand_name = brand_name
        self.start_date = start_date
        self.end_date = end_date
        self.performance_metrics = []
        self.communication_plan = []

    def add_performance_metric(self, metric):
        """
        Adds a performance metric to be tracked during the partnership.

        :param metric: Performance metric to be tracked
        :raises ValueError: If metric is not a string or is empty
        """
        if not isinstance(metric, str) or not metric:
            raise ValueError("Performance metric must be a non-empty string.")
        self.performance_metrics.append(metric)

    def add_communication_method(self, method):
        """
        Adds a communication method for the partnership.

        :param method: Communication method to be used
        :raises ValueError: If method is not a string or is empty
        """
        if not isinstance(method, str) or not method:
            raise ValueError("Communication method must be a non-empty string.")
        self.communication_plan.append(method)

    def display_contract(self):
        """
        Displays the details of the partnership contract.
        """
        print("Influencer Partnership Contract")
        print(f"Influencer Name: {self.influencer_name}")
        print(f"Brand Name: {self.brand_name}")
        print(f"Contract Start Date: {self.start_date}")
        print(f"Contract End Date: {self.end_date}")
        print("\nPerformance Metrics:")
        for metric in self.performance_metrics:
            print(f"- {metric}")
        print("\nCommunication Plan:")
        for method in self.communication_plan:
            print(f"- {method}")

    def is_active(self, current_date):
        """
        Checks if the contract is currently active.

        :param current_date: Current date to check against the contract (YYYY-MM-DD)
        :return: True if the contract is active, False otherwise
        """
        if not isinstance(current_date, str) or len(current_date) != 10:
            raise ValueError("Current date must be a string in YYYY-MM-DD format.")

        return self.start_date <= current_date <= self.end_date


# Sample usage
if __name__ == "__main__":
    try:
        # Creating an instance of the contract
        contract = InfluencerPartnershipContract("Jane Doe", "CoolBrand", "2023-01-01", "2023-12-31")
        
        # Adding performance metrics
        contract.add_performance_metric("Follower Growth Rate")
        contract.add_performance_metric("Engagement Rate")
        
        # Adding communication methods
        contract.add_communication_method("Weekly check-ins via Zoom")
        contract.add_communication_method("Monthly performance reports via email")
        
        # Displaying the contract
        contract.display_contract()
        
        # Checking if the contract is active
        current_date = "2023-07-15"
        print(f"\nIs the contract active on {current_date}? {contract.is_active(current_date)}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
