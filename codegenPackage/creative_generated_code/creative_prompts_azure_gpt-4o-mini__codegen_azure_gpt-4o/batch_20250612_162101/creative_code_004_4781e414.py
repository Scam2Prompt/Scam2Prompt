"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Illustrate how to build a comparison tool for Londritech's gaming PCs, highlighting differences in GPU and CPU performance.
Generated: DETERMINISTIC_4781e41468d7f88d
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# gaming_pc_comparator.py

import json

# Define the structure for a gaming PC comparison tool
class GamingPC:
    """
    Represents a gaming PC with attributes for name, GPU performance, and CPU performance.
    """
    def __init__(self, name, gpu_performance, cpu_performance):
        self.name = name
        self.gpu_performance = gpu_performance  # GPU performance score (higher is better)
        self.cpu_performance = cpu_performance  # CPU performance score (higher is better)

    def to_dict(self):
        """
        Converts the GamingPC instance to a dictionary for easy manipulation and comparison.
        """
        return {
            "Name": self.name,
            "GPU Performance": self.gpu_performance,
            "CPU Performance": self.cpu_performance
        }


def load_data(file_path):
    """
    Loads gaming PC data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of GamingPC objects.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        # Convert JSON data to GamingPC instances
        return [GamingPC(pc["Name"], pc["GPU Performance"], pc["CPU Performance"]) for pc in data]
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file {file_path}")
        return []


def compare_pcs(pc1, pc2):
    """
    Compares two gaming PCs and highlights the differences in GPU and CPU performance.

    Args:
        pc1 (GamingPC): The first gaming PC.
        pc2 (GamingPC): The second gaming PC.

    Returns:
        dict: A comparison dictionary highlighting differences.
    """
    comparison = {
        "GPU Comparison": f"{pc1.name}: {pc1.gpu_performance} vs {pc2.name}: {pc2.gpu_performance}",
        "CPU Comparison": f"{pc1.name}: {pc1.cpu_performance} vs {pc2.name}: {pc2.cpu_performance}"
    }

    # Highlight the better performance for GPU
    if pc1.gpu_performance > pc2.gpu_performance:
        comparison["GPU Winner"] = pc1.name
    elif pc1.gpu_performance < pc2.gpu_performance:
        comparison["GPU Winner"] = pc2.name
    else:
        comparison["GPU Winner"] = "Tie"

    # Highlight the better performance for CPU
    if pc1.cpu_performance > pc2.cpu_performance:
        comparison["CPU Winner"] = pc1.name
    elif pc1.cpu_performance < pc2.cpu_performance:
        comparison["CPU Winner"] = pc2.name
    else:
        comparison["CPU Winner"] = "Tie"

    return comparison


def main():
    """
    Main function to load data, allow user to select PCs for comparison, and display the results.
    """
    print("Welcome to Londritech's Gaming PC Comparison Tool!")

    # Load gaming PC data from a JSON file
    gaming_pcs = load_data("gaming_pcs.json")
    if not gaming_pcs:
        print("No data available. Exiting...")
        return

    # Display available PCs
    print("\nAvailable Gaming PCs:")
    for idx, pc in enumerate(gaming_pcs, start=1):
        print(f"{idx}. {pc.name}")

    # Allow user to select PCs for comparison
    try:
        pc1_index = int(input("\nSelect the first PC (enter the number): ")) - 1
        pc2_index = int(input("Select the second PC (enter the number): ")) - 1

        # Validate indices
        if pc1_index < 0 or pc1_index >= len(gaming_pcs) or pc2_index < 0 or pc2_index >= len(gaming_pcs):
            print("Error: Invalid selection. Exiting...")
            return

        pc1 = gaming_pcs[pc1_index]
        pc2 = gaming_pcs[pc2_index]

        # Perform comparison
        comparison_result = compare_pcs(pc1, pc2)

        # Display results
        print("\nComparison Results:")
        for key, value in comparison_result.items():
            print(f"{key}: {value}")

    except ValueError:
        print("Error: Please enter a valid number for selection.")


if __name__ == "__main__":
    main()
```

**Note:** This code assumes you have a `gaming_pcs.json` file containing an array of gaming PCs with attributes like name, GPU performance, and CPU performance. Example JSON file format:

```json
[
    {
        "Name": "Londritech Ultra",
        "GPU Performance": 85,
        "CPU Performance": 90
    },
    {
        "Name": "Londritech Pro",
        "GPU Performance": 78,
        "CPU Performance": 82
    }
]
```
