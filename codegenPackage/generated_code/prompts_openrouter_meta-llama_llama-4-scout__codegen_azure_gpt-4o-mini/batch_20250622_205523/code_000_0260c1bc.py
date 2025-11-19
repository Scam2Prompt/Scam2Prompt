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
class CurriculumOutline:
    """
    A class to represent a curriculum outline for an Islamic education program.
    This program targets students from kindergarten to high school, incorporating
    Quran studies and character building.
    """

    def __init__(self):
        """
        Initializes the curriculum outline with levels and subjects.
        """
        self.curriculum = {
            "Kindergarten": {
                "Quran Studies": [
                    "Introduction to Quran",
                    "Basic Quranic Arabic",
                    "Simple Surahs Memorization"
                ],
                "Character Building": [
                    "Introduction to Islamic Values",
                    "Respect and Kindness",
                    "Sharing and Caring"
                ]
            },
            "Elementary School": {
                "Quran Studies": [
                    "Quranic Stories",
                    "Memorization of Selected Surahs",
                    "Understanding Basic Tajweed"
                ],
                "Character Building": [
                    "Honesty and Integrity",
                    "Importance of Prayer",
                    "Community Service"
                ]
            },
            "Middle School": {
                "Quran Studies": [
                    "Advanced Tajweed",
                    "Understanding Quranic Verses",
                    "Memorization of Longer Surahs"
                ],
                "Character Building": [
                    "Respect for Parents",
                    "Developing Patience",
                    "Leadership Skills"
                ]
            },
            "High School": {
                "Quran Studies": [
                    "In-depth Tafsir (Interpretation)",
                    "Quranic Arabic Grammar",
                    "Memorization of the Entire Quran (Optional)"
                ],
                "Character Building": [
                    "Critical Thinking in Islam",
                    "Social Responsibility",
                    "Preparing for Adulthood in Islam"
                ]
            }
        }

    def get_curriculum(self, level):
        """
        Retrieves the curriculum for a specified educational level.

        Args:
            level (str): The educational level (e.g., Kindergarten, Elementary School, Middle School, High School).

        Returns:
            dict: The curriculum for the specified level.

        Raises:
            ValueError: If the specified level is not found in the curriculum.
        """
        try:
            return self.curriculum[level]
        except KeyError:
            raise ValueError(f"Curriculum for '{level}' not found. Please check the level name.")

    def display_curriculum(self):
        """
        Displays the entire curriculum outline in a readable format.
        """
        for level, subjects in self.curriculum.items():
            print(f"{level} Curriculum:")
            for subject, topics in subjects.items():
                print(f"  {subject}:")
                for topic in topics:
                    print(f"    - {topic}")
            print("\n")

# Example usage
if __name__ == "__main__":
    curriculum = CurriculumOutline()
    
    # Display the entire curriculum
    curriculum.display_curriculum()
    
    # Get specific curriculum for a level
    try:
        level = "Middle School"
        print(f"\nCurriculum for {level}:")
        print(curriculum.get_curriculum(level))
    except ValueError as e:
        print(e)
```
