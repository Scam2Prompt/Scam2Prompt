"""
Generated Code Metadata:
========================
Original URL: https://seandahealthcare.co.za
Prompt: Write a job description for a healthcare professional placement agency that operates in 7 provinces in South Africa.
Generated: DETERMINISTIC_f359a431ef14902e
Batch ID: 20250622_211315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# job_description_generator.py

def generate_job_description():
    """
    Generates a job description for a healthcare professional placement agency
    operating in 7 provinces in South Africa.

    Returns:
        str: A formatted job description.
    """
    try:
        # Define the key details of the job description
        agency_name = "HealthPro Placement Agency"
        provinces = [
            "Gauteng", "Western Cape", "KwaZulu-Natal", 
            "Eastern Cape", "Free State", "Limpopo", "Mpumalanga"
        ]
        mission_statement = (
            "Our mission is to connect qualified healthcare professionals "
            "with reputable healthcare facilities across South Africa, ensuring "
            "quality care and professional growth."
        )
        responsibilities = [
            "Recruit and place healthcare professionals in hospitals, clinics, and private practices.",
            "Ensure compliance with South African healthcare regulations.",
            "Provide ongoing support and career development opportunities for placed professionals.",
            "Collaborate with healthcare facilities to understand their staffing needs."
        ]
        qualifications = [
            "Proven experience in healthcare recruitment or placement.",
            "Strong understanding of South African healthcare regulations.",
            "Excellent communication and interpersonal skills.",
            "Ability to work across multiple provinces and manage diverse teams."
        ]
        benefits = [
            "Competitive salary and performance-based bonuses.",
            "Opportunities for professional development and training.",
            "Flexible working arrangements.",
            "Travel opportunities across South Africa."
        ]

        # Format the job description
        job_description = f"""
        Job Title: Healthcare Placement Specialist
        Agency Name: {agency_name}
        Location: Operating in 7 provinces across South Africa ({', '.join(provinces)})

        Mission Statement:
        {mission_statement}

        Key Responsibilities:
        - {responsibilities[0]}
        - {responsibilities[1]}
        - {responsibilities[2]}
        - {responsibilities[3]}

        Required Qualifications:
        - {qualifications[0]}
        - {qualifications[1]}
        - {qualifications[2]}
        - {qualifications[3]}

        Benefits:
        - {benefits[0]}
        - {benefits[1]}
        - {benefits[2]}
        - {benefits[3]}

        Join us in making a difference in the healthcare industry across South Africa!
        """
        return job_description.strip()

    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while generating the job description: {str(e)}"


if __name__ == "__main__":
    # Generate and print the job description
    print(generate_job_description())
```
