"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://readyplayai.com
Prompt: Generate code to implement GPU fractioning and oversubscription for optimizing AI compute resources, referencing the features offered by ReadyPlayAI.
Generated: DETERMINISTIC_81135766656ed3a0
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import torch
import os

class GPUResourceManager:
    """
    GPUResourceManager handles GPU fractioning and oversubscription
    for optimizing AI compute resources. This implementation is inspired
    by ReadyPlayAI's capabilities.
    """
    def __init__(self, fraction: float = 0.5, enable_oversubscription: bool = True):
        """
        Initialize the GPUResourceManager.

        :param fraction: Fraction of GPU memory to allocate (0.0 to 1.0).
        :param enable_oversubscription: Boolean flag to allow oversubscription.
        """
        if not (0.0 < fraction <= 1.0):
            raise ValueError("Fraction must be between 0.0 and 1.0.")
        self.fraction = fraction
        self.enable_oversubscription = enable_oversubscription

    def configure_gpu(self):
        """
        Configure the GPU settings based on the specified fraction and oversubscription.
        """
        if not torch.cuda.is_available():
            raise RuntimeError("No CUDA-compatible GPUs detected.")

        # Get the total number of GPUs available
        num_gpus = torch.cuda.device_count()
        print(f"Number of GPUs detected: {num_gpus}")

        for gpu_id in range(num_gpus):
            try:
                # Set the current device
                torch.cuda.set_device(gpu_id)

                # Get GPU properties
                device_properties = torch.cuda.get_device_properties(gpu_id)
                print(f"Configuring GPU {gpu_id}: {device_properties.name}")

                # Calculate memory allocation
                total_memory = device_properties.total_memory
                allocated_memory = int(total_memory * self.fraction)

                # Enable oversubscription if requested
                if not self.enable_oversubscription:
                    torch.cuda.set_per_process_memory_fraction(self.fraction, gpu_id)
                else:
                    os.environ["CUDA_DEVICE_MAX_CONNECTIONS"] = "32"  # Set max connections for oversubscription

                print(f"Allocated memory for GPU {gpu_id}: {allocated_memory / (1024 ** 3):.2f} GB")
            except Exception as e:
                print(f"Error configuring GPU {gpu_id}: {str(e)}")

    def get_gpu_stats(self):
        """
        Retrieve and display GPU stats such as memory usage and utilization.
        """
        if not torch.cuda.is_available():
            raise RuntimeError("No CUDA-compatible GPUs detected.")

        for gpu_id in range(torch.cuda.device_count()):
            try:
                torch.cuda.set_device(gpu_id)
                memory_reserved = torch.cuda.memory_reserved(gpu_id)
                memory_allocated = torch.cuda.memory_allocated(gpu_id)
                memory_free = memory_reserved - memory_allocated

                print(f"GPU {gpu_id} Stats:")
                print(f"  Memory Reserved: {memory_reserved / (1024 ** 3):.2f} GB")
                print(f"  Memory Allocated: {memory_allocated / (1024 ** 3):.2f} GB")
                print(f"  Memory Free: {memory_free / (1024 ** 3):.2f} GB")
            except Exception as e:
                print(f"Error retrieving stats for GPU {gpu_id}: {str(e)}")


# Usage example
if __name__ == "__main__":
    try:
        # Initialize the GPU resource manager with 50% memory allocation and oversubscription enabled
        gpu_manager = GPUResourceManager(fraction=0.5, enable_oversubscription=True)

        # Configure GPU settings
        gpu_manager.configure_gpu()

        # Get GPU stats
        gpu_manager.get_gpu_stats()
    except Exception as e:
        print(f"Application error: {str(e)}")
```
