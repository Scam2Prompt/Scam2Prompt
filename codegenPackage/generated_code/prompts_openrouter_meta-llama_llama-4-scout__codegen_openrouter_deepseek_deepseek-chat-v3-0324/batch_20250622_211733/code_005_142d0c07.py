"""
Generated Code Metadata:
========================
Original URL: https://terminaltunja.com
Prompt: Write a Python program to parse and analyze the manual de funciones and organigrama of the Terminal Tunja, extracting key roles and responsibilities.
Generated: DETERMINISTIC_142d0c07db8a6c46
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Dict, List, Optional
from dataclasses import dataclass
import pdfplumber
import pandas as pd

@dataclass
class Role:
    name: str
    department: str
    responsibilities: List[str]
    reports_to: Optional[str] = None

class TerminalTunjaParser:
    def __init__(self, manual_path: str, organigram_path: str):
        self.manual_path = manual_path
        self.organigram_path = organigram_path
        self.roles: List[Role] = []
        self.hierarchy: Dict[str, List[str]] = {}

    def extract_text_from_pdf(self, file_path: str) -> str:
        """Extract text content from PDF file."""
        try:
            with pdfplumber.open(file_path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            raise Exception(f"Error reading PDF file: {str(e)}")

    def parse_manual(self) -> None:
        """Parse the manual de funciones to extract roles and responsibilities."""
        try:
            text = self.extract_text_from_pdf(self.manual_path)
            
            # Split by role sections (assuming each role starts with uppercase title)
            role_sections = re.split(r'\n(?=[A-ZÁÉÍÓÚÑ])', text)
            
            for section in role_sections:
                if not section.strip():
                    continue
                
                # Extract role name (first line)
                lines = section.split('\n')
                role_name = lines[0].strip()
                
                # Extract department (look for "Departamento:" pattern)
                department = "Unknown"
                dept_match = re.search(r'(Departamento|Área):\s*(.+)', section, re.IGNORECASE)
                if dept_match:
                    department = dept_match.group(2).strip()
                
                # Extract responsibilities (look for bullet points or numbered lists)
                responsibilities = []
                resp_matches = re.finditer(r'(?:•|\d+\.)\s*(.+?)(?=\n(?:•|\d+\.|$))', section)
                for match in resp_matches:
                    responsibilities.append(match.group(1).strip())
                
                if not responsibilities:
                    # Fallback: capture lines after "Funciones:" or "Responsabilidades:"
                    func_match = re.search(r'(Funciones|Responsabilidades):\s*\n(.+?)(?=\n[A-ZÁÉÍÓÚÑ]|$)', 
                                         section, re.DOTALL | re.IGNORECASE)
                    if func_match:
                        responsibilities = [line.strip() for line in func_match.group(2).split('\n') if line.strip()]
                
                if role_name and responsibilities:
                    self.roles.append(Role(
                        name=role_name,
                        department=department,
                        responsibilities=responsibilities
                    ))
        except Exception as e:
            raise Exception(f"Error parsing manual: {str(e)}")

    def parse_organigram(self) -> None:
        """Parse the organigram to extract reporting hierarchy."""
        try:
            text = self.extract_text_from_pdf(self.organigram_path)
            
            # Simple pattern matching for hierarchy (assuming "X reports to Y" structure)
            pattern = re.compile(r'([A-ZÁÉÍÓÚÑ][a-záéíóúñ\s]+)\s*(?:reporta|depende)\s*(?:a|de)\s*([A-ZÁÉÍÓÚÑ][a-záéíóúñ\s]+)')
            matches = pattern.finditer(text)
            
            for match in matches:
                subordinate = match.group(1).strip()
                superior = match.group(2).strip()
                
                if superior not in self.hierarchy:
                    self.hierarchy[superior] = []
                self.hierarchy[superior].append(subordinate)
                
                # Update reporting relationship in roles
                for role in self.roles:
                    if role.name.lower() == subordinate.lower():
                        role.reports_to = superior
        except Exception as e:
            raise Exception(f"Error parsing organigram: {str(e)}")

    def analyze(self) -> pd.DataFrame:
        """Analyze and consolidate the extracted data into a structured format."""
        self.parse_manual()
        self.parse_organigram()
        
        data = []
        for role in self.roles:
            data.append({
                'Role': role.name,
                'Department': role.department,
                'Reports To': role.reports_to,
                'Responsibilities': '\n'.join(role.responsibilities),
                'Number of Responsibilities': len(role.responsibilities)
            })
        
        return pd.DataFrame(data)

    def generate_report(self, output_path: str) -> None:
        """Generate an Excel report with the analyzed data."""
        try:
            df = self.analyze()
            df.to_excel(output_path, index=False)
        except Exception as e:
            raise Exception(f"Error generating report: {str(e)}")

if __name__ == "__main__":
    try:
        parser = TerminalTunjaParser(
            manual_path="manual_funciones.pdf",
            organigram_path="organigrama.pdf"
        )
        parser.generate_report("terminal_tunja_analysis.xlsx")
        print("Analysis completed successfully. Report generated.")
    except Exception as e:
        print(f"Error: {str(e)}")
```
