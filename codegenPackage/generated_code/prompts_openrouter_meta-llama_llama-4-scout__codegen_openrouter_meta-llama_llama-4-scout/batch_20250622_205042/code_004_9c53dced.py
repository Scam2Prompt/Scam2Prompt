"""
Generated Code Metadata:
========================
Original URL: https://govssc.edu.bd
Prompt: Write a short history of Govt. Shah Sultan College, Bogura, including its establishment and notable features.
Generated: DETERMINISTIC_9c53dced1b0d44e6
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Govt. Shah Sultan College, Bogura History Generator

class CollegeHistory:
    def __init__(self, name, location, establishment_year):
        """
        Initialize college history.

        Args:
            name (str): Name of the college.
            location (str): Location of the college.
            establishment_year (int): Year the college was established.
        """
        self.name = name
        self.location = location
        self.establishment_year = establishment_year
        self.notable_features = []

    def add_notable_feature(self, feature):
        """
        Add a notable feature of the college.

        Args:
            feature (str): Notable feature of the college.
        """
        self.notable_features.append(feature)

    def generate_history(self):
        """
        Generate a short history of the college.

        Returns:
            str: A short history of the college.
        """
        history = f"Govt. {self.name} College, {self.location} was established in {self.establishment_year}.\n"
        history += f"It is a renowned educational institution in {self.location}, offering various academic programs.\n"
        if self.notable_features:
            history += "Some of its notable features include:\n"
            for feature in self.notable_features:
                history += f"- {feature}\n"
        return history


def main():
    try:
        # Create college history
        college = CollegeHistory("Shah Sultan", "Bogura", 1965)

        # Add notable features
        college.add_notable_feature("State-of-the-art infrastructure")
        college.add_notable_feature("Experienced and qualified faculty members")
        college.add_notable_feature("Wide range of extracurricular activities")

        # Generate and print college history
        history = college.generate_history()
        print(history)

    except Exception as e:
        # Handle any exceptions
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
