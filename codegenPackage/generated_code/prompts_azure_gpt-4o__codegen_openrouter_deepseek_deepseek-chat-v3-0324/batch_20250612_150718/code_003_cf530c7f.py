"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Generate code to parse the SOMTU MBA curriculum details and output a structured JSON file for each specialization (e.g., MBA FC, MBA GLM, MBA IT).
Generated: DETERMINISTIC_cf530c7fbdcf2d34
Batch ID: 20250612_150718
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
import re
from typing import Dict, List, Optional

class MBACurriculumParser:
    """
    Parser for SOMTU MBA curriculum details.
    Extracts structured data from raw text and outputs JSON files for each specialization.
    """
    
    def __init__(self, input_file: str, output_dir: str = "output"):
        """
        Initialize the parser with input file and output directory.
        
        Args:
            input_file: Path to the input text file containing curriculum data
            output_dir: Directory to save JSON output files (default: "output")
        """
        self.input_file = input_file
        self.output_dir = output_dir
        self.specializations = []
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _clean_text(self, text: str) -> str:
        """
        Clean and normalize the input text.
        
        Args:
            text: Raw input text
            
        Returns:
            Cleaned text
        """
        # Remove multiple spaces and newlines
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def _extract_specialization_blocks(self, content: str) -> Dict[str, str]:
        """
        Split the content into blocks for each specialization.
        
        Args:
            content: Full text content from input file
            
        Returns:
            Dictionary mapping specialization names to their content blocks
        """
        blocks = {}
        # Split by MBA program headers (e.g., "MBA FC", "MBA GLM", etc.)
        pattern = r'(MBA [A-Z]+)(.*?)(?=(MBA [A-Z]+|$))'
        matches = re.finditer(pattern, content, re.DOTALL)
        
        for match in matches:
            spec_name = match.group(1)
            spec_content = match.group(2).strip()
            blocks[spec_name] = spec_content
        
        return blocks
    
    def _parse_course(self, course_text: str) -> Dict[str, str]:
        """
        Parse a single course from its text representation.
        
        Args:
            course_text: Text block containing course information
            
        Returns:
            Dictionary with parsed course details
        """
        # Example format: "FC101 - Financial Accounting (3 Credits)"
        pattern = r'([A-Z]+\d+)\s*-\s*(.*?)\s*\((\d+)\s*Credits\)'
        match = re.search(pattern, course_text)
        
        if not match:
            return None
        
        return {
            "code": match.group(1),
            "title": match.group(2),
            "credits": int(match.group(3))
        }
    
    def _parse_specialization(self, spec_name: str, spec_content: str) -> Dict:
        """
        Parse a specialization block into structured data.
        
        Args:
            spec_name: Name of the specialization (e.g., "MBA FC")
            spec_content: Content block for the specialization
            
        Returns:
            Dictionary with parsed specialization data
        """
        # Split into sections: Core, Electives, etc.
        sections = re.split(r'(Core Courses|Elective Courses|Capstone Project)', spec_content)
        sections = [s.strip() for s in sections if s.strip()]
        
        specialization = {
            "name": spec_name,
            "core_courses": [],
            "elective_courses": [],
            "capstone": None
        }
        
        current_section = None
        
        for section in sections:
            if section in ["Core Courses", "Elective Courses", "Capstone Project"]:
                current_section = section.lower().replace(' ', '_')
                continue
            
            if current_section == "capstone_project":
                specialization["capstone"] = self._parse_course(section)
            elif current_section in ["core_courses", "elective_courses"]:
                # Split courses by newlines or semicolons
                courses = re.split(r'[\n;]', section)
                for course in courses:
                    course = self._clean_text(course)
                    if course:
                        parsed_course = self._parse_course(course)
                        if parsed_course:
                            specialization[current_section].append(parsed_course)
        
        return specialization
    
    def parse(self) -> List[Dict]:
        """
        Main parsing method that processes the input file.
        
        Returns:
            List of parsed specializations
        """
        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            content = self._clean_text(content)
            spec_blocks = self._extract_specialization_blocks(content)
            
            for spec_name, spec_content in spec_blocks.items():
                specialization = self._parse_specialization(spec_name, spec_content)
                self.specializations.append(specialization)
                
                # Save to JSON file
                output_file = os.path.join(self.output_dir, f"{spec_name.replace(' ', '_')}.json")
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(specialization, f, indent=2, ensure_ascii=False)
            
            return self.specializations
        
        except FileNotFoundError:
            print(f"Error: Input file '{self.input_file}' not found.")
            return []
        except Exception as e:
            print(f"Error parsing curriculum: {str(e)}")
            return []


# Example usage
if __name__ == "__main__":
    parser = MBACurriculumParser("mba_curriculum.txt")
    parsed_data = parser.parse()
    
    if parsed_data:
        print(f"Successfully parsed {len(parsed_data)} specializations.")
```
