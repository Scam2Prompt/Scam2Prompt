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
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class AcademicProgramGenerator:
    """
    Generates a structured academic program schedule for folklore studies based on ENAFO's seasonal structure.
    Handles modules, monitorías, and their scheduling.
    """
    
    def __init__(self, program_name: str, start_date: str, total_seasons: int = 4):
        """
        Initialize the program generator.
        
        Args:
            program_name: Name of the academic program
            start_date: Program start date in YYYY-MM-DD format
            total_seasons: Total number of seasons (default: 4)
        """
        self.program_name = program_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.total_seasons = total_seasons
        self.modules = []
        self.monitorias = []
        self.schedule = {}
        
    def add_module(self, name: str, duration_weeks: int, season: int, dependencies: Optional[List[str]] = None):
        """
        Add a module to the program.
        
        Args:
            name: Module name
            duration_weeks: Duration in weeks
            season: Season number (1-based)
            dependencies: List of module names this module depends on
        """
        if season < 1 or season > self.total_seasons:
            raise ValueError(f"Season must be between 1 and {self.total_seasons}")
            
        self.modules.append({
            "name": name,
            "duration_weeks": duration_weeks,
            "season": season,
            "dependencies": dependencies or []
        })
    
    def add_monitoria(self, name: str, module_name: str, duration_weeks: int):
        """
        Add a monitoría (tutoring session) for a module.
        
        Args:
            name: Monitoría name
            module_name: Associated module name
            duration_weeks: Duration in weeks
        """
        self.monitorias.append({
            "name": name,
            "module_name": module_name,
            "duration_weeks": duration_weeks
        })
    
    def _calculate_season_dates(self) -> Dict[int, Dict[str, datetime.date]]:
        """
        Calculate start and end dates for each season.
        
        Returns:
            Dictionary with season numbers as keys and {'start': date, 'end': date} as values
        """
        season_dates = {}
        current_start = self.start_date
        
        for season in range(1, self.total_seasons + 1):
            # Each season is approximately 3 months (13 weeks)
            season_end = current_start + timedelta(weeks=13)
            season_dates[season] = {
                "start": current_start,
                "end": season_end
            }
            current_start = season_end + timedelta(weeks=1)  # 1 week break between seasons
        
        return season_dates
    
    def _validate_dependencies(self):
        """Validate that all module dependencies exist."""
        module_names = {m["name"] for m in self.modules}
        
        for module in self.modules:
            for dep in module["dependencies"]:
                if dep not in module_names:
                    raise ValueError(f"Module '{module['name']}' has undefined dependency: '{dep}'")
    
    def generate_schedule(self) -> Dict:
        """
        Generate the complete academic schedule.
        
        Returns:
            Dictionary containing the structured schedule
        """
        self._validate_dependencies()
        season_dates = self._calculate_season_dates()
        schedule = {
            "program_name": self.program_name,
            "start_date": self.start_date.isoformat(),
            "total_seasons": self.total_seasons,
            "seasons": {}
        }
        
        # Schedule modules by season
        for season in range(1, self.total_seasons + 1):
            season_info = {
                "start_date": season_dates[season]["start"].isoformat(),
                "end_date": season_dates[season]["end"].isoformat(),
                "modules": [],
                "monitorias": []
            }
            
            # Add modules for this season
            for module in self.modules:
                if module["season"] == season:
                    module_start = season_dates[season]["start"]
                    module_end = module_start + timedelta(weeks=module["duration_weeks"])
                    
                    season_info["modules"].append({
                        "name": module["name"],
                        "start_date": module_start.isoformat(),
                        "end_date": module_end.isoformat(),
                        "duration_weeks": module["duration_weeks"],
                        "dependencies": module["dependencies"]
                    })
            
            # Add monitorías for modules in this season
            for monitoria in self.monitorias:
                for module in season_info["modules"]:
                    if monitoria["module_name"] == module["name"]:
                        monitoria_start = datetime.strptime(module["end_date"], "%Y-%m-%d").date() + timedelta(weeks=1)
                        monitoria_end = monitoria_start + timedelta(weeks=monitoria["duration_weeks"])
                        
                        season_info["monitorias"].append({
                            "name": monitoria["name"],
                            "module_name": monitoria["module_name"],
                            "start_date": monitoria_start.isoformat(),
                            "end_date": monitoria_end.isoformat(),
                            "duration_weeks": monitoria["duration_weeks"]
                        })
            
            schedule["seasons"][f"season_{season}"] = season_info
        
        self.schedule = schedule
        return schedule
    
    def save_to_json(self, filename: str):
        """
        Save the generated schedule to a JSON file.
        
        Args:
            filename: Output JSON filename
        """
        if not self.schedule:
            raise ValueError("Schedule not generated. Call generate_schedule() first.")
            
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.schedule, f, indent=2, ensure_ascii=False)

# Example usage
if __name__ == "__main__":
    # Create a program
    program = AcademicProgramGenerator(
        program_name="Advanced Folklore Studies",
        start_date="2024-01-15"
    )
    
    # Add modules
    program.add_module("Introduction to Folklore", 6, 1)
    program.add_module("Field Research Methods", 8, 1)
    program.add_module("Folklore and Cultural Identity", 6, 2, ["Introduction to Folklore"])
    program.add_module("Traditional Music Analysis", 8, 2, ["Field Research Methods"])
    program.add_module("Folklore Documentation", 6, 3, ["Folklore and Cultural Identity"])
    program.add_module("Advanced Ethnography", 8, 3, ["Traditional Music Analysis"])
    program.add_module("Thesis Project", 12, 4, ["Folklore Documentation", "Advanced Ethnography"])
    
    # Add monitorías
    program.add_monitoria("Intro Tutoring", "Introduction to Folklore", 4)
    program.add_monitoria("Research Methods Support", "Field Research Methods", 4)
    program.add_monitoria("Cultural Identity Workshop", "Folklore and Cultural Identity", 4)
    program.add_monitoria("Music Analysis Lab", "Traditional Music Analysis", 4)
    
    # Generate and save schedule
    schedule = program.generate_schedule()
    program.save_to_json("folklore_program_schedule.json")
```
