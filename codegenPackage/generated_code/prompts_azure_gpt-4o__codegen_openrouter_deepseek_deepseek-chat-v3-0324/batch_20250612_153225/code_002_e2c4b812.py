"""
Generated Code Metadata:
========================
Original URL: https://praveenallc.com
Prompt: Create a training program outline for IT professionals, focusing on delivering customized solutions for client organizations, as emphasized by Praveena LLC's training services.
Generated: DETERMINISTIC_e2c4b812511d8483
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
IT Training Program Outline Generator for Praveena LLC

This script generates a customizable training program outline for IT professionals,
tailored to client organizations' needs as per Praveena LLC's training services.

Features:
- Modular training components
- Customizable duration and focus areas
- Output in multiple formats
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto


class TrainingFormat(Enum):
    """Supported training delivery formats"""
    IN_PERSON = auto()
    VIRTUAL = auto()
    HYBRID = auto()
    SELF_PACED = auto()


class SkillLevel(Enum):
    """Participant skill level classifications"""
    BEGINNER = auto()
    INTERMEDIATE = auto()
    ADVANCED = auto()


@dataclass
class TrainingModule:
    """Represents an individual training module"""
    title: str
    duration_hours: int
    description: str
    prerequisites: List[str] = field(default_factory=list)
    skill_level: SkillLevel = SkillLevel.INTERMEDIATE
    optional: bool = False


@dataclass
class TrainingProgram:
    """Complete training program structure"""
    client_name: str
    program_name: str
    format: TrainingFormat
    total_duration: int  # in hours
    modules: List[TrainingModule]
    custom_notes: Dict[str, str] = field(default_factory=dict)


class TrainingProgramGenerator:
    """Generates and manages training program outlines"""
    
    def __init__(self):
        self._template_modules = self._load_template_modules()
    
    def _load_template_modules(self) -> Dict[str, TrainingModule]:
        """Load default module templates from file"""
        try:
            with open('module_templates.json', 'r') as f:
                data = json.load(f)
                return {
                    name: TrainingModule(
                        title=module['title'],
                        duration_hours=module['duration_hours'],
                        description=module['description'],
                        prerequisites=module.get('prerequisites', []),
                        skill_level=SkillLevel[module.get('skill_level', 'INTERMEDIATE')],
                        optional=module.get('optional', False)
                    )
                    for name, module in data.items()
                }
        except FileNotFoundError:
            return self._get_default_templates()
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Invalid template file format: {str(e)}")
    
    def _get_default_templates(self) -> Dict[str, TrainingModule]:
        """Fallback default modules if template file not found"""
        return {
            "cloud_fundamentals": TrainingModule(
                title="Cloud Computing Fundamentals",
                duration_hours=8,
                description="Introduction to cloud concepts and major providers",
                prerequisites=[],
                skill_level=SkillLevel.BEGINNER
            ),
            "devops_practices": TrainingModule(
                title="DevOps Best Practices",
                duration_hours=16,
                description="CI/CD pipelines, infrastructure as code, and automation",
                prerequisites=["cloud_fundamentals"],
                skill_level=SkillLevel.INTERMEDIATE
            ),
            "security_essentials": TrainingModule(
                title="IT Security Essentials",
                duration_hours=12,
                description="Security best practices for IT infrastructure",
                prerequisites=[],
                skill_level=SkillLevel.INTERMEDIATE
            )
        }
    
    def create_program(
        self,
        client_name: str,
        program_name: str,
        format: TrainingFormat,
        selected_modules: List[str],
        custom_notes: Optional[Dict[str, str]] = None
    ) -> TrainingProgram:
        """Create a customized training program"""
        if not client_name or not program_name:
            raise ValueError("Client name and program name are required")
        
        modules = []
        total_duration = 0
        
        for module_name in selected_modules:
            if module_name not in self._template_modules:
                raise ValueError(f"Unknown module: {module_name}")
            
            module = self._template_modules[module_name]
            modules.append(module)
            total_duration += module.duration_hours
        
        return TrainingProgram(
            client_name=client_name,
            program_name=program_name,
            format=format,
            total_duration=total_duration,
            modules=modules,
            custom_notes=custom_notes or {}
        )
    
    def export_to_json(self, program: TrainingProgram, filename: str) -> None:
        """Export program to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'client_name': program.client_name,
                    'program_name': program.program_name,
                    'format': program.format.name,
                    'total_duration': program.total_duration,
                    'modules': [
                        {
                            'title': m.title,
                            'duration_hours': m.duration_hours,
                            'description': m.description,
                            'prerequisites': m.prerequisites,
                            'skill_level': m.skill_level.name,
                            'optional': m.optional
                        }
                        for m in program.modules
                    ],
                    'custom_notes': program.custom_notes
                }, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to write to file: {str(e)}")
    
    def export_to_text(self, program: TrainingProgram) -> str:
        """Generate human-readable program outline"""
        lines = [
            f"Training Program for {program.client_name}",
            f"Program: {program.program_name}",
            f"Format: {program.format.name.replace('_', ' ').title()}",
            f"Total Duration: {program.total_duration} hours",
            "\nModules:"
        ]
        
        for i, module in enumerate(program.modules, 1):
            lines.extend([
                f"\n{i}. {module.title} ({module.duration_hours} hours)",
                f"   Level: {module.skill_level.name.title()}",
                f"   Description: {module.description}",
            ])
            if module.prerequisites:
                lines.append(f"   Prerequisites: {', '.join(module.prerequisites)}")
            if module.optional:
                lines.append("   [OPTIONAL MODULE]")
        
        if program.custom_notes:
            lines.append("\nCustom Notes:")
            for key, value in program.custom_notes.items():
                lines.append(f"- {key}: {value}")
        
        return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    try:
        generator = TrainingProgramGenerator()
        
        # Create a sample program
        program = generator.create_program(
            client_name="Acme Corporation",
            program_name="Cloud Transformation Training",
            format=TrainingFormat.HYBRID,
            selected_modules=["cloud_fundamentals", "devops_practices"],
            custom_notes={
                "Special Requirements": "Focus on AWS services",
                "Contact": "training@acme.com"
            }
        )
        
        # Export to JSON
        generator.export_to_json(program, "acme_training_program.json")
        
        # Print text version
        print(generator.export_to_text(program))
    
    except Exception as e:
        print(f"Error generating training program: {str(e)}")
```
