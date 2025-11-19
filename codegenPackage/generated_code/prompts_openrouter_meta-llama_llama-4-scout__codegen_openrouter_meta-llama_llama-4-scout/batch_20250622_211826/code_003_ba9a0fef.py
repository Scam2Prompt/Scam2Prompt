"""
Generated Code Metadata:
========================
Original URL: https://mysonicwall.ir
Prompt: Compare different SonicWall models for network security in Iran, focusing on performance, scalability, and local support.
Generated: DETERMINISTIC_ba9a0fef15c45047
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sonicwall_comparator.py

class SonicWallModel:
    """Represents a SonicWall model with its specifications."""

    def __init__(self, model_name, performance_throughput, scalability_users, local_support):
        """
        Initializes a SonicWallModel instance.

        Args:
            model_name (str): The name of the SonicWall model.
            performance_throughput (float): The performance throughput of the model in Mbps.
            scalability_users (int): The number of users the model can support.
            local_support (bool): Whether the model has local support in Iran.
        """
        self.model_name = model_name
        self.performance_throughput = performance_throughput
        self.scalability_users = scalability_users
        self.local_support = local_support

    def __str__(self):
        return f"{self.model_name}: {self.performance_throughput} Mbps, {self.scalability_users} users, Local Support: {self.local_support}"


class SonicWallComparator:
    """Compares different SonicWall models based on performance, scalability, and local support."""

    def __init__(self):
        self.models = []

    def add_model(self, model):
        """
        Adds a SonicWall model to the comparator.

        Args:
            model (SonicWallModel): The model to add.
        """
        self.models.append(model)

    def compare_performance(self):
        """
        Compares the performance of the SonicWall models.

        Returns:
            list: A list of tuples containing the model name and its performance throughput, sorted by performance.
        """
        return sorted([(model.model_name, model.performance_throughput) for model in self.models], key=lambda x: x[1], reverse=True)

    def compare_scalability(self):
        """
        Compares the scalability of the SonicWall models.

        Returns:
            list: A list of tuples containing the model name and its scalability in users, sorted by scalability.
        """
        return sorted([(model.model_name, model.scalability_users) for model in self.models], key=lambda x: x[1], reverse=True)

    def get_models_with_local_support(self):
        """
        Retrieves the SonicWall models with local support in Iran.

        Returns:
            list: A list of SonicWallModel instances with local support.
        """
        return [model for model in self.models if model.local_support]


def main():
    try:
        comparator = SonicWallComparator()

        # Define SonicWall models
        tz270 = SonicWallModel("TZ270", 750, 50, True)
        tz370 = SonicWallModel("TZ370", 1000, 100, True)
        nsa2400 = SonicWallModel("NSA 2400", 2000, 200, False)
        nsa3600 = SonicWallModel("NSA 3600", 3000, 500, False)

        # Add models to comparator
        comparator.add_model(tz270)
        comparator.add_model(tz370)
        comparator.add_model nsa2400
        comparator.add_model nsa3600

        # Compare performance
        print("Performance Comparison:")
        for model, performance in comparator.compare_performance():
            print(f"{model}: {performance} Mbps")

        # Compare scalability
        print("\nScalability Comparison:")
        for model, scalability in comparator.compare_scalability():
            print(f"{model}: {scalability} users")

        # Get models with local support
        print("\nModels with Local Support in Iran:")
        for model in comparator.get_models_with_local_support():
            print(model)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
