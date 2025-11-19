"""
Generated Code Metadata:
========================
Original URL: https://aethiredge.tw
Prompt: Compare the features of Aethir Edge with other decentralized cloud computing devices, focusing on Qualcomm chip efficiency and end-to-end encryption.
Generated: DETERMINISTIC_3fdebfb030539f8c
Batch ID: 20250622_211241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class EncryptionType(Enum):
    """Enum representing different types of encryption."""
    AES_256 = "AES-256"
    RSA_4096 = "RSA-4096"
    ECC = "Elliptic Curve Cryptography"

@dataclass
class DeviceSpecs:
    """Dataclass to store device specifications."""
    name: str
    chip_model: str
    cpu_cores: int
    ram_gb: int
    storage_gb: int
    encryption: EncryptionType
    power_consumption_w: float

@dataclass
class ComparisonResult:
    """Dataclass to store comparison results."""
    device_name: str
    chip_efficiency: float  # Higher is better
    encryption_strength: int  # Higher is better

class DeviceComparator:
    """Class to compare decentralized cloud computing devices."""
    
    def __init__(self, devices: List[DeviceSpecs]):
        """Initialize with a list of devices to compare."""
        self.devices = devices
    
    def _calculate_chip_efficiency(self, device: DeviceSpecs) -> float:
        """
        Calculate chip efficiency based on Qualcomm chip performance.
        Higher values indicate better efficiency.
        """
        qualcomm_chips = {
            "Snapdragon 888": 1.8,
            "Snapdragon 8 Gen 1": 2.0,
            "Snapdragon 8+ Gen 1": 2.2,
            "Snapdragon 8 Gen 2": 2.5,
        }
        base_efficiency = qualcomm_chips.get(device.chip_model, 1.0)
        return base_efficiency * (device.cpu_cores / device.power_consumption_w)
    
    def _calculate_encryption_strength(self, device: DeviceSpecs) -> int:
        """Assign a score based on encryption type. Higher is stronger."""
        encryption_scores = {
            EncryptionType.AES_256: 3,
            EncryptionType.RSA_4096: 4,
            EncryptionType.ECC: 5,
        }
        return encryption_scores.get(device.encryption, 0)
    
    def compare_devices(self) -> List[ComparisonResult]:
        """
        Compare all devices based on chip efficiency and encryption strength.
        
        Returns:
            List of ComparisonResult objects sorted by chip efficiency (descending).
        """
        results = []
        for device in self.devices:
            efficiency = self._calculate_chip_efficiency(device)
            encryption = self._calculate_encryption_strength(device)
            results.append(
                ComparisonResult(
                    device_name=device.name,
                    chip_efficiency=efficiency,
                    encryption_strength=encryption
                )
            )
        
        # Sort by chip efficiency (descending)
        return sorted(results, key=lambda x: x.chip_efficiency, reverse=True)
    
    def to_json(self, results: List[ComparisonResult]) -> str:
        """Convert comparison results to JSON format."""
        return json.dumps([result.__dict__ for result in results], indent=2)

# Example Usage
if __name__ == "__main__":
    # Sample device specifications
    devices = [
        DeviceSpecs(
            name="Aethir Edge",
            chip_model="Snapdragon 8 Gen 2",
            cpu_cores=8,
            ram_gb=16,
            storage_gb=512,
            encryption=EncryptionType.ECC,
            power_consumption_w=5.0
        ),
        DeviceSpecs(
            name="Competitor A",
            chip_model="Snapdragon 8+ Gen 1",
            cpu_cores=8,
            ram_gb=12,
            storage_gb=256,
            encryption=EncryptionType.AES_256,
            power_consumption_w=6.0
        ),
        DeviceSpecs(
            name="Competitor B",
            chip_model="Snapdragon 888",
            cpu_cores=8,
            ram_gb=8,
            storage_gb=128,
            encryption=EncryptionType.RSA_4096,
            power_consumption_w=7.0
        ),
    ]
    
    try:
        comparator = DeviceComparator(devices)
        results = comparator.compare_devices()
        print(comparator.to_json(results))
    except Exception as e:
        print(f"An error occurred during device comparison: {e}")
```
