"""
Generated Code Metadata:
========================
Original URL: https://tinaalstrom.com
Prompt: "Design a 15-minute conversation agenda for a business owner and a marketing and sales development consultant to discuss growth strategies, customer experience, and potential collaboration opportunities."
Generated: DETERMINISTIC_c2fc7d11269d15ff
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MeetingAgenda:
    """
    A class to represent a 15-minute meeting agenda between a business owner
    and a marketing/sales development consultant.
    """
    
    def __init__(self, business_name: str, consultant_name: str):
        """
        Initialize the meeting agenda with participant names.
        
        Args:
            business_name (str): Name of the business owner/company
            consultant_name (str): Name of the marketing/sales consultant
        """
        self.business_name = business_name
        self.consultant_name = consultant_name
        self.topics = []
        self.time_slots = []
        
    def add_topic(self, topic: str, duration: int, description: str = None):
        """
        Add a discussion topic to the agenda.
        
        Args:
            topic (str): Name of the topic
            duration (int): Duration in minutes
            description (str, optional): Additional details about the topic
        """
        if sum(self.time_slots) + duration > 15:
            raise ValueError("Total duration exceeds 15-minute meeting limit")
            
        self.topics.append({
            'topic': topic,
            'duration': duration,
            'description': description
        })
        self.time_slots.append(duration)
        
    def generate_agenda(self) -> str:
        """
        Generate a formatted meeting agenda.
        
        Returns:
            str: Formatted agenda with time allocations
        """
        if not self.topics:
            raise ValueError("No topics have been added to the agenda")
            
        agenda = f"15-Minute Meeting Agenda\n"
        agenda += f"Participants: {self.business_name} (Business Owner) & {self.consultant_name} (Consultant)\n\n"
        
        start_time = 0
        for i, topic in enumerate(self.topics, 1):
            end_time = start_time + topic['duration']
            agenda += f"{i}. {start_time:02d}:{end_time:02d} - {topic['topic']}"
            if topic['description']:
                agenda += f": {topic['description']}"
            agenda += "\n"
            start_time = end_time
            
        return agenda

# Example usage
try:
    meeting = MeetingAgenda("Acme Inc.", "Jane Doe Marketing")
    
    # Add discussion topics
    meeting.add_topic(
        "Current Growth Challenges",
        3,
        "Brief overview of current business growth obstacles"
    )
    meeting.add_topic(
        "Customer Experience Analysis",
        4,
        "Review of current customer journey and pain points"
    )
    meeting.add_topic(
        "Marketing Strategy Assessment",
        5,
        "Evaluation of current marketing efforts and ROI"
    )
    meeting.add_topic(
        "Collaboration Opportunities",
        3,
        "Potential areas for partnership and next steps"
    )
    
    # Generate and print the agenda
    print(meeting.generate_agenda())
    
except ValueError as e:
    print(f"Error creating agenda: {e}")
```
