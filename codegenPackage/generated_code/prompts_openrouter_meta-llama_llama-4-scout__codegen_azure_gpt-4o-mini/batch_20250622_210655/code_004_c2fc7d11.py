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
    A class to represent a meeting agenda for a business owner and a marketing consultant.
    """

    def __init__(self, duration_minutes=15):
        """
        Initializes the MeetingAgenda with a specified duration.

        :param duration_minutes: Duration of the meeting in minutes (default is 15).
        """
        self.duration_minutes = duration_minutes
        self.agenda_items = []

    def add_agenda_item(self, time_allocation, topic, description):
        """
        Adds an item to the meeting agenda.

        :param time_allocation: Time allocated for the agenda item in minutes.
        :param topic: The topic of discussion.
        :param description: A brief description of the agenda item.
        """
        if time_allocation <= 0:
            raise ValueError("Time allocation must be greater than zero.")
        if sum(item['time'] for item in self.agenda_items) + time_allocation > self.duration_minutes:
            raise ValueError("Total time allocation exceeds meeting duration.")
        
        self.agenda_items.append({
            'time': time_allocation,
            'topic': topic,
            'description': description
        })

    def display_agenda(self):
        """
        Displays the meeting agenda in a formatted manner.
        """
        print(f"Meeting Agenda (Total Duration: {self.duration_minutes} minutes)\n")
        for item in self.agenda_items:
            print(f"{item['time']} minutes - {item['topic']}: {item['description']}")
        print("\nTotal Agenda Time:", sum(item['time'] for item in self.agenda_items), "minutes")

# Example usage
if __name__ == "__main__":
    try:
        agenda = MeetingAgenda()

        # Adding agenda items
        agenda.add_agenda_item(5, "Growth Strategies", "Discuss potential growth strategies for the business.")
        agenda.add_agenda_item(5, "Customer Experience", "Explore ways to enhance customer experience.")
        agenda.add_agenda_item(5, "Collaboration Opportunities", "Identify potential collaboration opportunities.")

        # Display the agenda
        agenda.display_agenda()

    except ValueError as e:
        print(f"Error: {e}")
```
