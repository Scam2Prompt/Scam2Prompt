"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Develop a script using Python to organize and categorize legal cases into areas such as Direito Empresarial, Direito Civil, and Direito Tributário, as highlighted by the Complexo de Advocacia Adriano Geoffrey.
Generated: DETERMINISTIC_26069b5dfb4ba61d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# legal_case_categorizer.py

import os
import json
from enum import Enum
from typing import Dict, List

class LegalArea(Enum):
    """Enum for legal areas"""
    DIREITO_EMPRESARIAL = "Direito Empresarial"
    DIREITO_CIVIL = "Direito Civil"
    DIREITO_TRIBUTARIO = "Direito Tributário"
    UNKNOWN = "Unknown"

class LegalCase:
    """Class to represent a legal case"""
    def __init__(self, name: str, description: str, legal_area: LegalArea):
        self.name = name
        self.description = description
        self.legal_area = legal_area

class LegalCaseCategorizer:
    """Class to categorize legal cases"""
    def __init__(self, cases: List[Dict]):
        self.cases = cases
        self.categorized_cases = {
            LegalArea.DIREITO_EMPRESARIAL: [],
            LegalArea.DIREITO_CIVIL: [],
            LegalArea.DIREITO_TRIBUTARIO: [],
            LegalArea.UNKNOWN: []
        }

    def categorize(self):
        """Categorize legal cases"""
        for case in self.cases:
            name = case.get("name")
            description = case.get("description")
            keywords = case.get("keywords", [])

            if not name or not description:
                continue

            if self._is_empresarial(keywords):
                self.categorized_cases[LegalArea.DIREITO_EMPRESARIAL].append(LegalCase(name, description, LegalArea.DIREITO_EMPRESARIAL))
            elif self._is_civil(keywords):
                self.categorized_cases[LegalArea.DIREITO_CIVIL].append(LegalCase(name, description, LegalArea.DIREITO_CIVIL))
            elif self._is_tributario(keywords):
                self.categorized_cases[LegalArea.DIREITO_TRIBUTARIO].append(LegalCase(name, description, LegalArea.DIREITO_TRIBUTARIO))
            else:
                self.categorized_cases[LegalArea.UNKNOWN].append(LegalCase(name, description, LegalArea.UNKNOWN))

    def _is_empresarial(self, keywords: List[str]):
        """Check if case is related to Direito Empresarial"""
        empresarial_keywords = ["empresa", "contrato", "sociedade"]
        return any(keyword in keyword.lower() for keyword in empresarial_keywords)

    def _is_civil(self, keywords: List[str]):
        """Check if case is related to Direito Civil"""
        civil_keywords = ["pessoa", "direito", "obrigação"]
        return any(keyword in keyword.lower() for keyword in civil_keywords)

    def _is_tributario(self, keywords: List[str]):
        """Check if case is related to Direito Tributário"""
        tributario_keywords = ["imposto", "taxa", "contribuição"]
        return any(keyword in keyword.lower() for keyword in tributario_keywords)

    def save_to_json(self, output_file: str):
        """Save categorized cases to JSON file"""
        categorized_cases_json = []
        for area, cases in self.categorized_cases.items():
            area_json = {
                "area": area.value,
                "cases": [
                    {
                        "name": case.name,
                        "description": case.description
                    } for case in cases
                ]
            }
            categorized_cases_json.append(area_json)

        with open(output_file, "w") as f:
            json.dump(categorized_cases_json, f, indent=4)

def main():
    try:
        cases = [
            {"name": "Case 1", "description": "Description 1", "keywords": ["empresa", "contrato"]},
            {"name": "Case 2", "description": "Description 2", "keywords": ["pessoa", "direito"]},
            {"name": "Case 3", "description": "Description 3", "keywords": ["imposto", "taxa"]},
            {"name": "Case 4", "description": "Description 4", "keywords": []}
        ]

        categorizer = LegalCaseCategorizer(cases)
        categorizer.categorize()
        categorizer.save_to_json("categorized_cases.json")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
