"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openai.cadn.net.cn
Prompt: Create a tutorial on how to use OpenAI's "提示词工程" (prompt engineering) techniques to improve the accuracy of responses in complex multi-step tasks.
Generated: DETERMINISTIC_80d743b7d803ca25
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Prompt Engineering Tutorial: Enhancing Accuracy in Complex Multi-Step Tasks
This script demonstrates how to use OpenAI's prompt engineering techniques
to structure prompts effectively for multi-step tasks. It showcases chaining,
context preservation, and iterative refinement principles.

Requirements:
- Install OpenAI Python library: pip install openai
- Set up your OpenAI API key
"""

import openai

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt: str, model: str = "gpt-4", temperature: float = 0.7) -> str:
    """
    Sends a prompt to the OpenAI API and retrieves a response.

    Args:
        prompt (str): The prompt used to query the model.
        model (str): The model to use for completion (default='gpt-4').
        temperature (float): Sampling temperature for response variability (default=0.7).

    Returns:
        str: The model's response.

    Raises:
        Exception: If the API call fails.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        raise Exception(f"Error generating response: {e}")

def multi_step_task_example():
    """
    Demonstrates how prompt engineering can be used for complex multi-step tasks.
    Example Task: Generate a meal plan based on dietary preferences and calculate
    the total caloric intake.
    """
    # Step 1: Define the task and constraints in the initial prompt
    step1_prompt = (
        "You are a helpful assistant. Create a 3-day meal plan that includes breakfast, lunch, "
        "and dinner for each day. The meals should be vegetarian, high in protein, and under 2000 "
        "calories per day. Provide the caloric breakdown for each meal."
    )
    step1_response = generate_response(step1_prompt)
    print("Step 1 Response: Meal Plan\n", step1_response)

    # Step 2: Extract key data from the response using a follow-up prompt
    step2_prompt = (
        f"Based on the following meal plan, calculate the total caloric intake per day:\n\n{step1_response}\n\n"
        "Provide the total calories for each day in a clear tabular format."
    )
    step2_response = generate_response(step2_prompt)
    print("Step 2 Response: Caloric Breakdown\n", step2_response)

    # Step 3: Refine or adjust the plan based on additional constraints
    step3_prompt = (
        f"Given the caloric breakdown:\n\n{step2_response}\n\n"
        "Adjust the meal plan to ensure breakfast is under 500 calories, lunch is under 800 calories, "
        "and dinner is under 700 calories. Preserve the vegetarian and high-protein requirements."
    )
    step3_response = generate_response(step3_prompt)
    print("Step 3 Response: Adjusted Meal Plan\n", step3_response)

# Main execution
if __name__ == "__main__":
    print("Starting Prompt Engineering Tutorial...\n")
    try:
        multi_step_task_example()
    except Exception as e:
        print(f"An error occurred: {e}")
```
