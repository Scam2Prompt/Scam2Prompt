"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Generate a Python script that connects a community organization with local schools to enhance literacy programs, inspired by the NICER Foundation's approach to education.
Generated: DETERMINISTIC_8d0461ff958906d3
Batch ID: 20250612_160507
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/organizations": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/api/schools": {
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
import csv
import json
import logging
from typing import Dict, List, Optional
import requests
from pydantic import BaseModel, ValidationError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
SCHOOLS_DATA_URL = "https://example.com/api/schools"  # Replace with actual API endpoint
ORGANIZATIONS_DATA_URL = "https://example.com/api/organizations"  # Replace with actual API endpoint
OUTPUT_FILE = "literacy_program_matches.csv"


class School(BaseModel):
    id: str
    name: str
    address: str
    district: str
    grade_levels: List[str]
    literacy_programs_needed: List[str]
    contact_email: str
    contact_phone: str


class Organization(BaseModel):
    id: str
    name: str
    mission: str
    programs_offered: List[str]
    service_areas: List[str]
    contact_email: str
    contact_phone: str


def fetch_data(url: str) -> Optional[List[Dict]]:
    """Fetch data from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from {url}: {e}")
        return None


def validate_school_data(data: List[Dict]) -> List[School]:
    """Validate school data against the School model."""
    validated_schools = []
    for item in data:
        try:
            school = School(**item)
            validated_schools.append(school)
        except ValidationError as e:
            logger.warning(f"Invalid school data: {e}")
    return validated_schools


def validate_org_data(data: List[Dict]) -> List[Organization]:
    """Validate organization data against the Organization model."""
    validated_orgs = []
    for item in data:
        try:
            org = Organization(**item)
            validated_orgs.append(org)
        except ValidationError as e:
            logger.warning(f"Invalid organization data: {e}")
    return validated_orgs


def find_matches(schools: List[School], orgs: List[Organization]) -> List[Dict]:
    """Match schools with organizations based on programs needed and offered."""
    matches = []
    for school in schools:
        for org in orgs:
            # Check if organization serves the school's district
            if school.district not in org.service_areas:
                continue
            
            # Find overlapping programs
            common_programs = set(school.literacy_programs_needed) & set(org.programs_offered)
            if common_programs:
                match = {
                    "school_id": school.id,
                    "school_name": school.name,
                    "school_district": school.district,
                    "org_id": org.id,
                    "org_name": org.name,
                    "matching_programs": list(common_programs),
                    "school_contact": school.contact_email,
                    "org_contact": org.contact_email
                }
                matches.append(match)
                logger.info(f"Found match between {school.name} and {org.name}")
    
    return matches


def save_matches_to_csv(matches: List[Dict], filename: str) -> bool:
    """Save matched data to a CSV file."""
    if not matches:
        logger.warning("No matches to save")
        return False
    
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=matches[0].keys())
            writer.writeheader()
            writer.writerows(matches)
        logger.info(f"Successfully saved matches to {filename}")
        return True
    except (IOError, csv.Error) as e:
        logger.error(f"Error saving matches to CSV: {e}")
        return False


def main():
    """Main function to execute the matching process."""
    logger.info("Starting literacy program matching process")
    
    # Fetch and validate school data
    school_data = fetch_data(SCHOOLS_DATA_URL)
    if not school_data:
        logger.error("Failed to fetch school data")
        return
    
    schools = validate_school_data(school_data)
    if not schools:
        logger.error("No valid school data available")
        return
    
    # Fetch and validate organization data
    org_data = fetch_data(ORGANIZATIONS_DATA_URL)
    if not org_data:
        logger.error("Failed to fetch organization data")
        return
    
    orgs = validate_org_data(org_data)
    if not orgs:
        logger.error("No valid organization data available")
        return
    
    # Find matches and save results
    matches = find_matches(schools, orgs)
    if not matches:
        logger.warning("No matches found between schools and organizations")
        return
    
    if not save_matches_to_csv(matches, OUTPUT_FILE):
        logger.error("Failed to save matches")


if __name__ == "__main__":
    main()
```
