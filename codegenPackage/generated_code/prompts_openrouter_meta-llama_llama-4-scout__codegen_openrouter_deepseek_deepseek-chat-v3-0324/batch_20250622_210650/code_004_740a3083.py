"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Write a query letter to a literary agent for a political thriller novel that explores the intersection of romance, history, and nuclear politics in China.
Generated: DETERMINISTIC_740a30832d85a12f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_query_letter(agent_name, author_name, novel_title):
    """
    Generates a professional query letter for a literary agent.
    
    Args:
        agent_name (str): Name of the literary agent
        author_name (str): Name of the author
        novel_title (str): Title of the novel
    
    Returns:
        str: Formatted query letter
    """
    
    letter = f"""
{agent_name}

Dear {agent_name.split()[0]},

I am seeking representation for my political thriller, "{novel_title}", complete at 95,000 words. 
This novel explores the dangerous intersection of romance, history, and nuclear politics in 
contemporary China, where personal and geopolitical tensions reach a boiling point.

The story follows [PROTAGONIST NAME], a [PROTAGONIST DESCRIPTION], who becomes entangled in 
a high-stakes game of international intrigue when they discover [CENTRAL CONFLICT]. As 
relationships blur lines between love and espionage, the characters must navigate a landscape 
where historical grievances fuel present-day conflicts, with the threat of nuclear escalation 
looming over every decision.

This novel will appeal to readers who enjoyed the geopolitical tension of "The Sympathizer" 
by Viet Thanh Nguyen combined with the romantic suspense of "The Nightingale" by Kristin Hannah. 
As someone who represents [REFERENCE TO AGENT'S INTERESTS/CLIENT LIST], I believe this project 
would be a good fit for your list.

I am a [BRIEF AUTHOR BIO WITH RELEVANT CREDENTIALS]. Thank you for your time and consideration. 
I would be delighted to send the complete manuscript at your request.

Sincerely,
{author_name}
[CONTACT INFORMATION]
"""
    
    return letter.strip()

# Example usage
if __name__ == "__main__":
    try:
        agent_name = "Jane Doe"
        author_name = "John Smith"
        novel_title = "The Dragon's Gambit"
        
        query_letter = generate_query_letter(agent_name, author_name, novel_title)
        print(query_letter)
    except Exception as e:
        print(f"Error generating query letter: {e}")
```
