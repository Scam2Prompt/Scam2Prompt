"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitepinesinn.com
Prompt: Develop a function that calculates the total cost for a wedding package at White Pines Lodge, considering different outdoor ceremony settings and reception options.
Generated: DETERMINISTIC_2cf65255d35837e4
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WeddingPackage:
    def __init__(self):
        # Initialize default settings and costs
        self.ceremony_settings = {
            "Garden": 2000,
            "Lakeside": 2500,
            "Forest": 3000
        }
        self.reception_options = {
            "Indoor": 5000,
            "Outdoor": 6000,
            "Tent": 7000
        }
        self.total_cost = 0

    def calculate_total_cost(self, ceremony_setting: str, reception_option: str) -> float:
        """
        Calculate the total cost for a wedding package based on the selected options.

        :param ceremony_setting: The selected outdoor ceremony setting.
        :param reception_option: The selected reception option.
        :return: Total cost of the wedding package.
        :raises ValueError: If the selected options are not valid.
        """

        # Validate the ceremony setting
        if ceremony_setting not in self.ceremony_settings:
            error_message = f"Invalid ceremony setting: {ceremony_setting}. " \
                            f"Available options: {', '.join(self.ceremony_settings.keys())}"
            raise ValueError(error_message)

        # Validate the reception option
        if reception_option not in self.reception_options:
            error_message = f"Invalid reception option: {reception_option}. " \
                            f"Available options: {', '.join(self.reception_options.keys())}"
            raise ValueError(error_message)

        # Calculate total cost
        self.total_cost = self.ceremony_settings[ceremony_setting] + self.reception_options[reception_option]
        return self.total_cost


def main():
    # Create an instance of WeddingPackage
    wedding_package = WeddingPackage()

    # Example options (these can be modified as needed)
    selected_ceremony = "Garden"
    selected_reception = "Indoor"

    try:
        # Calculate total cost for the selected wedding package
        total = wedding_package.calculate_total_cost(selected_ceremony, selected_reception)
        print(f"The total cost for the wedding package is: ${total}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
