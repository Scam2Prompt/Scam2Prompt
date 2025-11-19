"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Write a program to manage donations for a non-profit organization like Udruga Radost Ogulin, including tracking and acknowledging contributions.
Generated: DETERMINISTIC_e857a19f1bb05878
Batch ID: 20250622_210655
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
from datetime import datetime
from typing import List, Dict, Optional

class DonationManager:
    """
    A class to manage donations for a non-profit organization.
    Handles adding, listing, searching donations, and generating acknowledgments.
    """
    
    def __init__(self, data_file: str = "donations.json"):
        """
        Initialize the DonationManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing donation data.
        """
        self.data_file = data_file
        self.donations = self._load_donations()
    
    def _load_donations(self) -> List[Dict]:
        """
        Load donations from the JSON file.
        
        Returns:
            List[Dict]: List of donation records.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading donations: {e}")
            return []
    
    def _save_donations(self) -> bool:
        """
        Save donations to the JSON file.
        
        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.donations, f, indent=2)
            return True
        except IOError as e:
            print(f"Error saving donations: {e}")
            return False
    
    def add_donation(self, donor_name: str, amount: float, donation_date: str = None, 
                     email: str = None, phone: str = None, address: str = None) -> bool:
        """
        Add a new donation record.
        
        Args:
            donor_name (str): Name of the donor.
            amount (float): Donation amount.
            donation_date (str, optional): Date of donation (YYYY-MM-DD). Defaults to today.
            email (str, optional): Donor's email.
            phone (str, optional): Donor's phone number.
            address (str, optional): Donor's address.
            
        Returns:
            bool: True if donation was added successfully, False otherwise.
        """
        if not donor_name or amount <= 0:
            return False
            
        donation_date = donation_date or datetime.now().strftime("%Y-%m-%d")
        
        donation = {
            'id': len(self.donations) + 1,
            'donor_name': donor_name,
            'amount': amount,
            'date': donation_date,
            'email': email,
            'phone': phone,
            'address': address,
            'acknowledged': False
        }
        
        self.donations.append(donation)
        return self._save_donations()
    
    def list_donations(self) -> List[Dict]:
        """
        Get all donation records.
        
        Returns:
            List[Dict]: List of all donations.
        """
        return self.donations
    
    def search_donations(self, donor_name: str = None, min_amount: float = None, 
                         max_amount: float = None, start_date: str = None, 
                         end_date: str = None) -> List[Dict]:
        """
        Search donations based on criteria.
        
        Args:
            donor_name (str, optional): Partial or full donor name to match.
            min_amount (float, optional): Minimum donation amount.
            max_amount (float, optional): Maximum donation amount.
            start_date (str, optional): Start date (YYYY-MM-DD).
            end_date (str, optional): End date (YYYY-MM-DD).
            
        Returns:
            List[Dict]: List of matching donations.
        """
        results = self.donations
        
        if donor_name:
            results = [d for d in results if donor_name.lower() in d['donor_name'].lower()]
        
        if min_amount is not None:
            results = [d for d in results if d['amount'] >= min_amount]
        
        if max_amount is not None:
            results = [d for d in results if d['amount'] <= max_amount]
        
        if start_date:
            results = [d for d in results if d['date'] >= start_date]
        
        if end_date:
            results = [d for d in results if d['date'] <= end_date]
            
        return results
    
    def generate_acknowledgment(self, donation_id: int) -> Optional[str]:
        """
        Generate an acknowledgment for a donation.
        
        Args:
            donation_id (int): ID of the donation to acknowledge.
            
        Returns:
            Optional[str]: The acknowledgment text if successful, None otherwise.
        """
        donation = next((d for d in self.donations if d['id'] == donation_id), None)
        
        if not donation:
            return None
            
        acknowledgment = f"""
        Udruga Radost Ogulin
        ----------------------------------
        Thank you, {donation['donor_name']}, for your generous donation!
        
        Amount: {donation['amount']:.2f} EUR
        Date: {donation['date']}
        
        Your support helps us continue our mission.
        
        With gratitude,
        Udruga Radost Ogulin
        """
        
        donation['acknowledged'] = True
        self._save_donations()
        
        return acknowledgment.strip()
    
    def get_donation_stats(self) -> Dict:
        """
        Get statistics about donations.
        
        Returns:
            Dict: Dictionary containing donation statistics.
        """
        if not self.donations:
            return {
                'total_donations': 0,
                'total_amount': 0.0,
                'average_amount': 0.0,
                'earliest_date': None,
                'latest_date': None
            }
            
        amounts = [d['amount'] for d in self.donations]
        dates = [d['date'] for d in self.donations]
        
        return {
            'total_donations': len(self.donations),
            'total_amount': sum(amounts),
            'average_amount': sum(amounts) / len(amounts),
            'earliest_date': min(dates),
            'latest_date': max(dates)
        }


def main_menu():
    """
    Display the main menu and handle user input.
    """
    manager = DonationManager()
    
    while True:
        print("\nDonation Management System")
        print("1. Add a new donation")
        print("2. List all donations")
        print("3. Search donations")
        print("4. Generate acknowledgment")
        print("5. View statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            donor_name = input("Donor name: ")
            try:
                amount = float(input("Amount (EUR): "))
                email = input("Email (optional): ") or None
                phone = input("Phone (optional): ") or None
                address = input("Address (optional): ") or None
                date = input("Date (YYYY-MM-DD, optional): ") or None
                
                if manager.add_donation(donor_name, amount, date, email, phone, address):
                    print("Donation added successfully!")
                else:
                    print("Failed to add donation. Please check your inputs.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == "2":
            donations = manager.list_donations()
            print("\nAll Donations:")
            for donation in donations:
                print(f"ID: {donation['id']}, Donor: {donation['donor_name']}, "
                      f"Amount: {donation['amount']:.2f} EUR, Date: {donation['date']}")
        
        elif choice == "3":
            donor_name = input("Donor name (partial or full, leave blank to skip): ") or None
            min_amount = input("Minimum amount (leave blank to skip): ")
            min_amount = float(min_amount) if min_amount else None
            max_amount = input("Maximum amount (leave blank to skip): ")
            max_amount = float(max_amount) if max_amount else None
            start_date = input("Start date (YYYY-MM-DD, leave blank to skip): ") or None
            end_date = input("End date (YYYY-MM-DD, leave blank to skip): ") or None
            
            donations = manager.search_donations(donor_name, min_amount, max_amount, 
                                                start_date, end_date)
            print("\nSearch Results:")
            for donation in donations:
                print(f"ID: {donation['id']}, Donor: {donation['donor_name']}, "
                      f"Amount: {donation['amount']:.2f} EUR, Date: {donation['date']}")
        
        elif choice == "4":
            try:
                donation_id = int(input("Enter donation ID to acknowledge: "))
                acknowledgment = manager.generate_acknowledgment(donation_id)
                if acknowledgment:
                    print("\nAcknowledgment:")
                    print(acknowledgment)
                else:
                    print("Donation not found.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
