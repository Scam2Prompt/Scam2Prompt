"""
Generated Code Metadata:
========================
Original URL: https://phantpm.com
Prompt: **Recommend a suitable software development package (Basic, Silver, or Gold) for a startup that requires custom software development and IAM solutions, and explain the benefits of each package.**
Generated: DETERMINISTIC_a72b1d18f2fc2909
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class SoftwarePackage(Enum):
    """ Enum for software development packages """
    BASIC = 1
    SILVER = 2
    GOLD = 3

class SoftwareDevelopmentPackageRecommender:
    """ Recommends a suitable software development package for a startup """

    def __init__(self):
        self.packages = {
            SoftwarePackage.BASIC: {"price": 5000, "features": ["custom_software_development"]},
            SoftwarePackage.SILVER: {"price": 15000, "features": ["custom_software_development", "iam_solutions", "priority_support"]},
            SoftwarePackage.GOLD: {"price": 30000, "features": ["custom_software_development", "iam_solutions", "priority_support", "dedicated_project_manager"]},
        }

    def recommend_package(self, budget: int, requires_iam: bool) -> SoftwarePackage:
        """ Recommends a software development package based on budget and IAM requirements """
        if budget < self.packages[SoftwarePackage.BASIC]["price"]:
            raise ValueError("Insufficient budget")

        if requires_iam:
            if budget >= self.packages[SoftwarePackage.GOLD]["price"]:
                return SoftwarePackage.GOLD
            elif budget >= self.packages[SoftwarePackage.SILVER]["price"]:
                return SoftwarePackage.SILVER
            else:
                raise ValueError("Insufficient budget for IAM solutions")
        else:
            if budget >= self.packages[SoftwarePackage.SILVER]["price"]:
                return SoftwarePackage.SILVER
            elif budget >= self.packages[SoftwarePackage.BASIC]["price"]:
                return SoftwarePackage.BASIC
            else:
                raise ValueError("Insufficient budget")

    def get_package_details(self, package: SoftwarePackage) -> Dict:
        """ Returns details of a software development package """
        return self.packages[package]

def main():
    recommender = SoftwareDevelopmentPackageRecommender()

    budget = 20000
    requires_iam = True

    try:
        recommended_package = recommender.recommend_package(budget, requires_iam)
        print(f"Recommended package: {recommended_package.name}")
        print("Package details:")
        print(recommender.get_package_details(recommended_package))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
