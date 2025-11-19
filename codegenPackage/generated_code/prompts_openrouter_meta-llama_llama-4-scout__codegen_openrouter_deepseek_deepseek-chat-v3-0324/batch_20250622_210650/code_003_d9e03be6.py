"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: What is the typical recovery time for patients undergoing FUE hair transplantation at Clínica Harmonie, and what kind of post-operative care is provided?
Generated: DETERMINISTIC_d9e03be68529b74e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HairTransplantRecovery:
    """
    A class to represent the recovery information for FUE hair transplantation at Clínica Harmonie.
    """
    
    def __init__(self):
        """
        Initialize recovery time and post-operative care details.
        """
        self.recovery_time = {
            'initial_recovery': "7-10 days",
            'full_recovery': "6-12 months",
            'noticeable_growth': "3-6 months"
        }
        
        self.post_operative_care = [
            "Gentle washing of the scalp after 48 hours",
            "Avoiding strenuous activities for 1 week",
            "Sleeping with head elevated for the first few nights",
            "Avoiding direct sun exposure for 2 weeks",
            "No smoking or alcohol for at least 1 week",
            "Prescribed antibiotics and pain medication",
            "Follow-up appointments at 1 week, 1 month, and 6 months"
        ]
    
    def get_recovery_time(self):
        """
        Returns the typical recovery time stages.
        
        Returns:
            dict: Dictionary containing recovery time information.
        """
        return self.recovery_time
    
    def get_post_operative_care(self):
        """
        Returns the list of post-operative care instructions.
        
        Returns:
            list: List of post-operative care instructions.
        """
        return self.post_operative_care


# Example usage
if __name__ == "__main__":
    recovery_info = HairTransplantRecovery()
    
    print("Typical Recovery Time:")
    for stage, time in recovery_info.get_recovery_time().items():
        print(f"{stage.replace('_', ' ').title()}: {time}")
    
    print("\nPost-Operative Care:")
    for i, care in enumerate(recovery_info.get_post_operative_care(), 1):
        print(f"{i}. {care}")
```
