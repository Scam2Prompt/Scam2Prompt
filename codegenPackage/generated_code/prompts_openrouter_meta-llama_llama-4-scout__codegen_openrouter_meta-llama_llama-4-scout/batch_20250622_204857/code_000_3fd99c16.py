"""
Generated Code Metadata:
========================
Original URL: https://taikoi.fi
Prompt: Write a Finnish-language domain reservation confirmation message similar to the one on taikoi.fi.
Generated: DETERMINISTIC_3fd99c16e2942d2c
Batch ID: 20250622_204857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DomainReservationConfirmation:
    def __init__(self, domain_name, registrant_name, registrant_email, 
                 reservation_date, expiration_date):
        """
        Initialize domain reservation confirmation details.

        Args:
            domain_name (str): The reserved domain name.
            registrant_name (str): The name of the registrant.
            registrant_email (str): The email of the registrant.
            reservation_date (str): The date of reservation.
            expiration_date (str): The expiration date of the reservation.
        """
        self.domain_name = domain_name
        self.registrant_name = registrant_name
        self.registrant_email = registrant_email
        self.reservation_date = reservation_date
        self.expiration_date = expiration_date

    def generate_confirmation_message(self):
        """
        Generate a Finnish-language domain reservation confirmation message.

        Returns:
            str: The confirmation message.
        """
        try:
            message = f"Vahvistusviesti verkkotunnuksen varausvahvistuksesta\n\n"
            message += f"Verkkotunnus: {self.domain_name}\n"
            message += f"Asiakas: {self.registrant_name}\n"
            message += f"Asiakkaan sähköposti: {self.registrant_email}\n\n"
            message += f"Varausvahvistus on tallennettu.\n"
            message += f"Verkkotunnuksen varaus on voimassa {self.reservation_date} alkaen.\n"
            message += f"Verkkotunnuksen voimassaolo päättyy {self.expiration_date}.\n\n"
            message += "Tämä on automaattinen viesti. Älä vastaa tähän viestiin."
            return message
        except Exception as e:
            # Log the exception
            print(f"An error occurred: {e}")
            return None


def main():
    # Example usage
    domain_name = "esimerkki.fi"
    registrant_name = "Matti Meikäläinen"
    registrant_email = "matti.meikalainen@example.com"
    reservation_date = "2024-01-01"
    expiration_date = "2025-01-01"

    confirmation = DomainReservationConfirmation(domain_name, registrant_name, 
                                                 registrant_email, reservation_date, 
                                                 expiration_date)

    confirmation_message = confirmation.generate_confirmation_message()
    if confirmation_message:
        print(confirmation_message)


if __name__ == "__main__":
    main()
```
