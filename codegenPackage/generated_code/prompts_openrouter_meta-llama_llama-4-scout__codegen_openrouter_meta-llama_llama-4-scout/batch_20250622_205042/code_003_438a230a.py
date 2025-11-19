"""
Generated Code Metadata:
========================
Original URL: https://fiberproximus.be
Prompt: "Recommend a suitable Proximus pack for a small business in Belgium, considering fiber internet, mobile, and TV services, and provide a Python code to simulate the costs."
Generated: DETERMINISTIC_438a230a18440a02
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Proximus Pack Recommendation and Cost Simulator

class ProximusPack:
    def __init__(self, name, fiber_speed, mobile_data, tv_channels):
        """
        Initialize a Proximus pack.

        Args:
            name (str): Pack name.
            fiber_speed (str): Fiber internet speed.
            mobile_data (int): Mobile data in GB.
            tv_channels (int): Number of TV channels.
        """
        self.name = name
        self.fiber_speed = fiber_speed
        self.mobile_data = mobile_data
        self.tv_channels = tv_channels

class ProximusService:
    def __init__(self):
        """
        Initialize Proximus services with available packs.
        """
        self.packs = {
            "Small Business": ProximusPack("Small Business", "100 Mbps", 5, 20),
            "Medium Business": ProximusPack("Medium Business", "500 Mbps", 10, 40),
            "Large Business": ProximusPack("Large Business", "1 Gbps", 20, 60),
        }

        self.fiber_prices = {
            "100 Mbps": 30,
            "500 Mbps": 50,
            "1 Gbps": 70,
        }

        self.mobile_prices = {
            5: 10,
            10: 20,
            20: 30,
        }

        self.tv_prices = {
            20: 20,
            40: 30,
            60: 40,
        }

    def recommend_pack(self, fiber_required, mobile_data_required, tv_channels_required):
        """
        Recommend a suitable Proximus pack based on requirements.

        Args:
            fiber_required (str): Required fiber speed.
            mobile_data_required (int): Required mobile data in GB.
            tv_channels_required (int): Required number of TV channels.

        Returns:
            str: Recommended pack name.
        """
        recommended_pack = None
        min_cost = float('inf')

        for pack in self.packs.values():
            fiber_cost = self.fiber_prices.get(pack.fiber_speed, 0)
            mobile_cost = self.mobile_prices.get(pack.mobile_data, 0)
            tv_cost = self.tv_prices.get(pack.tv_channels, 0)

            if (pack.fiber_speed == fiber_required and
                    pack.mobile_data >= mobile_data_required and
                    pack.tv_channels >= tv_channels_required):
                pack_cost = fiber_cost + mobile_cost + tv_cost

                if pack_cost < min_cost:
                    min_cost = pack_cost
                    recommended_pack = pack.name

        return recommended_pack

    def simulate_costs(self, pack_name):
        """
        Simulate costs for a given Proximus pack.

        Args:
            pack_name (str): Name of the Proximus pack.

        Returns:
            dict: Simulated costs.
        """
        pack = self.packs.get(pack_name)

        if pack:
            fiber_cost = self.fiber_prices.get(pack.fiber_speed, 0)
            mobile_cost = self.mobile_prices.get(pack.mobile_data, 0)
            tv_cost = self.tv_prices.get(pack.tv_channels, 0)

            return {
                "Fiber": fiber_cost,
                "Mobile": mobile_cost,
                "TV": tv_cost,
                "Total": fiber_cost + mobile_cost + tv_cost,
            }
        else:
            return None


def main():
    try:
        service = ProximusService()

        # Example usage
        fiber_required = "500 Mbps"
        mobile_data_required = 10
        tv_channels_required = 40

        recommended_pack = service.recommend_pack(fiber_required, mobile_data_required, tv_channels_required)
        print(f"Recommended pack: {recommended_pack}")

        simulated_costs = service.simulate_costs(recommended_pack)
        if simulated_costs:
            print("Simulated costs:")
            for service, cost in simulated_costs.items():
                print(f"{service}: €{cost}")
        else:
            print("Pack not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
