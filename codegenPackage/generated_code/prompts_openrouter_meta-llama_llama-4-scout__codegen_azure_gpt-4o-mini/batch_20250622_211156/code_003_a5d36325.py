"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Describe the regional structure of MN SWAP and how it facilitates networking and support among activity professionals in Minnesota.
Generated: DETERMINISTIC_a5d363257bbd2d01
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MN_SWAP:
    """
    A class to represent the Minnesota SWAP (Statewide Activity Professionals) network.
    
    Attributes
    ----------
    regions : dict
        A dictionary to hold regional information and their respective activity professionals.
    """

    def __init__(self):
        """
        Initializes the MN_SWAP with an empty regional structure.
        """
        self.regions = {}

    def add_region(self, region_name):
        """
        Adds a new region to the MN SWAP network.

        Parameters
        ----------
        region_name : str
            The name of the region to be added.

        Raises
        ------
        ValueError
            If the region already exists in the network.
        """
        if region_name in self.regions:
            raise ValueError(f"Region '{region_name}' already exists.")
        self.regions[region_name] = []
        print(f"Region '{region_name}' added successfully.")

    def add_activity_professional(self, region_name, professional_name):
        """
        Adds an activity professional to a specified region.

        Parameters
        ----------
        region_name : str
            The name of the region where the professional will be added.
        professional_name : str
            The name of the activity professional to be added.

        Raises
        ------
        ValueError
            If the region does not exist.
        """
        if region_name not in self.regions:
            raise ValueError(f"Region '{region_name}' does not exist.")
        self.regions[region_name].append(professional_name)
        print(f"Activity professional '{professional_name}' added to region '{region_name}'.")

    def get_professionals_by_region(self, region_name):
        """
        Retrieves the list of activity professionals in a specified region.

        Parameters
        ----------
        region_name : str
            The name of the region to retrieve professionals from.

        Returns
        -------
        list
            A list of activity professionals in the specified region.

        Raises
        ------
        ValueError
            If the region does not exist.
        """
        if region_name not in self.regions:
            raise ValueError(f"Region '{region_name}' does not exist.")
        return self.regions[region_name]

    def display_network(self):
        """
        Displays the entire MN SWAP network structure, including regions and their professionals.
        """
        for region, professionals in self.regions.items():
            print(f"Region: {region}, Activity Professionals: {', '.join(professionals) if professionals else 'None'}")


# Example usage
if __name__ == "__main__":
    try:
        mn_swap = MN_SWAP()
        mn_swap.add_region("Twin Cities")
        mn_swap.add_activity_professional("Twin Cities", "Alice Johnson")
        mn_swap.add_activity_professional("Twin Cities", "Bob Smith")
        
        mn_swap.add_region("Duluth")
        mn_swap.add_activity_professional("Duluth", "Charlie Brown")

        print("\nProfessionals in Twin Cities:")
        print(mn_swap.get_professionals_by_region("Twin Cities"))

        print("\nCurrent MN SWAP Network:")
        mn_swap.display_network()

    except ValueError as e:
        print(f"Error: {e}")
```
