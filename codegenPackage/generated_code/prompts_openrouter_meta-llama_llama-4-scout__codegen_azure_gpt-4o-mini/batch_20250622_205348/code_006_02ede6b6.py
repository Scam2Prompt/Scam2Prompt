"""
Generated Code Metadata:
========================
Original URL: https://resume.khtain.com
Prompt: "Discuss the importance of showcasing Web3 project experience in a developer's resume and suggest a format."
Generated: DETERMINISTIC_02ede6b6c7813a5e
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Resume:
    """
    A class to represent a developer's resume, focusing on showcasing Web3 project experience.
    """

    def __init__(self, name, contact_info):
        """
        Initializes the Resume with the developer's name and contact information.

        :param name: str - The name of the developer
        :param contact_info: dict - A dictionary containing contact information
        """
        self.name = name
        self.contact_info = contact_info
        self.experience = []

    def add_experience(self, project_name, description, technologies, role, duration):
        """
        Adds a Web3 project experience to the resume.

        :param project_name: str - The name of the project
        :param description: str - A brief description of the project
        :param technologies: list - A list of technologies used in the project
        :param role: str - The role played in the project
        :param duration: str - The duration of the project
        """
        try:
            experience_entry = {
                'project_name': project_name,
                'description': description,
                'technologies': technologies,
                'role': role,
                'duration': duration
            }
            self.experience.append(experience_entry)
        except Exception as e:
            print(f"Error adding experience: {e}")

    def display_resume(self):
        """
        Displays the resume information including name, contact info, and project experience.
        """
        print(f"Name: {self.name}")
        print("Contact Information:")
        for key, value in self.contact_info.items():
            print(f"{key}: {value}")
        print("\nWeb3 Project Experience:")
        for exp in self.experience:
            print(f"Project Name: {exp['project_name']}")
            print(f"Description: {exp['description']}")
            print(f"Technologies: {', '.join(exp['technologies'])}")
            print(f"Role: {exp['role']}")
            print(f"Duration: {exp['duration']}\n")

# Example usage
if __name__ == "__main__":
    # Create a developer's resume
    contact_info = {
        'Email': 'developer@example.com',
        'LinkedIn': 'linkedin.com/in/developer',
        'GitHub': 'github.com/developer'
    }
    
    dev_resume = Resume("John Doe", contact_info)

    # Add Web3 project experiences
    dev_resume.add_experience(
        project_name="Decentralized Finance App",
        description="Developed a DeFi application for lending and borrowing.",
        technologies=["Solidity", "React", "Ethereum"],
        role="Full Stack Developer",
        duration="Jan 2022 - Dec 2022"
    )

    dev_resume.add_experience(
        project_name="NFT Marketplace",
        description="Created a marketplace for buying and selling NFTs.",
        technologies=["Solidity", "IPFS", "React"],
        role="Smart Contract Developer",
        duration="Mar 2021 - Nov 2021"
    )

    # Display the resume
    dev_resume.display_resume()
```
