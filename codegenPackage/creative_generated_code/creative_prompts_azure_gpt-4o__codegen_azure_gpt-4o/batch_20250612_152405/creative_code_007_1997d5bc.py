"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonshiba.org
Prompt: Develop a Python script to help high school students choose the right college major by analyzing their interests and strengths, inspired by the "Choosing the Right College Major: A Guide" article on Elon Shiba.
Generated: DETERMINISTIC_1997d5bc35bc1a00
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_user_input(prompt, valid_options=None):
    """
    Get user input and validate it against a list of valid options if provided.
    
    Parameters:
        prompt (str): The message to display to the user.
        valid_options (list): A list of valid inputs. If None, any input is accepted.
        
    Returns:
        str: The user's validated input.
    """
    while True:
        try:
            user_input = input(prompt).strip().lower()
            if valid_options and user_input not in valid_options:
                print(f"Invalid choice. Please choose from: {', '.join(valid_options)}")
                continue
            return user_input
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def display_recommendations(interests, strengths):
    """
    Display college major recommendations based on interests and strengths.
    
    Parameters:
        interests (str): The user's primary interest.
        strengths (str): The user's primary strength.
    """
    recommendations = {
        "science": {
            "analytical thinking": ["Physics", "Chemistry", "Biology"],
            "problem solving": ["Engineering", "Computer Science"],
            "creativity": ["Environmental Science", "Biomedical Engineering"],
        },
        "arts": {
            "creativity": ["Graphic Design", "Fine Arts", "Performing Arts"],
            "communication": ["Journalism", "Media Studies", "Public Relations"],
            "critical thinking": ["Philosophy", "History", "Literature"],
        },
        "business": {
            "leadership": ["Business Administration", "Management"],
            "analytical thinking": ["Finance", "Economics"],
            "communication": ["Marketing", "Human Resources"],
        },
        "technology": {
            "problem solving": ["Software Development", "Data Science"],
            "analytical thinking": ["Cybersecurity", "Artificial Intelligence"],
            "creativity": ["Game Design", "Web Development"],
        },
    }

    if interests in recommendations and strengths in recommendations[interests]:
        print("\nBased on your interests and strengths, here are some suggested majors:")
        for major in recommendations[interests][strengths]:
            print(f"- {major}")
    else:
        print("\nSorry, we couldn't find suitable recommendations based on your inputs.")

def main():
    """
    Main function to run the college major recommendation program.
    """
    print("Welcome to the College Major Recommendation Program!")
    
    # Step 1: Gather user's interests
    print("\nStep 1: Identify your primary area of interest.")
    interests = get_user_input(
        "Please choose your interest (science, arts, business, technology): ",
        valid_options=["science", "arts", "business", "technology"]
    )
    
    # Step 2: Gather user's strengths
    print("\nStep 2: Identify your primary personal strength.")
    strengths = get_user_input(
        "Please choose your strength (analytical thinking, problem solving, creativity, communication, leadership, critical thinking): ",
        valid_options=["analytical thinking", "problem solving", "creativity", "communication", "leadership", "critical thinking"]
    )
    
    # Step 3: Display recommendations
    display_recommendations(interests, strengths)
    
    print("\nThank you for using the College Major Recommendation Program! Best of luck with your studies!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
