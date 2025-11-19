"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: "Compare the costs of different types of repairs (cosmetic, cosmetic+, investment, designer’s repair) offered by ПАНАМ for a 50m2 apartment, including materials and services included in each package."
Generated: DETERMINISTIC_40a0dcb6056af016
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RepairPackage:
    """
    Represents a repair package with its details and costs.
    """
    def __init__(self, name, description, cost_per_sqm, included_services):
        """
        Initialize a repair package.
        
        Args:
            name (str): Name of the package
            description (str): Description of the package
            cost_per_sqm (float): Cost per square meter
            included_services (list): List of services included
        """
        self.name = name
        self.description = description
        self.cost_per_sqm = cost_per_sqm
        self.included_services = included_services
    
    def calculate_total_cost(self, area):
        """
        Calculate total cost for given area.
        
        Args:
            area (float): Area in square meters
            
        Returns:
            float: Total cost
        """
        return self.cost_per_sqm * area
    
    def __str__(self):
        """
        String representation of the package.
        """
        services = "\n  - " + "\n  - ".join(self.included_services)
        return (f"Package: {self.name}\n"
                f"Description: {self.description}\n"
                f"Cost per m²: {self.cost_per_sqm} RUB\n"
                f"Included services:{services}")


def compare_repair_packages(area):
    """
    Compare different repair packages for a given area.
    
    Args:
        area (float): Area in square meters
        
    Returns:
        dict: Dictionary with package names as keys and total costs as values
    """
    packages = [
        RepairPackage(
            "Cosmetic",
            "Basic cosmetic repairs with standard materials",
            5000,
            [
                "Wall painting",
                "Floor covering installation",
                "Basic plumbing fixtures",
                "Standard electrical work"
            ]
        ),
        RepairPackage(
            "Cosmetic+",
            "Enhanced cosmetic repairs with better materials",
            7500,
            [
                "Premium wall painting",
                "Higher quality floor covering",
                "Improved plumbing fixtures",
                "Enhanced electrical work",
                "Basic lighting fixtures"
            ]
        ),
        RepairPackage(
            "Investment",
            "Repairs designed for rental properties with durable materials",
            10000,
            [
                "Durable wall finishes",
                "Wear-resistant flooring",
                "Quality plumbing fixtures",
                "Complete electrical work",
                "Basic kitchen installation",
                "Bathroom finishing"
            ]
        ),
        RepairPackage(
            "Designer's Repair",
            "Premium repairs with designer materials and supervision",
            15000,
            [
                "Designer wall finishes",
                "Premium flooring materials",
                "High-end plumbing fixtures",
                "Comprehensive electrical work",
                "Custom kitchen installation",
                "Luxury bathroom finishing",
                "Lighting design",
                "Designer supervision"
            ]
        )
    ]
    
    comparison = {}
    for package in packages:
        comparison[package.name] = {
            'total_cost': package.calculate_total_cost(area),
            'cost_per_sqm': package.cost_per_sqm,
            'description': package.description,
            'included_services': package.included_services
        }
    
    return comparison


def display_comparison(area):
    """
    Display comparison of repair packages in a user-friendly format.
    
    Args:
        area (float): Area in square meters
    """
    try:
        if area <= 0:
            raise ValueError("Area must be positive")
            
        comparison = compare_repair_packages(area)
        
        print(f"\nRepair Package Comparison for {area}m² apartment:\n")
        print("{:<15} {:<15} {:<20} {:<50}".format(
            "Package", "Cost/m²", "Total Cost", "Description"))
        print("-" * 100)
        
        for name, details in comparison.items():
            print("{:<15} {:<15} {:<20} {:<50}".format(
                name,
                f"{details['cost_per_sqm']} RUB",
                f"{details['total_cost']:,.0f} RUB",
                details['description'][:45] + "..."
            ))
        
        print("\nDetailed services included in each package:")
        for name, details in comparison.items():
            print(f"\n{name} Package Services:")
            for service in details['included_services']:
                print(f"  - {service}")
                
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    apartment_area = 50  # m²
    display_comparison(apartment_area)
```
