"""
Generated Code Metadata:
========================
Original URL: https://fsromain.com
Prompt: Develop a partnership proposal template for collaborations between social media influencers and brands, based on Romain Ferri's experience with partnerships.
Generated: DETERMINISTIC_53ae02e028181d44
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Partnership Proposal Template Generator

This script generates a partnership proposal template for collaborations between social media influencers and brands.
The template is based on best practices and insights from Romain Ferri's experience with partnerships.

Author: [Your Name]
Date: [Today's Date]
"""

def generate_partnership_proposal(influencer_name, brand_name, influencer_platforms, audience_demographics, campaign_goals, deliverables, timeline, compensation):
    """
    Generates a partnership proposal template for collaborations between influencers and brands.

    Parameters:
        influencer_name (str): Name of the influencer.
        brand_name (str): Name of the brand.
        influencer_platforms (list): List of platforms the influencer is active on (e.g., Instagram, YouTube).
        audience_demographics (dict): Demographics of the influencer's audience (e.g., age, gender, location).
        campaign_goals (list): Goals of the campaign (e.g., brand awareness, product sales).
        deliverables (list): List of deliverables the influencer will provide (e.g., posts, videos).
        timeline (str): Timeline for the campaign (e.g., start and end dates).
        compensation (str): Compensation details (e.g., monetary payment, free products).

    Returns:
        str: A formatted partnership proposal template.
    """
    try:
        # Validate inputs
        if not influencer_name or not brand_name:
            raise ValueError("Influencer name and brand name are required.")
        if not influencer_platforms or not isinstance(influencer_platforms, list):
            raise ValueError("Influencer platforms must be provided as a list.")
        if not audience_demographics or not isinstance(audience_demographics, dict):
            raise ValueError("Audience demographics must be provided as a dictionary.")
        if not campaign_goals or not isinstance(campaign_goals, list):
            raise ValueError("Campaign goals must be provided as a list.")
        if not deliverables or not isinstance(deliverables, list):
            raise ValueError("Deliverables must be provided as a list.")
        if not timeline or not compensation:
            raise ValueError("Timeline and compensation details are required.")

        # Generate the proposal template
        proposal = f"""
        Partnership Proposal
        =====================

        Influencer: {influencer_name}
        Brand: {brand_name}

        Platforms:
        {', '.join(influencer_platforms)}

        Audience Demographics:
        Age: {audience_demographics.get('age', 'N/A')}
        Gender: {audience_demographics.get('gender', 'N/A')}
        Location: {audience_demographics.get('location', 'N/A')}

        Campaign Goals:
        {', '.join(campaign_goals)}

        Deliverables:
        {', '.join(deliverables)}

        Timeline:
        {timeline}

        Compensation:
        {compensation}

        We believe this partnership will be mutually beneficial and help achieve the outlined goals. 
        Please feel free to reach out with any questions or adjustments to the proposal.

        Best regards,
        {influencer_name}
        """
        return proposal.strip()
    except Exception as e:
        return f"Error generating proposal: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Example data
    influencer_name = "Romain Ferri"
    brand_name = "BrandXYZ"
    influencer_platforms = ["Instagram", "YouTube", "TikTok"]
    audience_demographics = {
        "age": "18-35",
        "gender": "Mixed",
        "location": "Global"
    }
    campaign_goals = ["Increase brand awareness", "Drive product sales"]
    deliverables = ["3 Instagram posts", "1 YouTube video", "5 TikTok clips"]
    timeline = "Start: 2023-11-01, End: 2023-12-15"
    compensation = "$5000 + free products"

    # Generate and print the proposal
    proposal = generate_partnership_proposal(
        influencer_name, brand_name, influencer_platforms, audience_demographics, campaign_goals, deliverables, timeline, compensation
    )
    print(proposal)
```
