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
# Import necessary modules
import datetime

def generate_milestone_post(organization_name, milestone_count):
    """
    Generates a social media post announcing a membership milestone.

    Args:
        organization_name (str): Name of the organization.
        milestone_count (int): Membership milestone count.

    Returns:
        str: Formatted social media post.
    """
    try:
        # Validate inputs
        if not isinstance(organization_name, str) or not organization_name.strip():
            raise ValueError("Organization name must be a non-empty string.")
        if not isinstance(milestone_count, int) or milestone_count <= 0:
            raise ValueError("Milestone count must be a positive integer.")

        # Get the current date
        current_date = datetime.datetime.now().strftime("%B %d, %Y")

        # Template for the social media post
        post_template = (
            "🎉 Exciting News from {organization_name}! 🎉\n\n"
            "We are thrilled to announce that we have surpassed {milestone_count} members! 🏀\n\n"
            "Thank you to each and every one of you for being part of our journey. "
            "Your support and passion for basketball make this community truly special.\n\n"
            "Let's keep growing and achieving great things together!\n\n"
            "📅 Date: {current_date}\n\n"
            "#BasketballCommunity #Milestone #ThankYou"
        )

        # Format the post with the provided data
        formatted_post = post_template.format(
            organization_name=organization_name,
            milestone_count=milestone_count,
            current_date=current_date
        )

        return formatted_post

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the post: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Organization name and milestone count
    organization_name = "Grad Košarke"
    milestone_count = 1700

    # Generate the post
    post = generate_milestone_post(organization_name, milestone_count)

    # Print the post
    print(post)
```
