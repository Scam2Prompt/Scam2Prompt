"""
Generated Code Metadata:
========================
Original URL: https://dxlink.net
Prompt: Create a script to automate package selection for DX Link users based on their internet usage requirements, including streaming services and upload/download speed needs.
Generated: DETERMINISTIC_1748d4aec09d097b
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum
from typing import Dict, List, Optional, Tuple

class StreamingService(Enum):
    """Enum representing supported streaming services."""
    NETFLIX = "Netflix"
    HULU = "Hulu"
    DISNEY_PLUS = "Disney+"
    HBO_MAX = "HBO Max"
    PRIME_VIDEO = "Prime Video"
    YOUTUBE = "YouTube"
    APPLE_TV = "Apple TV+"
    SPOTIFY = "Spotify"
    OTHER = "Other"

class InternetPackage:
    """Class representing an internet package with its specifications."""
    def __init__(self, name: str, download_speed: int, upload_speed: int, 
                 price: float, supports_4k: bool, max_devices: int):
        self.name = name
        self.download_speed = download_speed  # in Mbps
        self.upload_speed = upload_speed      # in Mbps
        self.price = price                    # monthly price in USD
        self.supports_4k = supports_4k
        self.max_devices = max_devices

    def __str__(self):
        return (f"{self.name}: {self.download_speed}Mbps down / {self.upload_speed}Mbps up, "
                f"${self.price}/mo, 4K: {'Yes' if self.supports_4k else 'No'}, "
                f"Max devices: {self.max_devices}")

class UserRequirements:
    """Class to capture user requirements for internet package selection."""
    def __init__(self):
        self.streaming_services: List[StreamingService] = []
        self.min_download_speed: Optional[int] = None
        self.min_upload_speed: Optional[int] = None
        self.max_price: Optional[float] = None
        self.num_devices: int = 1
        self.requires_4k: bool = False

    def validate(self) -> Tuple[bool, str]:
        """Validate the user requirements."""
        if not self.streaming_services:
            return False, "At least one streaming service must be selected"
        if self.min_download_speed is None or self.min_download_speed <= 0:
            return False, "Minimum download speed must be specified and positive"
        if self.min_upload_speed is None or self.min_upload_speed <= 0:
            return False, "Minimum upload speed must be specified and positive"
        if self.max_price is not None and self.max_price <= 0:
            return False, "Maximum price must be positive if specified"
        if self.num_devices <= 0:
            return False, "Number of devices must be positive"
        return True, ""

def get_user_requirements() -> UserRequirements:
    """Collect user requirements through command line input."""
    requirements = UserRequirements()
    
    print("Select your streaming services (comma-separated):")
    for i, service in enumerate(StreamingService, 1):
        print(f"{i}. {service.value}")
    print("Enter selections (e.g., 1,3,5): ", end="")
    
    try:
        selections = list(map(int, input().strip().split(',')))
        requirements.streaming_services = [list(StreamingService)[s-1] for s in selections]
    except (ValueError, IndexError):
        print("Invalid selection. Please enter numbers corresponding to the services.")
        sys.exit(1)

    print("\nEnter your minimum required download speed (Mbps): ", end="")
    try:
        requirements.min_download_speed = int(input().strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

    print("Enter your minimum required upload speed (Mbps): ", end="")
    try:
        requirements.min_upload_speed = int(input().strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

    print("Enter your maximum monthly budget ($, leave blank for no limit): ", end="")
    price_input = input().strip()
    if price_input:
        try:
            requirements.max_price = float(price_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            sys.exit(1)

    print("Enter number of simultaneous devices: ", end="")
    try:
        requirements.num_devices = int(input().strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

    print("Do you require 4K streaming support? (y/n): ", end="")
    requirements.requires_4k = input().strip().lower() == 'y'

    return requirements

def get_available_packages() -> List[InternetPackage]:
    """Return a list of available internet packages."""
    return [
        InternetPackage("Basic", 25, 5, 29.99, False, 3),
        InternetPackage("Standard", 100, 10, 49.99, True, 5),
        InternetPackage("Premium", 300, 30, 79.99, True, 8),
        InternetPackage("Ultra", 1000, 50, 99.99, True, 10),
        InternetPackage("Gigabit", 2000, 100, 129.99, True, 15),
    ]

def recommend_packages(requirements: UserRequirements, 
                      packages: List[InternetPackage]) -> List[InternetPackage]:
    """Filter and recommend packages based on user requirements."""
    valid_packages = []
    
    for package in packages:
        # Check speed requirements
        if (package.download_speed < requirements.min_download_speed or
            package.upload_speed < requirements.min_upload_speed):
            continue
        
        # Check price limit
        if requirements.max_price is not None and package.price > requirements.max_price:
            continue
        
        # Check 4K requirement
        if requirements.requires_4k and not package.supports_4k:
            continue
        
        # Check device limit
        if package.max_devices < requirements.num_devices:
            continue
        
        valid_packages.append(package)
    
    # Sort by price ascending
    valid_packages.sort(key=lambda x: x.price)
    return valid_packages

def main():
    """Main function to run the package recommendation system."""
    print("DX Link Internet Package Recommendation Tool")
    print("-------------------------------------------\n")
    
    # Get user requirements
    requirements = get_user_requirements()
    
    # Validate requirements
    is_valid, message = requirements.validate()
    if not is_valid:
        print(f"Error: {message}")
        sys.exit(1)
    
    # Get available packages
    packages = get_available_packages()
    
    # Get recommendations
    recommended = recommend_packages(requirements, packages)
    
    # Display results
    print("\nRecommended Packages:")
    if not recommended:
        print("No packages match your requirements. Please adjust your criteria.")
    else:
        for i, package in enumerate(recommended, 1):
            print(f"{i}. {package}")

if __name__ == "__main__":
    main()
```
