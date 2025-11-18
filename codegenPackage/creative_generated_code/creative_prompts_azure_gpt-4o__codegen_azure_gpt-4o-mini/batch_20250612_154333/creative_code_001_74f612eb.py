"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fmt.co.id
Prompt: Generate a script that calculates the optimal depth for using an earth auger drill, incorporating details about its applications in construction and forestry as outlined on the PT. Fuji Metal Teknik webpage.
Generated: DETERMINISTIC_74f612eb400c1718
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Optimal Depth Calculator for Earth Auger Drill
# This script calculates the optimal drilling depth based on user input for applications in construction and forestry.

class AugerDrill:
    def __init__(self, application_type):
        """
        Initializes the AugerDrill with a specific application type.
        
        Parameters:
            application_type (str): Type of application ('construction' or 'forestry')
        """
        self.application_type = application_type.lower()
        self.depth_ranges = {
            'construction': (2, 6),  # Depth in meters
            'forestry': (1, 3)       # Depth in meters
        }
        
    def get_optimal_depth(self):
        """
        Calculates the optimal depth for the auger drill based on the application type.
        
        Returns:
            tuple: Minimum and maximum optimal depth for the specified application.
        """
        if self.application_type not in self.depth_ranges:
            raise ValueError("Invalid application type. Choose 'construction' or 'forestry'.")
        
        return self.depth_ranges[self.application_type]

def main():
    """
    Main function to execute the optimal depth calculation for the earth auger drill.
    """
    try:
        # User input for application type
        application_type = input("Enter the application type ('construction' or 'forestry'): ").strip()
        
        # Create an instance of AugerDrill
        auger_drill = AugerDrill(application_type)
        
        # Get the optimal depth range
        min_depth, max_depth = auger_drill.get_optimal_depth()
        
        # Display the result
        print(f"The optimal drilling depth for {application_type} is between {min_depth}m and {max_depth}m.")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
