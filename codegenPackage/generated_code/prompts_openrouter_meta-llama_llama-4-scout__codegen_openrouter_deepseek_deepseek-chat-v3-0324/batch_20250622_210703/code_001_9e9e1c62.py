"""
Generated Code Metadata:
========================
Original URL: https://somosvos.info
Prompt: Generate a public service announcement for businesses in Corrientes to advertise on the Somos Vos website and radio station, highlighting the benefits of reaching a large audience.
Generated: DETERMINISTIC_9e9e1c62c78d6882
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Public Service Announcement Generator for Somos Vos Advertising

def generate_psa(business_name, contact_info):
    """
    Generates a professional public service announcement for businesses in Corrientes
    to advertise on Somos Vos website and radio station.
    
    Args:
        business_name (str): Name of the business to be included in the PSA
        contact_info (str): Contact information for the business
        
    Returns:
        str: Formatted public service announcement text
    """
    
    # Validate input parameters
    if not business_name or not contact_info:
        raise ValueError("Business name and contact information are required")
    
    psa_template = f"""
    **PUBLIC SERVICE ANNOUNCEMENT - SOMOS VOS ADVERTISING OPPORTUNITY**
    
    Attention businesses in Corrientes! {business_name} invites you to join them in 
    reaching thousands of potential customers through Somos Vos - the leading 
    digital platform and radio station in our region.
    
    **Why advertise with Somos Vos?**
    - Reach a large, engaged audience across Corrientes
    - Targeted exposure on both digital (website) and traditional (radio) media
    - Affordable advertising packages tailored to your business needs
    - Professional production services to make your message stand out
    
    Take your business to the next level! Contact {business_name} at {contact_info} 
    to learn more about their experience advertising with Somos Vos, or visit 
    somosvos.com.ar/advertise to get started today.
    
    #SomosVos #Corrientes #LocalBusiness
    """
    
    return psa_template.strip()

# Example usage
try:
    business = "La Estrella Restaurant"
    contact = "info@laestrella.com | 3794-555123"
    announcement = generate_psa(business, contact)
    print(announcement)
except ValueError as e:
    print(f"Error generating PSA: {e}")
```
