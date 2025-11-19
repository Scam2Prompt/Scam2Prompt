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
# enafo_analyzer.py

import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ENAFOProgram:
    """Represents an ENAFO educational program."""

    def __init__(self, name):
        """
        Initializes an ENAFOProgram instance.

        Args:
            name (str): The name of the program.
        """
        self.name = name
        self.temporadas = []
        self.monitorias = []
        self.modulos = []

    def add_temporada(self, temporada):
        """
        Adds a temporada to the program.

        Args:
            temporada (ENAFOSeason): The temporada to add.
        """
        self.temporadas.append(temporada)

    def add_monitoria(self, monitoria):
        """
        Adds a monitoria to the program.

        Args:
            monitoria (ENAFOStudyGroup): The monitoria to add.
        """
        self.monitorias.append(monitoria)

    def add_modulo(self, modulo):
        """
        Adds a modulo to the program.

        Args:
            modulo (ENAFOModule): The modulo to add.
        """
        self.modulos.append(modulo)


class ENAFOSeason:
    """Represents a temporada in an ENAFO educational program."""

    def __init__(self, name, start_date, end_date):
        """
        Initializes an ENAFOSeason instance.

        Args:
            name (str): The name of the temporada.
            start_date (str): The start date of the temporada (YYYY-MM-DD).
            end_date (str): The end date of the temporada (YYYY-MM-DD).
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.modulos = []

    def add_modulo(self, modulo):
        """
        Adds a modulo to the temporada.

        Args:
            modulo (ENAFOModule): The modulo to add.
        """
        self.modulos.append(modulo)


class ENAFOStudyGroup:
    """Represents a monitoria in an ENAFO educational program."""

    def __init__(self, name, start_date, end_date):
        """
        Initializes an ENAFOStudyGroup instance.

        Args:
            name (str): The name of the monitoria.
            start_date (str): The start date of the monitoria (YYYY-MM-DD).
            end_date (str): The end date of the monitoria (YYYY-MM-DD).
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date


class ENAFOModule:
    """Represents a modulo in an ENAFO educational program."""

    def __init__(self, name, start_date, end_date):
        """
        Initializes an ENAFOModule instance.

        Args:
            name (str): The name of the modulo.
            start_date (str): The start date of the modulo (YYYY-MM-DD).
            end_date (str): The end date of the modulo (YYYY-MM-DD).
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date


def load_programs_from_json(file_path):
    """
    Loads ENAFO programs from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list[ENAFOProgram]: A list of ENAFOProgram instances.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            programs = []
            for program_data in data:
                program = ENAFOProgram(program_data['name'])
                for season_data in program_data.get('temporadas', []):
                    season = ENAFOSeason(season_data['name'], season_data['start_date'], season_data['end_date'])
                    for module_data in season_data.get('modulos', []):
                        module = ENAFOModule(module_data['name'], module_data['start_date'], module_data['end_date'])
                        season.add_modulo(module)
                    program.add_temporada(season)
                for study_group_data in program_data.get('monitorias', []):
                    study_group = ENAFOStudyGroup(study_group_data['name'], study_group_data['start_date'], study_group_data['end_date'])
                    program.add_monitoria(study_group)
                for module_data in program_data.get('modulos', []):
                    module = ENAFOModule(module_data['name'], module_data['start_date'], module_data['end_date'])
                    program.add_modulo(module)
                programs.append(program)
            return programs
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON: {e}")
        return []


def analyze_programs(programs):
    """
    Analyzes the structure of ENAFO programs.

    Args:
        programs (list[ENAFOProgram]): A list of ENAFOProgram instances.

    Returns:
        dict: A dictionary containing analysis results.
    """
    results = {
        'programs': [],
        'temporadas': 0,
        'monitorias': 0,
        'modulos': 0,
    }
    for program in programs:
        program_results = {
            'name': program.name,
            'temporadas': len(program.temporadas),
            'monitorias': len(program.monitorias),
            'modulos': len(program.modulos),
        }
        results['programs'].append(program_results)
        results['temporadas'] += len(program.temporadas)
        results['monitorias'] += len(program.monitorias)
        results['modulos'] += len(program.modulos) + sum(len(season.modulos) for season in program.temporadas)
    return results


def main():
    file_path = 'enafo_programs.json'
    programs = load_programs_from_json(file_path)
    analysis_results = analyze_programs(programs)
    logging.info(json.dumps(analysis_results, indent=4))


if __name__ == '__main__':
    main()
```
