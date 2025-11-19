"""
Generated Code Metadata:
========================
Original URL: https://ecoswap.us
Prompt: Create a program that compares Apple M1 and M2 chipsets for MacBooks and iPads, using the use cases and recommendations outlined in EcoSwap's blog post.
Generated: DETERMINISTIC_bde514ba0ccbdd4d
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chipset_comparator.py

class Chipset:
    def __init__(self, name, cpu_cores, gpu_cores, memory_bandwidth, use_cases):
        """
        Initialize a Chipset object.

        Args:
        - name (str): The name of the chipset.
        - cpu_cores (int): The number of CPU cores.
        - gpu_cores (int): The number of GPU cores.
        - memory_bandwidth (float): The memory bandwidth in GB/s.
        - use_cases (list): A list of recommended use cases.
        """
        self.name = name
        self.cpu_cores = cpu_cores
        self.gpu_cores = gpu_cores
        self.memory_bandwidth = memory_bandwidth
        self.use_cases = use_cases

    def __str__(self):
        return f"{self.name} - CPU Cores: {self.cpu_cores}, GPU Cores: {self.gpu_cores}, Memory Bandwidth: {self.memory_bandwidth} GB/s"


class ChipsetComparator:
    def __init__(self):
        self.chipsets = {}

    def add_chipset(self, chipset):
        """
        Add a chipset to the comparator.

        Args:
        - chipset (Chipset): The chipset to add.
        """
        self.chipsets[chipset.name] = chipset

    def compare_chipsets(self, name1, name2):
        """
        Compare two chipsets.

        Args:
        - name1 (str): The name of the first chipset.
        - name2 (str): The name of the second chipset.

        Returns:
        - A dictionary with the comparison results.
        """
        if name1 not in self.chipsets or name2 not in self.chipsets:
            raise ValueError("Both chipsets must be added to the comparator")

        chipset1 = self.chipsets[name1]
        chipset2 = self.chipsets[name2]

        comparison_results = {
            "cpu_cores": f"{chipset1.cpu_cores} vs {chipset2.cpu_cores}",
            "gpu_cores": f"{chipset1.gpu_cores} vs {chipset2.gpu_cores}",
            "memory_bandwidth": f"{chipset1.memory_bandwidth} GB/s vs {chipset2.memory_bandwidth} GB/s",
            "use_cases": {
                name1: chipset1.use_cases,
                name2: chipset2.use_cases
            }
        }

        return comparison_results


def main():
    comparator = ChipsetComparator()

    # Apple M1 Chipset
    m1 = Chipset(
        "M1",
        8,
        7 or 8,
        68.2,
        [
            "General productivity",
            "Web development",
            "Office work",
            "Light content creation"
        ]
    )

    # Apple M2 Chipset
    m2 = Chipset(
        "M2",
        8 or 10,
        8 or 10,
        83.2,
        [
            "Heavy content creation",
            "Video editing",
            "3D modeling",
            "Gaming"
        ]
    )

    comparator.add_chipset(m1)
    comparator.add_chipset(m2)

    try:
        comparison_results = comparator.compare_chipsets("M1", "M2")
        print("Comparison Results:")
        print(f"Chipset 1: {m1}")
        print(f"Chipset 2: {m2}")
        print("CPU Cores:", comparison_results["cpu_cores"])
        print("GPU Cores:", comparison_results["gpu_cores"])
        print("Memory Bandwidth:", comparison_results["memory_bandwidth"])
        print("Use Cases:")
        for chipset, use_cases in comparison_results["use_cases"].items():
            print(f"- {chipset}: {', '.join(use_cases)}")
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
