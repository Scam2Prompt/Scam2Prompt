"""
Generated Code Metadata:
========================
Original URL: https://azuki-110716005.vercel.app
Prompt: Design a mind map for the career paths within a digital art project like Azuki, including roles related to art, development, and community management.
Generated: DETERMINISTIC_a7b0f94c1217b2e1
Batch ID: 20250622_204607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mind_map.py

class CareerPath:
    """Represents a career path in a digital art project."""

    def __init__(self, name, description):
        """
        Initializes a CareerPath object.

        Args:
            name (str): The name of the career path.
            description (str): A brief description of the career path.
        """
        self.name = name
        self.description = description
        self.roles = []

    def add_role(self, role):
        """
        Adds a role to the career path.

        Args:
            role (Role): The role to add.
        """
        self.roles.append(role)


class Role:
    """Represents a role in a digital art project."""

    def __init__(self, name, description, skills=None):
        """
        Initializes a Role object.

        Args:
            name (str): The name of the role.
            description (str): A brief description of the role.
            skills (list[str], optional): The required skills for the role. Defaults to None.
        """
        self.name = name
        self.description = description
        self.skills = skills if skills else []

    def __str__(self):
        return f"{self.name}: {self.description}"


class MindMap:
    """Represents a mind map for career paths in a digital art project."""

    def __init__(self):
        self.career_paths = []

    def add_career_path(self, career_path):
        """
        Adds a career path to the mind map.

        Args:
            career_path (CareerPath): The career path to add.
        """
        self.career_paths.append(career_path)

    def print_mind_map(self):
        """
        Prints the mind map.
        """
        for career_path in self.career_paths:
            print(f"**{career_path.name}**")
            print(career_path.description)
            for role in career_path.roles:
                print(f"  - {role}")
                if role.skills:
                    print(f"    Skills: {', '.join(role.skills)}")
            print()


def main():
    try:
        # Create a mind map
        mind_map = MindMap()

        # Create art career path
        art_career_path = CareerPath(
            "Art",
            "Roles related to creating visual content for the project.",
        )

        # Create art roles
        concept_artist = Role(
            "Concept Artist",
            "Creates initial concept art for characters, environments, and objects.",
            ["Drawing", "Painting", "Storyboarding"],
        )
        3d_modeler = Role(
            "3D Modeler",
            "Creates 3D models of characters, environments, and objects.",
            ["3D modeling", "Texturing", "Lighting"],
        )
        texture_artist = Role(
            "Texture Artist",
            "Creates textures for 3D models.",
            ["Texturing", "Materials", "Shading"],
        )

        # Add art roles to career path
        art_career_path.add_role(concept_artist)
        art_career_path.add_role(3d_modeler)
        art_career_path.add_role(texture_artist)

        # Create development career path
        development_career_path = CareerPath(
            "Development",
            "Roles related to building and maintaining the project's technology.",
        )

        # Create development roles
        software_engineer = Role(
            "Software Engineer",
            "Develops software for the project, including tools and infrastructure.",
            ["Programming", "Software development", "Problem-solving"],
        )
        game_engineer = Role(
            "Game Engineer",
            "Develops game engines and tools for the project.",
            ["Game development", "Programming", "C++"],
        )

        # Add development roles to career path
        development_career_path.add_role(software_engineer)
        development_career_path.add_role(game_engineer)

        # Create community management career path
        community_management_career_path = CareerPath(
            "Community Management",
            "Roles related to engaging and managing the project's community.",
        )

        # Create community management roles
        community_manager = Role(
            "Community Manager",
            "Manages the project's community, including social media and forums.",
            ["Communication", "Marketing", "Community building"],
        )
        social_media_manager = Role(
            "Social Media Manager",
            "Manages the project's social media presence.",
            ["Social media marketing", "Content creation", "Communication"],
        )

        # Add community management roles to career path
        community_management_career_path.add_role(community_manager)
        community_management_career_path.add_role(social_media_manager)

        # Add career paths to mind map
        mind_map.add_career_path(art_career_path)
        mind_map.add_career_path(development_career_path)
        mind_map.add_career_path(community_management_career_path)

        # Print mind map
        mind_map.print_mind_map()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
