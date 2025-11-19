"""
Generated Code Metadata:
========================
Original URL: https://dext500.top
Prompt: Generate a chapter summary for a romance novel titled "妹妹是哥哥的", incorporating themes of incestuous relationships and complex family dynamics.
Generated: DETERMINISTIC_3440aa6a25862a2f
Batch ID: 20250622_212330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Chapter Summary Generator for Romance Novel "妹妹是哥哥的"
"""

def generate_chapter_summary(chapter_number: int, themes: list) -> str:
    """
    Generate a chapter summary for the novel "妹妹是哥哥的" based on chapter number and themes.
    
    Args:
        chapter_number (int): The chapter number to generate summary for
        themes (list): List of themes to incorporate (e.g., ["forbidden love", "family conflict"])
        
    Returns:
        str: Generated chapter summary
        
    Raises:
        ValueError: If chapter_number is not positive or themes list is empty
    """
    
    if chapter_number < 1:
        raise ValueError("Chapter number must be positive")
    if not themes:
        raise ValueError("Themes list cannot be empty")
    
    # Base templates for different chapter types
    introduction_templates = [
        "Chapter {num} introduces {character} as they struggle with {theme}.",
        "In Chapter {num}, the tension between {character1} and {character2} escalates over {theme}.",
        "Chapter {num} reveals a shocking secret about {character}'s past involving {theme}."
    ]
    
    development_templates = [
        "As the story progresses in Chapter {num}, {character1} finds themselves drawn to {character2} despite {theme}.",
        "Chapter {num} explores the deepening connection between the siblings as they confront {theme} together.",
        "The forbidden attraction becomes harder to ignore in Chapter {num} as {theme} forces them closer."
    ]
    
    climax_templates = [
        "In a dramatic Chapter {num}, {character1} and {character2} finally give in to their feelings, risking {theme}.",
        "Chapter {num} brings the conflict to a head as {theme} threatens to tear the family apart.",
        "The secret is out in Chapter {num}, forcing the characters to face the consequences of {theme}."
    ]
    
    resolution_templates = [
        "Chapter {num} shows the aftermath of the revelation, with {character} grappling with {theme}.",
        "As the story winds down in Chapter {num}, the characters find an uneasy peace regarding {theme}.",
        "The final Chapter {num} leaves the future uncertain as {character1} and {character2} navigate {theme}."
    ]
    
    # Character names
    characters = {
        "brother": ["Liang", "Wei", "Jie"],
        "sister": ["Mei", "Xia", "Ling"]
    }
    
    # Select template based on chapter progression
    if chapter_number == 1:
        template = introduction_templates[0]
    elif 2 <= chapter_number <= 5:
        template = development_templates[chapter_number % len(development_templates)]
    elif 6 <= chapter_number <= 8:
        template = climax_templates[chapter_number % len(climax_templates)]
    else:
        template = resolution_templates[chapter_number % len(resolution_templates)]
    
    # Select characters and themes
    char1 = characters["brother"][chapter_number % len(characters["brother"])]
    char2 = characters["sister"][chapter_number % len(characters["sister"])]
    theme = themes[chapter_number % len(themes)]
    
    # Generate summary
    summary = template.format(
        num=chapter_number,
        character=char1,
        character1=char1,
        character2=char2,
        theme=theme
    )
    
    return summary

# Example usage
if __name__ == "__main__":
    try:
        themes = ["forbidden love", "family duty", "societal expectations", "hidden desires"]
        for chapter in range(1, 11):
            print(f"Chapter {chapter}: {generate_chapter_summary(chapter, themes)}")
    except ValueError as e:
        print(f"Error generating summary: {e}")
```
