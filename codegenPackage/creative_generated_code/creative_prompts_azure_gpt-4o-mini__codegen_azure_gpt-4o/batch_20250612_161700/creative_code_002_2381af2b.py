"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: As an employer in Spain, what legal procedures must I follow to hire a non-EU worker, and how can I ensure compliance with immigration laws?
Generated: DETERMINISTIC_2381af2b8aa7f1cb
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

To generate legal compliance-related guidance for hiring non-EU workers in Spain, we can automate an informational checklist process using Python. Here's the clean, production-ready code:

```python
import datetime

# Function to check legal procedures for hiring non-EU workers in Spain
def hiring_non_eu_worker_in_spain(worker_nationality, job_position):
    """
    Provides a checklist of legal procedures for hiring a non-EU worker in Spain
    and ensures compliance with immigration laws.

    Args:
        worker_nationality (str): Nationality of the worker (e.g., 'India', 'China').
        job_position (str): Job position offered to the worker.
    
    Returns:
        dict: Steps and requirements for ensuring compliance with Spanish hiring laws.
    """
    try:
        # Verify worker's nationality
        if worker_nationality.lower() == "spain":
            raise ValueError("Worker is already a citizen of Spain. No special procedures required.")
        
        # Create a checklist for legal procedures
        compliance_checklist = {
            "Step 1": "Ensure the job position is listed in Spain's shortage occupation list.",
            "Step 2": "Advertise the job vacancy in Spain for at least 15 days to confirm no suitable EU candidates are available.",
            "Step 3": "Obtain a work permit for the worker by applying at the Ministry of Labor or through an authorized representative.",
            "Step 4": "Ensure the worker has a valid visa for entering Spain (apply at the Spanish consulate in the worker's home country).",
            "Step 5": "Register the worker with Spain's Social Security system (Seguridad Social).",
            "Step 6": "Ensure the worker has a NIE (Número de Identificación de Extranjero) – the Spanish foreigner identification number.",
            "Step 7": "Draft a valid employment contract in accordance with Spanish labor laws.",
            "Step 8": "Submit all required documentation to the relevant Spanish immigration authorities."
        }
        
        # Return the checklist to ensure compliance
        return {
            "Worker Nationality": worker_nationality,
            "Job Position": job_position,
            "Compliance Checklist": compliance_checklist,
            "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    except ValueError as ve:
        return {"Error": str(ve)}
    except Exception as e:
        return {"Error": f"An unexpected error occurred: {str(e)}"}


# Example Usage
if __name__ == "__main__":
    worker_nationality = "India"  # Replace with actual nationality
    job_position = "Software Engineer"  # Replace with actual job position
    
    # Get the legal compliance checklist
    result = hiring_non_eu_worker_in_spain(worker_nationality, job_position)
    
    # Print the result
    for key, value in result.items():
        print(f"{key}: {value}")
```

Run this script to obtain the legal procedures checklist for hiring a non-EU worker in Spain based on the worker's nationality and job position.
