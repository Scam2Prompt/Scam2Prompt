"""
Generated Code Metadata:
========================
Original URL: https://the-immediate-alora.com
Prompt: Draft a criminal complaint form in German for Anlagebetrug, referencing the contact information for local police stations as provided by the seized platform.
Generated: DETERMINISTIC_2c90d6933f80fa5d
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Criminal Complaint Form for Anlagebetrug (Investment Fraud) in German.
This form references local police station contact information from a seized platform.
"""

import json
from datetime import datetime

def generate_complaint_form(victim_info, fraud_details, police_stations):
    """
    Generates a criminal complaint form for Anlagebetrug in German.
    
    Args:
        victim_info (dict): Information about the victim (name, address, contact).
        fraud_details (dict): Details about the fraud (amount, description, platform).
        police_stations (list): List of police stations with contact information.
    
    Returns:
        str: Formatted criminal complaint form in German.
    """
    
    # Validate input data
    if not all(key in victim_info for key in ['name', 'address', 'contact']):
        raise ValueError("Victim info must include name, address, and contact")
    if not all(key in fraud_details for key in ['amount', 'description', 'platform']):
        raise ValueError("Fraud details must include amount, description, and platform")
    if not police_stations:
        raise ValueError("Police stations list cannot be empty")

    # Format the current date
    current_date = datetime.now().strftime("%d.%m.%Y")

    # Generate police station options
    police_options = "\n".join(
        f"[ ] {station['name']} - {station['address']} (Tel: {station['phone']})"
        for station in police_stations
    )

    # Create the complaint form
    form = f"""
==================================================
STRAFANZEIGE - ANLAGEBETRUG
==================================================

Datum: {current_date}

I. ANGABEN ZUR PERSON
---------------------
Name: {victim_info['name']}
Adresse: {victim_info['address']}
Telefon: {victim_info['contact']}

II. VORFALLSBESCHREIBUNG
------------------------
Betrugsplattform: {fraud_details['platform']}
Betrag: {fraud_details['amount']} EUR
Beschreibung:
{fraud_details['description']}

III. ZUSTÄNDIGE POLIZEIDIENSTSTELLE
-----------------------------------
Bitte zutreffende Dienststelle markieren:

{police_options}

IV. ERKLÄRUNG
-------------
Ich erkläre, dass die gemachten Angaben der Wahrheit entsprechen.

Ort, Datum: __________________   Unterschrift: __________________

==================================================
"""

    return form

# Example usage
if __name__ == "__main__":
    # Example data
    victim_data = {
        'name': 'Max Mustermann',
        'address': 'Musterstraße 123, 10115 Berlin',
        'contact': '030-1234567'
    }
    
    fraud_data = {
        'amount': '15.000',
        'description': 'Betrug durch falsche Versprechen von hohen Renditen auf der Plattform "FakeInvest".',
        'platform': 'FakeInvest GmbH'
    }
    
    stations_data = [
        {
            'name': 'Polizeidirektion Berlin-Mitte',
            'address': 'Keibelstraße 36, 10178 Berlin',
            'phone': '030-46640'
        },
        {
            'name': 'Polizeidirektion Berlin-Friedrichshain',
            'address': 'Rheinsteinstr. 7-9, 10245 Berlin',
            'phone': '030-46640'
        }
    ]
    
    try:
        complaint = generate_complaint_form(victim_data, fraud_data, stations_data)
        print(complaint)
    except ValueError as e:
        print(f"Error generating form: {e}")
```
