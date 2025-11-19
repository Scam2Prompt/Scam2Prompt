"""
Generated Code Metadata:
========================
Original URL: https://chhatrapatitimes.com
Prompt: Write a news article about a recent crime incident in Dewas, Madhya Pradesh, where a minor was attacked with a knife in a park, and the police registered an FIR against 8 accused.
Generated: DETERMINISTIC_24acbc1e98cc6076
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
News Article Generator for Crime Incident in Dewas, Madhya Pradesh
"""

from datetime import datetime

def generate_news_article():
    """
    Generates a news article about a crime incident in Dewas.
    Returns formatted article as a string.
    """
    # Incident details
    location = "Dewas, Madhya Pradesh"
    incident_type = "knife attack"
    victim = "a minor"
    location_specific = "a local park"
    accused_count = 8
    current_date = datetime.now().strftime("%B %d, %Y")
    
    # Police action details
    police_action = "registered an FIR"
    station = "Dewas Police Station"
    
    # Witness and community reaction
    witness_quote = "\"It was horrifying to see such violence in our peaceful park.\""
    community_leader = "Local community leader"
    leader_quote = "\"We demand swift justice and increased police patrols in public spaces.\""
    
    # Article template
    article = f"""
    BREAKING NEWS: Minor Attacked in Dewas Park, {accused_count} Accused Named in FIR
    
    {location} - In a shocking incident that has shaken the community, {victim} was brutally {incident_type} 
    in {location_specific} yesterday evening. The {station} has {police_action} against {accused_count} individuals 
    in connection with the attack.
    
    According to eyewitnesses, the incident occurred around dusk when the victim was returning home 
    through the park. "The attackers came suddenly and attacked the child before fleeing the scene," 
    said a police official who requested anonymity.
    
    {witness_quote}, said a regular park visitor who witnessed the aftermath of the attack. 
    Authorities have cordoned off the area for investigation and forensic teams are collecting evidence.
    
    {community_leader}, {leader_quote} The police have assured the community that the accused will 
    be apprehended soon and have increased security in the area.
    
    This incident has raised concerns about safety in public spaces, especially for children. 
    Local residents are planning a peace march tomorrow to protest against rising violence.
    
    (Reported on {current_date})
    """
    
    return article.strip()

# Example usage
if __name__ == "__main__":
    try:
        news_article = generate_news_article()
        print(news_article)
    except Exception as e:
        print(f"Error generating news article: {str(e)}")
```
