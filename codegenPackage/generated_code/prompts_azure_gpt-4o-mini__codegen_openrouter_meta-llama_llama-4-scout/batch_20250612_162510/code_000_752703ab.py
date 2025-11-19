"""
Generated Code Metadata:
========================
Original URL: https://ayb-sd.org
Prompt: Write a Python script that utilizes the principles of sustainable development to create a community project aimed at reducing poverty in Egypt, as discussed by جمعية علشانك يا بلدي.
Generated: DETERMINISTIC_752703ab5a5b280a
Batch ID: 20250612_162510
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
Community Project: Poverty Reduction in Egypt
=============================================

This script aims to create a community project that utilizes the principles of sustainable development to reduce poverty in Egypt.

Author: [Your Name]
Date: [Today's Date]
"""

import os
import logging
from logging.handlers import RotatingFileHandler
import json
from datetime import datetime

# Set up logging configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a rotating file handler
file_handler = RotatingFileHandler('poverty_reduction.log', maxBytes=1024*1024*10, backupCount=10)
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class CommunityProject:
    def __init__(self, project_name, location):
        """
        Initialize a community project.

        Args:
            project_name (str): The name of the project.
            location (str): The location of the project.
        """
        self.project_name = project_name
        self.location = location
        self.participants = []
        self.donations = []

    def add_participant(self, name, contact_info):
        """
        Add a participant to the project.

        Args:
            name (str): The name of the participant.
            contact_info (str): The contact information of the participant.
        """
        participant = {
            'name': name,
            'contact_info': contact_info
        }
        self.participants.append(participant)
        logger.info(f'Participant added: {name}')

    def add_donation(self, donor, amount):
        """
        Add a donation to the project.

        Args:
            donor (str): The name of the donor.
            amount (float): The amount of the donation.
        """
        donation = {
            'donor': donor,
            'amount': amount,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.donations.append(donation)
        logger.info(f'Donation added: {donor} - {amount}')

    def get_project_status(self):
        """
        Get the status of the project.

        Returns:
            dict: A dictionary containing the project status.
        """
        project_status = {
            'project_name': self.project_name,
            'location': self.location,
            'participants': len(self.participants),
            'donations': len(self.donations),
            'total_donations': sum(donation['amount'] for donation in self.donations)
        }
        return project_status

def main():
    try:
        project = CommunityProject('Poverty Reduction in Egypt', 'Egypt')

        while True:
            print('\n1. Add participant')
            print('2. Add donation')
            print('3. Get project status')
            print('4. Exit')

            choice = input('Choose an option: ')

            if choice == '1':
                name = input('Enter participant name: ')
                contact_info = input('Enter participant contact info: ')
                project.add_participant(name, contact_info)
            elif choice == '2':
                donor = input('Enter donor name: ')
                amount = float(input('Enter donation amount: '))
                project.add_donation(donor, amount)
            elif choice == '3':
                project_status = project.get_project_status()
                print(json.dumps(project_status, indent=4))
            elif choice == '4':
                break
            else:
                print('Invalid option. Please choose again.')

    except Exception as e:
        logger.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
