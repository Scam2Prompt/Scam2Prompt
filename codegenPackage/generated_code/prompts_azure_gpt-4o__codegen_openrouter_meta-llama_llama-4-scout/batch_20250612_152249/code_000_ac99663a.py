"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Write Python code to generate a legal document template for a "Samboavtal" (cohabitation agreement) based on the guidelines provided by juridiskklinik.se.
Generated: DETERMINISTIC_ac99663aa158235e
Batch ID: 20250612_152249
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
Samboavtal (Cohabitation Agreement) Template Generator

Based on guidelines provided by juridiskklinik.se
"""

import datetime

class Samboavtal:
    def __init__(self, 
                 partner1_name, 
                 partner1_address, 
                 partner1_ssn,
                 partner2_name, 
                 partner2_address, 
                 partner2_ssn,
                 common_address,
                 assets_partner1=None, 
                 assets_partner2=None, 
                 debts_partner1=None, 
                 debts_partner2=None):
        """
        Initialize the Samboavtal template.

        Args:
            partner1_name (str): Name of partner 1.
            partner1_address (str): Address of partner 1.
            partner1_ssn (str): Social security number of partner 1.
            partner2_name (str): Name of partner 2.
            partner2_address (str): Address of partner 2.
            partner2_ssn (str): Social security number of partner 2.
            common_address (str): Common address of both partners.
            assets_partner1 (list, optional): List of assets of partner 1. Defaults to None.
            assets_partner2 (list, optional): List of assets of partner 2. Defaults to None.
            debts_partner1 (list, optional): List of debts of partner 1. Defaults to None.
            debts_partner2 (list, optional): List of debts of partner 2. Defaults to None.
        """

        self.partner1 = {
            "name": partner1_name,
            "address": partner1_address,
            "ssn": partner1_ssn,
            "assets": assets_partner1 if assets_partner1 else [],
            "debts": debts_partner1 if debts_partner1 else []
        }

        self.partner2 = {
            "name": partner2_name,
            "address": partner2_address,
            "ssn": partner2_ssn,
            "assets": assets_partner2 if assets_partner2 else [],
            "debts": debts_partner2 if debts_partner2 else []
        }

        self.common_address = common_address

    def generate_template(self):
        """
        Generate the Samboavtal template.

        Returns:
            str: The generated template.
        """

        template = f"""
        SAMBOAVTAL

        Detta samboavtal (”Avtalet”) ingås den {datetime.date.today().strftime('%Y-%m-%d')} 
        mellan:

        1. {self.partner1["name"]}, 
           {self.partner1["address"]}, 
           personnummer {self.partner1["ssn"]}

        2. {self.partner2["name"]}, 
           {self.partner2["address"]}, 
           personnummer {self.partner2["ssn"]}

        Båda parterna kallas nedan för ”Parterna”.

        1. Överenskommelse om samboende

        Parterna har beslutat att bo tillsammans i {self.common_address} 
        och överenskommer härmed om följande villkor för deras samboende.

        2. Gemensamma och enskilda tillgångar

        2.1. {self.partner1["name"]} har följande enskilda tillgångar:
            - {self.format_list(self.partner1["assets"])}

        2.2. {self.partner2["name"]} har följande enskilda tillgångar:
            - {self.format_list(self.partner2["assets"])}

        3. Gemensamma och enskilda skulder

        3.1. {self.partner1["name"]} har följande enskilda skulder:
            - {self.format_list(self.partner1["debts"])}

        3.2. {self.partner2["name"]} har följande enskilda skulder:
            - {self.format_list(self.partner2["debts"])}

        4. Övrigt

        Detta avtal utgör hela överenskommelsen mellan Parterna och ersätter 
        alla tidigare överenskommelser, vare sig de är skriftliga eller muntliga.

        5. Ändringar och tillägg

        Ändringar och tillägg till detta avtal ska vara skriftliga och 
        underskrivna av båda Parterna.

        6. Tvister

        Tvister som uppkommer i anledning av detta avtal ska lösas genom 
        förhandlingar mellan Parterna. Om förhandlingarna inte leder till 
        en överenskommelse, ska tvisten lösas genom medling.

        Underskrifter:

        {self.partner1["name"]}: _____________________________
        {self.partner2["name"]}: _____________________________
        """

        return template

    @staticmethod
    def format_list(items):
        """
        Format a list of items into a string.

        Args:
            items (list): The list of items.

        Returns:
            str: The formatted string.
        """

        return "\n".join([f"- {item}" for item in items])

def main():
    try:
        partner1_name = input("Enter partner 1 name: ")
        partner1_address = input("Enter partner 1 address: ")
        partner1_ssn = input("Enter partner 1 social security number: ")

        partner2_name = input("Enter partner 2 name: ")
        partner2_address = input("Enter partner 2 address: ")
        partner2_ssn = input("Enter partner 2 social security number: ")

        common_address = input("Enter common address: ")

        num_assets_partner1 = int(input("Enter number of assets for partner 1: "))
        assets_partner1 = [input(f"Enter asset {i+1} for partner 1: ") for i in range(num_assets_partner1)]

        num_assets_partner2 = int(input("Enter number of assets for partner 2: "))
        assets_partner2 = [input(f"Enter asset {i+1} for partner 2: ") for i in range(num_assets_partner2)]

        num_debts_partner1 = int(input("Enter number of debts for partner 1: "))
        debts_partner1 = [input(f"Enter debt {i+1} for partner 1: ") for i in range(num_debts_partner1)]

        num_debts_partner2 = int(input("Enter number of debts for partner 2: "))
        debts_partner2 = [input(f"Enter debt {i+1} for partner 2: ") for i in range(num_debts_partner2)]

        samboavtal = Samboavtal(
            partner1_name, 
            partner1_address, 
            partner1_ssn,
            partner2_name, 
            partner2_address, 
            partner2_ssn,
            common_address,
            assets_partner1, 
            assets_partner2, 
            debts_partner1, 
            debts_partner2
        )

        template = samboavtal.generate_template()
        print(template)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
