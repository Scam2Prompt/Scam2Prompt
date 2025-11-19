"""
Generated Code Metadata:
========================
Original URL: https://pancarpos.com
Prompt: Write a news article about a local event in Bali, specifically about the Idul Adha celebration in Dusun Tegal Kori Kaja, including the importance of religious tolerance.
Generated: DETERMINISTIC_23011a9b6dbb3aa0
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_news_article(event_name, location, date, description, importance):
    """
    Generates a formatted news article based on the provided event details.

    Args:
        event_name (str): Name of the event.
        location (str): Location where the event is held.
        date (datetime.date): Date of the event.
        description (str): Description of the event.
        importance (str): Importance or significance of the event.

    Returns:
        str: A formatted news article as a string.
    """
    try:
        # Validate inputs
        if not event_name or not location or not date or not description or not importance:
            raise ValueError("All parameters must be provided and non-empty.")

        # Format the article
        article = f"""
        Local News: {event_name} Celebration in {location}

        {event_name} was celebrated in {location} on {date.strftime('%A, %d %B %Y')}. 
        The event was marked by a series of activities that brought the community together, 
        showcasing the rich cultural and religious traditions of the area.

        Event Details:
        {description}

        The celebration highlighted the importance of religious tolerance and harmony 
        in the diverse community of Dusun Tegal Kori Kaja, Bali. Residents from various 
        religious backgrounds came together to support and participate in the festivities, 
        fostering a spirit of unity and mutual respect.

        Why It Matters:
        {importance}

        Events like these serve as a reminder of the strength found in diversity and the 
        importance of understanding and respecting each other's beliefs. Dusun Tegal Kori Kaja 
        continues to set an example for communities around the world by embracing inclusivity 
        and celebrating shared values.

        """
        return article.strip()
    except Exception as e:
        # Handle unexpected errors
        return f"An error occurred while generating the article: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define event details
    event_name = "Idul Adha"
    location = "Dusun Tegal Kori Kaja, Bali"
    date = datetime.date(2023, 6, 29)  # Example date
    description = (
        "The Idul Adha celebration included prayers at the local mosque, "
        "followed by the traditional sacrificial ceremony and distribution of meat to the community."
    )
    importance = (
        "Religious tolerance is crucial in maintaining peace and harmony in a diverse society. "
        "This event demonstrated how different faiths can coexist and support one another."
    )

    # Generate and print the article
    article = generate_news_article(event_name, location, date, description, importance)
    print(article)
```
