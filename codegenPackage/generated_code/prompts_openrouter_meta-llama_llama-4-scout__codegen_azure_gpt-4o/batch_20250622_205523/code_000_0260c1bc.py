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
import json

def generate_curriculum():
    """
    Generates a curriculum outline for an Islamic education program targeting students
    from kindergarten to high school. The curriculum incorporates Quran studies and
    character building.
    """
    try:
        # Define the curriculum structure
        curriculum = {
            "Kindergarten": {
                "Quran Studies": [
                    "Introduction to Arabic letters (Hijaiyah)",
                    "Basic Quranic recitation (Iqra method)",
                    "Memorization of short Surahs (e.g., Al-Fatihah, Al-Ikhlas)",
                    "Learning basic Islamic prayers (Du'as)"
                ],
                "Character Building": [
                    "Learning good manners (Adab)",
                    "Respect for parents and elders",
                    "Sharing and kindness activities",
                    "Introduction to Islamic values (e.g., honesty, gratitude)"
                ]
            },
            "Elementary School": {
                "Quran Studies": [
                    "Advanced Quranic recitation (Tajweed basics)",
                    "Memorization of Juz Amma (30th Juz)",
                    "Understanding Quranic stories (e.g., Prophets)",
                    "Daily Quran reading habits"
                ],
                "Character Building": [
                    "Developing discipline through daily prayers",
                    "Teamwork and collaboration activities",
                    "Understanding the importance of charity (Zakat)",
                    "Learning patience and perseverance"
                ]
            },
            "Middle School": {
                "Quran Studies": [
                    "Mastering Tajweed rules",
                    "Memorization of selected Surahs from Juz 29 and Juz 28",
                    "Introduction to Quranic Tafsir (interpretation)",
                    "Understanding Quranic themes (e.g., justice, mercy)"
                ],
                "Character Building": [
                    "Leadership skills development",
                    "Conflict resolution and problem-solving",
                    "Strengthening Islamic identity and values",
                    "Community service and volunteerism"
                ]
            },
            "High School": {
                "Quran Studies": [
                    "Advanced Quranic Tafsir studies",
                    "Memorization of selected Surahs from Juz 1 and Juz 2",
                    "Understanding Quranic ethics and laws",
                    "Application of Quranic principles in daily life"
                ],
                "Character Building": [
                    "Critical thinking and decision-making skills",
                    "Preparing for adulthood with Islamic values",
                    "Engaging in interfaith dialogue respectfully",
                    "Contributing positively to society"
                ]
            }
        }

        # Convert the curriculum to JSON format for easy readability
        curriculum_json = json.dumps(curriculum, indent=4)

        # Return the curriculum JSON
        return curriculum_json

    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while generating the curriculum: {str(e)}"


# Main execution
if __name__ == "__main__":
    # Generate the curriculum and print it
    curriculum_outline = generate_curriculum()
    print(curriculum_outline)
```
