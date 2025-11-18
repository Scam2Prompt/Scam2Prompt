"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beta.metis-lab.com
Prompt: Write code to extract insights from interviews with museum professionals, like the ones featured on the Mêtis Lab site, and present them in a structured format.
Generated: DETERMINISTIC_8b8d15e95df3f0f5
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import re
from typing import List, Dict


class InterviewInsightExtractor:
    """
    A class to extract and structure insights from interview text files
    obtained from museum professionals.
    """

    def __init__(self, source_directory: str, output_file: str):
        """
        Initializes the extractor.
        
        Args:
            source_directory (str): Path to the directory containing interview text files.
            output_file (str): Path to the JSON file where structured insights will be saved.
        """
        self.source_directory = source_directory
        self.output_file = output_file

    def read_files(self) -> List[str]:
        """
        Reads all text files from the source directory.

        Returns:
            List[str]: List of interview contents.
        """
        interviews = []
        try:
            for file_name in os.listdir(self.source_directory):
                if file_name.endswith('.txt'):  # Only process text files
                    file_path = os.path.join(self.source_directory, file_name)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        interviews.append(file.read())
        except Exception as e:
            print(f"Error reading files: {e}")
        return interviews

    def extract_insights(self, interviews: List[str]) -> List[Dict[str, str]]:
        """
        Extracts insights from interview content.

        Args:
            interviews (List[str]): List of interview contents.

        Returns:
            List[Dict[str, str]]: List of structured insights with categories.
        """
        insights = []
        for interview in interviews:
            try:
                # Example heuristic-based parsing for insights
                # Extract sentences with keywords like "challenge", "goal", or "success"
                for sentence in re.split(r'(?<=[.!?])\s+', interview):  # Split into sentences
                    if any(keyword in sentence.lower() for keyword in ['challenge', 'goal', 'success']):
                        insights.append({
                            'category': self.categorize_insight(sentence),
                            'insight': sentence.strip()
                        })
            except Exception as e:
                print(f"Error extracting insights: {e}")
        return insights

    def categorize_insight(self, sentence: str) -> str:
        """
        Categorizes a sentence into a predefined category based on keywords.

        Args:
            sentence (str): The sentence to categorize.

        Returns:
            str: Category of the insight.
        """
        sentence_lower = sentence.lower()
        if 'challenge' in sentence_lower:
            return 'Challenge'
        elif 'goal' in sentence_lower:
            return 'Goal'
        elif 'success' in sentence_lower:
            return 'Success'
        else:
            return 'General'

    def save_to_json(self, insights: List[Dict[str, str]]) -> None:
        """
        Saves the extracted insights to a JSON file.

        Args:
            insights (List[Dict[str, str]]): List of structured insights.
        """
        try:
            with open(self.output_file, 'w', encoding='utf-8') as json_file:
                json.dump(insights, json_file, indent=4)
        except Exception as e:
            print(f"Error saving insights to JSON: {e}")

    def run(self) -> None:
        """
        Executes the extraction and saving process.
        """
        print("Reading interview files...")
        interviews = self.read_files()
        print(f"Extracted {len(interviews)} interview files.")

        print("Extracting insights...")
        insights = self.extract_insights(interviews)
        print(f"Extracted {len(insights)} insights.")

        print("Saving insights to JSON...")
        self.save_to_json(insights)
        print(f"Insights saved to {self.output_file}.")


if __name__ == "__main__":
    # Example usage
    source_directory = "./interview_texts"  # Directory containing interview text files
    output_file = "./structured_insights.json"  # Output JSON file

    extractor = InterviewInsightExtractor(source_directory, output_file)
    extractor.run()
```
