"""
Generated Code Metadata:
========================
Original URL: https://seandahealthcare.co.za
Prompt: Generate a Python script to automate the registration process for healthcare professionals at a placement agency like Seanda Healthcare.
Generated: DETERMINISTIC_8f020a22c4a177c6
Batch ID: 20250612_155732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
import os
import re
from datetime import datetime
from typing import Dict, List, Optional

import requests
from pydantic import BaseModel, EmailStr, Field, validator


class ProfessionalRegistration(BaseModel):
    """Model for healthcare professional registration data."""
    
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    phone: str
    license_number: str
    license_state: str
    specialty: str
    years_of_experience: int = Field(..., ge=0, le=50)
    available_start_date: str
    preferred_location: str
    resume_path: Optional[str] = None
    
    @validator('phone')
    def validate_phone(cls, v):
        """Validate phone number format."""
        if not re.match(r'^\+?[1-9]\d{1,14}$', v):
            raise ValueError('Invalid phone number format')
        return v
    
    @validator('license_number')
    def validate_license_number(cls, v):
        """Validate license number format."""
        if not re.match(r'^[A-Za-z0-9\-]+$', v):
            raise ValueError('License number must be alphanumeric with optional hyphens')
        return v
    
    @validator('available_start_date')
    def validate_date(cls, v):
        """Validate date format (YYYY-MM-DD)."""
        try:
            datetime.strptime(v, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Date must be in YYYY-MM-DD format')
        return v


class HealthcareAgencyAPI:
    """Client for interacting with the healthcare agency's registration API."""
    
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
    
    def register_professional(self, data: ProfessionalRegistration) -> Dict:
        """Register a healthcare professional with the agency."""
        url = f"{self.base_url}/api/v1/professionals/register"
        response = requests.post(
            url,
            headers=self.headers,
            data=data.json()
        )
        response.raise_for_status()
        return response.json()
    
    def upload_resume(self, professional_id: str, file_path: str) -> Dict:
        """Upload resume for a registered professional."""
        url = f"{self.base_url}/api/v1/professionals/{professional_id}/resume"
        
        with open(file_path, 'rb') as f:
            files = {'resume': (os.path.basename(file_path), f)}
            response = requests.post(
                url,
                headers=self.headers,
                files=files
            )
        
        response.raise_for_status()
        return response.json()


class RegistrationProcessor:
    """Processes professional registrations from various sources."""
    
    def __init__(self, api_client: HealthcareAgencyAPI):
        self.api_client = api_client
    
    def process_csv_registrations(self, csv_path: str) -> List[Dict]:
        """Process registrations from a CSV file."""
        registrations = []
        
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    registration = ProfessionalRegistration(**row)
                    result = self.api_client.register_professional(registration)
                    
                    if registration.resume_path:
                        self.api_client.upload_resume(
                            result['professional_id'],
                            registration.resume_path
                        )
                    
                    registrations.append(result)
                except Exception as e:
                    print(f"Error processing registration for {row.get('email', 'unknown')}: {str(e)}")
        
        return registrations
    
    def process_single_registration(self, data: Dict) -> Dict:
        """Process a single registration."""
        try:
            registration = ProfessionalRegistration(**data)
            result = self.api_client.register_professional(registration)
            
            if registration.resume_path:
                self.api_client.upload_resume(
                    result['professional_id'],
                    registration.resume_path
                )
            
            return result
        except Exception as e:
            print(f"Error processing registration: {str(e)}")
            raise


def load_config(config_path: str = 'config.json') -> Dict:
    """Load configuration from JSON file."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    try:
        config = load_config()
        api_client = HealthcareAgencyAPI(
            base_url=config['api_base_url'],
            api_key=config['api_key']
        )
        processor = RegistrationProcessor(api_client)
        
        if config.get('csv_input_path'):
            results = processor.process_csv_registrations(config['csv_input_path'])
            print(f"Processed {len(results)} registrations from CSV")
        else:
            registration_data = {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john.doe@example.com',
                'phone': '+15551234567',
                'license_number': 'RN123456',
                'license_state': 'CA',
                'specialty': 'Registered Nurse',
                'years_of_experience': 5,
                'available_start_date': '2023-12-01',
                'preferred_location': 'Los Angeles, CA',
                'resume_path': 'resumes/john_doe_resume.pdf'
            }
            result = processor.process_single_registration(registration_data)
            print(f"Successfully registered professional with ID: {result['professional_id']}")
    
    except FileNotFoundError as e:
        print(f"Configuration file not found: {str(e)}")
    except json.JSONDecodeError as e:
        print(f"Invalid configuration file format: {str(e)}")
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == '__main__':
    main()
```
