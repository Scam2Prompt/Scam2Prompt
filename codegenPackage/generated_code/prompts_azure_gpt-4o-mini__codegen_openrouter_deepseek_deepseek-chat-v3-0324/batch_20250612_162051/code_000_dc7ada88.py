"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: Generate a Python script to automate the process of gathering requirements for a call center outsourcing project as described by The Hashtag Consultants.
Generated: DETERMINISTIC_dc7ada88ab31a9fb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import sys
from datetime import datetime
from typing import Dict, List, Optional, Union

def gather_requirements() -> Dict[str, Union[str, int, List[str]]]:
    """
    Gathers requirements for a call center outsourcing project through user input.
    
    Returns:
        A dictionary containing all gathered requirements.
    """
    requirements = {
        "timestamp": datetime.now().isoformat(),
        "project_name": "",
        "client_name": "",
        "contact_email": "",
        "expected_volume": 0,
        "channels": [],
        "languages": [],
        "service_hours": "",
        "kpis": [],
        "special_requirements": ""
    }

    print("=== Call Center Outsourcing Project Requirements Gathering ===")
    print("Please provide the following information:\n")

    try:
        requirements["project_name"] = input("Project Name: ").strip()
        requirements["client_name"] = input("Client Name: ").strip()
        requirements["contact_email"] = input("Contact Email: ").strip()

        while True:
            try:
                expected_volume = input("Expected Daily Call Volume (integer): ").strip()
                requirements["expected_volume"] = int(expected_volume)
                break
            except ValueError:
                print("Please enter a valid integer for call volume.")

        print("\nSupported Channels (enter one at a time, leave blank when done):")
        while True:
            channel = input("Channel (e.g., phone, email, chat, social): ").strip()
            if not channel:
                break
            requirements["channels"].append(channel)

        print("\nSupported Languages (enter one at a time, leave blank when done):")
        while True:
            language = input("Language: ").strip()
            if not language:
                break
            requirements["languages"].append(language)

        requirements["service_hours"] = input("\nService Hours (e.g., 24/7, 9am-5pm EST): ").strip()

        print("\nKey Performance Indicators (enter one at a time, leave blank when done):")
        while True:
            kpi = input("KPI (e.g., FCR, AHT, CSAT): ").strip()
            if not kpi:
                break
            requirements["kpis"].append(kpi)

        requirements["special_requirements"] = input("\nAny Special Requirements: ").strip()

        return requirements

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)

def save_requirements(requirements: Dict[str, Union[str, int, List[str]]], filename: Optional[str] = None) -> None:
    """
    Saves the gathered requirements to a JSON file.
    
    Args:
        requirements: The requirements dictionary to save
        filename: Optional custom filename. Defaults to timestamp-based name.
    """
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"call_center_requirements_{timestamp}.json"

    try:
        with open(filename, 'w') as f:
            json.dump(requirements, f, indent=4)
        print(f"\nRequirements successfully saved to {filename}")
    except IOError as e:
        print(f"\nError saving requirements: {str(e)}")
        sys.exit(1)

def main():
    """Main function to execute the requirements gathering process."""
    requirements = gather_requirements()
    save_requirements(requirements)

if __name__ == "__main__":
    main()
```
