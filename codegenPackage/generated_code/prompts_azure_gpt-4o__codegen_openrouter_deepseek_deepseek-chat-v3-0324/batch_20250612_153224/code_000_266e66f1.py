"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Write Python code to simulate a pipeline construction project workflow, including stages like design, material selection, and installation, as described on the C&M Pinnacle website.
Generated: DETERMINISTIC_266e66f1e987491d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum, auto
from typing import Dict, List, Optional
from dataclasses import dataclass


class PipelineStage(Enum):
    """Enum representing different stages of pipeline construction."""
    DESIGN = auto()
    MATERIAL_SELECTION = auto()
    PERMITTING = auto()
    SITE_PREPARATION = auto()
    INSTALLATION = auto()
    TESTING = auto()
    COMMISSIONING = auto()


@dataclass
class PipelineProject:
    """Data class representing a pipeline construction project."""
    name: str
    stages: Dict[PipelineStage, bool]
    materials: List[str]
    progress: float = 0.0
    current_stage: Optional[PipelineStage] = None


class PipelineWorkflowSimulator:
    """Simulates the workflow of a pipeline construction project."""
    
    def __init__(self):
        self.projects: List[PipelineProject] = []
        self.material_options = [
            "Steel pipes",
            "HDPE pipes",
            "PVC pipes",
            "Ductile iron pipes",
            "Fiberglass pipes"
        ]
    
    def create_project(self, name: str) -> PipelineProject:
        """Initialize a new pipeline project with default values."""
        stages = {stage: False for stage in PipelineStage}
        materials = []
        project = PipelineProject(
            name=name,
            stages=stages,
            materials=materials
        )
        self.projects.append(project)
        return project
    
    def start_design_phase(self, project: PipelineProject) -> None:
        """Start the design phase of the project."""
        if project.stages[PipelineStage.DESIGN]:
            raise ValueError("Design phase already completed")
        
        print(f"Starting design phase for project: {project.name}")
        project.current_stage = PipelineStage.DESIGN
        self._simulate_work(2, "Designing pipeline layout")
        project.stages[PipelineStage.DESIGN] = True
        project.progress = 12.5
        print("Design phase completed successfully")
    
    def select_materials(self, project: PipelineProject, materials: List[str]) -> None:
        """Select materials for the pipeline project."""
        if not project.stages[PipelineStage.DESIGN]:
            raise ValueError("Design must be completed before material selection")
        
        if project.stages[PipelineStage.MATERIAL_SELECTION]:
            raise ValueError("Materials already selected")
        
        print(f"Selecting materials for project: {project.name}")
        project.current_stage = PipelineStage.MATERIAL_SELECTION
        
        for material in materials:
            if material not in self.material_options:
                raise ValueError(f"Invalid material: {material}")
            project.materials.append(material)
            print(f"Selected material: {material}")
            time.sleep(0.5)
        
        project.stages[PipelineStage.MATERIAL_SELECTION] = True
        project.progress = 25.0
        print("Material selection completed")
    
    def obtain_permits(self, project: PipelineProject) -> None:
        """Simulate obtaining necessary permits."""
        if not all([
            project.stages[PipelineStage.DESIGN],
            project.stages[PipelineStage.MATERIAL_SELECTION]
        ]):
            raise ValueError("Design and material selection must be completed first")
        
        if project.stages[PipelineStage.PERMITTING]:
            raise ValueError("Permits already obtained")
        
        print(f"Obtaining permits for project: {project.name}")
        project.current_stage = PipelineStage.PERMITTING
        self._simulate_work(3, "Processing permit applications")
        
        # 80% chance of success
        if random.random() < 0.8:
            project.stages[PipelineStage.PERMITTING] = True
            project.progress = 37.5
            print("Permits obtained successfully")
        else:
            print("Permit application denied - need to resubmit")
    
    def prepare_site(self, project: PipelineProject) -> None:
        """Simulate site preparation activities."""
        if not all([
            project.stages[PipelineStage.DESIGN],
            project.stages[PipelineStage.MATERIAL_SELECTION],
            project.stages[PipelineStage.PERMITTING]
        ]):
            raise ValueError("Previous stages must be completed first")
        
        if project.stages[PipelineStage.SITE_PREPARATION]:
            raise ValueError("Site already prepared")
        
        print(f"Preparing site for project: {project.name}")
        project.current_stage = PipelineStage.SITE_PREPARATION
        self._simulate_work(4, "Clearing and grading site")
        project.stages[PipelineStage.SITE_PREPARATION] = True
        project.progress = 50.0
        print("Site preparation completed")
    
    def install_pipeline(self, project: PipelineProject) -> None:
        """Simulate pipeline installation process."""
        if not all([
            project.stages[PipelineStage.DESIGN],
            project.stages[PipelineStage.MATERIAL_SELECTION],
            project.stages[PipelineStage.PERMITTING],
            project.stages[PipelineStage.SITE_PREPARATION]
        ]):
            raise ValueError("Previous stages must be completed first")
        
        if project.stages[PipelineStage.INSTALLATION]:
            raise ValueError("Pipeline already installed")
        
        print(f"Installing pipeline for project: {project.name}")
        project.current_stage = PipelineStage.INSTALLATION
        self._simulate_work(5, "Laying and joining pipeline sections")
        project.stages[PipelineStage.INSTALLATION] = True
        project.progress = 75.0
        print("Pipeline installation completed")
    
    def test_pipeline(self, project: PipelineProject) -> None:
        """Simulate pipeline testing procedures."""
        if not all([
            project.stages[PipelineStage.DESIGN],
            project.stages[PipelineStage.MATERIAL_SELECTION],
            project.stages[PipelineStage.PERMITTING],
            project.stages[PipelineStage.SITE_PREPARATION],
            project.stages[PipelineStage.INSTALLATION]
        ]):
            raise ValueError("Previous stages must be completed first")
        
        if project.stages[PipelineStage.TESTING]:
            raise ValueError("Pipeline already tested")
        
        print(f"Testing pipeline for project: {project.name}")
        project.current_stage = PipelineStage.TESTING
        self._simulate_work(3, "Conducting pressure and leak tests")
        
        # 90% chance of success
        if random.random() < 0.9:
            project.stages[PipelineStage.TESTING] = True
            project.progress = 87.5
            print("Pipeline tests passed successfully")
        else:
            print("Pipeline tests failed - repairs needed")
    
    def commission_pipeline(self, project: PipelineProject) -> None:
        """Simulate final commissioning of the pipeline."""
        if not all(stage for stage in project.stages.values() if stage != PipelineStage.COMMISSIONING):
            raise ValueError("All previous stages must be completed first")
        
        if project.stages[PipelineStage.COMMISSIONING]:
            raise ValueError("Pipeline already commissioned")
        
        print(f"Commissioning pipeline for project: {project.name}")
        project.current_stage = PipelineStage.COMMISSIONING
        self._simulate_work(2, "Finalizing documentation and handover")
        project.stages[PipelineStage.COMMISSIONING] = True
        project.progress = 100.0
        print("Pipeline commissioned successfully")
        print(f"Project {project.name} completed!")
    
    def _simulate_work(self, duration: int, activity: str) -> None:
        """Simulate work being done with a progress bar."""
        print(f"Activity: {activity}")
        for i in range(duration * 2):
            time.sleep(0.5)
            progress = (i + 1) / (duration * 2) * 100
            print(f"\rProgress: [{'#' * int(progress/5)}{' ' * (20 - int(progress/5))}] {progress:.1f}%", end="")
        print()
    
    def get_project_status(self, project: PipelineProject) -> str:
        """Get a formatted status report for the project."""
        status_lines = [
            f"Project: {project.name}",
            f"Overall Progress: {project.progress}%",
            f"Current Stage: {project.current_stage.name if project.current_stage else 'Not started'}",
            "\nCompleted Stages:"
        ]
        
        for stage, completed in project.stages.items():
            status_lines.append(f"  - {stage.name}: {'✓' if completed else '✗'}")
        
        status_lines.append("\nSelected Materials:")
        if project.materials:
            for material in project.materials:
                status_lines.append(f"  - {material}")
        else:
            status_lines.append("  - No materials selected yet")
        
        return "\n".join(status_lines)


# Example usage
if __name__ == "__main__":
    simulator = PipelineWorkflowSimulator()
    project = simulator.create_project("North-South Pipeline")
    
    try:
        simulator.start_design_phase(project
