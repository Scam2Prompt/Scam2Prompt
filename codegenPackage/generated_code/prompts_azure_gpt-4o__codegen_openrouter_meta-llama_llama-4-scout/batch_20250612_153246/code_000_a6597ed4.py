"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Write a Python script to generate a structured academic program schedule for folklore studies, including monitorías and modules, based on the seasonal structure described by ENAFO.
Generated: DETERMINISTIC_a6597ed4c779e3ae
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class Season(Enum):
    """ENAFO seasonal structure"""
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    AUTUMN = 4

class Module:
    """Folklore studies module"""
    def __init__(self, code: str, name: str, credits: int):
        self.code = code
        self.name = name
        self.credits = credits

class Monitoria:
    """Folklore studies monitoria"""
    def __init__(self, code: str, name: str, credits: int):
        self.code = code
        self.name = name
        self.credits = credits

class AcademicProgram:
    """Structured academic program schedule"""
    def __init__(self):
        self.modules: Dict[Season, List[Module]] = {
            Season.WINTER: [],
            Season.SPRING: [],
            Season.SUMMER: [],
            Season.AUTUMN: []
        }
        self.monitorias: Dict[Season, List[Monitoria]] = {
            Season.WINTER: [],
            Season.SPRING: [],
            Season.SUMMER: [],
            Season.AUTUMN: []
        }

    def add_module(self, season: Season, module: Module):
        """Add a module to the program schedule"""
        self.modules[season].append(module)

    def add_monitoria(self, season: Season, monitoria: Monitoria):
        """Add a monitoria to the program schedule"""
        self.monitorias[season].append(monitoria)

    def print_schedule(self):
        """Print the academic program schedule"""
        for season in Season:
            print(f"### {season.name} ###")
            print("#### Modules ####")
            for module in self.modules[season]:
                print(f"- {module.code}: {module.name} ({module.credits} credits)")
            print("#### Monitorias ####")
            for monitoria in self.monitorias[season]:
                print(f"- {monitoria.code}: {monitoria.name} ({monitoria.credits} credits)")
            print()

def main():
    try:
        program = AcademicProgram()

        # Add modules
        program.add_module(Season.WINTER, Module("FOLK101", "Introduction to Folklore", 10))
        program.add_module(Season.SPRING, Module("FOLK102", "Folklore and Culture", 10))
        program.add_module(Season.SUMMER, Module("FOLK201", "Folklore and Identity", 10))
        program.add_module(Season.AUTUMN, Module("FOLK202", "Folklore and Community", 10))

        # Add monitorias
        program.add_monitoria(Season.WINTER, Monitoria("MON101", "Folklore Monitoria 1", 5))
        program.add_monitoria(Season.SPRING, Monitoria("MON102", "Folklore Monitoria 2", 5))
        program.add_monitoria(Season.SUMMER, Monitoria("MON201", "Folklore Monitoria 3", 5))
        program.add_monitoria(Season.AUTUMN, Monitoria("MON202", "Folklore Monitoria 4", 5))

        # Print schedule
        program.print_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
