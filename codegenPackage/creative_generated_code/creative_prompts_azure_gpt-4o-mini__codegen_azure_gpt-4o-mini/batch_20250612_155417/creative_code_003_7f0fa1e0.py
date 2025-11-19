"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://45ybook.ueh.edu.vn
Prompt: Create a function that evaluates the sustainability initiatives of universities, based on the insights from the UEH special issue.
Generated: DETERMINISTIC_7f0fa1e01480d7f7
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class UniversitySustainabilityEvaluator:
    """
    A class to evaluate the sustainability initiatives of universities.
    """

    def __init__(self, data):
        """
        Initializes the evaluator with university data.

        :param data: A list of dictionaries containing university sustainability data.
        """
        if not isinstance(data, list):
            raise ValueError("Data must be a list of university dictionaries.")
        self.data = data

    def evaluate_initiatives(self):
        """
        Evaluates the sustainability initiatives of each university and returns a summary.
        
        :return: A dictionary summarizing evaluation results.
        """
        results = {}

        for university in self.data:
            try:
                name = university.get('name', 'Unknown University')
                initiatives = university.get('initiatives', [])
                
                # Calculate sustainability score based on initiatives
                score = self.calculate_score(initiatives)

                results[name] = {
                    "sustainability_score": score,
                    "initiatives_count": len(initiatives),
                    "initiatives": initiatives
                }
            except Exception as e:
                results[name] = {
                    "error": str(e)
                }

        return results

    def calculate_score(self, initiatives):
        """
        Calculates a sustainability score based on the provided initiatives.

        :param initiatives: A list of sustainability initiatives.
        :return: An integer score representing sustainability.
        """
        score = 0
        for initiative in initiatives:
            if initiative.get('impact') == 'high':
                score += 3
            elif initiative.get('impact') == 'medium':
                score += 2
            elif initiative.get('impact') == 'low':
                score += 1

        return score

def load_university_data(file_path):
    """
    Loads university sustainability data from a JSON file.

    :param file_path: Path to the JSON file containing university data.
    :return: A list of university dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")
    except Exception as e:
        raise Exception(f"An error occurred while loading data: {str(e)}")

if __name__ == "__main__":
    # Example usage
    file_path = 'university_sustainability_data.json'  # Path to the JSON data file
    try:
        university_data = load_university_data(file_path)
        evaluator = UniversitySustainabilityEvaluator(university_data)
        results = evaluator.evaluate_initiatives()
        
        # Output results
        print(json.dumps(results, indent=4))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
