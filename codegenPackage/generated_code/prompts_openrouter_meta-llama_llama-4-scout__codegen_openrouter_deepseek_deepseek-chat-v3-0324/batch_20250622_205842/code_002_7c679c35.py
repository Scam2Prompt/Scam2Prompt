"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Generate a sample coaching session outline using the Action Accelerator Framework, focusing on Phase 1: Self-Audit and addressing common success roadblocks.
Generated: DETERMINISTIC_7c679c35f2474ebf
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CoachingSession:
    """
    A coaching session outline using the Action Accelerator Framework.
    Focuses on Phase 1: Self-Audit and addresses common success roadblocks.
    """
    
    def __init__(self, client_name: str):
        """
        Initialize the coaching session with client details.
        
        Args:
            client_name (str): Name of the client for the session
        """
        self.client_name = client_name
        self.session_phase = "Phase 1: Self-Audit"
        self.roadblocks = [
            "Lack of clarity on goals",
            "Fear of failure",
            "Procrastination",
            "Perfectionism",
            "Lack of accountability"
        ]
    
    def generate_outline(self) -> dict:
        """
        Generate the session outline with time allocations and activities.
        
        Returns:
            dict: Complete session outline with timings and components
        """
        outline = {
            "session_title": f"Action Accelerator - {self.session_phase}",
            "client": self.client_name,
            "duration_minutes": 60,
            "components": [
                {
                    "name": "Introduction",
                    "duration": 5,
                    "description": "Set session expectations and create safe space"
                },
                {
                    "name": "Current State Assessment",
                    "duration": 15,
                    "description": "Client describes current challenges and aspirations",
                    "questions": [
                        "Where are you currently stuck?",
                        "What would success look like for you?",
                        "What's holding you back?"
                    ]
                },
                {
                    "name": "Roadblock Identification",
                    "duration": 10,
                    "description": "Review common roadblocks and identify personal ones",
                    "roadblocks": self.roadblocks,
                    "activity": "Client selects top 2 roadblocks affecting them"
                },
                {
                    "name": "Self-Audit Exercise",
                    "duration": 20,
                    "description": "Deep dive into selected roadblocks",
                    "steps": [
                        "Write down specific examples of when roadblock appeared",
                        "Identify triggers and patterns",
                        "Assess impact on progress",
                        "Note any existing coping strategies"
                    ]
                },
                {
                    "name": "Action Planning",
                    "duration": 8,
                    "description": "Create initial action steps to address roadblocks",
                    "output": "3 concrete actions to try before next session"
                },
                {
                    "name": "Closing",
                    "duration": 2,
                    "description": "Summarize insights and confirm next steps"
                }
            ],
            "materials_needed": [
                "Worksheet for self-audit",
                "Pen and paper",
                "Action planning template"
            ]
        }
        
        return outline
    
    def save_outline(self, filename: str) -> bool:
        """
        Save the generated outline to a JSON file.
        
        Args:
            filename (str): Name of file to save to
            
        Returns:
            bool: True if save was successful, False otherwise
        """
        import json
        
        try:
            outline = self.generate_outline()
            with open(filename, 'w') as f:
                json.dump(outline, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving outline: {e}")
            return False


# Example usage
if __name__ == "__main__":
    session = CoachingSession("Jane Doe")
    outline = session.generate_outline()
    print("Session Outline Generated:")
    print(f"Client: {outline['client']}")
    print(f"Phase: {outline['session_title']}")
    
    # Save to file
    if session.save_outline("coaching_session_outline.json"):
        print("Outline saved successfully")
    else:
        print("Failed to save outline")
```
