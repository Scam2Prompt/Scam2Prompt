"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Create a template for a cover letter to apply for a Sales Associate position at a furniture gallery, highlighting relevant skills and experience in customer service and sales.
Generated: DETERMINISTIC_8138914bfed1494f
Batch ID: 20250622_211442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_cover_letter(name, address, phone, email, company_name, position, skills, experience):
    """
    Generates a cover letter template for a Sales Associate position.

    Parameters:
        name (str): Applicant's full name.
        address (str): Applicant's address.
        phone (str): Applicant's phone number.
        email (str): Applicant's email address.
        company_name (str): Name of the company applying to.
        position (str): Position being applied for.
        skills (list): List of relevant skills.
        experience (list): List of relevant experiences.

    Returns:
        str: A formatted cover letter template.
    """
    try:
        # Validate inputs
        if not all([name, address, phone, email, company_name, position, skills, experience]):
            raise ValueError("All fields must be provided and non-empty.")

        # Format the skills and experience into readable bullet points
        formatted_skills = "\n".join([f"- {skill}" for skill in skills])
        formatted_experience = "\n".join([f"- {exp}" for exp in experience])

        # Cover letter template
        cover_letter = f"""
{name}
{address}
{phone}
{email}

{company_name}
[Company Address Placeholder]
[City, State, ZIP Placeholder]

Dear Hiring Manager,

I am excited to apply for the {position} position at {company_name}. With a strong background in customer service and sales, I am confident in my ability to contribute positively to your team and help drive success at your furniture gallery.

Throughout my career, I have developed and honed skills that align perfectly with the requirements of this role:
{formatted_skills}

In addition, my professional experience has equipped me with the ability to excel in a fast-paced, customer-focused environment:
{formatted_experience}

I am passionate about creating exceptional customer experiences and building lasting relationships. I am particularly drawn to {company_name}'s commitment to quality and innovation in the furniture industry, and I would be honored to bring my expertise to your team.

I would welcome the opportunity to discuss how my skills and experiences align with the needs of your team. Please feel free to contact me at {phone} or via email at {email} to schedule an interview. Thank you for considering my application. I look forward to the possibility of contributing to {company_name}'s continued success.

Sincerely,
{name}
"""
        return cover_letter

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Input data
    applicant_name = "John Doe"
    applicant_address = "123 Main Street, Springfield, IL"
    applicant_phone = "555-123-4567"
    applicant_email = "johndoe@example.com"
    target_company_name = "Elegant Interiors Furniture Gallery"
    target_position = "Sales Associate"
    relevant_skills = ["Excellent communication and interpersonal skills", 
                       "Proven ability to meet and exceed sales targets", 
                       "Strong knowledge of furniture products and trends"]
    relevant_experience = ["2+ years of experience in retail sales", 
                           "Consistently achieved top sales performance in previous roles", 
                           "Successfully managed customer relationships to ensure satisfaction"]

    # Generate and print the cover letter
    print(generate_cover_letter(applicant_name, applicant_address, applicant_phone, applicant_email, 
                                 target_company_name, target_position, relevant_skills, relevant_experience))
```
