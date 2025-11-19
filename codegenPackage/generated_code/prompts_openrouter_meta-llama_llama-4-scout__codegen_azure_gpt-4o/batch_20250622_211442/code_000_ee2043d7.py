"""
Generated Code Metadata:
========================
Original URL: https://presale-topgs.com
Prompt: Write a job description for a Furniture Designer at a company that values craftsmanship and innovation, with a focus on creating functional and aesthetically pleasing furniture pieces in Seoul, South Korea.
Generated: DETERMINISTIC_ee2043d7e17bec77
Batch ID: 20250622_211442
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
    Generates a job description for a Furniture Designer position.
    The company values craftsmanship and innovation, with a focus on creating functional
    and aesthetically pleasing furniture pieces in Seoul, South Korea.
    
    Returns:
        str: A formatted job description.
    """
    try:
        # Job title
        job_title = "Furniture Designer"

        # Company values
        company_values = (
            "At our company, we are dedicated to craftsmanship and innovation. "
            "We believe in creating furniture that is not only functional but also "
            "aesthetically pleasing, enhancing the lives of our customers."
        )

        # Job location
        job_location = "Seoul, South Korea"

        # Responsibilities
        responsibilities = [
            "Design and develop innovative furniture pieces that align with the company's vision.",
            "Collaborate with cross-functional teams, including production and marketing, "
            "to ensure designs are feasible and marketable.",
            "Conduct research on furniture trends, materials, and manufacturing techniques.",
            "Create detailed sketches, prototypes, and 3D models of furniture designs.",
            "Ensure all designs meet ergonomic and functional standards.",
        ]

        # Requirements
        requirements = [
            "Bachelor's degree in Furniture Design, Industrial Design, or a related field.",
            "Proven experience in furniture design with a strong portfolio showcasing craftsmanship and innovation.",
            "Proficiency in design software such as AutoCAD, SketchUp, or Rhino.",
            "Knowledge of materials, manufacturing processes, and production techniques.",
            "Strong attention to detail and a passion for creating functional yet beautiful furniture.",
            "Excellent communication and teamwork skills.",
            "Ability to work in Seoul, South Korea or willingness to relocate.",
        ]

        # Benefits
        benefits = [
            "Competitive salary and performance-based bonuses.",
            "Opportunities for professional growth and development.",
            "Collaborative and creative work environment.",
            "Health insurance and wellness programs.",
            "Relocation assistance for qualified candidates.",
        ]

        # Format the job description
        job_description = f"""
        Job Title: {job_title}
        Location: {job_location}

        About Us:
        {company_values}

        Responsibilities:
        {"".join([f"- {resp}\n" for resp in responsibilities])}

        Requirements:
        {"".join([f"- {req}\n" for req in requirements])}

        Benefits:
        {"".join([f"- {benefit}\n" for benefit in benefits])}

        How to Apply:
        Please submit your resume, portfolio, and a cover letter detailing your experience and design philosophy to careers@ourcompany.com.
        """
        
        return job_description.strip()

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the job description: {str(e)}"


if __name__ == "__main__":
    # Generate and print the job description
    print(generate_job_description())
```
