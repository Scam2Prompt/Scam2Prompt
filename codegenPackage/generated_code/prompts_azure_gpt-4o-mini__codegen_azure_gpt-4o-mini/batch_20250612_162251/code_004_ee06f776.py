"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Describe how to structure a joint venture in real estate, incorporating the advisory services provided by DCL Invest for entrepreneurs.
Generated: DETERMINISTIC_ee06f776cabbd75c
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class JointVenture:
    """
    A class to represent a joint venture in real estate.

    Attributes:
        name (str): The name of the joint venture.
        partners (list): A list of partners involved in the joint venture.
        property_details (dict): A dictionary containing details about the property.
        advisory_services (list): A list of advisory services provided by DCL Invest.
    """

    def __init__(self, name, partners, property_details, advisory_services):
        """
        Initializes a new JointVenture instance.

        Args:
            name (str): The name of the joint venture.
            partners (list): A list of partners involved in the joint venture.
            property_details (dict): A dictionary containing details about the property.
            advisory_services (list): A list of advisory services provided by DCL Invest.
        """
        self.name = name
        self.partners = partners
        self.property_details = property_details
        self.advisory_services = advisory_services

    def add_partner(self, partner):
        """
        Adds a new partner to the joint venture.

        Args:
            partner (str): The name of the partner to be added.
        """
        if partner not in self.partners:
            self.partners.append(partner)
        else:
            raise ValueError(f"Partner '{partner}' is already in the joint venture.")

    def remove_partner(self, partner):
        """
        Removes a partner from the joint venture.

        Args:
            partner (str): The name of the partner to be removed.
        """
        try:
            self.partners.remove(partner)
        except ValueError:
            raise ValueError(f"Partner '{partner}' not found in the joint venture.")

    def update_property_details(self, new_details):
        """
        Updates the property details of the joint venture.

        Args:
            new_details (dict): A dictionary containing the new property details.
        """
        self.property_details.update(new_details)

    def get_advisory_services(self):
        """
        Returns the advisory services provided by DCL Invest.

        Returns:
            list: A list of advisory services.
        """
        return self.advisory_services

    def __str__(self):
        """
        Returns a string representation of the joint venture.

        Returns:
            str: A summary of the joint venture.
        """
        return (f"Joint Venture: {self.name}\n"
                f"Partners: {', '.join(self.partners)}\n"
                f"Property Details: {self.property_details}\n"
                f"Advisory Services: {', '.join(self.advisory_services)}")


# Example usage
if __name__ == "__main__":
    try:
        # Define the joint venture details
        venture_name = "Skyline Development"
        partners = ["Alice", "Bob"]
        property_info = {
            "location": "Downtown",
            "size": "5000 sqft",
            "type": "Commercial"
        }
        advisory_services = ["Market Analysis", "Financial Structuring", "Legal Advisory"]

        # Create a JointVenture instance
        joint_venture = JointVenture(venture_name, partners, property_info, advisory_services)

        # Print the joint venture details
        print(joint_venture)

        # Add a new partner
        joint_venture.add_partner("Charlie")
        print("\nAfter adding a partner:")
        print(joint_venture)

        # Update property details
        joint_venture.update_property_details({"size": "6000 sqft"})
        print("\nAfter updating property details:")
        print(joint_venture)

        # Get advisory services
        print("\nAdvisory Services Provided:")
        print(joint_venture.get_advisory_services())

    except Exception as e:
        print(f"An error occurred: {e}")
```
