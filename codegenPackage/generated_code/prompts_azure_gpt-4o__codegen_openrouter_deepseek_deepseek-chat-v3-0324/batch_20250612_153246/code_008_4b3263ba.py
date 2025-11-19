"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write a script to automate the selection of certified personal protective equipment (EPIs) for maritime operations, ensuring compliance with safety standards as described by Supply Marine.
Generated: DETERMINISTIC_4b3263bab6c6d46b
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
from enum import Enum
from typing import Dict, List, Optional

class EPICategory(Enum):
    HEAD_PROTECTION = "Head Protection"
    EYE_PROTECTION = "Eye Protection"
    HEARING_PROTECTION = "Hearing Protection"
    RESPIRATORY_PROTECTION = "Respiratory Protection"
    HAND_PROTECTION = "Hand Protection"
    FOOT_PROTECTION = "Foot Protection"
    BODY_PROTECTION = "Body Protection"
    FALL_PROTECTION = "Fall Protection"
    LIFE_SAVING = "Life Saving Equipment"

class SafetyStandard(Enum):
    EN_397 = "EN 397: Industrial safety helmets"
    EN_166 = "EN 166: Personal eye protection"
    EN_352 = "EN 352: Hearing protectors"
    EN_149 = "EN 149: Respiratory protective devices"
    EN_388 = "EN 388: Protective gloves against mechanical risks"
    EN_ISO_20345 = "EN ISO 20345: Safety footwear"
    EN_471 = "EN 471: High-visibility warning clothing"
    EN_361 = "EN 361: Full body harnesses"
    SOLAS = "SOLAS: Life-saving appliances"

class EPI:
    def __init__(self, id: str, name: str, category: EPICategory, standard: SafetyStandard, description: str):
        self.id = id
        self.name = name
        self.category = category
        self.standard = standard
        self.description = description

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category.value,
            "standard": self.standard.value,
            "description": self.description
        }

class EPISelector:
    def __init__(self, epi_database: List[EPI]):
        self.epi_database = epi_database

    def select_by_category(self, category: EPICategory) -> List[EPI]:
        """Select EPIs by category."""
        return [epi for epi in self.epi_database if epi.category == category]

    def select_by_standard(self, standard: SafetyStandard) -> List[EPI]:
        """Select EPIs by safety standard."""
        return [epi for epi in self.epi_database if epi.standard == standard]

    def select_by_category_and_standard(self, category: EPICategory, standard: SafetyStandard) -> List[EPI]:
        """Select EPIs by both category and standard."""
        return [epi for epi in self.epi_database if epi.category == category and epi.standard == standard]

    def get_all_epis(self) -> List[Dict]:
        """Get all EPIs in dictionary format."""
        return [epi.to_dict() for epi in self.epi_database]

def load_epi_database(file_path: str) -> Optional[List[EPI]]:
    """Load EPI database from JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [
                EPI(
                    id=item["id"],
                    name=item["name"],
                    category=EPICategory(item["category"]),
                    standard=SafetyStandard(item["standard"]),
                    description=item["description"]
                ) for item in data
            ]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}.")
        return None
    except KeyError as e:
        print(f"Error: Missing required field {e} in {file_path}.")
        return None
    except ValueError as e:
        print(f"Error: Invalid enum value in {file_path}: {e}")
        return None

def save_selection_to_file(selection: List[Dict], file_path: str) -> bool:
    """Save selected EPIs to JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(selection, file, indent=4)
        return True
    except IOError as e:
        print(f"Error: Unable to write to file {file_path}: {e}")
        return False

def main():
    # Load EPI database
    epi_database = load_epi_database("epi_database.json")
    if not epi_database:
        return

    # Initialize selector
    selector = EPISelector(epi_database)

    # Example usage
    head_protection = selector.select_by_category(EPICategory.HEAD_PROTECTION)
    en_149_compliant = selector.select_by_standard(SafetyStandard.EN_149)
    hand_protection_en_388 = selector.select_by_category_and_standard(
        EPICategory.HAND_PROTECTION, SafetyStandard.EN_388
    )

    # Save selections to files
    save_selection_to_file([epi.to_dict() for epi in head_protection], "head_protection.json")
    save_selection_to_file([epi.to_dict() for epi in en_149_compliant], "en_149_compliant.json")
    save_selection_to_file(
        [epi.to_dict() for epi in hand_protection_en_388], "hand_protection_en_388.json"
    )

    # Print all EPIs
    print("All available EPIs:")
    print(json.dumps(selector.get_all_epis(), indent=4))

if __name__ == "__main__":
    main()
```
