"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: "Write a Python code to calculate the total cost for a family of 4 to play unlimited games at Playland Kenya's Trampoline Park and Soft Play Area."
Generated: DETERMINISTIC_302a82e710b962f5
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for PlaylandKenya
class PlaylandKenya:
    def __init__(self):
        # Define prices for Trampoline Park and Soft Play Area
        self.trampoline_park_price_per_person = 800  # KES
        self.soft_play_area_price_per_person = 600  # KES

    def calculate_total_cost(self, num_family_members):
        """
        Calculate total cost for a family to play unlimited games.

        Args:
            num_family_members (int): Number of family members.

        Returns:
            dict: Total cost for Trampoline Park and Soft Play Area.

        Raises:
            ValueError: If number of family members is less than 1.
        """
        if num_family_members < 1:
            raise ValueError("Number of family members must be at least 1.")

        # Calculate total cost for Trampoline Park
        trampoline_park_total_cost = self.trampoline_park_price_per_person * num_family_members

        # Calculate total cost for Soft Play Area
        soft_play_area_total_cost = self.soft_play_area_price_per_person * num_family_members

        return {
            "trampoline_park": trampoline_park_total_cost,
            "soft_play_area": soft_play_area_total_cost,
            "total": trampoline_park_total_cost + soft_play_area_total_cost,
        }


def main():
    try:
        playland_kenya = PlaylandKenya()
        num_family_members = 4
        costs = playland_kenya.calculate_total_cost(num_family_members)

        print(f"Cost for {num_family_members} family members:")
        print(f"Trampoline Park: KES {costs['trampoline_park']}")
        print(f"Soft Play Area: KES {costs['soft_play_area']}")
        print(f"Total Cost: KES {costs['total']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
