"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Write code to compare computer configurations, such as those listed on Londritech's site, and recommend the best option for gaming based on GPU and processor performance.
Generated: DETERMINISTIC_d77036f62842c34d
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# computer_config_comparator.py

class ComputerConfig:
    """Represents a computer configuration with GPU and processor performance metrics."""

    def __init__(self, name, gpu_name, gpu_performance, processor_name, processor_performance):
        """
        Initializes a ComputerConfig instance.

        Args:
            name (str): The name of the computer configuration.
            gpu_name (str): The name of the GPU.
            gpu_performance (float): The performance score of the GPU.
            processor_name (str): The name of the processor.
            processor_performance (float): The performance score of the processor.
        """
        self.name = name
        self.gpu_name = gpu_name
        self.gpu_performance = gpu_performance
        self.processor_name = processor_name
        self.processor_performance = processor_performance

    def __repr__(self):
        return f"ComputerConfig(name='{self.name}', gpu_name='{self.gpu_name}', gpu_performance={self.gpu_performance}, processor_name='{self.processor_name}', processor_performance={self.processor_performance})"


class ComputerConfigComparator:
    """Compares computer configurations and recommends the best option for gaming."""

    def __init__(self):
        self.configs = []

    def add_config(self, config):
        """
        Adds a computer configuration to the comparator.

        Args:
            config (ComputerConfig): The computer configuration to add.
        """
        self.configs.append(config)

    def compare_configs(self):
        """
        Compares the computer configurations and returns the recommended configuration for gaming.

        Returns:
            ComputerConfig: The recommended computer configuration for gaming.
        """
        if not self.configs:
            raise ValueError("No computer configurations added")

        # Calculate a weighted performance score for each configuration (GPU: 70%, Processor: 30%)
        weighted_configs = [
            (config, config.gpu_performance * 0.7 + config.processor_performance * 0.3)
            for config in self.configs
        ]

        # Sort the configurations by their weighted performance scores in descending order
        weighted_configs.sort(key=lambda x: x[1], reverse=True)

        return weighted_configs[0][0]

    def print_comparison_results(self):
        """
        Prints the comparison results of the computer configurations.
        """
        if not self.configs:
            print("No computer configurations added")
            return

        recommended_config = self.compare_configs()

        print("Computer Configuration Comparison Results:")
        for config in self.configs:
            print(f"Name: {config.name}")
            print(f"GPU: {config.gpu_name} (Performance: {config.gpu_performance})")
            print(f"Processor: {config.processor_name} (Performance: {config.processor_performance})")
            print()

        print(f"Recommended configuration for gaming: {recommended_config.name}")
        print(f"GPU: {recommended_config.gpu_name} (Performance: {recommended_config.gpu_performance})")
        print(f"Processor: {recommended_config.processor_name} (Performance: {recommended_config.processor_performance})")


def main():
    comparator = ComputerConfigComparator()

    # Example computer configurations
    config1 = ComputerConfig(
        "Londritech Gaming PC",
        "NVIDIA GeForce RTX 3080",
        10000,
        "AMD Ryzen 9 5900X",
        8000
    )

    config2 = ComputerConfig(
        "Londritech Budget Gaming PC",
        "NVIDIA GeForce GTX 1660",
        4000,
        "AMD Ryzen 5 5600X",
        6000
    )

    config3 = ComputerConfig(
        "Londritech High-End Gaming PC",
        "NVIDIA GeForce RTX 3090",
        12000,
        "AMD Ryzen 9 5950X",
        9000
    )

    comparator.add_config(config1)
    comparator.add_config(config2)
    comparator.add_config(config3)

    comparator.print_comparison_results()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
