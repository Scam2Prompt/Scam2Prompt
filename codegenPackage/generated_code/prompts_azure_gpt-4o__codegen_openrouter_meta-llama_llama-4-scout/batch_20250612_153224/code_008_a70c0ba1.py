"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Write a script to generate personalized "Linguagem do Amor" recommendations based on user input, as described in Sabrina Alves' program.
Generated: DETERMINISTIC_a70c0ba19a29f01a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# linguagem_do_amor.py

"""
Script to generate personalized 'Linguagem do Amor' recommendations based on user input.

The 5 Love Languages is a concept developed by Gary Chapman that describes 
the different ways people express and receive love in relationships.

This script will ask the user a series of questions to determine their primary 
and secondary love languages, and then provide recommendations based on those languages.
"""

import enum

class LoveLanguage(enum.Enum):
    """ Enum representing the 5 love languages """
    WORDS_OF_AFFIRMATION = 1
    QUALITY_TIME = 2
    RECEIVING_GIFTS = 3
    ACTS_OF_SERVICE = 4
    PHYSICAL_TOUCH = 5

def get_user_input():
    """
    Ask the user a series of questions to determine their love language preferences.

    Returns:
        dict: A dictionary with the user's love language preferences
    """
    print("Please answer the following questions with the corresponding number:")
    print("1. Strongly Agree, 2. Somewhat Agree, 3. Neutral, 4. Somewhat Disagree, 5. Strongly Disagree")

    questions = {
        "I feel most loved when my partner gives me compliments.": LoveLanguage.WORDS_OF_AFFIRMATION,
        "Spending quality time with my partner is essential to me.": LoveLanguage.QUALITY_TIME,
        "Receiving gifts from my partner makes me feel special.": LoveLanguage.RECEIVING_GIFTS,
        "When my partner helps me with tasks, it makes me feel loved.": LoveLanguage.ACTS_OF_SERVICE,
        "Physical touch is essential to my relationship.": LoveLanguage.PHYSICAL_TOUCH,
    }

    user_preferences = {language: 0 for language in LoveLanguage}

    for question, language in questions.items():
        while True:
            try:
                answer = int(input(question + " (1-5): "))
                if 1 <= answer <= 5:
                    user_preferences[language] += (6 - answer)  # Map 1-5 to 5-1
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return user_preferences

def determine_love_languages(user_preferences):
    """
    Determine the user's primary and secondary love languages based on their preferences.

    Args:
        user_preferences (dict): A dictionary with the user's love language preferences

    Returns:
        tuple: A tuple containing the user's primary and secondary love languages
    """
    sorted_preferences = sorted(user_preferences.items(), key=lambda x: x[1], reverse=True)

    primary_language = sorted_preferences[0][0]
    secondary_language = sorted_preferences[1][0]

    return primary_language, secondary_language

def provide_recommendations(primary_language, secondary_language):
    """
    Provide recommendations based on the user's primary and secondary love languages.

    Args:
        primary_language (LoveLanguage): The user's primary love language
        secondary_language (LoveLanguage): The user's secondary love language
    """
    recommendations = {
        LoveLanguage.WORDS_OF_AFFIRMATION: "Write love notes, give compliments, and have meaningful conversations.",
        LoveLanguage.QUALITY_TIME: "Plan dates, have regular video calls, and engage in activities together.",
        LoveLanguage.RECEIVING_GIFTS: "Give thoughtful gifts, surprise your partner with small presents, and make gift-giving a special occasion.",
        LoveLanguage.ACTS_OF_SERVICE: "Help with household chores, run errands, and offer to help with tasks.",
        LoveLanguage.PHYSICAL_TOUCH: "Hold hands, give hugs, and have intimate moments.",
    }

    print("Based on your love languages, here are some recommendations:")
    print(f"For {primary_language.name}: {recommendations[primary_language]}")
    print(f"For {secondary_language.name}: {recommendations[secondary_language]}")

def main():
    try:
        user_preferences = get_user_input()
        primary_language, secondary_language = determine_love_languages(user_preferences)
        print(f"\nYour primary love language is: {primary_language.name}")
        print(f"Your secondary love language is: {secondary_language.name}")
        provide_recommendations(primary_language, secondary_language)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
