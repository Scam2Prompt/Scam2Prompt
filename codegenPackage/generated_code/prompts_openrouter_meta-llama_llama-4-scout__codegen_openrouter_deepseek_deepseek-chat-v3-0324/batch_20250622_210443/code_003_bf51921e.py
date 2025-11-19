"""
Generated Code Metadata:
========================
Original URL: https://ammaparivaar.org
Prompt: Develop a social media post encouraging people to support NGOs like Amma Parivaar that work towards making India a better country.
Generated: DETERMINISTIC_bf51921e2c671450
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_social_media_post(ngo_name="Amma Parivaar"):
    """
    Generates a social media post encouraging support for NGOs working in India.
    
    Args:
        ngo_name (str): Name of the NGO to highlight in the post. Defaults to "Amma Parivaar".
    
    Returns:
        str: Formatted social media post text with hashtags.
    """
    post = f"""
    🌟 Let's Come Together to Make India Better! 🌟

    NGOs like {ngo_name} are doing incredible work to uplift communities and create positive change across our nation. 
    From education to healthcare, women's empowerment to rural development - their impact is truly inspiring!

    🤝 Here's how YOU can help:
    ✅ Donate to support their initiatives
    ✅ Volunteer your time and skills
    ✅ Spread awareness about their work
    ✅ Encourage others to get involved

    Every small contribution makes a BIG difference in someone's life. 
    Together, we can build a stronger, more compassionate India!

    #SupportNGOs #MakeADifference #IndiaForGood #{ngo_name.replace(' ', '')} #SocialChange #GiveBack #CommunityFirst
    """
    
    return post.strip()

if __name__ == "__main__":
    try:
        post_content = generate_social_media_post()
        print(post_content)
    except Exception as e:
        print(f"Error generating post: {str(e)}")
```
