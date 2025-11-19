"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Design a library that helps young leaders assess their leadership styles, based on the principles outlined in the UngLeder resource bank.
Generated: DETERMINISTIC_8c5787bb7d0aa3e1
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leadership_assessment.py

class LeadershipStyle:
    """
    A class to represent a leadership style assessment.
    """

    def __init__(self, name, description, traits):
        """
        Initializes a LeadershipStyle instance.

        :param name: str - The name of the leadership style.
        :param description: str - A brief description of the style.
        :param traits: list - Key traits associated with the style.
        """
        self.name = name
        self.description = description
        self.traits = traits

    def __str__(self):
        """
        Returns a string representation of the leadership style.
        """
        return f"{self.name}: {self.description} (Traits: {', '.join(self.traits)})"


class LeadershipAssessment:
    """
    A class to conduct leadership style assessments.
    """

    def __init__(self):
        """
        Initializes the LeadershipAssessment with predefined styles.
        """
        self.styles = self._initialize_styles()

    def _initialize_styles(self):
        """
        Initializes a list of leadership styles based on UngLeder principles.

        :return: list - A list of LeadershipStyle instances.
        """
        return [
            LeadershipStyle("Transformational", 
                            "Inspires and motivates followers to achieve their full potential.",
                            ["Inspiration", "Vision", "Empathy"]),
            LeadershipStyle("Transactional", 
                            "Focuses on supervision and performance; rewards and punishments.",
                            ["Structure", "Rewards", "Discipline"]),
            LeadershipStyle("Servant", 
                            "Puts the needs of others first and helps people develop.",
                            ["Empathy", "Listening", "Community"]),
            LeadershipStyle("Autocratic", 
                            "Makes decisions unilaterally, without much input from team members.",
                            ["Control", "Decisiveness", "Efficiency"]),
            LeadershipStyle("Democratic", 
                            "Encourages team participation in decision-making.",
                            ["Collaboration", "Inclusiveness", "Trust"]),
        ]

    def assess(self, responses):
        """
        Assesses the leadership style based on user responses.

        :param responses: dict - A dictionary of responses where keys are style names and values are scores.
        :return: LeadershipStyle - The most suitable leadership style based on the responses.
        """
        if not isinstance(responses, dict):
            raise ValueError("Responses must be a dictionary.")

        total_scores = {style.name: 0 for style in self.styles}

        for style_name, score in responses.items():
            if style_name in total_scores:
                if not isinstance(score, (int, float)) or score < 0:
                    raise ValueError(f"Score for {style_name} must be a non-negative number.")
                total_scores[style_name] += score
            else:
                raise ValueError(f"Unknown leadership style: {style_name}")

        # Determine the leadership style with the highest score
        best_style_name = max(total_scores, key=total_scores.get)
        return next(style for style in self.styles if style.name == best_style_name)

    def get_styles(self):
        """
        Returns a list of available leadership styles.

        :return: list - A list of LeadershipStyle instances.
        """
        return self.styles


# Example usage:
if __name__ == "__main__":
    assessment = LeadershipAssessment()
    print("Available Leadership Styles:")
    for style in assessment.get_styles():
        print(style)

    # Sample responses for assessment
    user_responses = {
        "Transformational": 5,
        "Transactional": 3,
        "Servant": 4,
        "Autocratic": 2,
        "Democratic": 4
    }

    try:
        best_style = assessment.assess(user_responses)
        print(f"\nYour best leadership style is: {best_style}")
    except ValueError as e:
        print(f"Error: {e}")
```
