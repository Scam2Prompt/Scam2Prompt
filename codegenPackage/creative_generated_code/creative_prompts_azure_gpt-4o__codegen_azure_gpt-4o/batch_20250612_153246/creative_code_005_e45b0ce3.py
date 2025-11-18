"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerafricasolar.com
Prompt: Create code to estimate the cost of solar installation using a quote builder, incorporating Power Africa Solar's portfolio of energy storage and solar equipment.
Generated: DETERMINISTIC_e45b0ce3889d6339
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SolarQuoteBuilder:
    """
    A class to estimate the cost of solar installation using Power Africa Solar's portfolio.
    """

    def __init__(self):
        # Initialize the portfolio of solar equipment and energy storage options.
        # Simulating loading from a database or external API.
        self.portfolio = {
            "solar_panels": [
                {"name": "Economy Panel", "cost_per_unit": 100, "unit_size_kw": 1},
                {"name": "Premium Panel", "cost_per_unit": 250, "unit_size_kw": 1.5}
            ],
            "energy_storage": [
                {"name": "Basic Battery", "cost_per_unit": 500, "capacity_kwh": 5},
                {"name": "Advanced Battery", "cost_per_unit": 1200, "capacity_kwh": 10}
            ]
        }

    def get_portfolio(self):
        """
        Returns the portfolio of solar equipment and energy storage options.

        Returns:
            dict: Portfolio of items available for selection.
        """
        return self.portfolio

    def calculate_quote(self, energy_need_kw, storage_need_kwh, panel_choice, battery_choice):
        """
        Calculates the total cost of the solar installation.

        Args:
            energy_need_kw (float): The energy requirement in kilowatts.
            storage_need_kwh (float): The storage requirement in kilowatt-hours.
            panel_choice (str): The chosen solar panel name from the portfolio.
            battery_choice (str): The chosen battery name from the portfolio.

        Returns:
            dict: A detailed quote containing itemized costs and total cost.
        """
        try:
            # Find the chosen solar panel and battery in the portfolio.
            selected_panel = next(
                panel for panel in self.portfolio["solar_panels"] if panel["name"] == panel_choice
            )
            selected_battery = next(
                battery for battery in self.portfolio["energy_storage"] if battery["name"] == battery_choice
            )

            # Calculate the number of solar panels needed and total cost for panels.
            panels_needed = int((energy_need_kw / selected_panel["unit_size_kw"]) + 0.5)  # Round up
            panels_cost = panels_needed * selected_panel["cost_per_unit"]

            # Calculate the number of batteries needed and total cost for batteries.
            batteries_needed = int((storage_need_kwh / selected_battery["capacity_kwh"]) + 0.5)  # Round up
            batteries_cost = batteries_needed * selected_battery["cost_per_unit"]

            # Calculate the total cost.
            total_cost = panels_cost + batteries_cost

            # Build the quote summary.
            quote = {
                "solar_panels": {
                    "type": selected_panel["name"],
                    "quantity": panels_needed,
                    "cost": panels_cost
                },
                "energy_storage": {
                    "type": selected_battery["name"],
                    "quantity": batteries_needed,
                    "cost": batteries_cost
                },
                "total_cost": total_cost
            }

            return quote
        except StopIteration:
            raise ValueError("Invalid panel or battery choice. Please select from the portfolio.")

        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage (uncomment the following lines to test the code):
# builder = SolarQuoteBuilder()
# print("Portfolio:", json.dumps(builder.get_portfolio(), indent=2))
# quote = builder.calculate_quote(
#     energy_need_kw=6, 
#     storage_need_kwh=15, 
#     panel_choice="Premium Panel", 
#     battery_choice="Advanced Battery"
# )
# print("Quote:", json.dumps(quote, indent=2))
```
