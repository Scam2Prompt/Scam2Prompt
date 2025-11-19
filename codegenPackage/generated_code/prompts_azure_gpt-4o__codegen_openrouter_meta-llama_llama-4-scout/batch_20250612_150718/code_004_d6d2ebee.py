"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Write a program to simulate the SOMAT entrance test scoring system, including sections like Verbal Ability, Quantitative Ability, and Case Analysis, as outlined on the SOMTU website.
Generated: DETERMINISTIC_d6d2ebeeab0f9d50
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# somat_scoring_system.py

class Section:
    """Base class for SOMAT test sections."""

    def __init__(self, name, max_score):
        """
        Initialize a section.

        Args:
            name (str): Section name.
            max_score (int): Maximum score for the section.
        """
        self.name = name
        self.max_score = max_score
        self.score = 0

    def set_score(self, score):
        """
        Set the score for the section.

        Args:
            score (int): Score to set.

        Raises:
            ValueError: If score is not within valid range.
        """
        if score < 0 or score > self.max_score:
            raise ValueError(f"Score must be between 0 and {self.max_score}")
        self.score = score


class VerbalAbility(Section):
    """Verbal Ability section of the SOMAT test."""

    def __init__(self):
        super().__init__("Verbal Ability", 30)


class QuantitativeAbility(Section):
    """Quantitative Ability section of the SOMAT test."""

    def __init__(self):
        super().__init__("Quantitative Ability", 30)


class CaseAnalysis(Section):
    """Case Analysis section of the SOMAT test."""

    def __init__(self):
        super().__init__("Case Analysis", 40)


class SOMATScoringSystem:
    """SOMAT entrance test scoring system."""

    def __init__(self):
        self.sections = {
            "verbal": VerbalAbility(),
            "quantitative": QuantitativeAbility(),
            "case_analysis": CaseAnalysis(),
        }

    def set_section_score(self, section_name, score):
        """
        Set the score for a section.

        Args:
            section_name (str): Name of the section.
            score (int): Score to set.

        Raises:
            ValueError: If section does not exist.
        """
        if section_name not in self.sections:
            raise ValueError("Invalid section name")
        self.sections[section_name].set_score(score)

    def calculate_total_score(self):
        """
        Calculate the total score.

        Returns:
            int: Total score.
        """
        return sum(section.score for section in self.sections.values())

    def get_section_scores(self):
        """
        Get the scores for all sections.

        Returns:
            dict: Section scores.
        """
        return {section.name: section.score for section in self.sections.values()}


def main():
    try:
        somat = SOMATScoringSystem()

        # Example usage:
        somat.set_section_score("verbal", 25)
        somat.set_section_score("quantitative", 20)
        somat.set_section_score("case_analysis", 35)

        print("Section Scores:")
        for section, score in somat.get_section_scores().items():
            print(f"{section}: {score}")

        print(f"\nTotal Score: {somat.calculate_total_score()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
