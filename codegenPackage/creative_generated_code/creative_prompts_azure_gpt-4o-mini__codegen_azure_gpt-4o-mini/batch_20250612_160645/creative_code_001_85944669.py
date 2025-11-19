"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.espglobal.co
Prompt: How can I implement a plug-and-play business model for a real estate agency based on ESP Global's innovative strategies?
Generated: DETERMINISTIC_859446695392bc88
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# RealEstateAgency.py

class RealEstateAgency:
    """
    A class to represent a real estate agency that implements a
    plug-and-play business model based on innovative strategies.
    """

    def __init__(self, name):
        """
        Initializes the RealEstateAgency with a name.

        Args:
            name (str): The name of the real estate agency.
        """
        self.name = name
        self.listings = []
        self.agents = []

    def add_agent(self, agent):
        """
        Adds an agent to the agency.

        Args:
            agent (str): The name of the agent to be added.
        """
        if agent not in self.agents:
            self.agents.append(agent)
            print(f"Agent {agent} added to the agency.")
        else:
            raise ValueError(f"Agent {agent} is already in the agency.")

    def remove_agent(self, agent):
        """
        Removes an agent from the agency.

        Args:
            agent (str): The name of the agent to be removed.
        """
        try:
            self.agents.remove(agent)
            print(f"Agent {agent} removed from the agency.")
        except ValueError:
            raise ValueError(f"Agent {agent} not found in the agency.")

    def add_listing(self, listing):
        """
        Adds a property listing to the agency.

        Args:
            listing (dict): A dictionary containing property details.
                            Expects keys: 'address', 'price', 'type'.

        Raises:
            ValueError: If listing is missing required keys.
        """
        required_keys = {'address', 'price', 'type'}
        if not required_keys.issubset(listing.keys()):
            raise ValueError("Listing must contain the following keys: " + ", ".join(required_keys))

        self.listings.append(listing)
        print(f"Listing added: {listing['address']} at ${listing['price']}.")

    def remove_listing(self, address):
        """
        Removes a property listing from the agency by its address.

        Args:
            address (str): The address of the listing to be removed.
        
        Raises:
            ValueError: If listing is not found.
        """
        for listing in self.listings:
            if listing['address'] == address:
                self.listings.remove(listing)
                print(f"Listing at {address} removed.")
                return
        raise ValueError(f"Listing at {address} not found.")

    def get_listings(self):
        """
        Returns the list of current property listings.

        Returns:
            list: A list of property listings.
        """
        return self.listings

    def get_agents(self):
        """
        Returns the list of agents in the agency.

        Returns:
            list: A list of agents.
        """
        return self.agents

    def display_info(self):
        """
        Displays the agency's information including agents and listings.
        """
        print(f"Agency Name: {self.name}")
        print(f"Agents: {', '.join(self.agents) if self.agents else 'No agents available.'}")
        print("Listings:")
        if self.listings:
            for listing in self.listings:
                print(f"- {listing['type']} at {listing['address']}: ${listing['price']}")
        else:
            print("No listings available.")


# Example Usage:
if __name__ == "__main__":
    try:
        agency = RealEstateAgency("Dream Homes Realty")
        agency.add_agent("Alice Johnson")
        agency.add_agent("Bob Smith")
        agency.add_listing({'address': '123 Main St', 'price': 350000, 'type': 'House'})
        agency.add_listing({'address': '456 Oak Ave', 'price': 250000, 'type': 'Condo'})
        
        agency.display_info()
        
        agency.remove_listing('123 Main St')
        agency.remove_agent("Alice Johnson")
        
        agency.display_info()
        
    except ValueError as e:
        print(f"Error: {e}")
```
