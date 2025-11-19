"""
Generated Code Metadata:
========================
Original URL: https://rodi.co.id
Prompt: Write a short biography of Rodi, S.Kom, MM, including his educational background and career in politics, specifically highlighting his role as Chairman of Commission 2 in DPRD Kota Bengkulu.
Generated: DETERMINISTIC_d1d0432f5f941082
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Biography:
    def __init__(self, name, title, educational_background, career):
        """
        Initialize a Biography object.

        Args:
            name (str): The person's name.
            title (str): The person's title.
            educational_background (str): The person's educational background.
            career (str): The person's career.
        """
        self.name = name
        self.title = title
        self.educational_background = educational_background
        self.career = career

    def __str__(self):
        return f"{self.name}, {self.title}"

    def print_biography(self):
        """
        Print the person's biography.
        """
        print(f"## Biography of {self.name}, {self.title} ##")
        print(f"### Educational Background ###")
        print(self.educational_background)
        print(f"### Career ###")
        print(self.career)


class Politician(Biography):
    def __init__(self, name, title, educational_background, career, role, institution):
        """
        Initialize a Politician object.

        Args:
            name (str): The politician's name.
            title (str): The politician's title.
            educational_background (str): The politician's educational background.
            career (str): The politician's career.
            role (str): The politician's role.
            institution (str): The institution where the politician serves.
        """
        super().__init__(name, title, educational_background, career)
        self.role = role
        self.institution = institution

    def print_biography(self):
        """
        Print the politician's biography.
        """
        super().print_biography()
        print(f"### Role ###")
        print(f"{self.role} at {self.institution}")


def main():
    try:
        # Create a Politician object for Rodi, S.Kom, MM
        rodi = Politician(
            name="Rodi",
            title="S.Kom, MM",
            educational_background="Bachelor's degree in Computer Science, Master's degree in Management",
            career="Active in politics, serving as a member of DPRD Kota Bengkulu",
            role="Chairman of Commission 2",
            institution="DPRD Kota Bengkulu"
        )

        # Print Rodi's biography
        rodi.print_biography()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
