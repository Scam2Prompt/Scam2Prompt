"""
Generated Code Metadata:
========================
Original URL: https://butterfieldtechnology.com
Prompt: Write a pitch for a London-based ecommerce agency that has a proven track record of success with clients of all sizes, from home office entrepreneurs to global leaders.
Generated: DETERMINISTIC_608cfa765c980753
Batch ID: 20250622_205926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ecommerce_agency_pitch.py

class EcommerceAgency:
    def __init__(self, name, location, description):
        """
        Initialize an EcommerceAgency object.

        Args:
            name (str): The name of the agency.
            location (str): The location of the agency.
            description (str): A brief description of the agency.
        """
        self.name = name
        self.location = location
        self.description = description
        self.success_stories = []

    def add_success_story(self, client_name, client_size):
        """
        Add a success story to the agency's portfolio.

        Args:
            client_name (str): The name of the client.
            client_size (str): The size of the client (e.g. "home office", "global leader").
        """
        self.success_stories.append({"client_name": client_name, "client_size": client_size})

    def generate_pitch(self):
        """
        Generate a pitch for the ecommerce agency.

        Returns:
            str: A pitch for the ecommerce agency.
        """
        pitch = f"Welcome to {self.name}, a leading ecommerce agency based in {self.location}.\n\n"
        pitch += f"{self.description}\n\n"
        pitch += "Our Proven Track Record:\n"
        for i, story in enumerate(self.success_stories, start=1):
            pitch += f"{i}. {story['client_name']} ({story['client_size']})\n"
        pitch += "\n"
        pitch += "Whether you're a home office entrepreneur or a global leader, we've got the expertise to help you succeed in ecommerce."

        return pitch


def main():
    try:
        agency = EcommerceAgency(
            name="London Ecommerce Experts",
            location="London",
            description="A proven ecommerce agency with a track record of success"
        )

        agency.add_success_story("Entrepreneur X", "home office")
        agency.add_success_story("Global Leader Y", "global leader")

        pitch = agency.generate_pitch()
        print(pitch)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
