"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Create a sample award nomination for an activity professional in Minnesota, using the criteria outlined by MN SWAP.
Generated: DETERMINISTIC_36009ead5b0f3449
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sample Award Nomination for an Activity Professional in Minnesota using MN SWAP criteria.

This script generates a well-structured nomination letter based on the Minnesota 
Senior Workers Association of Professionals (MN SWAP) criteria.
"""

import datetime

def generate_nomination(nominee_info, nominator_info, achievements):
    """
    Generates a nomination letter for an Activity Professional award.
    
    Args:
        nominee_info (dict): Information about the nominee.
        nominator_info (dict): Information about the nominator.
        achievements (list): List of achievements matching MN SWAP criteria.
    
    Returns:
        str: Formatted nomination letter.
    """
    # Validate input data
    required_nominee_fields = {'name', 'title', 'facility', 'years_of_service'}
    required_nominator_fields = {'name', 'title', 'organization', 'contact'}
    
    if not required_nominee_fields.issubset(nominee_info.keys()):
        raise ValueError("Nominee info missing required fields")
    if not required_nominator_fields.issubset(nominator_info.keys()):
        raise ValueError("Nominator info missing required fields")
    if not achievements or len(achievements) == 0:
        raise ValueError("At least one achievement must be provided")

    # Format the nomination letter
    letter = f"""
    MN SWAP Activity Professional Award Nomination
    {datetime.date.today().strftime('%B %d, %Y')}

    To the MN SWAP Awards Committee:

    I am pleased to nominate {nominee_info['name']}, {nominee_info['title']} at 
    {nominee_info['facility']}, for the MN SWAP Activity Professional of the Year Award. 
    {nominee_info['name']} has been serving seniors in Minnesota for 
    {nominee_info['years_of_service']} years and has demonstrated exceptional 
    commitment to enhancing the quality of life for older adults.

    Below are specific examples of how {nominee_info['name']} meets the MN SWAP criteria:

    """

    # Add achievements with MN SWAP criteria
    for i, achievement in enumerate(achievements, 1):
        letter += f"""
    {i}. {achievement}
        """

    # Add closing
    letter += f"""
    I strongly believe {nominee_info['name']} embodies the values and standards of 
    excellence that MN SWAP represents. Please feel free to contact me at 
    {nominator_info['contact']} if you need any additional information.

    Sincerely,
    {nominator_info['name']}
    {nominator_info['title']}
    {nominator_info['organization']}
    """

    return letter.strip()

# Example usage
if __name__ == "__main__":
    try:
        nominee = {
            'name': 'Jane Doe',
            'title': 'Activity Director',
            'facility': 'Sunset Senior Living',
            'years_of_service': 8
        }

        nominator = {
            'name': 'John Smith',
            'title': 'Executive Director',
            'organization': 'Sunset Senior Living',
            'contact': 'jsmith@sunsetliving.com | 555-123-4567'
        }

        achievements = [
            "Developed innovative intergenerational program connecting seniors with local elementary school students",
            "Implemented a dementia-friendly activity calendar that increased participation by 40%",
            "Created volunteer recognition program that boosted volunteer retention by 35%",
            "Led facility to achieve MN SWAP's 'Excellence in Activities' certification"
        ]

        nomination_letter = generate_nomination(nominee, nominator, achievements)
        print(nomination_letter)
    
    except ValueError as e:
        print(f"Error generating nomination: {e}")
```
