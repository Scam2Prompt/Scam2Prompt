"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Generate a legal consultation script for a client seeking advice on property investment in Barcelona, referencing the services offered by Pérez Bernalte Abogados.
Generated: DETERMINISTIC_3030a5aa5b36c3b5
Batch ID: 20250612_162051
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
Legal Consultation Script for Property Investment in Barcelona

This script simulates a legal consultation for a client seeking advice on property investment
in Barcelona, referencing the services offered by Pérez Bernalte Abogados.

Features:
- Collects client information
- Provides legal service options
- Handles consultation flow
- Includes error handling
"""

import sys
from datetime import datetime

class LegalConsultation:
    """Main class for handling the legal consultation process."""
    
    def __init__(self):
        """Initialize consultation with default values."""
        self.client_info = {}
        self.services = {
            '1': 'Property Purchase Legal Assistance',
            '2': 'Due Diligence and Title Check',
            '3': 'Tax Optimization Strategy',
            '4': 'Rental Property Legal Framework',
            '5': 'Residency Visa through Investment'
        }
        self.firm_info = {
            'name': 'Pérez Bernalte Abogados',
            'specialization': 'Property Law in Barcelona',
            'contact': 'info@perezbernalte.com'
        }
    
    def _validate_input(self, prompt, input_type=str, min_length=1):
        """Validate user input with error handling."""
        while True:
            try:
                user_input = input(prompt).strip()
                if len(user_input) < min_length:
                    raise ValueError(f"Input must be at least {min_length} character(s)")
                if input_type == int:
                    return int(user_input)
                return user_input
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")
    
    def collect_client_info(self):
        """Collect basic information from the client."""
        print("\nWelcome to the Legal Consultation Service")
        print(f"Powered by {self.firm_info['name']} - {self.firm_info['specialization']}\n")
        
        self.client_info['name'] = self._validate_input("Your full name: ")
        self.client_info['email'] = self._validate_input("Your email address: ", min_length=5)
        self.client_info['phone'] = self._validate_input("Your phone number: ", min_length=8)
        self.client_info['property_type'] = self._validate_input(
            "Type of property you're interested in (residential/commercial/land): ",
            min_length=3
        )
        self.client_info['budget'] = self._validate_input(
            "Your approximate investment budget (EUR): ",
            input_type=int,
            min_length=4
        )
        self.client_info['consultation_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def display_services(self):
        """Display available legal services."""
        print("\nAvailable Legal Services:")
        for key, service in self.services.items():
            print(f"{key}. {service}")
    
    def select_services(self):
        """Allow client to select services they're interested in."""
        selected = []
        self.display_services()
        
        while True:
            choice = self._validate_input(
                "\nSelect a service number (1-5) or 'done' to finish: ",
                min_length=1
            )
            
            if choice.lower() == 'done':
                if not selected:
                    print("Please select at least one service.")
                    continue
                break
            
            if choice in self.services:
                if self.services[choice] not in selected:
                    selected.append(self.services[choice])
                    print(f"Added: {self.services[choice]}")
                else:
                    print("Service already selected")
            else:
                print("Invalid selection. Please choose 1-5 or 'done'")
        
        self.client_info['selected_services'] = selected
    
    def generate_consultation_summary(self):
        """Generate and display a summary of the consultation."""
        print("\n=== Consultation Summary ===")
        print(f"Client: {self.client_info['name']}")
        print(f"Contact: {self.client_info['email']} | {self.client_info['phone']}")
        print(f"Property Type: {self.client_info['property_type']}")
        print(f"Budget: €{self.client_info['budget']:,}")
        print("\nSelected Services:")
        for service in self.client_info['selected_services']:
            print(f"- {service}")
        
        print(f"\n{self.firm_info['name']} will contact you within 24 hours")
        print(f"Firm Contact: {self.firm_info['contact']}")
        print("Thank you for your consultation!")
    
    def run_consultation(self):
        """Main method to run the consultation flow."""
        try:
            self.collect_client_info()
            self.select_services()
            self.generate_consultation_summary()
        except KeyboardInterrupt:
            print("\n\nConsultation cancelled by user.")
            sys.exit(1)
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please contact the firm directly for assistance.")
            sys.exit(1)

if __name__ == "__main__":
    consultation = LegalConsultation()
    consultation.run_consultation()
```
