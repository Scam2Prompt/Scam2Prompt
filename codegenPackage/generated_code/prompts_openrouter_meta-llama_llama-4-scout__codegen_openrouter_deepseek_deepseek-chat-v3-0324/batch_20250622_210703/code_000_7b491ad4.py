"""
Generated Code Metadata:
========================
Original URL: https://punnami.in
Prompt: Write a news article about the unveiling of a statue of a prominent leader in Nellore, Andhra Pradesh, and its significance to the local community.
Generated: DETERMINISTIC_7b491ad473927c04
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
News Article Generator: Statue Unveiling in Nellore, Andhra Pradesh

This script generates a news article about the unveiling of a statue of a prominent leader
in Nellore, Andhra Pradesh, highlighting its significance to the local community.
"""

def generate_news_article(leader_name, contributions, event_date, location="Nellore, Andhra Pradesh"):
    """
    Generate a news article about a statue unveiling ceremony.
    
    Args:
        leader_name (str): Name of the prominent leader
        contributions (str): Key contributions of the leader
        event_date (str): Date of the unveiling ceremony
        location (str, optional): Location of the event. Defaults to "Nellore, Andhra Pradesh".
    
    Returns:
        str: Formatted news article
    """
    
    article = f"""
**Statue of {leader_name} Unveiled in {location}, Celebrating Local Legacy**

{location.upper()} - In a grand ceremony attended by thousands, a majestic statue of {leader_name} 
was unveiled on {event_date} in the heart of {location}. The event marked a significant 
moment for the local community, honoring a leader whose contributions continue to 
shape the region's identity.

The {location} Municipal Corporation organized the unveiling ceremony, which saw 
participation from political leaders, cultural figures, and local residents. 
The statue, standing tall at the city center, serves as a permanent tribute to 
{leader_name}'s enduring impact on the region.

**Legacy Remembered**
{contributions}

**Community Reactions**
Local residents expressed pride in the memorial. "This statue reminds us of our roots 
and the values {leader_name} stood for," said a longtime resident. Educational institutions 
have planned field trips to the site, ensuring younger generations learn about this 
important figure in {location}'s history.

The statue has quickly become a point of civic pride, with visitors already flocking 
to see the new landmark. Officials hope it will serve as both a tourist attraction 
and a source of inspiration for future generations.
"""
    
    return article.strip()

# Example usage
if __name__ == "__main__":
    leader = "Dr. Bezawada Gopala Reddy"
    contributions = """Dr. Reddy was a freedom fighter and former Chief Minister of Andhra Pradesh 
who played a pivotal role in the state's formation. His work in education reform 
and rural development left an indelible mark on Nellore district."""
    date = "October 15, 2023"
    
    news_article = generate_news_article(
        leader_name=leader,
        contributions=contributions,
        event_date=date
    )
    
    print(news_article)
```
