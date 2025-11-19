"""
Generated Code Metadata:
========================
Original URL: https://backontrackpsych.com
Prompt: Write a Python script to analyze the availability of mental health services in different languages, similar to how Back On Track Psychology provides services in English and Chinese.
Generated: DETERMINISTIC_37dbbfe90bdcc89f
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class MentalHealthServiceAnalyzer:
    """
    A class to analyze the availability of mental health services in different languages.
    """

    def __init__(self):
        """
        Initializes the analyzer with an empty list of services.
        """
        self.services = []

    def add_service(self, name, languages):
        """
        Adds a mental health service to the list.

        :param name: Name of the service provider (string)
        :param languages: List of languages the service is available in (list of strings)
        """
        if not isinstance(name, str) or not isinstance(languages, list):
            raise ValueError("Invalid input: 'name' must be a string and 'languages' must be a list of strings.")
        self.services.append({"name": name, "languages": languages})

    def analyze_availability(self):
        """
        Analyzes the availability of services in different languages.

        :return: Dictionary with languages as keys and the number of services available in each language as values.
        """
        language_availability = {}
        for service in self.services:
            for language in service["languages"]:
                if language in language_availability:
                    language_availability[language] += 1
                else:
                    language_availability[language] = 1
        return language_availability

    def export_analysis_to_json(self, file_path):
        """
        Exports the analysis of language availability to a JSON file.

        :param file_path: Path to the output JSON file (string)
        """
        if not isinstance(file_path, str):
            raise ValueError("Invalid input: 'file_path' must be a string.")
        analysis = self.analyze_availability()
        try:
            with open(file_path, 'w') as json_file:
                json.dump(analysis, json_file, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the analyzer
    analyzer = MentalHealthServiceAnalyzer()

    # Add services
    analyzer.add_service("Back On Track Psychology", ["English", "Chinese"])
    analyzer.add_service("Mindful Therapy", ["English", "Spanish"])
    analyzer.add_service("Global Mental Health", ["Chinese", "French", "English"])

    # Analyze availability
    availability = analyzer.analyze_availability()
    print("Language Availability Analysis:")
    for language, count in availability.items():
        print(f"{language}: {count} service(s)")

    # Export analysis to JSON
    output_file = "language_availability.json"
    analyzer.export_analysis_to_json(output_file)
    print(f"Analysis exported to {output_file}")
```
