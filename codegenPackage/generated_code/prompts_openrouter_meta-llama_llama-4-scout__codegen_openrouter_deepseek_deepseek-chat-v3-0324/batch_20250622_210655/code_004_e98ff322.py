"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: What are the primary applications of Yanmar mini excavators in construction, agriculture, landscaping, and urban planning?
Generated: DETERMINISTIC_e98ff3220727dfac
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides information on the primary applications of Yanmar mini excavators
in various industries including construction, agriculture, landscaping, and urban planning.
"""

class YanmarMiniExcavatorApplications:
    """
    A class to represent the applications of Yanmar mini excavators in different industries.
    """
    
    def __init__(self):
        """
        Initialize the applications dictionary with industry-specific uses.
        """
        self.applications = {
            'construction': [
                'Trenching for utilities',
                'Foundation digging',
                'Demolition of small structures',
                'Material handling',
                'Site preparation'
            ],
            'agriculture': [
                'Digging irrigation channels',
                'Land clearing',
                'Pond digging',
                'Fence post hole digging',
                'Livestock barn cleanup'
            ],
            'landscaping': [
                'Tree planting',
                'Grading and leveling',
                'Rock and debris removal',
                'Pond and water feature construction',
                'Pathway creation'
            ],
            'urban_planning': [
                'Sidewalk repair',
                'Park development',
                'Small-scale excavation in tight spaces',
                'Utility maintenance in congested areas',
                'Green space development'
            ]
        }
    
    def get_applications(self, industry):
        """
        Retrieve applications for a specific industry.
        
        Args:
            industry (str): The industry to query (construction, agriculture, landscaping, urban_planning)
        
        Returns:
            list: List of applications for the specified industry
            None: If industry is not found
        
        Raises:
            ValueError: If industry argument is not a string
        """
        if not isinstance(industry, str):
            raise ValueError("Industry must be a string")
        
        return self.applications.get(industry.lower(), None)
    
    def list_all_applications(self):
        """
        Return all applications organized by industry.
        
        Returns:
            dict: Complete dictionary of all applications by industry
        """
        return self.applications


# Example usage
if __name__ == "__main__":
    try:
        excavator_apps = YanmarMiniExcavatorApplications()
        
        # Get applications for a specific industry
        print("Construction Applications:")
        print(excavator_apps.get_applications('construction'))
        
        # Get all applications
        print("\nAll Applications:")
        for industry, apps in excavator_apps.list_all_applications().items():
            print(f"\n{industry.capitalize().replace('_', ' ')}:")
            for app in apps:
                print(f"- {app}")
                
    except Exception as e:
        print(f"An error occurred: {e}")
```
