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
# MN SWAP Regional Structure Implementation

class Region:
    """
    Represents a MN SWAP region with its properties and networking capabilities.
    """
    def __init__(self, name, counties, coordinator, contact_info):
        """
        Initialize a MN SWAP region.
        
        Args:
            name (str): Name of the region
            counties (list): List of counties in the region
            coordinator (str): Regional coordinator name
            contact_info (str): Coordinator contact information
        """
        self.name = name
        self.counties = counties
        self.coordinator = coordinator
        self.contact_info = contact_info
        self.members = []
        
    def add_member(self, member):
        """
        Add an activity professional to the region.
        
        Args:
            member (dict): Dictionary containing member information
                          Expected keys: 'name', 'organization', 'role', 'contact'
        """
        if not isinstance(member, dict) or not all(key in member for key in ['name', 'organization', 'role', 'contact']):
            raise ValueError("Member must be a dictionary with required keys")
        self.members.append(member)
        
    def get_member_network(self):
        """
        Return all members in the region for networking purposes.
        
        Returns:
            list: List of member dictionaries
        """
        return self.members.copy()
    
    def get_region_info(self):
        """
        Return formatted region information.
        
        Returns:
            dict: Region information including coordinator details
        """
        return {
            'region_name': self.name,
            'counties': self.counties,
            'coordinator': self.coordinator,
            'contact_info': self.contact_info,
            'member_count': len(self.members)
        }


class MNSWAP:
    """
    Main class representing the MN SWAP organization and its regional structure.
    """
    def __init__(self):
        """Initialize MN SWAP with its regional structure."""
        self.regions = {
            'Northwest': Region(
                'Northwest',
                ['Beltrami', 'Clearwater', 'Hubbard', 'Lake of the Woods', 'Mahnomen', 'Marshall', 'Norman', 'Pennington', 'Polk', 'Red Lake', 'Roseau'],
                'Northwest Coordinator',
                'nwcoordinator@mnswap.org'
            ),
            'Northeast': Region(
                'Northeast',
                ['Aitkin', 'Carlton', 'Cook', 'Itasca', 'Koochiching', 'Lake', 'St. Louis'],
                'Northeast Coordinator',
                'necoordinator@mnswap.org'
            ),
            # Additional regions would be added here following the same pattern
            'Central': Region(
                'Central',
                ['Benton', 'Cass', 'Crow Wing', 'Morrison', 'Sherburne', 'Stearns', 'Todd', 'Wadena', 'Wright'],
                'Central Coordinator',
                'centralcoordinator@mnswap.org'
            ),
            'Metro': Region(
                'Metro',
                ['Anoka', 'Carver', 'Dakota', 'Hennepin', 'Ramsey', 'Scott', 'Washington'],
                'Metro Coordinator',
                'metrocoordinator@mnswap.org'
            ),
            'Southwest': Region(
                'Southwest',
                ['Big Stone', 'Chippewa', 'Cottonwood', 'Jackson', 'Kandiyohi', 'Lac qui Parle', 'Lincoln', 'Lyon', 'McLeod', 'Meeker', 'Murray', 'Nobles', 'Pipestone', 'Redwood', 'Renville', 'Rock', 'Swift', 'Yellow Medicine'],
                'Southwest Coordinator',
                'swcoordinator@mnswap.org'
            ),
            'Southeast': Region(
                'Southeast',
                ['Blue Earth', 'Brown', 'Dodge', 'Faribault', 'Fillmore', 'Freeborn', 'Goodhue', 'Houston', 'Le Sueur', 'Mower', 'Nicollet', 'Olmsted', 'Rice', 'Steele', 'Wabasha', 'Waseca', 'Winona'],
                'Southeast Coordinator',
                'secoordinator@mnswap.org'
            )
        }
        
    def get_region(self, region_name):
        """
        Retrieve a region by name.
        
        Args:
            region_name (str): Name of the region to retrieve
            
        Returns:
            Region: The requested region object
            
        Raises:
            ValueError: If region name is invalid
        """
        if region_name not in self.regions:
            raise ValueError(f"Invalid region name. Valid regions are: {', '.join(self.regions.keys())}")
        return self.regions[region_name]
    
    def add_member_to_region(self, region_name, member_info):
        """
        Add a member to a specific region.
        
        Args:
            region_name (str): Name of the region
            member_info (dict): Member information dictionary
            
        Raises:
            ValueError: If region name is invalid or member info is incomplete
        """
        region = self.get_region(region_name)
        region.add_member(member_info)
        
    def get_network_for_region(self, region_name):
        """
        Get all members in a specific region for networking purposes.
        
        Args:
            region_name (str): Name of the region
            
        Returns:
            list: List of members in the region
        """
        region = self.get_region(region_name)
        return region.get_member_network()
    
    def get_all_regions_info(self):
        """
        Get information about all regions in MN SWAP.
        
        Returns:
            dict: Dictionary with region names as keys and region info as values
        """
        return {name: region.get_region_info() for name, region in self.regions.items()}
    
    def find_member_regions(self, member_name):
        """
        Find which regions a member belongs to.
        
        Args:
            member_name (str): Name of member to search for
            
        Returns:
            list: Names of regions the member belongs to
        """
        return [
            region_name 
            for region_name, region in self.regions.items() 
            if any(member['name'] == member_name for member in region.members)
        ]


# Example usage
if __name__ == "__main__":
    # Initialize MN SWAP
    mnswap = MNSWAP()
    
    # Add a member to a region
    try:
        mnswap.add_member_to_region(
            'Metro',
            {
                'name': 'Jane Doe',
                'organization': 'Minneapolis Parks',
                'role': 'Activity Director',
                'contact': 'jane.doe@mplsparks.org'
            }
        )
    except ValueError as e:
        print(f"Error adding member: {e}")
    
    # Get network for a region
    metro_network = mnswap.get_network_for_region('Metro')
    print(f"Metro region network: {metro_network}")
    
    # Get all regions info
    all_regions = mnswap.get_all_regions_info()
    print("All regions information:", all_regions)
```
