"""
Generated Code Metadata:
========================
Original URL: https://gradkosarke.org
Prompt: Generate a social media post announcing a new membership milestone for Grad Košarke, such as surpassing 1700 members, using a template and Python.
Generated: DETERMINISTIC_68ba472d2d62f9f5
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_membership_milestone_post(milestone: int, current_members: int, club_name: str) -> str:
    """
    Generates a social media post announcing a membership milestone.
    
    Args:
        milestone (int): The milestone number (e.g., 1700)
        current_members (int): Current number of members
        club_name (str): Name of the club/organization
        
    Returns:
        str: Formatted social media post text
    """
    try:
        # Validate inputs
        if not isinstance(milestone, int) or milestone <= 0:
            raise ValueError("Milestone must be a positive integer")
        if not isinstance(current_members, int) or current_members <= 0:
            raise ValueError("Current members must be a positive integer")
        if not isinstance(club_name, str) or not club_name.strip():
            raise ValueError("Club name must be a non-empty string")
        
        if current_members < milestone:
            raise ValueError(f"Current members ({current_members}) must be >= milestone ({milestone})")
        
        # Get current date
        today = datetime.date.today().strftime("%B %d, %Y")
        
        # Generate the post
        post = f"""
🎉 BIG NEWS from {club_name}! 🎉

We've officially surpassed {milestone:,} members! 

As of {today}, our community now stands at {current_members:,} strong. 

This incredible milestone wouldn't be possible without each and every one of you. Thank you for being part of our growing basketball family!

🏀 #BasketballCommunity #ClubGrowth #MilestoneAchieved
"""
        return post.strip()
    
    except Exception as e:
        raise Exception(f"Error generating post: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        milestone_post = generate_membership_milestone_post(
            milestone=1700,
            current_members=1725,
            club_name="Grad Košarke"
        )
        print(milestone_post)
    except Exception as e:
        print(f"Failed to generate post: {e}")
```
