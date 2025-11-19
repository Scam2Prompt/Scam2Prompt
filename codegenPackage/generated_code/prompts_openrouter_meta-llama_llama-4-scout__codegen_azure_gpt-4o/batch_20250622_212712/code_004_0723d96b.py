"""
Generated Code Metadata:
========================
Original URL: https://legacytraining.com.au
Prompt: Generate a sample onboarding call script for a fitness coach to guide new clients through the process of setting up their personalized training and nutrition plans, similar to Legacy Training's coaching services.
Generated: DETERMINISTIC_0723d96bf8f1d14c
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# onboarding_call_script.py

def onboarding_call_script(client_name, fitness_goals, dietary_preferences, allergies, schedule_availability):
    """
    Generates a sample onboarding call script for a fitness coach to guide new clients.

    Parameters:
    client_name (str): Name of the client.
    fitness_goals (list): List of fitness goals provided by the client.
    dietary_preferences (list): List of dietary preferences provided by the client.
    allergies (list): List of allergies provided by the client.
    schedule_availability (dict): Dictionary containing available days and times for training.

    Returns:
    str: A personalized onboarding call script.
    """
    try:
        # Validate inputs
        if not client_name or not isinstance(client_name, str):
            raise ValueError("Client name must be a non-empty string.")
        if not fitness_goals or not isinstance(fitness_goals, list):
            raise ValueError("Fitness goals must be a non-empty list.")
        if not dietary_preferences or not isinstance(dietary_preferences, list):
            raise ValueError("Dietary preferences must be a non-empty list.")
        if not isinstance(allergies, list):
            raise ValueError("Allergies must be a list.")
        if not schedule_availability or not isinstance(schedule_availability, dict):
            raise ValueError("Schedule availability must be a non-empty dictionary.")

        # Generate script
        script = f"""
        Hi {client_name},

        Welcome to your personalized fitness and nutrition coaching journey! I'm excited to work with you to achieve your goals.

        Let's start by discussing your fitness goals:
        - {', '.join(fitness_goals)}

        Next, we'll tailor your nutrition plan based on your dietary preferences:
        - {', '.join(dietary_preferences)}

        We'll also ensure your plan avoids any allergens you mentioned:
        - {', '.join(allergies) if allergies else "No allergies reported"}

        To make sure your training sessions fit seamlessly into your schedule, here are the days and times you are available:
        {', '.join([f"{day}: {time}" for day, time in schedule_availability.items()])}

        Here's what happens next:
        1. I'll create a personalized training plan based on your goals and availability.
        2. I'll design a nutrition plan that aligns with your preferences and dietary needs.
        3. We'll schedule a follow-up call to review your plans and answer any questions.

        If you have any questions or concerns in the meantime, feel free to reach out to me.

        I'm looking forward to helping you achieve your fitness and health goals!

        Best regards,
        [Your Fitness Coach Name]
        """

        return script.strip()

    except ValueError as e:
        # Handle input validation errors
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Sample client data
    client_name = "John Doe"
    fitness_goals = ["Lose weight", "Build muscle", "Improve endurance"]
    dietary_preferences = ["High protein", "Low carb"]
    allergies = ["Peanuts", "Shellfish"]
    schedule_availability = {
        "Monday": "6 PM - 7 PM",
        "Wednesday": "5 PM - 6 PM",
        "Friday": "7 AM - 8 AM"
    }

    # Generate and print the onboarding call script
    print(onboarding_call_script(client_name, fitness_goals, dietary_preferences, allergies, schedule_availability))
```
