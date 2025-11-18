"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://readyplayai.com
Prompt: Create a Python script to manage AI clusters with automatic GPU provisioning and resource contention avoidance, as described in ReadyPlayAI's documentation.
Generated: DETERMINISTIC_7406bfc25f364453
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import psutil
import logging
from typing import List

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AIClusterManager:
    """
    A class to manage AI clusters with automatic GPU provisioning
    and resource contention avoidance.
    """

    def __init__(self):
        """
        Initialize the AI Cluster Manager.
        """
        self.gpus = self._detect_gpus()
        logging.info(f"Detected GPUs: {self.gpus}")

    def _detect_gpus(self) -> List[str]:
        """
        Detect available GPUs on the system.

        Returns:
            List of GPU IDs detected.
        """
        try:
            gpu_info = subprocess.check_output(["nvidia-smi", "--query-gpu=index", "--format=csv,noheader"], 
                                               universal_newlines=True)
            return gpu_info.strip().split("\n")
        except FileNotFoundError:
            logging.error("nvidia-smi not found. Ensure NVIDIA drivers are installed.")
            return []
        except Exception as e:
            logging.error(f"An error occurred while detecting GPUs: {e}")
            return []

    def _get_gpu_utilization(self, gpu_id: str) -> float:
        """
        Get the GPU utilization percentage for a specific GPU.

        Args:
            gpu_id (str): GPU ID.

        Returns:
            GPU utilization percentage as a float.
        """
        try:
            utilization_info = subprocess.check_output(
                ["nvidia-smi", "--query-gpu=utilization.gpu", "--id=" + gpu_id, "--format=csv,noheader"], 
                universal_newlines=True
            )
            return float(utilization_info.strip().replace('%', ''))
        except Exception as e:
            logging.error(f"Error fetching utilization for GPU {gpu_id}: {e}")
            return -1.0

    def _get_available_gpu(self) -> str:
        """
        Get the ID of the most available GPU based on utilization.

        Returns:
            GPU ID as a string or None if no GPU is available.
        """
        min_utilization = float('inf')
        available_gpu = None

        for gpu_id in self.gpus:
            utilization = self._get_gpu_utilization(gpu_id)
            if utilization >= 0 and utilization < min_utilization:
                min_utilization = utilization
                available_gpu = gpu_id

        if available_gpu is None:
            logging.warning("No available GPUs detected.")
        else:
            logging.info(f"Selected GPU {available_gpu} with utilization {min_utilization}%")

        return available_gpu

    def _check_cpu_memory(self):
        """
        Check CPU utilization and available memory for resource contention avoidance.
        
        Raises:
            RuntimeError: If CPU utilization or memory usage is too high.
        """
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()

        if cpu_usage > 90:
            raise RuntimeError(f"High CPU usage detected: {cpu_usage}%")
        
        if memory.percent > 90:
            raise RuntimeError(f"High memory usage detected: {memory.percent}%")

        logging.info(f"CPU usage: {cpu_usage}%, Memory usage: {memory.percent}%")

    def provision_resources(self) -> str:
        """
        Provision resources for AI workload.

        Returns:
            GPU ID allocated for the workload or None if provisioning fails.
        """
        try:
            # Check resource contention
            self._check_cpu_memory()

            # Select the best available GPU
            available_gpu = self._get_available_gpu()
            if available_gpu is not None:
                logging.info(f"Provisioned GPU {available_gpu} for AI workload.")
                return available_gpu

        except RuntimeError as e:
            logging.error(f"Resource contention detected: {e}")
        
        return None

    def run_workload(self, gpu_id: str, script_path: str):
        """
        Run AI workload on the provisioned GPU.

        Args:
            gpu_id (str): GPU ID to run the workload.
            script_path (str): Path to the script or executable to run.
        """
        if not gpu_id:
            logging.error("No GPU provisioned. Cannot run workload.")
            return

        if not os.path.exists(script_path):
            logging.error(f"Script not found: {script_path}")
            return

        try:
            env = os.environ.copy()
            env["CUDA_VISIBLE_DEVICES"] = gpu_id  # Set environment variable for GPU selection

            logging.info(f"Running workload on GPU {gpu_id} using script {script_path}")
            subprocess.run(["python", script_path], env=env, check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error while running workload: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Example usage
    manager = AIClusterManager()
    gpu_id = manager.provision_resources()
    workload_script = "path/to/your/ai_workload.py"  # Replace with actual script path
    manager.run_workload(gpu_id, workload_script)
```
