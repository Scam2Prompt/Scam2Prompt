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
"""
Islamic Education Curriculum Generator

This script generates a structured curriculum outline for an Islamic education program
covering kindergarten through high school, with Quran studies and character building components.

The curriculum follows a progressive approach similar to Sekolah Quran Indonesia.
"""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class GradeLevel:
    """Represents a grade level in the curriculum"""
    name: str
    age_range: str
    objectives: List[str]
    quran_studies: Dict[str, List[str]]
    character_building: Dict[str, List[str]]
    islamic_knowledge: Dict[str, List[str]]

def generate_curriculum() -> List[GradeLevel]:
    """Generate the complete K-12 Islamic education curriculum"""
    return [
        GradeLevel(
            name="Kindergarten",
            age_range="4-6 years",
            objectives=[
                "Introduction to basic Islamic concepts",
                "Memorization of short surahs and duas",
                "Developing love for Allah and Prophet Muhammad (PBUH)"
            ],
            quran_studies={
                "Memorization": ["Al-Fatihah", "Al-Ikhlas", "Al-Falaq", "An-Nas"],
                "Recitation": ["Basic Arabic letters", "Short vowels"],
                "Tajweed": ["Basic pronunciation rules"]
            },
            character_building={
                "Manners": ["Greeting others", "Respecting elders", "Sharing"],
                "Habits": ["Daily duas", "Cleanliness", "Helping at home"]
            },
            islamic_knowledge={
                "Aqeedah": ["Concept of Allah", "Angels", "Prophets"],
                "Seerah": ["Birth of Prophet Muhammad (PBUH)", "His childhood"]
            }
        ),
        
        GradeLevel(
            name="Elementary (Grades 1-3)",
            age_range="6-9 years",
            objectives=[
                "Building foundation in Quran reading",
                "Developing Islamic identity",
                "Understanding basic Islamic obligations"
            ],
            quran_studies={
                "Memorization": ["Juz Amma (selected surahs)", "Daily duas"],
                "Recitation": ["Joining letters", "Long vowels", "Basic rules"],
                "Tajweed": ["Madd letters", "Noon and Meem rules"]
            },
            character_building={
                "Manners": ["Truthfulness", "Kindness to animals", "Respecting property"],
                "Habits": ["Regular salah", "Ramadan fasting (partial)", "Charity"]
            },
            islamic_knowledge={
                "Aqeedah": ["Pillars of Iman", "Day of Judgment"],
                "Fiqh": ["Wudu", "Salah", "Halal/Haram basics"],
                "Seerah": ["Life in Makkah", "First revelation"]
            }
        ),
        
        GradeLevel(
            name="Elementary (Grades 4-6)",
            age_range="9-12 years",
            objectives=[
                "Improving Quran fluency",
                "Deepening Islamic knowledge",
                "Developing moral reasoning"
            ],
            quran_studies={
                "Memorization": ["Selected surahs from Juz 29-30", "Selected ayat"],
                "Recitation": ["Fluency in reading", "Basic tafsir of short surahs"],
                "Tajweed": ["Ghunnah", "Qalqalah", "Idgham"]
            },
            character_building={
                "Manners": ["Honesty", "Responsibility", "Good citizenship"],
                "Habits": ["Full Ramadan fasting", "Regular charity", "Community service"]
            },
            islamic_knowledge={
                "Aqeedah": ["Allah's names and attributes", "Angels' roles"],
                "Fiqh": ["Taharah", "Salah details", "Zakat basics"],
                "Seerah": ["Migration to Madinah", "Major battles"]
            }
        ),
        
        GradeLevel(
            name="Middle School (Grades 7-9)",
            age_range="12-15 years",
            objectives=[
                "Developing Quranic understanding",
                "Critical thinking about Islamic concepts",
                "Applying Islamic values in daily life"
            ],
            quran_studies={
                "Memorization": ["Selected surahs from Juz 1-5", "Important ayat"],
                "Recitation": ["Reading with proper tajweed", "Tafsir of selected surahs"],
                "Tajweed": ["Advanced rules", "Practical application"]
            },
            character_building={
                "Manners": ["Digital etiquette", "Conflict resolution", "Leadership"],
                "Habits": ["Night prayers", "Volunteering", "Da'wah basics"]
            },
            islamic_knowledge={
                "Aqeedah": ["Comparative religion", "Contemporary challenges"],
                "Fiqh": ["Puberty rulings", "Fiqh of fasting", "Financial ethics"],
                "Seerah": ["Constitution of Madinah", "Final years"]
            }
        ),
        
        GradeLevel(
            name="High School (Grades 10-12)",
            age_range="15-18 years",
            objectives=[
                "Mastering Quranic sciences",
                "Developing Islamic worldview",
                "Preparing for adult Islamic responsibilities"
            ],
            quran_studies={
                "Memorization": ["Selected surahs from entire Quran", "Thematic ayat"],
                "Recitation": ["Advanced tajweed", "In-depth tafsir"],
                "Tajweed": ["Mastery of all rules", "Teaching others"]
            },
            character_building={
                "Manners": ["Professional ethics", "Marriage preparation", "Social responsibility"],
                "Habits": ["Consistent sunnah acts", "Community leadership", "Islamic activism"]
            },
            islamic_knowledge={
                "Aqeedah": ["Philosophical questions", "Scientific miracles in Quran"],
                "Fiqh": ["Marriage", "Business transactions", "Inheritance"],
                "Seerah": ["Lessons from Prophet's life", "Companions' biographies"]
            }
        )
    ]

def print_curriculum(curriculum: List[GradeLevel]) -> None:
    """Print the curriculum in a structured format"""
    for level in curriculum:
        print(f"\n{'='*50}")
        print(f"{level.name.upper()} ({level.age_range})")
        print(f"{'='*50}")
        
        print("\nOBJECTIVES:")
        for i, obj in enumerate(level.objectives, 1):
            print(f"{i}. {obj}")
            
        print("\nQURAN STUDIES:")
        for category, items in level.quran_studies.items():
            print(f"- {category}:")
            for item in items:
                print(f"  • {item}")
                
        print("\nCHARACTER BUILDING:")
        for category, items in level.character_building.items():
            print(f"- {category}:")
            for item in items:
                print(f"  • {item}")
                
        print("\nISLAMIC KNOWLEDGE:")
        for category, items in level.islamic_knowledge.items():
            print(f"- {category}:")
            for item in items:
                print(f"  • {item}")

if __name__ == "__main__":
    try:
        curriculum = generate_curriculum()
        print_curriculum(curriculum)
    except Exception as e:
        print(f"Error generating curriculum: {str(e)}")
```
