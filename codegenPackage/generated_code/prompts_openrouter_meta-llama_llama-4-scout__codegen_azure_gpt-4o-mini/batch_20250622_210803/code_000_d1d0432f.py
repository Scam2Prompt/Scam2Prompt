"""
Generated Code Metadata:
========================
Original URL: https://rodi.co.id
Prompt: Write a short biography of Rodi, S.Kom, MM, including his educational background and career in politics, specifically highlighting his role as Chairman of Commission 2 in DPRD Kota Bengkulu.
Generated: DETERMINISTIC_d1d0432f5f941082
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Biography:
    """
    A class to represent a biography of an individual.
    """

    def __init__(self, name, education, career_highlights):
        """
        Initializes the Biography object with name, education, and career highlights.

        :param name: str - Name of the individual
        :param education: str - Educational background
        :param career_highlights: str - Highlights of the individual's career
        """
        self.name = name
        self.education = education
        self.career_highlights = career_highlights

    def display_biography(self):
        """
        Displays the biography of the individual in a formatted manner.
        """
        try:
            print(f"Biography of {self.name}\n")
            print("Educational Background:")
            print(self.education)
            print("\nCareer Highlights:")
            print(self.career_highlights)
        except Exception as e:
            print(f"An error occurred while displaying the biography: {e}")


def main():
    """
    Main function to create and display the biography of Rodi, S.Kom, MM.
    """
    # Define the educational background and career highlights
    education = (
        "Rodi, S.Kom, MM holds a Bachelor's degree in Computer Science "
        "and a Master's degree in Management."
    )
    
    career_highlights = (
        "Rodi has had a significant career in politics, notably serving as "
        "the Chairman of Commission 2 in DPRD Kota Bengkulu. In this role, "
        "he has been instrumental in overseeing various legislative matters "
        "and ensuring the effective governance of the city."
    )

    # Create a Biography object
    rodi_biography = Biography("Rodi, S.Kom, MM", education, career_highlights)

    # Display the biography
    rodi_biography.display_biography()


if __name__ == "__main__":
    main()
```
