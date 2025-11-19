"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Generate a glossary of slo-pitch softball terms and definitions, referencing the Slo-Pitch Softball Terms Glossary on Slo-Pitch Central.
Generated: DETERMINISTIC_154b6a173d05cdcf
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Slo-Pitch Softball Glossary
This module contains a dictionary of common slo-pitch softball terms and their definitions,
referenced from Slo-Pitch Central's glossary.
"""

glossary = {
    "Arc": "The height the ball reaches after being pitched, must be between 6-12 feet.",
    "Backstop": "The fence or net behind home plate that stops wild pitches.",
    "Batting Order": "The sequence in which players take their turns batting.",
    "Bunt": "A soft hit where the batter doesn't swing but lets the ball hit the bat.",
    "Dead Ball": "A ball that is no longer in play, resulting in a stoppage of play.",
    "Double Play": "Two outs made on one continuous play.",
    "Fair Ball": "A batted ball that lands in fair territory.",
    "Foul Ball": "A batted ball that lands in foul territory.",
    "Home Run": "A hit that allows the batter to circle all bases and score.",
    "Infield": "The area of the field within the baselines.",
    "Inning": "A division of the game consisting of each team having a turn at bat.",
    "Line Drive": "A hard-hit ball that travels in a straight line.",
    "On Deck": "The next batter due to bat after the current batter.",
    "Outfield": "The area of the field beyond the infield.",
    "Pitcher": "The player who delivers the ball to the batter.",
    "Run": "A point scored when a player successfully rounds all bases.",
    "Sacrifice Fly": "A fly ball caught for an out that allows a runner to score.",
    "Strike Zone": "The area over home plate between the batter's knees and chest.",
    "Tag Up": "A runner waiting on base until a fly ball is caught before advancing.",
    "Walk": "Advancing to first base after four balls are called.",
    "Wild Pitch": "A pitch that is too high, low, or wide to be hit."
}

def get_term_definition(term):
    """
    Retrieve the definition of a slo-pitch softball term.
    
    Args:
        term (str): The term to look up in the glossary.
        
    Returns:
        str: The definition if found, otherwise a message indicating the term wasn't found.
    """
    return glossary.get(term.title(), f"Term '{term}' not found in the glossary.")

def list_all_terms():
    """
    List all terms in the glossary alphabetically.
    
    Returns:
        list: Alphabetically sorted list of all glossary terms.
    """
    return sorted(glossary.keys())

def search_terms(keyword):
    """
    Search for terms containing the given keyword (case-insensitive).
    
    Args:
        keyword (str): The keyword to search for in term names.
        
    Returns:
        list: Matching terms that contain the keyword.
    """
    keyword = keyword.lower()
    return [term for term in glossary if keyword in term.lower()]

if __name__ == "__main__":
    # Example usage
    print("Slo-Pitch Softball Glossary")
    print("---------------------------")
    print("Available terms:", ", ".join(list_all_terms()))
    print("\nDefinition of 'Arc':", get_term_definition("Arc"))
    print("\nTerms containing 'ball':", ", ".join(search_terms("ball")))
```
