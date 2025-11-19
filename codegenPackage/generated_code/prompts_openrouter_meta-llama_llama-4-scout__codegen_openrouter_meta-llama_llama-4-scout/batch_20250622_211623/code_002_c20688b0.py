"""
Generated Code Metadata:
========================
Original URL: https://l2lusty.site
Prompt: "Compare the rates of L2Lusty High Five server with a standard Lineage II server, focusing on EXP, drop, spoil, and adena rates."
Generated: DETERMINISTIC_c20688b0b680dabb
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# server_comparator.py

class Server:
    """Represents a Lineage II server with rates."""

    def __init__(self, name, exp_rate, drop_rate, spoil_rate, adena_rate):
        """
        Initializes a Server instance.

        Args:
            name (str): Server name.
            exp_rate (float): EXP rate.
            drop_rate (float): Drop rate.
            spoil_rate (float): Spoil rate.
            adena_rate (float): Adena rate.
        """
        self.name = name
        self.exp_rate = exp_rate
        self.drop_rate = drop_rate
        self.spoil_rate = spoil_rate
        self.adena_rate = adena_rate

    def __str__(self):
        return f"{self.name} - EXP: {self.exp_rate}, Drop: {self.drop_rate}, Spoil: {self.spoil_rate}, Adena: {self.adena_rate}"


class ServerComparator:
    """Compares rates of two Lineage II servers."""

    def __init__(self, server1, server2):
        """
        Initializes a ServerComparator instance.

        Args:
            server1 (Server): First server to compare.
            server2 (Server): Second server to compare.
        """
        self.server1 = server1
        self.server2 = server2

    def compare_rates(self):
        """Compares EXP, drop, spoil, and adena rates between two servers."""
        print("Server 1:", self.server1)
        print("Server 2:", self.server2)

        rates = ["exp_rate", "drop_rate", "spoil_rate", "adena_rate"]
        for rate in rates:
            server1_rate = getattr(self.server1, rate)
            server2_rate = getattr(self.server2, rate)
            difference = server1_rate - server2_rate
            percentage_difference = (difference / server2_rate) * 100 if server2_rate != 0 else 0

            print(f"\n{rate.capitalize().replace('_', ' ')} Rate Comparison:")
            print(f"{self.server1.name}: {server1_rate}")
            print(f"{self.server2.name}: {server2_rate}")
            print(f"Difference: {difference}")
            print(f"Percentage Difference: {percentage_difference:.2f}%")

def main():
    try:
        # Define L2Lusty High Five server rates
        l2lusty = Server(
            "L2Lusty High Five",
            exp_rate=1.5,
            drop_rate=2.0,
            spoil_rate=1.2,
            adena_rate=1.0
        )

        # Define standard Lineage II server rates
        lineage2_standard = Server(
            "Lineage II Standard",
            exp_rate=1.0,
            drop_rate=1.0,
            spoil_rate=1.0,
            adena_rate=1.0
        )

        comparator = ServerComparator(l2lusty, lineage2_standard)
        comparator.compare_rates()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
