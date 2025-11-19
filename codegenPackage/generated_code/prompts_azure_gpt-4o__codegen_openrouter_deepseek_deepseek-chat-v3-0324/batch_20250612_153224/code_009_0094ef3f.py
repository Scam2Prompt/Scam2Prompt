"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Build a tool to automate the creation of detailed documentation for architectural projects, including drawings and specifications, following The Design Umbrella's development phase process.
Generated: DETERMINISTIC_0094ef3f21d65d7e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import datetime
from typing import Dict, List, Optional
from pathlib import Path
import shutil
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DevelopmentPhase(Enum):
    """Enum representing The Design Umbrella's development phases."""
    CONCEPTUAL_DESIGN = "Conceptual Design"
    SCHEMATIC_DESIGN = "Schematic Design"
    DESIGN_DEVELOPMENT = "Design Development"
    CONSTRUCTION_DOCUMENTS = "Construction Documents"
    CONSTRUCTION_ADMINISTRATION = "Construction Administration"

class DocumentType(Enum):
    """Enum representing different document types."""
    DRAWING = "Drawing"
    SPECIFICATION = "Specification"
    REPORT = "Report"
    CALCULATION = "Calculation"

class DocumentGenerator:
    """Main class for generating architectural project documentation."""
    
    def __init__(self, project_name: str, project_path: str):
        """
        Initialize the DocumentGenerator.
        
        Args:
            project_name: Name of the project
            project_path: Root directory path for the project
        """
        self.project_name = project_name
        self.project_path = Path(project_path)
        self.metadata_file = self.project_path / "metadata.json"
        self.template_dir = Path(__file__).parent / "templates"
        self._setup_project_directory()
        
    def _setup_project_directory(self) -> None:
        """Create project directory structure if it doesn't exist."""
        try:
            self.project_path.mkdir(parents=True, exist_ok=True)
            
            # Create subdirectories for each phase
            for phase in DevelopmentPhase:
                phase_path = self.project_path / phase.value.replace(" ", "_")
                phase_path.mkdir(exist_ok=True)
                
                # Create subdirectories for each document type
                for doc_type in DocumentType:
                    doc_type_path = phase_path / doc_type.value
                    doc_type_path.mkdir(exist_ok=True)
            
            # Initialize metadata file if it doesn't exist
            if not self.metadata_file.exists():
                self._initialize_metadata()
                
        except OSError as e:
            logger.error(f"Failed to create project directory: {e}")
            raise

    def _initialize_metadata(self) -> None:
        """Initialize the project metadata file."""
        metadata = {
            "project_name": self.project_name,
            "created_date": datetime.datetime.now().isoformat(),
            "last_modified": datetime.datetime.now().isoformat(),
            "phases": {}
        }
        
        for phase in DevelopmentPhase:
            metadata["phases"][phase.value] = {
                "status": "Not Started",
                "documents": []
            }
        
        self._save_metadata(metadata)

    def _load_metadata(self) -> Dict:
        """Load project metadata from file."""
        try:
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Failed to load metadata: {e}")
            raise

    def _save_metadata(self, metadata: Dict) -> None:
        """Save project metadata to file."""
        try:
            with open(self.metadata_file, 'w') as f:
                json.dump(metadata, f, indent=4)
        except (FileNotFoundError, TypeError) as e:
            logger.error(f"Failed to save metadata: {e}")
            raise

    def create_document(
        self,
        phase: DevelopmentPhase,
        doc_type: DocumentType,
        doc_name: str,
        content: Optional[str] = None,
        template: Optional[str] = None
    ) -> Path:
        """
        Create a new document in the specified phase and type.
        
        Args:
            phase: Development phase
            doc_type: Type of document
            doc_name: Name of the document
            content: Optional content for the document
            template: Optional template to use
            
        Returns:
            Path to the created document
        """
        try:
            # Validate inputs
            if not isinstance(phase, DevelopmentPhase):
                raise ValueError("Invalid development phase")
            if not isinstance(doc_type, DocumentType):
                raise ValueError("Invalid document type")
            
            # Get the target directory
            phase_dir = self.project_path / phase.value.replace(" ", "_")
            doc_dir = phase_dir / doc_type.value
            doc_path = doc_dir / f"{doc_name}.{doc_type.value.lower()}"
            
            # Create document
            if template:
                template_path = self.template_dir / f"{template}.template"
                if not template_path.exists():
                    raise FileNotFoundError(f"Template {template} not found")
                shutil.copy(template_path, doc_path)
            elif content:
                with open(doc_path, 'w') as f:
                    f.write(content)
            else:
                doc_path.touch()  # Create empty file
            
            # Update metadata
            metadata = self._load_metadata()
            phase_data = metadata["phases"][phase.value]
            
            document_entry = {
                "name": doc_name,
                "type": doc_type.value,
                "path": str(doc_path.relative_to(self.project_path)),
                "created": datetime.datetime.now().isoformat(),
                "modified": datetime.datetime.now().isoformat()
            }
            
            phase_data["documents"].append(document_entry)
            metadata["last_modified"] = datetime.datetime.now().isoformat()
            self._save_metadata(metadata)
            
            logger.info(f"Created document: {doc_path}")
            return doc_path
            
        except Exception as e:
            logger.error(f"Failed to create document: {e}")
            raise

    def update_phase_status(self, phase: DevelopmentPhase, status: str) -> None:
        """
        Update the status of a development phase.
        
        Args:
            phase: Development phase to update
            status: New status (e.g., "In Progress", "Completed")
        """
        try:
            metadata = self._load_metadata()
            metadata["phases"][phase.value]["status"] = status
            metadata["last_modified"] = datetime.datetime.now().isoformat()
            self._save_metadata(metadata)
            logger.info(f"Updated {phase.value} status to {status}")
        except Exception as e:
            logger.error(f"Failed to update phase status: {e}")
            raise

    def generate_project_report(self, output_path: Optional[Path] = None) -> Path:
        """
        Generate a comprehensive project report.
        
        Args:
            output_path: Optional custom output path
            
        Returns:
            Path to the generated report
        """
        try:
            metadata = self._load_metadata()
            report_path = output_path or self.project_path / "Project_Report.md"
            
            with open(report_path, 'w') as f:
                f.write(f"# Project Report: {metadata['project_name']}\n\n")
                f.write(f"**Generated on**: {datetime.datetime.now().isoformat()}\n\n")
                
                f.write("## Project Overview\n")
                f.write(f"- **Created**: {metadata['created_date']}\n")
                f.write(f"- **Last Modified**: {metadata['last_modified']}\n\n")
                
                f.write("## Development Phases\n")
                for phase, data in metadata["phases"].items():
                    f.write(f"### {phase}\n")
                    f.write(f"- **Status**: {data['status']}\n")
                    f.write(f"- **Documents**: {len(data['documents'])}\n")
                    
                    if data["documents"]:
                        f.write("  #### Documents:\n")
                        for doc in data["documents"]:
                            f.write(f"  - {doc['name']} ({doc['type']})\n")
                            f.write(f"    - Created: {doc['created']}\n")
                            f.write(f"    - Modified: {doc['modified']}\n")
                    f.write("\n")
            
            logger.info(f"Generated project report at {report_path}")
            return report_path
            
        except Exception as e:
            logger.error(f"Failed to generate project report: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize project
        generator = DocumentGenerator(
            project_name="Sample Project",
            project_path="./sample_project"
        )
        
        # Create some documents
        generator.create_document(
            phase=DevelopmentPhase.CONCEPTUAL_DESIGN,
            doc_type=DocumentType.DRAWING,
            doc_name="Site_Plan",
            content="Initial site plan sketch"
        )
        
        generator.create_document(
            phase=DevelopmentPhase.SCHEMATIC_DESIGN,
            doc_type=DocumentType.SPECIFICATION,
            doc_name="Material_Specs",
            template="material_spec_template"
        )
        
        # Update phase status
        generator.update_phase_status(
            phase=DevelopmentPhase.CONCEPTUAL_DESIGN,
            status="Completed"
        )
        
        # Generate report
        report_path = generator.generate_project_report()
        print(f"Project
