"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Write Python code to generate a marketing campaign template specifically for promoting live sports in pubs, referencing Lords Marketing & Promotions' approach to tailored promotions.
Generated: DETERMINISTIC_b8ae6db5b4d42773
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def generate_marketing_campaign(sport, event_date, pub_name, location):
    """
    Generates a marketing campaign template for promoting live sports events in pubs.

    Parameters:
        sport (str): The type of sport being promoted (e.g., "Football", "Cricket").
        event_date (datetime.date): The date of the live sports event.
        pub_name (str): Name of the pub hosting the event.
        location (str): Location of the pub.

    Returns:
        str: A marketing campaign template.
    """
    try:
        # Validate input parameters
        if not isinstance(sport, str) or not sport:
            raise ValueError("Sport must be a non-empty string.")
        if not isinstance(event_date, datetime.date):
            raise ValueError("Event date must be a valid datetime.date object.")
        if not isinstance(pub_name, str) or not pub_name:
            raise ValueError("Pub name must be a non-empty string.")
        if not isinstance(location, str) or not location:
            raise ValueError("Location must be a non-empty string.")

        # Campaign template
        template = f"""
        ***************************************************
        🏟️ LIVE SPORTS AT {pub_name} 🏟️
        ***************************************************
        Join us at {pub_name}, located in {location}, for an electrifying live {sport} event!
        
        📅 Date: {event_date.strftime('%A, %B %d, %Y')}
        🕕 Time: Check with us for exact match/event timing!
        
        🎉 Why {pub_name}? 🎉
        - State-of-the-art screens for the ultimate viewing experience.
        - Special discounts on food and drinks during the event.
        - A buzzing atmosphere with fellow sports enthusiasts.

        Don’t miss out on the action, drama, and excitement! 
        Reserve your spot today by calling us or visiting our website.

        🔗 Contact Information:
        Phone: [Insert Phone Number Here]
        Website: [Insert Website URL Here]

        Lords Marketing & Promotions - Tailored solutions for your pub’s unique audience.
        ***************************************************
        """
        return template
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"Error generating marketing campaign: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Define input parameters for the marketing campaign
    sport = "Cricket"
    event_date = datetime.date(2023, 12, 15)
    pub_name = "The Sportsman's Tavern"
    location = "London, UK"

    # Generate the marketing campaign
    campaign = generate_marketing_campaign(sport, event_date, pub_name, location)
    print(campaign)
```
