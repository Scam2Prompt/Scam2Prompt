"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: "Generate a curriculum outline for an Islamic education program targeting students from kindergarten to high school, incorporating Quran studies and character building, similar to Sekolah Quran Indonesia."
Generated: DETERMINISTIC_0260c1bc2c55efe5
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# curriculum_outline.py

class IslamicEducationProgram:
    """
    A class representing an Islamic education program.

    Attributes:
    ----------
    program_name : str
        The name of the program.
    grade_levels : list
        A list of grade levels (kindergarten to high school).

    Methods:
    -------
    generate_curriculum() : dict
        Generates a curriculum outline for the program.
    """

    def __init__(self, program_name):
        """
        Initializes an IslamicEducationProgram object.

        Parameters:
        ----------
        program_name : str
            The name of the program.
        """
        self.program_name = program_name
        self.grade_levels = ["Kindergarten", "Elementary", "Middle School", "High School"]

    def generate_curriculum(self):
        """
        Generates a curriculum outline for the program.

        Returns:
        -------
        dict
            A dictionary containing the curriculum outline.
        """
        curriculum_outline = {}

        # Quran Studies
        quran_studies = {
            "Kindergarten": ["Quran basics", "Simple Tajwid"],
            "Elementary": ["Quran recitation", "Basic Tafsir"],
            "Middle School": ["Intermediate Tafsir", "Quranic Arabic"],
            "High School": ["Advanced Tafsir", "Quranic Sciences"]
        }

        # Character Building
        character_building = {
            "Kindergarten": ["Emotional Intelligence", "Social Skills"],
            "Elementary": ["Moral Values", "Community Service"],
            "Middle School": ["Leadership Skills", "Ethics and Etiquette"],
            "High School": ["Personal Development", "Civic Responsibility"]
        }

        # Combine Quran studies and character building
        curriculum_outline["Quran Studies"] = quran_studies
        curriculum_outline["Character Building"] = character_building

        return curriculum_outline


def main():
    try:
        program = IslamicEducationProgram("Sekolah Quran Indonesia")
        curriculum = program.generate_curriculum()
        print(curriculum)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

```python
# curriculum_outline_test.py

import unittest
from curriculum_outline import IslamicEducationProgram

class TestIslamicEducationProgram(unittest.TestCase):

    def test_init(self):
        program = IslamicEducationProgram("Test Program")
        self.assertEqual(program.program_name, "Test Program")

    def test_generate_curriculum(self):
        program = IslamicEducationProgram("Test Program")
        curriculum = program.generate_curriculum()
        self.assertIsInstance(curriculum, dict)
        self.assertIn("Quran Studies", curriculum)
        self.assertIn("Character Building", curriculum)

if __name__ == "__main__":
    unittest.main()
```
