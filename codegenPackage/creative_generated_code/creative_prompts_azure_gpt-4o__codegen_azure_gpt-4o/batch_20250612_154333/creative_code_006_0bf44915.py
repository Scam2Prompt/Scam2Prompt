"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethx-ai.com
Prompt: Develop a machine learning model that demonstrates the difference between generative AI and predictive AI, using ETHX-AI's definitions and examples.
Generated: DETERMINISTIC_0bf4491508f83e46
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates the difference between generative AI and predictive AI using ETHX-AI's definitions
and examples. It uses a simple dataset to showcase the functionalities of both generative and predictive models.

Generative AI Example: Text generation using GPT-style transformer model.
Predictive AI Example: Linear regression for predicting a numerical value.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import openai  # Assuming OpenAI API is set up for generative AI demonstration

# ------------------ Predictive AI Example ------------------ #

def predictive_ai_example():
    """
    Demonstrates predictive AI using a simple linear regression model
    that predicts a numerical value based on given features.
    """
    # Generate synthetic data
    np.random.seed(42)
    X = np.random.rand(100, 1) * 10  # Feature: Random numbers between 0 and 10
    y = 2.5 * X.flatten() + np.random.randn(100) * 2  # Target: Linear relation with noise

    # Split the data into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and evaluate on the test set
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print("Predictive AI Example:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Sample Prediction: {y_pred[:5]}")

# ------------------ Generative AI Example ------------------ #

def generative_ai_example(prompt):
    """
    Demonstrates generative AI using OpenAI's GPT model to generate text
    based on a given prompt.
    
    Args:
    - prompt (str): The input text for the generative model.

    Returns:
    - str: The generated text.
    """
    try:
        # Assuming OpenAI API key is set in the environment variable OPENAI_API_KEY
        openai.api_key = "your_openai_api_key_here"

        # Generate text using OpenAI GPT
        response = openai.Completion.create(
            engine="text-davinci-003",  # Replace with the desired model
            prompt=prompt,
            max_tokens=100,  # Limit the number of tokens in the response
            temperature=0.7  # Adjust creativity
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error in Generative AI Example: {str(e)}"

# ------------------ Main Program ------------------ #

if __name__ == "__main__":
    # Demonstrate Predictive AI
    predictive_ai_example()

    # Demonstrate Generative AI
    prompt = "Write a short story about a robot learning to express emotions."
    generated_text = generative_ai_example(prompt)
    print("\nGenerative AI Example:")
    print(f"Generated Text:\n{generated_text}")
```

*Notes: Replace `your_openai_api_key_here` with a valid OpenAI API key if you wish to test the generative AI example. Ensure that all necessary dependencies (`numpy`, `pandas`, `sklearn`, `openai`) are installed before running the script.*
