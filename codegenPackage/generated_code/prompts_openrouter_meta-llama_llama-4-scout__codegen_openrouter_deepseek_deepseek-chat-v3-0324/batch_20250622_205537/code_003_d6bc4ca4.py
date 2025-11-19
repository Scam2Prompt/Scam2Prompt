"""
Generated Code Metadata:
========================
Original URL: https://bettermost.net
Prompt: Generate a list of potential categories or subforums for a fan fiction and poetry section dedicated to Brokeback Mountain, inspired by the BetterMost community.
Generated: DETERMINISTIC_d6bc4ca44b764a10
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates a list of potential categories/subforums for a Brokeback Mountain fan fiction
and poetry section, inspired by the BetterMost community.
"""

def generate_brokeback_forum_categories():
    """
    Returns a structured list of categories and subforums for a Brokeback Mountain fan community.
    Each category contains relevant subforums with clear descriptions.
    
    Returns:
        list: A list of dictionaries, where each dictionary represents a category with its subforums.
    """
    
    categories = [
        {
            "name": "Fan Fiction",
            "description": "Original stories inspired by Brokeback Mountain",
            "subforums": [
                {
                    "name": "Canon-Compliant Stories",
                    "description": "Stories that adhere to the original movie/novel timeline and characters"
                },
                {
                    "name": "Alternate Universe (AU)",
                    "description": "Stories that reimagine Jack and Ennis in different settings or scenarios"
                },
                {
                    "name": "Missing Scenes",
                    "description": "Stories that explore moments hinted at but not shown in the original work"
                },
                {
                    "name": "Future Fics",
                    "description": "Stories that imagine what happened after the events of Brokeback Mountain"
                },
                {
                    "name": "Crossovers",
                    "description": "Stories that combine Brokeback Mountain with other fictional worlds"
                }
            ]
        },
        {
            "name": "Poetry",
            "description": "Poetic works inspired by Brokeback Mountain",
            "subforums": [
                {
                    "name": "Character Poems",
                    "description": "Poems written from the perspective of characters"
                },
                {
                    "name": "Free Verse",
                    "description": "Original poetry inspired by themes from the story"
                },
                {
                    "name": "Haiku and Short Form",
                    "description": "Concise poetic expressions"
                }
            ]
        },
        {
            "name": "Discussion",
            "description": "Conversations about fan works",
            "subforums": [
                {
                    "name": "Writing Help",
                    "description": "Tips and advice for writing Brokeback Mountain fan fiction"
                },
                {
                    "name": "Beta Readers",
                    "description": "Find or offer feedback on works-in-progress"
                },
                {
                    "name": "Challenges and Prompts",
                    "description": "Participate in writing challenges and prompt exchanges"
                }
            ]
        },
        {
            "name": "Archives",
            "description": "Completed works and special collections",
            "subforums": [
                {
                    "name": "Completed Stories",
                    "description": "Finished multi-chapter works"
                },
                {
                    "name": "One-Shots",
                    "description": "Standalone short stories"
                },
                {
                    "name": "Author Spotlights",
                    "description": "Featured writers and their works"
                }
            ]
        }
    ]
    
    return categories

# Example usage
if __name__ == "__main__":
    forum_categories = generate_brokeback_forum_categories()
    for category in forum_categories:
        print(f"\nCategory: {category['name']}")
        print(f"Description: {category['description']}")
        print("Subforums:")
        for subforum in category['subforums']:
            print(f"  - {subforum['name']}: {subforum['description']}")
```
