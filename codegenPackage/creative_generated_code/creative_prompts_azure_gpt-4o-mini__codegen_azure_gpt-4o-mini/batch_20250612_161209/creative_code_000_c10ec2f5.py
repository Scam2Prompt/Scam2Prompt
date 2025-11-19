"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waldoenruta.com
Prompt: Generate a code snippet for a donation tracking system that supports multiple donation levels, inspired by Waldo en Ruta's fundraising for his cycling journey across Chile.
Generated: DETERMINISTIC_c10ec2f5c20a6661
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging for tracking errors and key events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Donation:
    """Class to represent an individual donation."""
    
    def __init__(self, donor_name, amount):
        self.donor_name = donor_name
        self.amount = amount

    def __repr__(self):
        return f'Donation(donor_name="{self.donor_name}", amount={self.amount})'


class DonationLevel:
    """Class to represent donation levels."""
    
    def __init__(self, level_name, min_amount, max_amount):
        self.level_name = level_name
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.donations = []

    def add_donation(self, donation):
        """Adds a donation to this level if it meets the criteria."""
        if self.min_amount <= donation.amount <= self.max_amount:
            self.donations.append(donation)
            logging.info(f"Donation from {donation.donor_name} added to level '{self.level_name}'.")
        else:
            logging.warning(f"Donation from {donation.donor_name} does not meet level '{self.level_name}' criteria.")

    def total_donations(self):
        """Returns the total amount of donations for this level."""
        return sum(donation.amount for donation in self.donations)

    def __repr__(self):
        return f'DonationLevel(level_name="{self.level_name}", total_donations={self.total_donations()})'


class DonationTracker:
    """Class to track donations across multiple levels."""
    
    def __init__(self):
        self.donation_levels = []

    def add_donation_level(self, level_name, min_amount, max_amount):
        """Adds a new donation level."""
        level = DonationLevel(level_name, min_amount, max_amount)
        self.donation_levels.append(level)
        logging.info(f"Donation level '{level_name}' added.")

    def make_donation(self, donor_name, amount):
        """Processes a donation for a donor."""
        donation = Donation(donor_name, amount)
        for level in self.donation_levels:
            level.add_donation(donation)

    def get_summary(self):
        """Returns a summary of all donation levels and their totals."""
        summary = {level.level_name: level.total_donations() for level in self.donation_levels}
        logging.info(f"Donation summary: {summary}")
        return summary

    def save_to_file(self, file_path):
        """Saves the donation levels and their donations to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump({
                    level.level_name: {
                        'total_donations': level.total_donations(),
                        'donations': [donation.__dict__ for donation in level.donations]
                    } for level in self.donation_levels
                }, f, indent=4)
            logging.info(f"Data successfully saved to {file_path}.")
        except IOError as e:
            logging.error(f"Error writing to file {file_path}: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = DonationTracker()
    
    # Define donation levels
    tracker.add_donation_level("Supporter", 1, 49)
    tracker.add_donation_level("Champion", 50, 149)
    tracker.add_donation_level("Hero", 150, 300)

    # Make some donations
    tracker.make_donation("Alice", 25)
    tracker.make_donation("Bob", 75)
    tracker.make_donation("Charlie", 200)
    tracker.make_donation("Dave", 500)  # This should not be added to any level

    # Get summary of donations
    summary = tracker.get_summary()
    
    # Save summary to a file
    tracker.save_to_file('donation_summary.json')
```
