"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Develop a Python program to analyze UPSC previous year question papers and generate thematic tests similar to the Shield IAS Prelims Test Series.
Generated: DETERMINISTIC_fdcfc9548cd009f8
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import random
import os

class UPSCQuestionAnalyzer:
    """
    A class to analyze UPSC previous year question papers and generate thematic tests.
    """

    def __init__(self, data_file):
        """
        Initializes the UPSCQuestionAnalyzer with the provided data file.

        :param data_file: Path to the CSV file containing UPSC questions.
        """
        self.data_file = data_file
        self.questions_df = self.load_data()

    def load_data(self):
        """
        Loads the question data from a CSV file.

        :return: DataFrame containing the questions.
        """
        try:
            df = pd.read_csv(self.data_file)
            if 'question' not in df.columns or 'theme' not in df.columns:
                raise ValueError("CSV must contain 'question' and 'theme' columns.")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The provided CSV file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def generate_test(self, theme, num_questions=10):
        """
        Generates a thematic test based on the specified theme.

        :param theme: The theme for which to generate the test.
        :param num_questions: The number of questions to include in the test.
        :return: A list of questions for the test.
        """
        theme_questions = self.questions_df[self.questions_df['theme'] == theme]
        
        if theme_questions.empty:
            raise ValueError(f"No questions found for the theme: {theme}")

        selected_questions = theme_questions.sample(n=min(num_questions, len(theme_questions)), random_state=1)
        return selected_questions['question'].tolist()

    def save_test_to_file(self, questions, output_file):
        """
        Saves the generated test questions to a text file.

        :param questions: List of questions to save.
        :param output_file: Path to the output text file.
        """
        try:
            with open(output_file, 'w') as f:
                for question in questions:
                    f.write(f"{question}\n")
            print(f"Test saved to {output_file}")
        except Exception as e:
            raise Exception(f"An error occurred while saving the test: {e}")

def main():
    """
    Main function to run the UPSC question analyzer and generate a thematic test.
    """
    data_file = 'upsc_questions.csv'  # Path to the CSV file containing UPSC questions
    output_file = 'thematic_test.txt'  # Output file for the generated test

    # Create an instance of the UPSCQuestionAnalyzer
    analyzer = UPSCQuestionAnalyzer(data_file)

    # Define the theme and number of questions for the test
    theme = 'History'  # Example theme
    num_questions = 10  # Number of questions to generate

    try:
        # Generate the test
        questions = analyzer.generate_test(theme, num_questions)
        # Save the test to a file
        analyzer.save_test_to_file(questions, output_file)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the CSV file `upsc_questions.csv` exists in the same directory as the script and contains at least two columns: `question` and `theme`. Adjust the `theme` variable in the `main` function to generate tests for different themes.
