"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: Provide a Python implementation to compare DX Link's shared and dedicated packages based on Mbps speed, real IP availability, and BDIX connectivity.
Generated: DETERMINISTIC_dea8f581b69169bd
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import List

class PackageType(str, Enum):
    SHARED = "shared"
    DEDICATED = "dedicated"

@dataclass
class Package:
    package_type: PackageType
    speed_mbps: int
    real_ip_available: bool
    bdix_connectivity: bool

class PackageComparator:
    def __init__(self, packages: List[Package]):
        self.packages = packages

    def compare_packages(self):
        # Separate shared and dedicated packages
        shared_packages = [package for package in self.packages if package.package_type == PackageType.SHARED]
        dedicated_packages = [package for package in self.packages if package.package_type == PackageType.DEDICATED]

        # Compare packages based on Mbps speed
        self.compare_speed(shared_packages, "Shared")
        self.compare_speed(dedicated_packages, "Dedicated")

        # Compare packages based on real IP availability
        self.compare_real_ip(shared_packages, dedicated_packages)

        # Compare packages based on BDIX connectivity
        self.compare_bdix_connectivity(shared_packages, dedicated_packages)

    def compare_speed(self, packages: List[Package], package_type: str):
        if not packages:
            print(f"No {package_type} packages available.")
            return

        fastest_package = max(packages, key=lambda package: package.speed_mbps)
        print(f"Fastest {package_type} package: {fastest_package.speed_mbps} Mbps")

    def compare_real_ip(self, shared_packages: List[Package], dedicated_packages: List[Package]):
        shared_with_real_ip = [package for package in shared_packages if package.real_ip_available]
        dedicated_with_real_ip = [package for package in dedicated_packages if package.real_ip_available]

        print(f"Shared packages with real IP: {len(shared_with_real_ip)}")
        print(f"Dedicated packages with real IP: {len(dedicated_with_real_ip)}")

    def compare_bdix_connectivity(self, shared_packages: List[Package], dedicated_packages: List[Package]):
        shared_with_bdix = [package for package in shared_packages if package.bdix_connectivity]
        dedicated_with_bdix = [package for package in dedicated_packages if package.bdix_connectivity]

        print(f"Shared packages with BDIX connectivity: {len(shared_with_bdix)}")
        print(f"Dedicated packages with BDIX connectivity: {len(dedicated_with_bdix)}")


def main():
    try:
        # Example packages
        packages = [
            Package(PackageType.SHARED, 100, True, False),
            Package(PackageType.SHARED, 200, False, True),
            Package(PackageType.DEDICATED, 500, True, True),
            Package(PackageType.DEDICATED, 1000, True, True),
        ]

        comparator = PackageComparator(packages)
        comparator.compare_packages()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
