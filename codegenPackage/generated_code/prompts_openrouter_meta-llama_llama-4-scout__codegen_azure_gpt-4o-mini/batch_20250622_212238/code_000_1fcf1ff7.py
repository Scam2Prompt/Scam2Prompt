"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: "Generate a project proposal for a brand strategy campaign using a flexible project-based model, including services such as research, brand architecture, and visual identity."
Generated: DETERMINISTIC_1fcf1ff76b5d017f
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BrandStrategyCampaign:
    """
    A class to represent a brand strategy campaign using a flexible project-based model.
    """

    def __init__(self, client_name, campaign_name):
        """
        Initializes the BrandStrategyCampaign with client name and campaign name.

        :param client_name: Name of the client
        :param campaign_name: Name of the campaign
        """
        self.client_name = client_name
        self.campaign_name = campaign_name
        self.services = []
        self.budget = 0.0

    def add_service(self, service_name, service_cost):
        """
        Adds a service to the campaign.

        :param service_name: Name of the service to be added
        :param service_cost: Cost of the service
        :raises ValueError: If service_cost is negative
        """
        if service_cost < 0:
            raise ValueError("Service cost cannot be negative.")
        
        self.services.append({'name': service_name, 'cost': service_cost})
        self.budget += service_cost

    def remove_service(self, service_name):
        """
        Removes a service from the campaign.

        :param service_name: Name of the service to be removed
        :raises ValueError: If the service is not found
        """
        for service in self.services:
            if service['name'] == service_name:
                self.services.remove(service)
                self.budget -= service['cost']
                return
        raise ValueError("Service not found.")

    def get_campaign_details(self):
        """
        Returns the details of the campaign including services and total budget.

        :return: A dictionary containing campaign details
        """
        return {
            'client_name': self.client_name,
            'campaign_name': self.campaign_name,
            'services': self.services,
            'total_budget': self.budget
        }

    def generate_proposal(self):
        """
        Generates a project proposal for the brand strategy campaign.

        :return: A formatted string proposal
        """
        details = self.get_campaign_details()
        proposal = f"Brand Strategy Campaign Proposal\n"
        proposal += f"Client: {details['client_name']}\n"
        proposal += f"Campaign: {details['campaign_name']}\n"
        proposal += "Services Offered:\n"
        
        for service in details['services']:
            proposal += f"- {service['name']}: ${service['cost']:.2f}\n"
        
        proposal += f"Total Budget: ${details['total_budget']:.2f}\n"
        return proposal


# Example usage
if __name__ == "__main__":
    try:
        campaign = BrandStrategyCampaign("Acme Corp", "Rebranding Initiative")
        campaign.add_service("Market Research", 5000)
        campaign.add_service("Brand Architecture", 7000)
        campaign.add_service("Visual Identity", 8000)

        print(campaign.generate_proposal())
        
        # Removing a service
        campaign.remove_service("Market Research")
        print("\nUpdated Proposal After Removing a Service:\n")
        print(campaign.generate_proposal())

    except ValueError as e:
        print(f"Error: {e}")
```
