"""
Generated Code Metadata:
========================
Original URL: https://artahub.com
Prompt: Create a module for generating interactive educational content, such as quizzes, games, or simulations, using a tool like Articulate Storyline or Adobe Captivate, and write a script to export the content in a format compatible with an LMS.
Generated: DETERMINISTIC_d61516ab607f9c57
Batch ID: 20250622_210703
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2001/XMLSchema-instance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.adlnet.org/xsd/adlcp_v1p3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.imsglobal.org/xsd/imscp_v1p1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
"""
Module for generating interactive educational content and exporting to LMS-compatible formats.
Supports SCORM and xAPI (Tin Can) standards.
"""

import json
import zipfile
import os
from datetime import datetime
from typing import Dict, List, Optional, Union

class QuizQuestion:
    """Represents a single quiz question with possible answers."""
    
    def __init__(self, question_id: str, question_text: str, question_type: str):
        """
        Initialize a quiz question.
        
        Args:
            question_id: Unique identifier for the question
            question_text: The question text
            question_type: Type of question (multiple_choice, true_false, fill_in)
        """
        self.question_id = question_id
        self.question_text = question_text
        self.question_type = question_type
        self.answers = []
        self.correct_answer = None
    
    def add_answer(self, answer_id: str, answer_text: str, is_correct: bool = False):
        """Add an answer option to the question."""
        self.answers.append({
            'id': answer_id,
            'text': answer_text,
            'is_correct': is_correct
        })
        if is_correct:
            self.correct_answer = answer_id

class InteractiveContent:
    """Base class for interactive educational content."""
    
    def __init__(self, content_id: str, title: str, description: str = ""):
        """
        Initialize interactive content.
        
        Args:
            content_id: Unique identifier for the content
            title: Title of the content
            description: Description of the content
        """
        self.content_id = content_id
        self.title = title
        self.description = description
        self.created_at = datetime.now().isoformat()
        self.modified_at = self.created_at
    
    def update_modified_date(self):
        """Update the modified date to current timestamp."""
        self.modified_at = datetime.now().isoformat()

class Quiz(InteractiveContent):
    """Represents a quiz with multiple questions."""
    
    def __init__(self, content_id: str, title: str, description: str = ""):
        super().__init__(content_id, title, description)
        self.questions = []
    
    def add_question(self, question: QuizQuestion):
        """Add a question to the quiz."""
        self.questions.append(question)
        self.update_modified_date()

class Simulation(InteractiveContent):
    """Represents an interactive simulation."""
    
    def __init__(self, content_id: str, title: str, description: str = ""):
        super().__init__(content_id, title, description)
        self.scenes = []
    
    def add_scene(self, scene_id: str, scene_data: Dict):
        """Add a scene to the simulation."""
        self.scenes.append({
            'id': scene_id,
            'data': scene_data
        })
        self.update_modified_date()

class LMSExporter:
    """Handles exporting content to LMS-compatible formats."""
    
    SCORM_VERSION = "1.2"
    XAPI_VERSION = "1.0.0"
    
    def __init__(self, output_dir: str = "exports"):
        """
        Initialize the exporter.
        
        Args:
            output_dir: Directory to save exported files
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def export_scorm(self, content: InteractiveContent, package_name: str) -> str:
        """
        Export content as SCORM package.
        
        Args:
            content: The content to export
            package_name: Name for the output package
            
        Returns:
            Path to the created SCORM package
            
        Raises:
            ValueError: If content type is not supported
        """
        if not isinstance(content, (Quiz, Simulation)):
            raise ValueError("Unsupported content type for SCORM export")
        
        package_path = os.path.join(self.output_dir, f"{package_name}.zip")
        manifest = self._generate_scorm_manifest(content)
        
        with zipfile.ZipFile(package_path, 'w') as zipf:
            zipf.writestr("imsmanifest.xml", manifest)
            if isinstance(content, Quiz):
                quiz_data = self._generate_quiz_data(content)
                zipf.writestr("quiz_data.json", json.dumps(quiz_data))
            elif isinstance(content, Simulation):
                sim_data = self._generate_simulation_data(content)
                zipf.writestr("simulation_data.json", json.dumps(sim_data))
        
        return package_path
    
    def export_xapi(self, content: InteractiveContent, package_name: str) -> str:
        """
        Export content as xAPI package.
        
        Args:
            content: The content to export
            package_name: Name for the output package
            
        Returns:
            Path to the created xAPI package
        """
        package_path = os.path.join(self.output_dir, f"{package_name}_xapi.json")
        xapi_data = self._generate_xapi_data(content)
        
        with open(package_path, 'w') as f:
            json.dump(xapi_data, f, indent=2)
        
        return package_path
    
    def _generate_scorm_manifest(self, content: InteractiveContent) -> str:
        """Generate SCORM manifest XML."""
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{content.content_id}" 
           version="1.1"
           xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
           xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_v1p3"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <metadata>
        <schema>ADL SCORM</schema>
        <schemaversion>{self.SCORM_VERSION}</schemaversion>
        <adlcp:location>metadata.xml</adlcp:location>
    </metadata>
    <organizations default="{content.content_id}">
        <organization identifier="{content.content_id}">
            <title>{content.title}</title>
            <item identifier="ITEM-1" identifierref="RESOURCE-1">
                <title>{content.title}</title>
            </item>
        </organization>
    </organizations>
    <resources>
        <resource identifier="RESOURCE-1" type="webcontent" adlcp:scormType="sco">
            <file href="content.html"/>
        </resource>
    </resources>
</manifest>"""
    
    def _generate_quiz_data(self, quiz: Quiz) -> Dict:
        """Generate quiz data structure."""
        return {
            'id': quiz.content_id,
            'title': quiz.title,
            'description': quiz.description,
            'questions': [{
                'id': q.question_id,
                'text': q.question_text,
                'type': q.question_type,
                'answers': q.answers,
                'correct_answer': q.correct_answer
            } for q in quiz.questions]
        }
    
    def _generate_simulation_data(self, simulation: Simulation) -> Dict:
        """Generate simulation data structure."""
        return {
            'id': simulation.content_id,
            'title': simulation.title,
            'description': simulation.description,
            'scenes': simulation.scenes
        }
    
    def _generate_xapi_data(self, content: InteractiveContent) -> Dict:
        """Generate xAPI data structure."""
        return {
            'version': self.XAPI_VERSION,
            'id': content.content_id,
            'title': content.title,
            'description': content.description,
            'type': type(content).__name__.lower(),
            'created': content.created_at,
            'modified': content.modified_at
        }

# Example usage
if __name__ == "__main__":
    # Create a quiz
    quiz = Quiz("quiz1", "Python Basics Quiz", "Test your Python knowledge")
    
    q1 = QuizQuestion("q1", "What is Python?", "multiple_choice")
    q1.add_answer("a1", "A programming language", True)
    q1.add_answer("a2", "A snake")
    q1.add_answer("a3", "A type of coffee")
    quiz.add_question(q1)
    
    q2 = QuizQuestion("q2", "Python uses dynamic typing.", "true_false")
    q2.add_answer("a1", "True", True)
    q2.add_answer("a2", "False")
    quiz.add_question(q2)
    
    # Export to SCORM
    exporter = LMSExporter()
    scorm_path = exporter.export_scorm(quiz, "python_quiz")
    print(f"SCORM package created at: {scorm_path}")
    
    # Export to xAPI
    xapi_path = exporter.export_xapi(quiz, "python_quiz")
    print(f"xAPI package created at: {xapi_path}")
```
