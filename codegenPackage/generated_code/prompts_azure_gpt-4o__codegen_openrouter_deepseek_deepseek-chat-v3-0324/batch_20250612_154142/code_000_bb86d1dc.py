"""
Generated Code Metadata:
========================
Original URL: https://segroegg.gitbook.io
Prompt: Write Python code to check the eligibility of a GPU for connection to the Aethir decentralized cloud network, referencing the steps outlined in the Aethir documentation.
Generated: DETERMINISTIC_bb86d1dc9dbb4b23
Batch ID: 20250612_154142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import json
import platform
import logging
from typing import Dict, Any, Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GPUEligibilityChecker:
    """
    Checks if a GPU meets the requirements for connection to the Aethir decentralized cloud network.
    """
    
    MIN_CUDA_VERSION = "11.0"
    MIN_VRAM_GB = 8
    SUPPORTED_ARCHITECTURES = ["Ampere", "Turing", "Pascal", "Volta"]
    
    def __init__(self):
        self.system_info = self._get_system_info()
    
    def _get_system_info(self) -> Dict[str, Any]:
        """Gather system information including OS, GPU details, and CUDA version."""
        system_info = {
            "os": platform.system(),
            "os_version": platform.version(),
            "gpu_info": self._get_gpu_info(),
            "cuda_version": self._get_cuda_version()
        }
        return system_info
    
    def _get_gpu_info(self) -> List[Dict[str, Any]]:
        """Retrieve GPU information using nvidia-smi."""
        try:
            result = subprocess.run(
                ["nvidia-smi", "--query-gpu=name,memory.total,driver_version,architecture", "--format=csv,noheader"],
                capture_output=True,
                text=True,
                check=True
            )
            
            gpus = []
            for line in result.stdout.strip().split('\n'):
                if not line.strip():
                    continue
                name, memory, driver_version, architecture = map(str.strip, line.split(','))
                gpus.append({
                    "name": name,
                    "memory_gb": int(memory.split()[0]) / 1024,
                    "driver_version": driver_version,
                    "architecture": architecture
                })
            return gpus
        
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to get GPU info: {e.stderr}")
            raise RuntimeError("Could not retrieve GPU information. Is nvidia-smi installed?")
        except Exception as e:
            logger.error(f"Unexpected error getting GPU info: {e}")
            raise RuntimeError("Unexpected error while retrieving GPU information")
    
    def _get_cuda_version(self) -> Optional[str]:
        """Check installed CUDA version."""
        try:
            result = subprocess.run(
                ["nvcc", "--version"],
                capture_output=True,
                text=True,
                check=True
            )
            version_line = result.stdout.split('\n')[-2]  # Last line is empty
            version = version_line.split()[-1]
            return version
        except subprocess.CalledProcessError:
            logger.warning("CUDA not found or nvcc not in PATH")
            return None
        except Exception as e:
            logger.error(f"Unexpected error checking CUDA version: {e}")
            return None
    
    def _compare_versions(self, version1: str, version2: str) -> int:
        """Compare two version strings (e.g., '11.0' vs '10.2')."""
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        for i in range(max(len(v1), len(v2))):
            n1 = v1[i] if i < len(v1) else 0
            n2 = v2[i] if i < len(v2) else 0
            
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        
        return 0
    
    def check_eligibility(self) -> Dict[str, Any]:
        """
        Check if the system meets all requirements for Aethir network.
        
        Returns:
            Dict containing eligibility status and detailed information.
        """
        results = {
            "eligible": True,
            "system_info": self.system_info,
            "requirements": {
                "min_cuda_version": self.MIN_CUDA_VERSION,
                "min_vram_gb": self.MIN_VRAM_GB,
                "supported_architectures": self.SUPPORTED_ARCHITECTURES
            },
            "issues": []
        }
        
        # Check if any GPU is present
        if not self.system_info["gpu_info"]:
            results["eligible"] = False
            results["issues"].append("No GPU detected")
            return results
        
        # Check CUDA version
        if not self.system_info["cuda_version"]:
            results["eligible"] = False
            results["issues"].append("CUDA not installed")
        elif self._compare_versions(self.system_info["cuda_version"], self.MIN_CUDA_VERSION) < 0:
            results["eligible"] = False
            results["issues"].append(
                f"CUDA version {self.system_info['cuda_version']} is below minimum required {self.MIN_CUDA_VERSION}"
            )
        
        # Check each GPU
        for gpu in self.system_info["gpu_info"]:
            # Check VRAM
            if gpu["memory_gb"] < self.MIN_VRAM_GB:
                results["eligible"] = False
                results["issues"].append(
                    f"GPU {gpu['name']} has insufficient VRAM: {gpu['memory_gb']}GB (minimum {self.MIN_VRAM_GB}GB)"
                )
            
            # Check architecture
            if gpu["architecture"] not in self.SUPPORTED_ARCHITECTURES:
                results["eligible"] = False
                results["issues"].append(
                    f"GPU {gpu['name']} architecture {gpu['architecture']} is not supported"
                )
        
        return results

def main():
    """Main function to check GPU eligibility."""
    try:
        checker = GPUEligibilityChecker()
        results = checker.check_eligibility()
        
        print("\nAethir GPU Eligibility Check Results:")
        print("=" * 40)
        print(f"System OS: {results['system_info']['os']} {results['system_info']['os_version']}")
        
        if results['system_info']['cuda_version']:
            print(f"CUDA Version: {results['system_info']['cuda_version']}")
        else:
            print("CUDA Version: Not detected")
        
        print("\nDetected GPUs:")
        for i, gpu in enumerate(results['system_info']['gpu_info'], 1):
            print(f"  GPU {i}: {gpu['name']}")
            print(f"    VRAM: {gpu['memory_gb']:.1f}GB")
            print(f"    Architecture: {gpu['architecture']}")
            print(f"    Driver Version: {gpu['driver_version']}")
        
        print("\nRequirements:")
        print(f"  Minimum CUDA Version: {results['requirements']['min_cuda_version']}")
        print(f"  Minimum VRAM: {results['requirements']['min_vram_gb']}GB")
        print(f"  Supported Architectures: {', '.join(results['requirements']['supported_architectures'])}")
        
        print("\nEligibility Status:", "PASS" if results['eligible'] else "FAIL")
        
        if results['issues']:
            print("\nIssues Found:")
            for issue in results['issues']:
                print(f"  - {issue}")
        
        print("\n" + "=" * 40)
        
    except Exception as e:
        logger.error(f"Failed to check eligibility: {e}")
        print("An error occurred while checking GPU eligibility. See logs for details.")

if __name__ == "__main__":
    main()
```
