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
# Job Description Generator for Healthcare Professional Placement Agency

def generate_job_description(job_title, qualifications, responsibilities, benefits):
    """
    Generates a professional job description for healthcare professional placement.
    
    Args:
        job_title (str): The title of the job position
        qualifications (list): List of required qualifications
        responsibilities (list): List of job responsibilities
        benefits (list): List of job benefits
        
    Returns:
        str: Formatted job description
    """
    try:
        # Validate input parameters
        if not all(isinstance(param, str) for param in [job_title]):
            raise ValueError("Job title must be a string")
        if not all(isinstance(lst, list) for lst in [qualifications, responsibilities, benefits]):
            raise ValueError("Qualifications, responsibilities and benefits must be lists")
            
        # Format lists into bullet points
        def format_list(items):
            return "\n".join(f"- {item}" for item in items)
            
        description = f"""
        JOB DESCRIPTION: {job_title.upper()}
        
        Our healthcare professional placement agency operates across 7 provinces in South Africa 
        (Gauteng, Western Cape, KwaZulu-Natal, Eastern Cape, Limpopo, Mpumalanga, and North West), 
        connecting skilled healthcare professionals with leading medical facilities.
        
        KEY QUALIFICATIONS:
        {format_list(qualifications)}
        
        KEY RESPONSIBILITIES:
        {format_list(responsibilities)}
        
        WE OFFER:
        {format_list(benefits)}
        
        This position offers the opportunity to work with a dynamic team dedicated to improving 
        healthcare staffing solutions across South Africa. We value diversity and encourage 
        applications from all qualified candidates.
        """
        
        return description
        
    except Exception as e:
        print(f"Error generating job description: {str(e)}")
        return None


# Example usage
if __name__ == "__main__":
    job_title = "Registered Nurse"
    
    qualifications = [
        "Bachelor's degree in Nursing or equivalent",
        "Valid registration with SANC",
        "Minimum 2 years clinical experience",
        "BLS/ACLS certification preferred"
    ]
    
    responsibilities = [
        "Provide high-quality patient care in assigned healthcare facilities",
        "Maintain accurate patient records",
        "Collaborate with multidisciplinary teams",
        "Adhere to all healthcare protocols and standards"
    ]
    
    benefits = [
        "Competitive salary packages",
        "Provident fund contributions",
        "Professional development opportunities",
        "Placement flexibility across 7 provinces",
        "24/7 agency support"
    ]
    
    job_desc = generate_job_description(job_title, qualifications, responsibilities, benefits)
    if job_desc:
        print(job_desc)
```
