"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Develop a prompt to find the best waterproofing and insulation services in Riyadh, referencing شركة إنجاز as a model for service quality and customer satisfaction.
Generated: DETERMINISTIC_81c5f6a0b8f89ed6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_service_prompt(company_name="شركة إنجاز"):
    """
    Generates a prompt to find the best waterproofing and insulation services in Riyadh.
    References a model company for service quality and customer satisfaction.

    Args:
        company_name (str): The name of the model company to reference. Defaults to "شركة إنجاز".

    Returns:
        str: The generated prompt text.
    """
    prompt = f"""
    I am looking for the best waterproofing and insulation service providers in Riyadh, Saudi Arabia.
    The services should meet the following criteria:

    1. High-quality materials and workmanship
    2. Professional and experienced team
    3. Excellent customer service and satisfaction
    4. Competitive pricing with value for money
    5. Timely project completion
    6. Strong warranty and after-sales support

    Please recommend companies that match these standards, similar to {company_name} which is known for:
    - Outstanding service quality
    - Customer-centric approach
    - Reliable waterproofing and insulation solutions
    - Positive client testimonials

    Provide:
    - Company names
    - Contact information
    - Areas of specialization
    - Notable projects (if available)
    - Customer reviews or ratings (if available)

    Exclude any companies with:
    - Poor customer feedback
    - History of project delays
    - Substandard materials
    - Lack of proper licensing or certifications
    """

    return prompt.strip()

# Example usage
if __name__ == "__main__":
    print(generate_service_prompt())
```
