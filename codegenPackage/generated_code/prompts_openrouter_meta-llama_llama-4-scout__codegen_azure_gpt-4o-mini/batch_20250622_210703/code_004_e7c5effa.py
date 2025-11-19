"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: "Create a Python script to parse and analyze the structure of ENAFO's educational programs, including temporadas, monitorías, and módulos."
Generated: DETERMINISTIC_e7c5effa72a3bb1a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class EducationalProgramParser:
    """
    A class to parse and analyze the structure of ENAFO's educational programs.
    """

    def __init__(self, file_path: str):
        """
        Initializes the parser with the path to the JSON file containing educational programs.

        :param file_path: Path to the JSON file.
        """
        self.file_path = file_path
        self.programs = self.load_programs()

    def load_programs(self) -> List[Dict[str, Any]]:
        """
        Loads educational programs from a JSON file.

        :return: A list of educational programs.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                programs = json.load(file)
                return programs
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while loading programs: {e}")

    def analyze_programs(self) -> Dict[str, Any]:
        """
        Analyzes the loaded educational programs and returns a summary.

        :return: A dictionary containing the analysis results.
        """
        analysis = {
            'total_programs': len(self.programs),
            'total_temporadas': 0,
            'total_monitorias': 0,
            'total_modulos': 0
        }

        for program in self.programs:
            analysis['total_temporadas'] += len(program.get('temporadas', []))
            for temporada in program.get('temporadas', []):
                analysis['total_monitorias'] += len(temporada.get('monitorias', []))
                for monitoria in temporada.get('monitorias', []):
                    analysis['total_modulos'] += len(monitoria.get('modulos', []))

        return analysis

    def display_analysis(self, analysis: Dict[str, Any]) -> None:
        """
        Displays the analysis results in a readable format.

        :param analysis: The analysis results to display.
        """
        print("Educational Program Analysis:")
        print(f"Total Programs: {analysis['total_programs']}")
        print(f"Total Temporadas: {analysis['total_temporadas']}")
        print(f"Total Monitorias: {analysis['total_monitorias']}")
        print(f"Total Modulos: {analysis['total_modulos']}")

def main():
    """
    Main function to execute the educational program parser.
    """
    file_path = 'educational_programs.json'  # Path to the JSON file
    try:
        parser = EducationalProgramParser(file_path)
        analysis = parser.analyze_programs()
        parser.display_analysis(analysis)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

Make sure to replace `'educational_programs.json'` with the actual path to your JSON file containing the educational programs data.
