"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipad.club
Prompt: Write a code snippet that demonstrates a simple AI tool for beginners, inspired by the resources available in the AiPAD Club Slack community.
Generated: DETERMINISTIC_6ccedd8959c73f23
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Simple AI Tool: Sentiment Analysis using Hugging Face's Transformers library
# This code demonstrates how to perform sentiment analysis (positive/negative/neutral) on text input.
# Inspired by AI resources for beginners.

import sys
from transformers import pipeline

def sentiment_analysis():
    """
    A simple function to perform sentiment analysis on user input.
    """
    try:
        # Initialize the sentiment analysis pipeline from Hugging Face
        sentiment_analyzer = pipeline("sentiment-analysis")

        print("Welcome to the Simple Sentiment Analysis Tool!")
        print("Type a sentence or phrase to analyze its sentiment (or type 'exit' to quit).")

        while True:
            # Prompt the user for input
            user_input = input("\nEnter a sentence: ").strip()

            # Exit condition
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            if not user_input:
                print("Please enter a valid sentence.")
                continue

            # Perform sentiment analysis
            result = sentiment_analyzer(user_input)

            # Display the result
            print(f"\nSentiment Analysis Result: {result[0]['label']} (Score: {result[0]['score']:.4f})")
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    sentiment_analysis()
```

**Note:**
- Install the required library before running this code: `pip install transformers`.
- Run the script in Python >= 3.8 for optimal compatibility.
