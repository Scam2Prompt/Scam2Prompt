"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Illustrate how to build a comparison tool for Londritech's gaming PCs, highlighting differences in GPU and CPU performance.
Generated: DETERMINISTIC_4781e41468d7f88d
Batch ID: 20250612_162101
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class GamingPC:
    """
    A class to represent a gaming PC with its specifications.
    """

    def __init__(self, name, cpu, gpu, cpu_score, gpu_score):
        """
        Initializes a GamingPC instance.

        :param name: Name of the gaming PC
        :param cpu: CPU model
        :param gpu: GPU model
        :param cpu_score: Performance score of the CPU
        :param gpu_score: Performance score of the GPU
        """
        self.name = name
        self.cpu = cpu
        self.gpu = gpu
        self.cpu_score = cpu_score
        self.gpu_score = gpu_score

    def __repr__(self):
        return f"{self.name}: CPU({self.cpu}) - GPU({self.gpu})"

def compare_gaming_pcs(pc_list):
    """
    Compares a list of GamingPC instances and returns a DataFrame highlighting differences.

    :param pc_list: List of GamingPC instances
    :return: DataFrame containing comparison of CPU and GPU scores
    """
    # Create a DataFrame from the list of GamingPC instances
    data = {
        'Name': [pc.name for pc in pc_list],
        'CPU': [pc.cpu for pc in pc_list],
        'GPU': [pc.gpu for pc in pc_list],
        'CPU Score': [pc.cpu_score for pc in pc_list],
        'GPU Score': [pc.gpu_score for pc in pc_list],
    }
    
    df = pd.DataFrame(data)

    # Sort the DataFrame by CPU and GPU scores
    df_sorted = df.sort_values(by=['CPU Score', 'GPU Score'], ascending=False)
    
    return df_sorted

def main():
    """
    Main function to execute the comparison tool.
    """
    # List of gaming PCs to compare
    pcs = [
        GamingPC("PC A", "Intel i9-11900K", "NVIDIA RTX 3080", 3000, 9000),
        GamingPC("PC B", "AMD Ryzen 9 5900X", "NVIDIA RTX 3070", 2800, 8000),
        GamingPC("PC C", "Intel i7-11700K", "AMD RX 6800", 2500, 8500),
        GamingPC("PC D", "AMD Ryzen 5 5600X", "NVIDIA RTX 3060", 2200, 7000),
    ]

    try:
        # Compare the gaming PCs and print the results
        comparison_df = compare_gaming_pcs(pcs)
        print(comparison_df)
    except Exception as e:
        print(f"An error occurred during comparison: {e}")

if __name__ == "__main__":
    main()
```
