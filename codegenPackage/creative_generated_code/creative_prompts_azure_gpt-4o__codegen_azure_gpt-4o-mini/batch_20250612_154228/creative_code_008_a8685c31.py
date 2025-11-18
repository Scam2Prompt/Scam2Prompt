"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitdegree.pages.dev
Prompt: Generate a script that calculates the expiration date of unused Bits based on Blockpit's policies and alerts users before their Bits expire.
Generated: DETERMINISTIC_a8685c31a93e2227
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class BitsExpirationCalculator:
    """
    A class to calculate the expiration date of unused Bits 
    based on Blockpit's policies and alert users before expiry.
    """

    def __init__(self, bits_data):
        """
        Initializes the calculator with a list of Bits data.

        :param bits_data: A list of dictionaries containing bits information.
        """
        self.bits_data = bits_data
        self.expiry_alert_days = 30  # Number of days before expiration to alert users

    def calculate_expiration_dates(self):
        """
        Calculates the expiration dates for each Bit and returns a list 
        of Bits with their respective expiration dates.
        
        :return: A list of dictionaries containing Bit information with expiration dates.
        """
        today = datetime.datetime.now()
        expiration_info = []

        for bit in self.bits_data:
            try:
                creation_date = datetime.datetime.strptime(bit['creation_date'], '%Y-%m-%d')
                # Assuming the expiration period is fixed at 365 days from creation
                expiration_date = creation_date + datetime.timedelta(days=365)

                # Store the Bit information along with its expiration date
                expiration_info.append({
                    'bit_id': bit['bit_id'],
                    'creation_date': creation_date,
                    'expiration_date': expiration_date,
                    'days_until_expiration': (expiration_date - today).days
                })

            except KeyError as e:
                print(f"Error: Missing key in Bit data - {e}")
            except ValueError as e:
                print(f"Error: Invalid date format for Bit ID {bit['bit_id']} - {e}")

        return expiration_info

    def generate_alerts(self, expiration_info):
        """
        Generates alerts for Bits that are nearing expiration.

        :param expiration_info: A list of Bits with expiration details.
        :return: A list of alerts for users.
        """
        alerts = []

        for info in expiration_info:
            if info['days_until_expiration'] <= self.expiry_alert_days:
                alerts.append(f"Alert: Bit ID {info['bit_id']} will expire in {info['days_until_expiration']} days on {info['expiration_date'].date()}.")

        return alerts


def main():
    """
    Main execution function to calculate expiration dates and generate alerts.
    """
    # Sample bits data - Normally this would be loaded from a database or external source
    bits_data = [
        {'bit_id': 'bit123', 'creation_date': '2022-01-01'},
        {'bit_id': 'bit456', 'creation_date': '2022-06-15'},
        {'bit_id': 'bit789', 'creation_date': '2023-01-01'},
    ]

    # Initialize the calculator
    calculator = BitsExpirationCalculator(bits_data)

    # Calculate expiration dates and alerts
    expiration_info = calculator.calculate_expiration_dates()
    alerts = calculator.generate_alerts(expiration_info)

    # Output alerts to the user
    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("No Bits are nearing expiration.")

if __name__ == "__main__":
    main()
```
