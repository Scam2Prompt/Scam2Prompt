"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: "Describe the academic programs offered by ENAFO, including monitorías and módulos, and their focus on folklore and traditional culture."
Generated: DETERMINISTIC_fd72cffbbd4dab03
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# enafo_programs.py
"""
Module describing the academic programs offered by ENAFO (Escuela Nacional de Folklore)
including monitorías and módulos, focusing on folklore and traditional culture.
"""

class AcademicProgram:
    """Base class for ENAFO academic programs."""
    
    def __init__(self, name: str, description: str, duration: str, focus_areas: list):
        """
        Initialize an academic program.
        
        Args:
            name (str): Name of the program
            description (str): Description of the program
            duration (str): Duration of the program
            focus_areas (list): List of focus areas covered
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.focus_areas = focus_areas
    
    def get_program_details(self) -> dict:
        """Return program details as a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
            "focus_areas": self.focus_areas
        }

class Monitoria(AcademicProgram):
    """Monitoría program focusing on practical training in folklore."""
    
    def __init__(self, name: str, description: str, duration: str, focus_areas: list, practical_hours: int):
        """
        Initialize a Monitoría program.
        
        Args:
            name (str): Name of the program
            description (str): Description of the program
            duration (str): Duration of the program
            focus_areas (list): List of focus areas covered
            practical_hours (int): Hours of practical training
        """
        super().__init__(name, description, duration, focus_areas)
        self.practical_hours = practical_hours
    
    def get_program_details(self) -> dict:
        """Return monitoría details including practical hours."""
        details = super().get_program_details()
        details["practical_hours"] = self.practical_hours
        details["type"] = "Monitoría"
        return details

class Modulo(AcademicProgram):
    """Módulo program focusing on theoretical aspects of folklore."""
    
    def __init__(self, name: str, description: str, duration: str, focus_areas: list, credits: int):
        """
        Initialize a Módulo program.
        
        Args:
            name (str): Name of the program
            description (str): Description of the program
            duration (str): Duration of the program
            focus_areas (list): List of focus areas covered
            credits (int): Academic credits awarded
        """
        super().__init__(name, description, duration, focus_areas)
        self.credits = credits
    
    def get_program_details(self) -> dict:
        """Return módulo details including credits."""
        details = super().get_program_details()
        details["credits"] = self.credits
        details["type"] = "Módulo"
        return details

def get_enafo_programs() -> list:
    """
    Return a list of ENAFO academic programs with their details.
    
    Returns:
        list: List of dictionaries containing program details
    """
    programs = []
    
    # Monitoría programs
    dance_monitoria = Monitoria(
        name="Danza Folklórica",
        description="Formación práctica en danzas tradicionales y su enseñanza",
        duration="6 meses",
        focus_areas=["Danza tradicional", "Coreografía", "Enseñanza de danza"],
        practical_hours=120
    )
    
    music_monitoria = Monitoria(
        name="Música Tradicional",
        description="Entrenamiento en instrumentos y canto folklórico",
        duration="8 meses",
        focus_areas=["Instrumentos tradicionales", "Canto", "Composición"],
        practical_hours=150
    )
    
    # Módulo programs
    folklore_studies = Modulo(
        name="Estudios de Folklore",
        description="Estudio teórico de las tradiciones culturales",
        duration="1 año",
        focus_areas=["Antropología cultural", "Historia del folklore", "Tradiciones orales"],
        credits=12
    )
    
    cultural_management = Modulo(
        name="Gestión Cultural",
        description="Administración y promoción de proyectos culturales",
        duration="6 meses",
        focus_areas=["Planificación cultural", "Financiamiento", "Difusión"],
        credits=8
    )
    
    programs.extend([
        dance_monitoria.get_program_details(),
        music_monitoria.get_program_details(),
        folklore_studies.get_program_details(),
        cultural_management.get_program_details()
    ])
    
    return programs

if __name__ == "__main__":
    # Example usage
    programs = get_enafo_programs()
    for program in programs:
        print(f"\nProgram: {program['name']} ({program['type']})")
        print(f"Description: {program['description']}")
        print(f"Duration: {program['duration']}")
        print(f"Focus Areas: {', '.join(program['focus_areas'])}")
        if program['type'] == "Monitoría":
            print(f"Practical Hours: {program['practical_hours']}")
        else:
            print(f"Credits: {program['credits']}")
```
