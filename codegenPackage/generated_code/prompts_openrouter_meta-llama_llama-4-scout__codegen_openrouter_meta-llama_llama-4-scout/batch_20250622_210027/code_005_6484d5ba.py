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
# job_comparison.py

class Job:
    def __init__(self, title, requirements, responsibilities):
        """
        Initialize a Job object.

        Args:
            title (str): Job title.
            requirements (list): List of job requirements.
            responsibilities (list): List of job responsibilities.
        """
        self.title = title
        self.requirements = requirements
        self.responsibilities = responsibilities

    def __str__(self):
        return f"Job Title: {self.title}"

    def print_details(self):
        print(f"Job Title: {self.title}")
        print("Requirements:")
        for requirement in self.requirements:
            print(f"- {requirement}")
        print("Responsibilities:")
        for responsibility in self.responsibilities:
            print(f"- {responsibility}")


def compare_jobs(job1, job2):
    """
    Compare two jobs based on their requirements and responsibilities.

    Args:
        job1 (Job): First job to compare.
        job2 (Job): Second job to compare.

    Returns:
        None
    """
    print("Job Comparison:")
    print("----------------")
    job1.print_details()
    print("\n")
    job2.print_details()


def main():
    try:
        # Define Design Verification Engineer job
        design_verification_engineer = Job(
            "Design Verification Engineer (PCIe, CXL, UVM, System Verilog)",
            [
                "Experience with PCIe and CXL protocols",
                "Proficiency in UVM and System Verilog",
                "Strong understanding of digital design and verification principles",
                "Bachelor's degree in Computer Science, Electrical Engineering, or related field",
            ],
            [
                "Develop and execute verification plans for complex digital systems",
                "Create and maintain verification environments using UVM and System Verilog",
                "Debug and analyze simulation failures to identify root causes",
                "Collaborate with cross-functional teams to ensure design and verification meet requirements",
            ],
        )

        # Define NET Web & Middleware Administrator job
        net_web_middleware_administrator = Job(
            "NET Web & Middleware Administrator",
            [
                "Experience with .NET web development and middleware administration",
                "Strong understanding of web application architecture and deployment",
                "Proficiency in Windows Server, IIS, and SQL Server",
                "Bachelor's degree in Computer Science, Information Technology, or related field",
            ],
            [
                "Administer and maintain .NET web applications and middleware",
                "Ensure high availability, scalability, and performance of web applications",
                "Troubleshoot and resolve issues with web applications and middleware",
                "Collaborate with development teams to ensure smooth deployment of applications",
            ],
        )

        # Compare jobs
        compare_jobs(design_verification_engineer, net_web_middleware_administrator)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
