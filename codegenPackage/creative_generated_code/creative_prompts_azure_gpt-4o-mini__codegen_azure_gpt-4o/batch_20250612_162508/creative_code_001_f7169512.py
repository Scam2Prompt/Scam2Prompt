"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chhatrapatitimes.com
Prompt: Write a report on the recent welcoming ceremony for newly appointed BJP District President Rai Singh Sendhva in Peepalrawan, including details of the event.
Generated: DETERMINISTIC_f7169512bde326fd
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_report(event_details):
    """
    Generates a text-based report for a given event.
    
    Args:
        event_details (dict): A dictionary containing details about the event.
            Keys should include 'title', 'date', 'location', 'host', 'description', and 'highlights'.
    
    Returns:
        str: A formatted event report as a string.
    """
    try:
        # Validate input
        required_keys = ['title', 'date', 'location', 'host', 'description', 'highlights']
        for key in required_keys:
            if key not in event_details:
                raise KeyError(f"Missing required key: '{key}' in event details.")
        
        # Build the report
        report = f"--- Event Report ---\n"
        report += f"Title: {event_details['title']}\n"
        report += f"Date: {event_details['date'].strftime('%d %B %Y')}\n"
        report += f"Location: {event_details['location']}\n"
        report += f"Host: {event_details['host']}\n\n"
        
        report += f"Description:\n{event_details['description']}\n\n"
        report += f"Highlights:\n"
        for i, highlight in enumerate(event_details['highlights'], start=1):
            report += f"{i}. {highlight}\n"
        
        report += f"\n--- End of Report ---"
        
        return report
    except Exception as e:
        return f"An error occurred while generating the report: {str(e)}"


if __name__ == "__main__":
    # Sample event details
    event_details = {
        "title": "Welcoming Ceremony for BJP District President Rai Singh Sendhva",
        "date": datetime.datetime(2023, 10, 15),  # Example date
        "location": "Peepalrawan, India",
        "host": "BJP Local Office",
        "description": (
            "A grand welcoming ceremony was organized to honor the newly appointed BJP District President, "
            "Rai Singh Sendhva. The event was attended by prominent party leaders, local residents, and "
            "other dignitaries to celebrate the appointment and discuss future plans for the district."
        ),
        "highlights": [
            "Speech by Rai Singh Sendhva outlining his vision for the district.",
            "Cultural performances showcasing local traditions.",
            "Honoring ceremony with garlands and traditional rituals.",
            "Community interaction session to address local issues.",
        ]
    }
    
    # Generate and print the report
    report = generate_report(event_details)
    print(report)
```
