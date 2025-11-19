"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Write a script to automate the generation of study guides tailored to specific admission exams, referencing the "Biblioteca de estudio en casa" concept from Educar Comitán's site.
Generated: DETERMINISTIC_e3aebdf0c7af2c3d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Study Guide Generator for Admission Exams
Automates the creation of personalized study guides based on exam requirements.
References the "Biblioteca de estudio en casa" concept from Educar Comitán.
"""

import os
import json
import random
import argparse
from datetime import datetime
from typing import Dict, List, Optional

# Constants
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "study_guides"
RESOURCES_FILE = "resources.json"
DEFAULT_EXAM = "general"

class StudyGuideGenerator:
    """Generates personalized study guides for admission exams."""
    
    def __init__(self):
        self.resources = self._load_resources()
        self.ensure_directories()
        
    def ensure_directories(self) -> None:
        """Ensure required directories exist."""
        os.makedirs(TEMPLATE_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
    def _load_resources(self) -> Dict:
        """Load study resources from JSON file."""
        try:
            with open(RESOURCES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Resources file '{RESOURCES_FILE}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in '{RESOURCES_FILE}'.")
    
    def get_exam_topics(self, exam_type: str) -> List[str]:
        """Get topics for specified exam type."""
        if exam_type not in self.resources["exams"]:
            raise ValueError(f"Exam type '{exam_type}' not supported.")
        return self.resources["exams"][exam_type]
    
    def select_resources(self, topics: List[str], count: int = 5) -> Dict[str, List[str]]:
        """Select random resources for each topic."""
        selected = {}
        for topic in topics:
            if topic not in self.resources["materials"]:
                continue
            materials = self.resources["materials"][topic]
            selected[topic] = random.sample(materials, min(count, len(materials)))
        return selected
    
    def generate_guide(self, exam_type: str, student_name: str, output_format: str = "txt") -> str:
        """Generate a personalized study guide."""
        try:
            topics = self.get_exam_topics(exam_type)
            resources = self.select_resources(topics)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{OUTPUT_DIR}/{student_name}_{exam_type}_{timestamp}.{output_format}"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Study Guide for: {student_name}\n")
                f.write(f"Exam Type: {exam_type.upper()}\n")
                f.write("=" * 50 + "\n\n")
                
                for topic, materials in resources.items():
                    f.write(f"TOPIC: {topic.upper()}\n")
                    f.write("-" * 50 + "\n")
                    for i, material in enumerate(materials, 1):
                        f.write(f"{i}. {material}\n")
                    f.write("\n")
                
                f.write("\nGood luck with your studies!\n")
                f.write("Reference: Biblioteca de estudio en casa - Educar Comitán\n")
            
            return filename
        except Exception as e:
            raise RuntimeError(f"Failed to generate study guide: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Generate personalized study guides for admission exams.")
    parser.add_argument("--name", required=True, help="Student name")
    parser.add_argument("--exam", default=DEFAULT_EXAM, help="Exam type (default: general)")
    parser.add_argument("--format", choices=["txt", "md"], default="txt", help="Output format")
    
    args = parser.parse_args()
    
    try:
        generator = StudyGuideGenerator()
        output_file = generator.generate_guide(args.exam, args.name, args.format)
        print(f"Successfully generated study guide: {output_file}")
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
```
