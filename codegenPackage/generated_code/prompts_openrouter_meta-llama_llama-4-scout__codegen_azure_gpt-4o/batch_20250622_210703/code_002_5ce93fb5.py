"""
Generated Code Metadata:
========================
Original URL: https://accuratehire.co.in
Prompt: "Generate a job description for a recruiter position at Accurate Hire, highlighting the company's mission, values, and benefits, such as working with cutting-edge technology and a dynamic team."
Generated: DETERMINISTIC_5ce93fb5bf360a95
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# job_description_generator.py

def generate_job_description(company_name, position, mission, values, benefits):
    """
    Generates a job description for a given position at a company.

    Args:
        company_name (str): Name of the company.
        position (str): Job title for the position.
        mission (str): Company's mission statement.
        values (list): List of company values.
        benefits (list): List of benefits offered by the company.

    Returns:
        str: A formatted job description.
    """
    try:
        # Validate inputs
        if not company_name or not position or not mission or not values or not benefits:
            raise ValueError("All inputs must be provided and non-empty.")

        # Format the job description
        job_description = f"""
        Job Title: {position}
        Company: {company_name}

        About Us:
        {company_name} is dedicated to {mission}. We are committed to upholding our core values:
        {', '.join(values)}.

        Position Overview:
        As a {position}, you will play a key role in helping us achieve our mission by identifying and recruiting top talent to join our dynamic team.

        Why Join Us:
        At {company_name}, we offer:
        {', '.join(benefits)}.

        If you're passionate about working with cutting-edge technology and being part of a collaborative and innovative team, we encourage you to apply!
        """
        return job_description.strip()

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"Error generating job description: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define company details
    company_name = "Accurate Hire"
    position = "Recruiter"
    mission = "connecting top talent with leading organizations"
    values = ["Integrity", "Innovation", "Collaboration", "Excellence"]
    benefits = [
        "Working with cutting-edge technology",
        "Being part of a dynamic and supportive team",
        "Opportunities for professional growth",
        "Competitive salary and benefits package"
    ]

    # Generate and print the job description
    job_description = generate_job_description(company_name, position, mission, values, benefits)
    print(job_description)
```
