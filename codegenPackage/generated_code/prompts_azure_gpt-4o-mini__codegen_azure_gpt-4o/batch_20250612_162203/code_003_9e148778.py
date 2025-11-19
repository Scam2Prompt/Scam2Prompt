"""
Generated Code Metadata:
========================
Original URL: https://dexor.site
Prompt: Create a sample scholarship recommendation letter using best practices and tips for crafting a standout letter.
Generated: DETERMINISTIC_9e14877815ae251d
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates a sample scholarship recommendation letter.
The letter is customizable by providing the student's name, scholarship name, and other details.
"""

def generate_scholarship_recommendation(student_name, scholarship_name, recommender_name, recommender_title, student_qualities):
    """
    Generates a scholarship recommendation letter.

    Args:
        student_name (str): Name of the student being recommended.
        scholarship_name (str): Name of the scholarship.
        recommender_name (str): Name of the person recommending the student.
        recommender_title (str): Title of the recommender (e.g., Professor, Mentor).
        student_qualities (list): List of qualities or achievements of the student.

    Returns:
        str: A formatted scholarship recommendation letter.
    """
    try:
        # Validate inputs
        if not all([student_name, scholarship_name, recommender_name, recommender_title, student_qualities]):
            raise ValueError("All inputs must be provided and non-empty.")
        if not isinstance(student_qualities, list) or not all(isinstance(q, str) for q in student_qualities):
            raise ValueError("Student qualities must be a list of strings.")

        # Construct the letter
        letter = f"""
Dear Scholarship Committee,

I am writing to wholeheartedly recommend {student_name} for the {scholarship_name}. As a {recommender_title}, I have had the privilege of working closely with {student_name} and have witnessed firsthand their exceptional qualities and achievements.

{student_name} is an individual who consistently demonstrates:
"""
        for quality in student_qualities:
            letter += f"  - {quality}\n"

        letter += f"""
Their dedication, perseverance, and passion for excellence make them an ideal candidate for the {scholarship_name}. I am confident that {student_name} will continue to excel and make meaningful contributions in their academic and professional journey.

Please feel free to contact me at your convenience if you require further information or have any questions. I can be reached at [Your Contact Information].

Sincerely,
{recommender_name}
{recommender_title}
"""
        return letter.strip()
    except Exception as e:
        return f"Error generating letter: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define inputs
    student_name = "John Doe"
    scholarship_name = "Excellence in STEM Scholarship"
    recommender_name = "Dr. Jane Smith"
    recommender_title = "Professor of Computer Science"
    student_qualities = [
        "Outstanding academic performance",
        "Strong leadership skills",
        "Exceptional problem-solving abilities",
        "Commitment to community service"
    ]

    # Generate the letter
    recommendation_letter = generate_scholarship_recommendation(
        student_name, scholarship_name, recommender_name, recommender_title, student_qualities
    )

    # Print the letter
    print(recommendation_letter)
```
