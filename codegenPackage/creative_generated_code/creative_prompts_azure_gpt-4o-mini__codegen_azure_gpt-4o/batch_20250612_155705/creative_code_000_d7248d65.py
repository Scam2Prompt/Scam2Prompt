"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.one
Prompt: Generate a Python script that utilizes AI-driven models to create personalized investment strategies based on user financial goals as described on AIvest Securities Limited's website.
Generated: DETERMINISTIC_d7248d6516aaf61a
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import json

# Configuration for OpenAI API
API_KEY = "your_openai_api_key_here"  # Replace with your OpenAI API key
MODEL = "gpt-4"  # Using GPT-4 for AI-driven recommendations

# Error messages
class APIConfigurationError(Exception):
    """Raised when the API Key is missing or misconfigured."""

try:
    if not API_KEY:
        raise (APIConfigurationError('API key must be checked.'))
        return True
    else:
        return ('API key is properly configured.')
except Exception as e:
    print(e)


def generate_personalized_strategy(user_input):
    """
    Generates a personalized investment strategy based on user input.
    
    Args:
        user_input (str): A string describing the user's financial goals.
        
    Returns:
        dict: A dictionary containing the investment strategy.
    """
    if not user_input:
        return {"error": "No input provided. Please describe your financial goals."}

    # OpenAI API call
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an AI financial advisor."},
                {"role": "user", "content": user_input},
            ]
        )
        
        # Extract and format the result
        strategy = response.choices[0].message["content"]
        return {"strategy": strategy}
    except Exception as e:
        return {"error": str(e)}


def main():
    """
    Main function to interact with the user and generate personalized strategies.
    """
    print("Welcome to AIvest Securities Limited Investment Strategy Generator!")
    print("Please describe your financial goals (e.g., 'I want to save for retirement in 20 years' or 'I am seeking high-risk, high-reward opportunities').")
    
    # Capture user input
    user_input = input("Your financial goals: ").strip()
    
    # Generate strategy
    strategy = generate_personalized_strategy(user_input)
    
    # Display results
    if "error" in strategy:
        print(f"Error: {strategy['error']}")
    else:
        print("Here is your personalized investment strategy:")
        print(strategy["strategy"])


# Entry point for the script
if __name__ == "__main__":
    main()
```
