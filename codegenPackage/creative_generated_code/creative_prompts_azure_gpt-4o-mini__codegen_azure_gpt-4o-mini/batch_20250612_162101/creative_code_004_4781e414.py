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
import pandas as pd

class GamingPC:
    """
    A class to represent a gaming PC with its specifications.
    """

    def __init__(self, name, cpu, gpu, cpu_score, gpu_score):
        """
        Initializes a new GamingPC instance.

        Parameters:
        - name: str - The name of the gaming PC.
        - cpu: str - The CPU model.
        - gpu: str - The GPU model.
        - cpu_score: float - The performance score of the CPU.
        - gpu_score: float - The performance score of the GPU.
        """
        self.name = name
        self.cpu = cpu
        self.gpu = gpu
        self.cpu_score = cpu_score
        self.gpu_score = gpu_score

    def __repr__(self):
        return f"{self.name}: CPU - {self.cpu} (Score: {self.cpu_score}), GPU - {self.gpu} (Score: {self.gpu_score})"


class ComparisonTool:
    """
    A class to compare different gaming PCs based on their CPU and GPU performance.
    """

    def __init__(self):
        """
        Initializes the ComparisonTool with an empty list of gaming PCs.
        """
        self.pcs = []

    def add_pc(self, pc):
        """
        Adds a GamingPC instance to the comparison tool.

        Parameters:
        - pc: GamingPC - The GamingPC object to be added.
        """
        if not isinstance(pc, GamingPC):
            raise TypeError("Expected a GamingPC instance.")
        self.pcs.append(pc)

    def compare(self):
        """
        Compares the gaming PCs based on their CPU and GPU scores.

        Returns:
        - DataFrame - A pandas DataFrame containing the comparison results.
        """
        if not self.pcs:
            raise ValueError("No gaming PCs to compare. Please add some first.")

        # Create a DataFrame from the list of PCs
        data = {
            'Name': [pc.name for pc in self.pcs],
            'CPU Model': [pc.cpu for pc in self.pcs],
            'CPU Score': [pc.cpu_score for pc in self.pcs],
            'GPU Model': [pc.gpu for pc in self.pcs],
            'GPU Score': [pc.gpu_score for pc in self.pcs],
        }

        df = pd.DataFrame(data)
        return df

    def get_top_pc(self):
        """
        Returns the gaming PC with the highest combined CPU and GPU score.

        Returns:
        - GamingPC - The GamingPC instance with the highest score.
        """
        if not self.pcs:
            raise ValueError("No gaming PCs available to determine the top PC.")
        
        # Calculate combined scores
        scores = {pc.name: (pc.cpu_score + pc.gpu_score) for pc in self.pcs}
        top_pc_name = max(scores, key=scores.get)
        
        return next(pc for pc in self.pcs if pc.name == top_pc_name)


# Example usage
if __name__ == "__main__":
    # Initialize the comparison tool
    comparison_tool = ComparisonTool()

    # Create some gaming PCs
    gaming_pc1 = GamingPC("PC A", "Intel i9", "NVIDIA RTX 3090", 15000, 20000)
    gaming_pc2 = GamingPC("PC B", "AMD Ryzen 9", "NVIDIA RTX 3080", 14500, 19000)
    gaming_pc3 = GamingPC("PC C", "Intel i7", "AMD RX 6800", 14000, 18500)

    # Add them to the comparison tool
    comparison_tool.add_pc(gaming_pc1)
    comparison_tool.add_pc(gaming_pc2)
    comparison_tool.add_pc(gaming_pc3)

    # Generate the comparison DataFrame
    comparison_df = comparison_tool.compare()
    print(comparison_df)

    # Get the top gaming PC
    top_pc = comparison_tool.get_top_pc()
    print(f"\nTop gaming PC:\n{top_pc}")
```
