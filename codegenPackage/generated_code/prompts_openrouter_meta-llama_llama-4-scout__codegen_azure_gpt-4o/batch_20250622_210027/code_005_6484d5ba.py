"""
Generated Code Metadata:
========================
Original URL: https://remote-job.org
Prompt: Compare job requirements and responsibilities for a Design Verification Engineer (PCIe, CXL, UVM, System Verilog) versus a NET Web & Middleware Administrator role.
Generated: DETERMINISTIC_6484d5ba7187bb2c
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define the job roles and their respective requirements and responsibilities
job_roles = {
    "Design Verification Engineer": {
        "Requirements": [
            "Proficiency in PCIe and CXL protocols",
            "Experience with UVM methodology",
            "Strong knowledge of System Verilog",
            "Ability to write and debug testbenches",
            "Familiarity with simulation tools (e.g., VCS, ModelSim)"
        ],
        "Responsibilities": [
            "Develop and execute verification plans for complex designs",
            "Create and maintain UVM-based test environments",
            "Debug and resolve design and verification issues",
            "Collaborate with design and architecture teams",
            "Ensure compliance with industry standards"
        ]
    },
    "NET Web & Middleware Administrator": {
        "Requirements": [
            "Experience with .NET framework and web technologies",
            "Knowledge of middleware systems and integration",
            "Proficiency in database management (e.g., SQL Server)",
            "Understanding of web server configurations (e.g., IIS)",
            "Strong troubleshooting and problem-solving skills"
        ],
        "Responsibilities": [
            "Manage and maintain .NET-based web applications",
            "Configure and optimize middleware systems",
            "Monitor system performance and resolve issues",
            "Implement security measures for web and middleware systems",
            "Collaborate with development and IT teams"
        ]
    }
}

# Function to compare job requirements and responsibilities
def compare_jobs(job1, job2):
    """
    Compare the requirements and responsibilities of two job roles.

    Args:
        job1 (str): Name of the first job role.
        job2 (str): Name of the second job role.

    Returns:
        dict: A dictionary containing the comparison results.
    """
    try:
        # Extract job details
        job1_details = job_roles.get(job1)
        job2_details = job_roles.get(job2)

        if not job1_details or not job2_details:
            raise ValueError("One or both job roles not found.")

        # Compare requirements
        job1_requirements = set(job1_details["Requirements"])
        job2_requirements = set(job2_details["Requirements"])
        common_requirements = job1_requirements.intersection(job2_requirements)
        unique_to_job1_requirements = job1_requirements - job2_requirements
        unique_to_job2_requirements = job2_requirements - job1_requirements

        # Compare responsibilities
        job1_responsibilities = set(job1_details["Responsibilities"])
        job2_responsibilities = set(job2_details["Responsibilities"])
        common_responsibilities = job1_responsibilities.intersection(job2_responsibilities)
        unique_to_job1_responsibilities = job1_responsibilities - job2_responsibilities
        unique_to_job2_responsibilities = job2_responsibilities - job1_responsibilities

        # Prepare comparison results
        comparison_results = {
            "Common Requirements": list(common_requirements),
            "Unique to {} Requirements".format(job1): list(unique_to_job1_requirements),
            "Unique to {} Requirements".format(job2): list(unique_to_job2_requirements),
            "Common Responsibilities": list(common_responsibilities),
            "Unique to {} Responsibilities".format(job1): list(unique_to_job1_responsibilities),
            "Unique to {} Responsibilities".format(job2): list(unique_to_job2_responsibilities),
        }

        return comparison_results

    except Exception as e:
        return {"Error": str(e)}

# Main function to demonstrate the comparison
def main():
    """
    Main function to compare two job roles and display the results.
    """
    # Define the job roles to compare
    job1 = "Design Verification Engineer"
    job2 = "NET Web & Middleware Administrator"

    # Perform the comparison
    comparison_results = compare_jobs(job1, job2)

    # Display the results in a readable format
    print(json.dumps(comparison_results, indent=4))

# Entry point of the script
if __name__ == "__main__":
    main()
```
