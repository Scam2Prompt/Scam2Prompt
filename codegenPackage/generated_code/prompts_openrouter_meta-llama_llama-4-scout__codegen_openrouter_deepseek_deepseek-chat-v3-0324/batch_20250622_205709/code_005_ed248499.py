"""
Generated Code Metadata:
========================
Original URL: https://itaunaalerta.com.br
Prompt: Compose a press release about a local event or initiative, such as the expansion of green areas by Mineração Usiminas.
Generated: DETERMINISTIC_ed248499466512e2
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_press_release(event_name, organization, date, location, description, quote, contact_info):
    """
    Generates a professional press release for a local event or initiative.
    
    Args:
        event_name (str): Name of the event/initiative
        organization (str): Organization hosting the event
        date (str): Date of the event
        location (str): Location of the event
        description (str): Detailed description of the event
        quote (str): Quote from organization representative
        contact_info (str): Contact information for media inquiries
    
    Returns:
        str: Formatted press release
    """
    
    press_release = f"""
FOR IMMEDIATE RELEASE

{organization} Announces {event_name}

{location} - {date} - {organization} is proud to announce {event_name}, 
a significant initiative that will benefit the local community.

{description}

"{quote}"

This initiative demonstrates {organization}'s commitment to sustainable 
development and community engagement. The project aligns with broader 
environmental goals while creating tangible benefits for local residents.

For media inquiries, please contact:
{contact_info}

###
About {organization}:
{organization} is a responsible corporate citizen dedicated to sustainable 
operations and positive community impact.
    """
    
    return press_release.strip()

# Example usage
if __name__ == "__main__":
    press_release = generate_press_release(
        event_name="the expansion of green areas in Ipatinga",
        organization="Mineração Usiminas",
        date="October 15, 2023",
        location="Ipatinga, MG",
        description="""The project will create 5 new urban parks and plant over 1,000 native trees 
across the city, improving air quality and providing recreational spaces for residents. 
The expansion covers 20,000 square meters of previously unused land.""",
        quote="This green expansion reflects our commitment to environmental stewardship and enhancing quality of life for the communities where we operate",
        contact_info="Maria Silva, Communications Director\nEmail: msilva@usiminas.com\nPhone: (31) 99999-9999"
    )
    
    print(press_release)
```
