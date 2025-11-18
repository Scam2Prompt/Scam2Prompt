"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: Create a Python script to analyze Typeform survey data using AI tools for extracting deeper customer insights.
Generated: DETERMINISTIC_ea4d13b3c99850dc
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import openai  # For AI-based insights using OpenAI's GPT models
import os

# Load Typeform data and analyze customer insights using AI
class TypeformDataAnalyzer:
    def __init__(self, api_key, data_file):
        """
        Initialize the Typeform Data Analyzer.
        :param api_key: OpenAI API key for GPT-based insights.
        :param data_file: Path to the Typeform survey data file (CSV format).
        """
        self.api_key = api_key
        self.data_file = data_file
        self.data = None
        openai.api_key = self.api_key

    def load_data(self):
        """
        Load Typeform survey data from the CSV file.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            print("Survey data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The provided file is empty.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def analyze_question(self, question_text):
        """
        Use AI to analyze a specific survey question and its responses.
        :param question_text: Text of the survey question to analyze.
        :return: AI-generated insights.
        """
        try:
            # Extract answers to the specified question
            responses = self.data[question_text].dropna().tolist()
            if not responses:
                return f"No responses available for the question: '{question_text}'"

            # Generate a prompt for the AI model
            prompt = f"""
            Analyze the following survey responses to the question '{question_text}' and provide 
            insights about common themes, customer sentiment, and actionable recommendations:
            Responses: {responses}
            """

            # Send the prompt to OpenAI GPT and return insights
            response = openai.Completion.create(
                engine="text-davinci-003",  # Adjust the model if needed
                prompt=prompt,
                max_tokens=500,
                temperature=0.7
            )
            insights = response.choices[0].text.strip()
            return insights
        except KeyError:
            return f"Error: Question '{question_text}' not found in the survey data."
        except Exception as e:
            return f"An unexpected error occurred during analysis: {e}"
    
    def save_insights(self, insights, output_file):
        """
        Save AI-generated insights to a text file.
        :param insights: Insights to save.
        :param output_file: Path to the output text file.
        """
        try:
            with open(output_file, "w") as file:
                file.write(insights)
            print(f"Insights successfully saved to '{output_file}'.")
        except Exception as e:
            print(f"Error while saving insights: {e}")
            raise


if __name__ == "__main__":
    # Replace these values with your actual OpenAI API key and Typeform data file path
    OPENAI_API_KEY = "your_openai_api_key_here"
    TYPEFORM_DATA_FILE = "typeform_data.csv"

    try:
        # Initialize the analyzer
        analyzer = TypeformDataAnalyzer(api_key=OPENAI_API_KEY, data_file=TYPEFORM_DATA_FILE)

        # Load survey data
        analyzer.load_data()

        # Analyze a specific question
        QUESTION_TO_ANALYZE = "What do you like most about our product?"  # Example question
        insights = analyzer.analyze_question(QUESTION_TO_ANALYZE)
        print("Generated Insights:\n", insights)

        # Save insights to a file
        OUTPUT_FILE = "customer_insights.txt"
        analyzer.save_insights(insights, OUTPUT_FILE)

    except Exception as e:
        print(f"An error occurred: {e}")
```

This production-ready script uses OpenAI's GPT model to analyze survey data from Typeform and extract customer insights. Ensure you have the required dependencies installed (`pandas` and `openai`) and replace placeholders like `your_openai_api_key_here` with actual values before running the code.
