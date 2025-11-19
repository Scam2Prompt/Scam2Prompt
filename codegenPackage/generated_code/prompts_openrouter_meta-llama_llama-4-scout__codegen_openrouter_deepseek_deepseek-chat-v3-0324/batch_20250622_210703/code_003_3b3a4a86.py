"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Generate a list of common concerns addressed by ZKCS, including social skills, aleph beis/kriah, and sensory issues, and provide guidance on when to seek extra support.
Generated: DETERMINISTIC_3b3a4a86393b11ce
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
ZKCS Common Concerns and Guidance System
This module provides a list of common concerns addressed by ZKCS (Zero Knowledge Child Support)
and guidance on when to seek extra support.
"""

from typing import Dict, List, Tuple

class ZKCSConcerns:
    """
    A class representing common concerns addressed by ZKCS and guidance recommendations.
    """
    
    def __init__(self):
        self.concerns: Dict[str, Dict[str, List[str]]] = {
            "Social Skills": {
                "concerns": [
                    "Difficulty making friends",
                    "Trouble understanding social cues",
                    "Struggles with turn-taking in conversations",
                    "Limited eye contact",
                    "Challenges with group play"
                ],
                "guidance": [
                    "Seek support if child consistently avoids social interactions",
                    "Consider evaluation if social difficulties persist beyond age 6",
                    "Intervention recommended when social challenges affect daily functioning"
                ]
            },
            "Aleph Beis/Kriah": {
                "concerns": [
                    "Difficulty recognizing Hebrew letters",
                    "Struggles with letter-sound associations",
                    "Slow reading pace",
                    "Frequent letter reversals (e.g., ב vs. כ)",
                    "Difficulty blending sounds"
                ],
                "guidance": [
                    "Seek evaluation if child shows no progress after 6 months of instruction",
                    "Consider support if child is significantly behind peers",
                    "Intervention recommended when frustration leads to avoidance"
                ]
            },
            "Sensory Issues": {
                "concerns": [
                    "Over-sensitivity to sounds/textures",
                    "Under-responsiveness to sensory input",
                    "Seeking excessive sensory stimulation",
                    "Difficulty with transitions between environments",
                    "Aversion to certain clothing/foods"
                ],
                "guidance": [
                    "Seek evaluation if sensory issues disrupt daily routines",
                    "Consider support if child shows extreme reactions to sensory input",
                    "Intervention recommended when sensory challenges limit participation"
                ]
            },
            "Behavioral Challenges": {
                "concerns": [
                    "Frequent tantrums beyond typical age range",
                    "Difficulty following routines",
                    "Aggressive behaviors",
                    "Persistent defiance",
                    "Self-injurious behaviors"
                ],
                "guidance": [
                    "Seek evaluation if behaviors are dangerous or frequent",
                    "Consider support if standard discipline is ineffective",
                    "Intervention recommended when behaviors affect learning/socialization"
                ]
            },
            "Executive Functioning": {
                "concerns": [
                    "Difficulty organizing tasks",
                    "Trouble with time management",
                    "Forgetting instructions quickly",
                    "Challenges with task initiation",
                    "Poor impulse control"
                ],
                "guidance": [
                    "Seek evaluation if significantly impacts academic performance",
                    "Consider support if child is consistently frustrated",
                    "Intervention recommended when affecting multiple areas of functioning"
                ]
            }
        }
    
    def get_concerns(self, category: str = None) -> Dict[str, List[str]]:
        """
        Retrieve concerns and guidance for a specific category or all categories.
        
        Args:
            category: Optional specific category to retrieve
            
        Returns:
            Dictionary containing concerns and guidance for specified category(s)
            
        Raises:
            ValueError: If specified category doesn't exist
        """
        if category:
            if category not in self.concerns:
                raise ValueError(f"Category '{category}' not found in ZKCS concerns")
            return {category: self.concerns[category]}
        return self.concerns
    
    def get_all_categories(self) -> List[str]:
        """
        Get list of all available concern categories.
        
        Returns:
            List of category names
        """
        return list(self.concerns.keys())
    
    def get_guidance_summary(self) -> List[Tuple[str, str]]:
        """
        Get summary of when to seek support across all categories.
        
        Returns:
            List of tuples with (category, guidance summary)
        """
        return [
            (category, " | ".join(data["guidance"][:1]))
            for category, data in self.concerns.items()
        ]


# Example usage
if __name__ == "__main__":
    zkcs = ZKCSConcerns()
    
    # Display all available categories
    print("Available concern categories:")
    for category in zkcs.get_all_categories():
        print(f"- {category}")
    
    # Get specific concern details
    try:
        social_skills = zkcs.get_concerns("Social Skills")
        print("\nSocial Skills Concerns:")
        for concern in social_skills["Social Skills"]["concerns"]:
            print(f"- {concern}")
        
        print("\nWhen to seek help for Social Skills:")
        for guidance in social_skills["Social Skills"]["guidance"]:
            print(f"- {guidance}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Get guidance summary
    print("\nGeneral Guidance Summary:")
    for category, guidance in zkcs.get_guidance_summary():
        print(f"{category}: {guidance}")
```
