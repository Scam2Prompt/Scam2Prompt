"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.com
Prompt: Generate a list of pros and cons of part-time jobs with variable hourly wages, focusing on the impact of work environment and flexibility on job satisfaction.
Generated: DETERMINISTIC_20673a5494a5758d
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# part_time_jobs.py

class PartTimeJob:
    def __init__(self, name, hourly_wage, work_environment, flexibility):
        """
        Initialize a PartTimeJob object.

        Args:
            name (str): Job name
            hourly_wage (float): Hourly wage
            work_environment (str): Work environment (e.g., office, remote)
            flexibility (str): Flexibility level (e.g., low, medium, high)
        """
        self.name = name
        self.hourly_wage = hourly_wage
        self.work_environment = work_environment
        self.flexibility = flexibility

    def __str__(self):
        return f"{self.name}: ${self.hourly_wage}/hour, {self.work_environment}, {self.flexibility} flexibility"


class JobSatisfactionSurvey:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        """
        Add a part-time job to the survey.

        Args:
            job (PartTimeJob): Part-time job object
        """
        self.jobs.append(job)

    def generate_pros_cons(self):
        """
        Generate a list of pros and cons of part-time jobs with variable hourly wages.

        Returns:
            dict: Dictionary with pros and cons
        """
        pros = []
        cons = []

        for job in self.jobs:
            if job.flexibility == "high":
                pros.append(f"{job.name} offers flexible scheduling.")
            else:
                cons.append(f"{job.name} has limited scheduling flexibility.")

            if job.work_environment == "remote":
                pros.append(f"{job.name} offers remote work options.")
            else:
                cons.append(f"{job.name} requires working in an office.")

            if job.hourly_wage > 20:
                pros.append(f"{job.name} offers a high hourly wage (${job.hourly_wage}/hour).")
            else:
                cons.append(f"{job.name} has a relatively low hourly wage (${job.hourly_wage}/hour).")

        return {"pros": pros, "cons": cons}


def main():
    try:
        survey = JobSatisfactionSurvey()

        job1 = PartTimeJob("Freelance Writing", 30, "remote", "high")
        job2 = PartTimeJob("Part-time Retail", 15, "office", "low")
        job3 = PartTimeJob("Online Tutoring", 25, "remote", "medium")

        survey.add_job(job1)
        survey.add_job(job2)
        survey.add_job(job3)

        pros_cons = survey.generate_pros_cons()

        print("Pros:")
        for pro in pros_cons["pros"]:
            print(f"* {pro}")

        print("\nCons:")
        for con in pros_cons["cons"]:
            print(f"* {con}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
