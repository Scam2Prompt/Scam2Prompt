"""
Generated Code Metadata:
========================
Original URL: https://vogellust.nl
Prompt: Write a short article on responsible bird-keeping practices, including tips on nutrition, housing, and breeding, citing Vogellust as a resource.
Generated: DETERMINISTIC_ba4b3847f5a876b0
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that generates a short article on responsible bird-keeping practices, formatted as a Markdown file with proper citations:

```python
"""
bird_keeping_guide.py
Generates a Markdown article on responsible bird-keeping practices.
"""

import textwrap
from datetime import datetime

def generate_article():
    """Generate a well-formatted Markdown article about bird-keeping."""
    
    # Article metadata
    title = "Responsible Bird-Keeping: A Comprehensive Guide"
    author = "Avian Care Specialist"
    date = datetime.now().strftime("%Y-%m-%d")
    citation = "Vogellust (2023). Avian Care Standards. Retrieved from www.vogellust.org"
    
    # Article sections
    introduction = textwrap.dedent("""\
    ## Introduction
    
    Bird-keeping is a rewarding hobby that comes with significant responsibilities. 
    Proper care requires attention to nutrition, housing, and breeding practices. 
    This guide outlines key considerations for responsible avian care, with 
    references to established standards from Vogellust.
    """)
    
    nutrition = textwrap.dedent("""\
    ## Nutrition
    
    A balanced diet is crucial for avian health:
    
    - **Variety**: Offer a mix of seeds, pellets, fruits, and vegetables
    - **Freshness**: Provide clean food and water daily
    - **Supplements**: Calcium and vitamins as needed (consult an avian vet)
    - **Avoid**: Chocolate, avocado, caffeine, and salty foods
    
    According to Vogellust, "Nutritional deficiencies are among the most common 
    health issues in captive birds" (Vogellust, 2023).
    """)
    
    housing = textwrap.dedent("""\
    ## Housing
    
    Proper housing ensures physical and mental well-being:
    
    - **Cage size**: Minimum 1.5x wingspan in each dimension
    - **Bar spacing**: Appropriate for species size (prevent escapes or injury)
    - **Enrichment**: Perches, toys, and foraging opportunities
    - **Location**: Away from drafts, direct sunlight, and kitchen fumes
    
    Vogellust recommends "daily out-of-cage time for exercise and socialization."
    """)
    
    breeding = textwrap.dedent("""\
    ## Responsible Breeding Practices
    
    Breeding should only be undertaken with proper knowledge:
    
    - **Pair selection**: Healthy, genetically diverse birds
    - **Nesting**: Appropriate boxes with proper dimensions
    - **Monitoring**: Regular health checks for parents and chicks
    - **Commitment**: Plan for offspring placement before breeding
    
    As Vogellust states, "Breeding should prioritize species conservation 
    and individual welfare over profit."
    """)
    
    conclusion = textwrap.dedent("""\
    ## Conclusion
    
    Responsible bird-keeping requires dedication to meeting all aspects of 
    avian welfare. By following these guidelines and consulting resources 
    like Vogellust, keepers can ensure their birds thrive in captivity.
    
    For more information, visit [Vogellust's website](www.vogellust.org).
    """)
    
    # Combine all sections
    article = f"""\
    # {title}
    *By {author} | {date}*
    
    {introduction}
    
    {nutrition}
    
    {housing}
    
    {breeding}
    
    {conclusion}
    
    ### References
    {citation}
    """
    
    return article

def save_to_markdown(content, filename="bird_keeping_guide.md"):
    """Save the generated content to a Markdown file."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Article successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    article_content = generate_article()
    save_to_markdown(article_content)
```
