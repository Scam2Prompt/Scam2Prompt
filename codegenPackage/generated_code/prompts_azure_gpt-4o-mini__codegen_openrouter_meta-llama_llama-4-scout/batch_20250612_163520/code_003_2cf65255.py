"""
Generated Code Metadata:
========================
Original URL: https://whitepinesinn.com
Prompt: Develop a function that calculates the total cost for a wedding package at White Pines Lodge, considering different outdoor ceremony settings and reception options.
Generated: DETERMINISTIC_2cf65255d35837e4
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class CeremonySetting(Enum):
    """ Enum for outdoor ceremony settings """
    GARDEN = 1
    LAKEFRONT = 2
    FOREST = 3

class ReceptionOption(Enum):
    """ Enum for reception options """
    BASIC = 1
    DELUXE = 2
    PREMIUM = 3

class WeddingPackage:
    """ Class to calculate total cost for a wedding package """

    def __init__(self):
        self.ceremony_settings: Dict[CeremonySetting, float] = {
            CeremonySetting.GARDEN: 1000.0,
            CeremonySetting.LAKEFRONT: 2000.0,
            CeremonySetting.FOREST: 1500.0
        }
        self.reception_options: Dict[ReceptionOption, float] = {
            ReceptionOption.BASIC: 5000.0,
            ReceptionOption.DELUXE: 7500.0,
            ReceptionOption.PREMIUM: 10000.0
        }

    def calculate_ceremony_cost(self, ceremony_setting: CeremonySetting) -> float:
        """ Calculate ceremony cost based on setting """
        if ceremony_setting not in self.ceremony_settings:
            raise ValueError("Invalid ceremony setting")
        return self.ceremony_settings[ceremony_setting]

    def calculate_reception_cost(self, reception_option: ReceptionOption, guest_count: int) -> float:
        """ Calculate reception cost based on option and guest count """
        if reception_option not in self.reception_options:
            raise ValueError("Invalid reception option")
        base_cost = self.reception_options[reception_option]
        # assume $50 per guest
        guest_cost = guest_count * 50.0
        return base_cost + guest_cost

    def calculate_total_cost(self, ceremony_setting: CeremonySetting, reception_option: ReceptionOption, guest_count: int) -> float:
        """ Calculate total cost for wedding package """
        ceremony_cost = self.calculate_ceremony_cost(ceremony_setting)
        reception_cost = self.calculate_reception_cost(reception_option, guest_count)
        return ceremony_cost + reception_cost


def main():
    try:
        package = WeddingPackage()
        ceremony_setting = CeremonySetting.LAKEFRONT
        reception_option = ReceptionOption.DELUXE
        guest_count = 100
        total_cost = package.calculate_total_cost(ceremony_setting, reception_option, guest_count)
        print(f"Total cost for wedding package: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
