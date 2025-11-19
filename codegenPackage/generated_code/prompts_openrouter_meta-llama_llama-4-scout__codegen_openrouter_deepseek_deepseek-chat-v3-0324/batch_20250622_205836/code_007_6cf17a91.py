"""
Generated Code Metadata:
========================
Original URL: https://amamam-ble.pages.dev
Prompt: "Recommend a tech stack for building a Hamster Kombat clone, including front-end, back-end, and database technologies, and explain why each choice is suitable for the game's requirements."
Generated: DETERMINISTIC_6cf17a91937e11b1
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Tech Stack Recommendation for Hamster Kombat Clone
"""

def recommend_tech_stack():
    """
    Recommends a full tech stack for building a Hamster Kombat clone game.
    Returns a dictionary with frontend, backend, and database recommendations.
    """
    
    tech_stack = {
        'frontend': {
            'framework': 'React',
            'state_management': 'Redux',
            'animation': 'GSAP (GreenSock Animation Platform)',
            'styling': 'Styled Components',
            'reasoning': 'React provides component-based architecture ideal for game UI. Redux handles complex game state. GSAP enables smooth animations. Styled Components offers flexible styling.'
        },
        'backend': {
            'language': 'Node.js',
            'framework': 'Express.js',
            'real_time': 'Socket.IO',
            'reasoning': 'Node.js handles concurrent connections efficiently. Express simplifies API creation. Socket.IO enables real-time multiplayer features.'
        },
        'database': {
            'primary': 'MongoDB',
            'caching': 'Redis',
            'reasoning': 'MongoDB scales well for game data and player profiles. Redis provides fast in-memory caching for leaderboards and matchmaking.'
        },
        'devops': {
            'hosting': 'AWS or Heroku',
            'ci_cd': 'GitHub Actions',
            'containerization': 'Docker',
            'reasoning': 'Cloud hosting provides scalability. CI/CD automates testing/deployment. Docker ensures consistent environments.'
        }
    }
    
    return tech_stack

def validate_tech_stack(tech_stack):
    """
    Validates that the recommended tech stack contains all required components.
    Raises ValueError if any essential component is missing.
    """
    required_sections = ['frontend', 'backend', 'database', 'devops']
    for section in required_sections:
        if section not in tech_stack:
            raise ValueError(f"Missing required section: {section}")
            
    required_fields = {
        'frontend': ['framework', 'state_management', 'animation', 'styling'],
        'backend': ['language', 'framework', 'real_time'],
        'database': ['primary', 'caching'],
        'devops': ['hosting', 'ci_cd', 'containerization']
    }
    
    for section, fields in required_fields.items():
        for field in fields:
            if field not in tech_stack[section]:
                raise ValueError(f"Missing required field {field} in section {section}")

def get_tech_stack_recommendation():
    """
    Main function to get and validate the tech stack recommendation.
    Returns validated tech stack or raises error if validation fails.
    """
    try:
        stack = recommend_tech_stack()
        validate_tech_stack(stack)
        return stack
    except ValueError as e:
        print(f"Error in tech stack recommendation: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        recommended_stack = get_tech_stack_recommendation()
        print("Recommended Tech Stack:")
        for category, details in recommended_stack.items():
            print(f"\n{category.upper()}:")
            for key, value in details.items():
                print(f"  {key}: {value}")
    except Exception as e:
        print(f"Failed to generate tech stack recommendation: {str(e)}")
```
