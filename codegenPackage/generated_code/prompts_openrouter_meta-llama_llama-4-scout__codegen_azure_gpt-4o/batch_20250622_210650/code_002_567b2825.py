"""
Generated Code Metadata:
========================
Original URL: https://corporacionelcristal.com.co
Prompt: Generate a social media post announcing the next "Fiesta de los Títeres" event, incorporating details from Corporación El Cristal's previous events.
Generated: DETERMINISTIC_567b282590b5b22d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_social_media_post(event_name, event_date, event_location, organizer_name, previous_event_details):
    """
    Generates a social media post for an upcoming event.

    Args:
        event_name (str): Name of the event.
        event_date (datetime.date): Date of the event.
        event_location (str): Location of the event.
        organizer_name (str): Name of the organizing entity.
        previous_event_details (str): Highlights or details from previous events.

    Returns:
        str: A formatted social media post.
    """
    try:
        # Format the event date for readability
        formatted_date = event_date.strftime("%A, %B %d, %Y")
        
        # Construct the social media post
        post = (
            f"🎭✨ Get ready for the next big celebration! ✨🎭\n\n"
            f"Join us for the '{event_name}' happening on {formatted_date} at {event_location}.\n"
            f"Organized by {organizer_name}, this event promises to be a magical experience for all ages!\n\n"
            f"🌟 Highlights from our previous events:\n"
            f"{previous_event_details}\n\n"
            f"Don't miss out on this unforgettable experience! Mark your calendars and stay tuned for more updates.\n\n"
            f"#FiestaDeLosTíteres #FamilyFun #LiveEntertainment #CorporaciónElCristal"
        )
        
        return post
    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while generating the post: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Event details
    event_name = "Fiesta de los Títeres"
    event_date = datetime.date(2023, 11, 25)
    event_location = "Plaza Central, Bogotá"
    organizer_name = "Corporación El Cristal"
    previous_event_details = (
        "- Spectacular puppet shows that captivated audiences.\n"
        "- Interactive workshops for children and families.\n"
        "- Live music and cultural performances that brought the community together."
    )
    
    # Generate the post
    social_media_post = generate_social_media_post(
        event_name, event_date, event_location, organizer_name, previous_event_details
    )
    
    # Print the post
    print(social_media_post)
```
