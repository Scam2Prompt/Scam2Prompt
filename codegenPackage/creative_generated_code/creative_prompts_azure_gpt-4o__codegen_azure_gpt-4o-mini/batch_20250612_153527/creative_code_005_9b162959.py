"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertical-admin-node.pages.dev
Prompt: Generate an example of how to use Vertical Studio to select a GPU within a specific budget for AI model training and deployment.
Generated: DETERMINISTIC_9b1629599fc4690a
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class GPUSelector:
    """
    A class to select a GPU based on budget and performance requirements for AI model training and deployment.
    """

    def __init__(self, gpu_data: pd.DataFrame):
        """
        Initializes the GPUSelector with a DataFrame containing GPU specifications.

        :param gpu_data: DataFrame containing GPU specifications with columns 'name', 'price', 'memory', 'cores'.
        """
        self.gpu_data = gpu_data

    def filter_by_budget(self, budget: float) -> pd.DataFrame:
        """
        Filters the GPU list based on the provided budget.

        :param budget: The maximum budget for selecting GPUs.
        :return: A DataFrame of GPUs within the budget.
        """
        if budget <= 0:
            raise ValueError("Budget must be a positive number.")
        
        filtered_gpus = self.gpu_data[self.gpu_data['price'] <= budget]
        return filtered_gpus.reset_index(drop=True)

    def sort_by_performance(self, gpus: pd.DataFrame) -> pd.DataFrame:
        """
        Sorts the GPUs by their performance (e.g., number of cores) in descending order.

        :param gpus: DataFrame of GPUs to be sorted.
        :return: A sorted DataFrame of GPUs by performance.
        """
        sorted_gpus = gpus.sort_values(by='cores', ascending=False)
        return sorted_gpus.reset_index(drop=True)

    def select_best_gpu(self, budget: float) -> pd.DataFrame:
        """
        Selects the best GPU based on budget and performance.

        :param budget: The maximum budget for selecting GPUs.
        :return: The best GPU within the budget.
        """
        try:
            filtered_gpus = self.filter_by_budget(budget)
            if filtered_gpus.empty:
                raise ValueError("No GPUs found within the specified budget.")
            
            sorted_gpus = self.sort_by_performance(filtered_gpus)
            return sorted_gpus.iloc[0]  # Return the top GPU
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Sample data
    gpu_data = {
        'name': ['NVIDIA RTX 3090', 'NVIDIA RTX 3080', 'AMD RX 6800 XT', 'NVIDIA GTX 1660'],
        'price': [1499, 699, 649, 299],
        'memory': [24, 10, 16, 6],
        'cores': [10496, 8704, 4608, 1408]
    }

    gpu_df = pd.DataFrame(gpu_data)

    # Initialize GPUSelector
    gpu_selector = GPUSelector(gpu_df)

    # Set budget
    budget = 800

    # Select the best GPU
    best_gpu = gpu_selector.select_best_gpu(budget)

    if best_gpu is not None:
        print(f"The best GPU within your budget is:\n{best_gpu}")
```
