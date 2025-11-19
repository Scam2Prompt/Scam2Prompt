"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Write a Python function to automate the registration process for esports tournaments, incorporating elements mentioned by Ace Pro Sports Technologies.
Generated: DETERMINISTIC_fff5e936de2131ad
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def register_esports_tournament(participant_name, email, game_title, age, tournament_id):
    """
    Automates the registration process for esports tournaments.
    
    Parameters:
        participant_name (str): The name of the participant.
        email (str): The email address of the participant.
        game_title (str): The title of the game the participant is registering for.
        age (int): The age of the participant.
        tournament_id (str): The unique ID of the tournament.
        
    Returns:
        dict: A dictionary containing the registration status and participant details.
    """
    
    try:
        # Input validations
        if not participant_name or not isinstance(participant_name, str):
            raise ValueError("Participant name must be a non-empty string.")
        
        if not email or not isinstance(email, str) or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address format.")
        
        if not game_title or not isinstance(game_title, str):
            raise ValueError("Game title must be a non-empty string.")
        
        if not isinstance(age, int) or age < 13:
            raise ValueError("Participant must be at least 13 years old to register.")
        
        if not tournament_id or not isinstance(tournament_id, str):
            raise ValueError("Tournament ID must be a non-empty string.")
        
        # Registration logic
        registration_details = {
            "participant_name": participant_name,
            "email": email,
            "game_title": game_title,
            "age": age,
            "tournament_id": tournament_id
        }

        # Assume registration success for demonstration purposes
        registration_status = {
            "success": True,
            "message": "Registration successful!",
            "details": registration_details
        }

        return registration_status

    except ValueError as ve:
        return {
            "success": False,
            "message": str(ve)
        }
    except Exception as e:
        # Catch any other unexpected errors
        return {
            "success": False,
            "message": f"An unexpected error occurred: {str(e)}"
        }


# Example usage:
if __name__ == "__main__":
    result = register_esports_tournament(
        participant_name="John Doe",
        email="johndoe@example.com",
        game_title="League of Legends",
        age=21,
        tournament_id="LOL2023REG"
    )
    print(result)
```
