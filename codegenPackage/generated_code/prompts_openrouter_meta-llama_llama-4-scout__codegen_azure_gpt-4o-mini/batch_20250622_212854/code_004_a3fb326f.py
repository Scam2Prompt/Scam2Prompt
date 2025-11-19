"""
Generated Code Metadata:
========================
Original URL: https://johnbarrybaker.com
Prompt: Describe the experience of Attorney John Barry Baker in handling personal injury cases.
Generated: DETERMINISTIC_a3fb326fb3114c21
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Attorney:
    """
    A class to represent an attorney and their experience in handling personal injury cases.
    """

    def __init__(self, name, years_of_experience, cases_handled):
        """
        Initializes the Attorney instance.

        :param name: str - The name of the attorney.
        :param years_of_experience: int - The number of years the attorney has been practicing.
        :param cases_handled: list - A list of personal injury cases handled by the attorney.
        """
        self.name = name
        self.years_of_experience = years_of_experience
        self.cases_handled = cases_handled

    def add_case(self, case):
        """
        Adds a personal injury case to the attorney's list of handled cases.

        :param case: str - The name of the personal injury case to add.
        :raises ValueError: If the case is not a string or is empty.
        """
        if not isinstance(case, str) or not case.strip():
            raise ValueError("Case must be a non-empty string.")
        self.cases_handled.append(case)

    def experience_summary(self):
        """
        Provides a summary of the attorney's experience in handling personal injury cases.

        :return: str - A summary of the attorney's experience.
        """
        summary = (f"Attorney {self.name} has {self.years_of_experience} years of experience "
                   f"handling personal injury cases. They have successfully managed the following cases:\n")
        for case in self.cases_handled:
            summary += f"- {case}\n"
        return summary


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of Attorney
        john_barry_baker = Attorney("John Barry Baker", 15, ["Case A", "Case B", "Case C"])

        # Add a new case
        john_barry_baker.add_case("Case D")

        # Print the experience summary
        print(john_barry_baker.experience_summary())
    except Exception as e:
        print(f"An error occurred: {e}")
```
