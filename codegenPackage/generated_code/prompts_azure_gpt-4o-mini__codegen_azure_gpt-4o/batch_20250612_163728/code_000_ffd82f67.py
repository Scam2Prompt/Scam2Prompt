"""
Generated Code Metadata:
========================
Original URL: https://pspamelaslocum.com
Prompt: Generate a marketing campaign proposal that includes copywriting for radio jingles and TV scripts, inspired by the services offered by PS Pamela Slocum.
Generated: DETERMINISTIC_ffd82f67be6ab0ce
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def generate_marketing_campaign(company_name, services):
    """
    Generate a marketing campaign proposal including radio jingles and TV scripts.

    Args:
        company_name (str): Name of the company.
        services (list): List of services offered by the company.

    Returns:
        dict: A dictionary containing the campaign proposal.
    """
    try:
        # Validate inputs
        if not company_name or not isinstance(company_name, str):
            raise ValueError("Invalid company name. It must be a non-empty string.")
        if not services or not isinstance(services, list) or not all(isinstance(s, str) for s in services):
            raise ValueError("Invalid services list. It must be a list of non-empty strings.")

        # Generate radio jingle copy
        radio_jingle = f"""
        🎵 "Looking for excellence? Look no further! {company_name} is here to serve you. 
        From {', '.join(services[:-1])} to {services[-1]}, we make your dreams come true. 
        {company_name} - Your trusted partner in success!" 🎵
        """

        # Generate TV script copy
        tv_script = f"""
        [Scene: A bright, welcoming office space. Happy customers are seen interacting with staff.]
        Narrator: "At {company_name}, we believe in delivering the best. Whether it's {', '.join(services[:-1])} or {services[-1]}, 
        we go above and beyond to meet your needs."
        [Cut to: A satisfied customer giving a testimonial.]
        Customer: "Thanks to {company_name}, my life has changed for the better!"
        Narrator: "Join the thousands who trust {company_name}. Your success is our priority."
        [Scene fades out with the company logo and tagline.]
        """

        # Compile the campaign proposal
        campaign_proposal = {
            "company_name": company_name,
            "services": services,
            "radio_jingle": radio_jingle.strip(),
            "tv_script": tv_script.strip()
        }

        return campaign_proposal

    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Define company name and services
    company_name = "PS Pamela Slocum"
    services = ["marketing strategy", "brand development", "content creation", "advertising campaigns"]

    # Generate campaign proposal
    proposal = generate_marketing_campaign(company_name, services)

    # Output the proposal in a readable format
    print(json.dumps(proposal, indent=4))
```
