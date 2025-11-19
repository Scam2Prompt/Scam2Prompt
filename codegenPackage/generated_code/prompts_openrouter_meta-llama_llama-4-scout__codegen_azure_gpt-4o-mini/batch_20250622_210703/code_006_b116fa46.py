"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: What are the key differences between Occupational Therapy, Behavioural Therapy, and Speech Therapy in the context of Autism treatment, as offered by Jewel Autism Centre?
Generated: DETERMINISTIC_b116fa469310f1e7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AutismTherapy:
    """
    A class to represent different types of therapies offered for Autism treatment.
    """

    def __init__(self, therapy_type, description, target_areas):
        """
        Initializes the therapy with its type, description, and target areas.

        :param therapy_type: str - The type of therapy (e.g., Occupational, Behavioural, Speech)
        :param description: str - A brief description of the therapy
        :param target_areas: list - Key areas that the therapy focuses on
        """
        self.therapy_type = therapy_type
        self.description = description
        self.target_areas = target_areas

    def get_info(self):
        """
        Returns a formatted string with information about the therapy.

        :return: str - Information about the therapy
        """
        return f"{self.therapy_type} Therapy:\nDescription: {self.description}\nTarget Areas: {', '.join(self.target_areas)}\n"


def main():
    """
    Main function to demonstrate the differences between therapies.
    """
    try:
        # Define the therapies offered at Jewel Autism Centre
        occupational_therapy = AutismTherapy(
            therapy_type="Occupational",
            description="Focuses on improving daily living skills and sensory integration.",
            target_areas=["Daily Living Skills", "Fine Motor Skills", "Sensory Processing"]
        )

        behavioural_therapy = AutismTherapy(
            therapy_type="Behavioural",
            description="Uses techniques to modify behavior and improve social skills.",
            target_areas=["Social Skills", "Communication", "Behavior Modification"]
        )

        speech_therapy = AutismTherapy(
            therapy_type="Speech",
            description="Aims to improve communication skills and language development.",
            target_areas=["Verbal Communication", "Non-Verbal Communication", "Language Skills"]
        )

        # Print information about each therapy
        print(occupational_therapy.get_info())
        print(behavioural_therapy.get_info())
        print(speech_therapy.get_info())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
