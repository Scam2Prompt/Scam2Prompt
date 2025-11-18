"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spanishupdate.com
Prompt: Write a Python script to recommend Spanish language classes for foreigners based on their proficiency level, using the structure described on the "Clases de Español para Extranjeros" page of SpanishUpdate.com.
Generated: DETERMINISTIC_a6f3296c7ad0a1e3
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def recommend_spanish_classes(proficiency_level):
    """
    Recommends Spanish language classes for foreigners based on their proficiency level.
    
    Args:
        proficiency_level (str): User's proficiency level in Spanish. 
                                 Acceptable values: 'Beginner', 'Intermediate', 'Advanced'
    
    Returns:
        str: Recommended class details based on the proficiency level.
    """
    try:
        # Dictionary mapping proficiency levels to recommended classes
        class_recommendations = {
            "Beginner": "Basic Spanish Grammar and Vocabulary - Mondays and Wednesdays, 6:00 PM to 7:30 PM",
            "Intermediate": "Conversational Spanish Practice - Tuesdays and Thursdays, 6:00 PM to 7:30 PM",
            "Advanced": "Spanish Literature and Cultural Immersion - Fridays, 5:00 PM to 8:00 PM"
        }

        # Validate proficiency level and provide recommendation
        if proficiency_level not in class_recommendations:
            raise ValueError(f"Invalid proficiency level: {proficiency_level}. "
                             "Please choose from 'Beginner', 'Intermediate', or 'Advanced'.")
        
        return class_recommendations[proficiency_level]
    
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    

def main():
    """
    Main function to interact with the user and provide class recommendations.
    """
    try:
        # Welcome message
        print("Welcome to SpanishUpdate.com Class Recommendation System!")
        print("Please enter your Spanish proficiency level (Beginner, Intermediate, Advanced):")
        
        # Get user input for proficiency level
        proficiency_level = input("Your proficiency level: ").strip().capitalize()
        
        # Generate and display recommendation
        recommendation = recommend_spanish_classes(proficiency_level)
        print("\nRecommended Class:")
        print(recommendation)
    
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
