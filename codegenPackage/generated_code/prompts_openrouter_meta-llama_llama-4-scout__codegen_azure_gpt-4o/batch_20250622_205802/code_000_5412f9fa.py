"""
Generated Code Metadata:
========================
Original URL: https://the-defiant.com
Prompt: Write a news article about a recent unlawful arrest by the Stormwind Guard, including quotes from witnesses and victims.
Generated: DETERMINISTIC_5412f9fa6f036a24
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_news_article(title, incident_date, location, summary, victim_quote, witness_quote):
    """
    Generates a formatted news article based on the provided details.

    Args:
        title (str): The title of the news article.
        incident_date (datetime.date): The date of the incident.
        location (str): The location where the incident occurred.
        summary (str): A brief summary of the incident.
        victim_quote (str): A quote from the victim.
        witness_quote (str): A quote from a witness.

    Returns:
        str: A formatted news article as a string.
    """
    try:
        # Validate inputs
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(incident_date, datetime.date):
            raise ValueError("Incident date must be a valid datetime.date object.")
        if not location or not isinstance(location, str):
            raise ValueError("Location must be a non-empty string.")
        if not summary or not isinstance(summary, str):
            raise ValueError("Summary must be a non-empty string.")
        if not victim_quote or not isinstance(victim_quote, str):
            raise ValueError("Victim quote must be a non-empty string.")
        if not witness_quote or not isinstance(witness_quote, str):
            raise ValueError("Witness quote must be a non-empty string.")

        # Format the article
        article = f"""
        {title}
        Date: {incident_date.strftime('%B %d, %Y')}
        Location: {location}

        Summary:
        {summary}

        Victim's Statement:
        "{victim_quote}"

        Witness's Statement:
        "{witness_quote}"

        Reported by: Stormwind Times
        """
        return article.strip()
    except Exception as e:
        # Handle unexpected errors
        return f"Error generating article: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define article details
    article_title = "Unlawful Arrest by Stormwind Guard Sparks Outrage"
    incident_date = datetime.date(2023, 10, 15)
    location = "Stormwind Market District"
    summary = (
        "A local merchant was unlawfully arrested by the Stormwind Guard yesterday, "
        "causing widespread concern among residents. Eyewitnesses claim the arrest was "
        "made without proper justification, raising questions about abuse of power."
    )
    victim_quote = "I was just minding my own business when they suddenly accused me of theft. I have done nothing wrong!"
    witness_quote = "I saw the whole thing. The merchant was just standing there when the guards grabbed him. It was completely uncalled for."

    # Generate and print the article
    news_article = generate_news_article(
        article_title, incident_date, location, summary, victim_quote, witness_quote
    )
    print(news_article)
```
