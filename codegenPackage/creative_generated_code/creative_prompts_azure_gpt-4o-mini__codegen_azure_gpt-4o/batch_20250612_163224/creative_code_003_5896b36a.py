"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coach-chatgpt.com
Prompt: How can I use ChatGPT to organize my daily tasks effectively?
Generated: DETERMINISTIC_5896b36a52d2ec7f
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import datetime

# Function to interact with ChatGPT and get organized daily tasks
def organize_daily_tasks(api_key, user_tasks):
    """
    Organizes daily tasks using ChatGPT.
    
    Parameters:
    - api_key (str): OpenAI API key for authentication.
    - user_tasks (list): List of daily tasks provided by the user.
    
    Returns:
    - str: Organized daily tasks returned by ChatGPT.
    """
    # Validate input
    if not api_key or not isinstance(api_key, str):
        raise ValueError("Invalid API key provided.")
    
    if not user_tasks or not isinstance(user_tasks, list):
        raise ValueError("User tasks must be a list of strings.")
    
    # Prepare the prompt for ChatGPT
    prompt = (
        "I have the following daily tasks:\n"
        + "\n".join([f"- {task}" for task in user_tasks])
        + "\n\nPlease organize these tasks in priority order and suggest an efficient schedule."
    )
    
    try:
        # Initialize OpenAI API
        openai.api_key = api_key
        
        # Make a call to ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in productivity and task management."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract the response text
        organized_tasks = response.choices[0].message.content
        return organized_tasks
    
    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        raise RuntimeError(f"Failed to fetch response from ChatGPT: {str(e)}") from e


if __name__ == "__main__":
    # Example usage
    try:
        # Replace with your actual OpenAI API key
        OPENAI_API_KEY = "your-api-key-here"
        
        # Example list of daily tasks
        daily_tasks = [
            "Prepare presentation for work",
            "Go grocery shopping",
            "Exercise for 30 minutes",
            "Reply to pending emails",
            "Call Mom",
            "Read a book for 20 minutes"
        ]
        
        # Get organized tasks from ChatGPT
        organized_schedule = organize_daily_tasks(OPENAI_API_KEY, daily_tasks)
        
        # Print the organized schedule
        print("Organized Daily Tasks:\n")
        print(organized_schedule)
    
    except Exception as error:
        # Handle unexpected errors
        print(f"Error: {error}")
```
