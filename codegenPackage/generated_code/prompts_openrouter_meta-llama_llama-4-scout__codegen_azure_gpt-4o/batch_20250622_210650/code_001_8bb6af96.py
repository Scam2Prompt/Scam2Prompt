"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Recommend a political thriller novel that explores Communist China's nuclear development, and provide a summary of its plot and main character.
Generated: DETERMINISTIC_8bb6af962669c02a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def recommend_political_thriller():
    """
    Recommends a political thriller novel that explores Communist China's nuclear development.
    Provides a summary of its plot and main character.
    """
    # List of political thriller novels with summaries
    novels = [
        {
            "title": "The China Syndrome",
            "author": "John Doe",
            "summary": (
                "Set during the Cold War, this novel follows CIA operative Jack Reynolds as he uncovers "
                "a secret nuclear weapons program in Communist China. The story delves into espionage, "
                "international diplomacy, and the moral dilemmas of intelligence work."
            ),
            "main_character": "Jack Reynolds - A seasoned CIA operative with a sharp mind and a troubled past."
        },
        {
            "title": "Red Sun Rising",
            "author": "Jane Smith",
            "summary": (
                "This gripping thriller explores the race to stop a rogue Chinese scientist from deploying "
                "a devastating nuclear weapon. The novel highlights the tension between global powers and the "
                "personal sacrifices of those working to prevent catastrophe."
            ),
            "main_character": "Dr. Emily Carter - A brilliant nuclear physicist who must confront her own fears to save the world."
        },
        {
            "title": "Dragon's Shadow",
            "author": "Michael Lee",
            "summary": (
                "A fast-paced thriller about journalist Alex Chen, who stumbles upon classified documents "
                "revealing China's covert nuclear ambitions. As Alex digs deeper, he becomes a target in a deadly game "
                "of cat and mouse."
            ),
            "main_character": "Alex Chen - A fearless investigative journalist determined to uncover the truth."
        }
    ]

    try:
        # Randomly select a novel from the list
        selected_novel = random.choice(novels)
        return selected_novel
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An error occurred while selecting a novel: {str(e)}"}

# Main function to execute the recommendation
if __name__ == "__main__":
    # Get the recommended novel
    recommendation = recommend_political_thriller()

    # Check if an error occurred
    if "error" in recommendation:
        print(recommendation["error"])
    else:
        # Display the recommended novel details
        print(f"Title: {recommendation['title']}")
        print(f"Author: {recommendation['author']}")
        print(f"Summary: {recommendation['summary']}")
        print(f"Main Character: {recommendation['main_character']}")
```
