"""
Generated Code Metadata:
========================
Original URL: https://mimsr.edu.in
Prompt: What are the core objectives and values of MAEER's Maharashtra Institute of Medical Sciences & Research (MIMSR) in providing medical education and healthcare services, as stated in their mission and vision statements?
Generated: DETERMINISTIC_15563db664ea09bc
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script outlines the core objectives and values of MAEER's Maharashtra Institute of Medical Sciences & Research (MIMSR)
based on their mission and vision statements for providing medical education and healthcare services.
"""

class MIMSRCoreValues:
    """
    A class representing the core values and objectives of MIMSR Medical College.
    """
    
    def __init__(self):
        """
        Initialize the core values and objectives from MIMSR's mission and vision statements.
        """
        self.mission = {
            'education': "To provide quality medical education with emphasis on ethical practice and research",
            'healthcare': "To deliver compassionate and affordable healthcare services to all sections of society",
            'research': "To promote innovative research in medical sciences for societal benefit",
            'community': "To serve the community through health awareness programs and outreach activities"
        }
        
        self.vision = {
            'excellence': "To be a center of excellence in medical education, healthcare, and research",
            'innovation': "To foster innovation in medical education and patient care",
            'leadership': "To develop future healthcare leaders with strong ethical values",
            'accessibility': "To make quality healthcare accessible to underserved populations"
        }
    
    def get_mission(self):
        """
        Returns the mission statement components.
        """
        return self.mission
    
    def get_vision(self):
        """
        Returns the vision statement components.
        """
        return self.vision
    
    def get_core_values(self):
        """
        Returns a combined list of core values from both mission and vision.
        """
        return {
            'mission_values': list(self.mission.values()),
            'vision_values': list(self.vision.values())
        }


# Example usage
if __name__ == "__main__":
    mimsr = MIMSRCoreValues()
    
    print("Mission Statement Components:")
    for key, value in mimsr.get_mission().items():
        print(f"- {key.capitalize()}: {value}")
    
    print("\nVision Statement Components:")
    for key, value in mimsr.get_vision().items():
        print(f"- {key.capitalize()}: {value}")
    
    print("\nCore Values:")
    for value in mimsr.get_core_values()['mission_values']:
        print(f"- {value}")
    for value in mimsr.get_core_values()['vision_values']:
        print(f"- {value}")
```
