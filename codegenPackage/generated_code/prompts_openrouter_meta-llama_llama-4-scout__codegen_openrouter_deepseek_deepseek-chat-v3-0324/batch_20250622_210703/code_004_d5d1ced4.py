"""
Generated Code Metadata:
========================
Original URL: https://otoekspertiz.com.tr
Prompt: Write a code snippet to compare the features of different vehicle inspection packages (e.g., KB Paket, MM Paket, EKS Paket) offered by Computest Oto Ekspertiz and recommend the most suitable package based on user input.
Generated: DETERMINISTIC_d5d1ced4fd575c04
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class VehicleInspectionPackage:
    def __init__(self, name, price, features):
        """
        Initialize a vehicle inspection package.
        
        Args:
            name (str): Name of the package
            price (float): Price of the package
            features (dict): Dictionary of features with boolean values
        """
        self.name = name
        self.price = price
        self.features = features
    
    def has_feature(self, feature_name):
        """Check if package includes a specific feature."""
        return self.features.get(feature_name, False)
    
    def __str__(self):
        """String representation of the package."""
        return f"{self.name} (${self.price:.2f})"

class PackageRecommender:
    def __init__(self):
        """Initialize the recommender with available packages."""
        self.packages = [
            VehicleInspectionPackage(
                "KB Paket",
                99.99,
                {
                    "basic_inspection": True,
                    "road_test": False,
                    "computer_diagnostics": False,
                    "detailed_report": False
                }
            ),
            VehicleInspectionPackage(
                "MM Paket",
                149.99,
                {
                    "basic_inspection": True,
                    "road_test": True,
                    "computer_diagnostics": False,
                    "detailed_report": True
                }
            ),
            VehicleInspectionPackage(
                "EKS Paket",
                199.99,
                {
                    "basic_inspection": True,
                    "road_test": True,
                    "computer_diagnostics": True,
                    "detailed_report": True
                }
            )
        ]
    
    def get_package_by_name(self, name):
        """Get package by its name."""
        for package in self.packages:
            if package.name.lower() == name.lower():
                return package
        return None
    
    def recommend_package(self, required_features, max_budget=None):
        """
        Recommend the most suitable package based on requirements.
        
        Args:
            required_features (list): List of required feature names
            max_budget (float, optional): Maximum budget constraint
            
        Returns:
            VehicleInspectionPackage: Recommended package or None if no match
        """
        suitable_packages = []
        
        for package in self.packages:
            # Skip if budget constraint is not met
            if max_budget is not None and package.price > max_budget:
                continue
            
            # Check if all required features are present
            has_all_features = all(package.has_feature(feat) for feat in required_features)
            
            if has_all_features:
                suitable_packages.append(package)
        
        if not suitable_packages:
            return None
        
        # Return the cheapest suitable package
        return min(suitable_packages, key=lambda x: x.price)
    
    def compare_packages(self):
        """Print a comparison table of all packages."""
        print("\nPackage Comparison:")
        print("{:<10} {:<10} {:<20} {:<20} {:<20} {:<20}".format(
            "Package", "Price", "Basic Inspection", "Road Test", 
            "Computer Diagnostics", "Detailed Report"
        ))
        
        for package in self.packages:
            print("{:<10} ${:<9.2f} {:<20} {:<20} {:<20} {:<20}".format(
                package.name,
                package.price,
                "✓" if package.has_feature("basic_inspection") else "✗",
                "✓" if package.has_feature("road_test") else "✗",
                "✓" if package.has_feature("computer_diagnostics") else "✗",
                "✓" if package.has_feature("detailed_report") else "✗"
            ))

def get_user_input():
    """Collect user requirements for package recommendation."""
    print("Available features:")
    print("- basic_inspection\n- road_test\n- computer_diagnostics\n- detailed_report")
    
    features = input("Enter required features (comma separated): ").strip().lower()
    features = [f.strip() for f in features.split(",") if f.strip()]
    
    budget = input("Enter maximum budget (leave blank for no limit): ").strip()
    try:
        budget = float(budget) if budget else None
    except ValueError:
        print("Invalid budget input. Ignoring budget constraint.")
        budget = None
    
    return features, budget

def main():
    """Main program flow."""
    recommender = PackageRecommender()
    
    print("Welcome to Computest Oto Ekspertiz Package Recommender")
    recommender.compare_packages()
    
    while True:
        print("\nOptions:")
        print("1. Get package recommendation")
        print("2. Compare packages")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            features, budget = get_user_input()
            recommended = recommender.recommend_package(features, budget)
            
            if recommended:
                print(f"\nRecommended package: {recommended}")
            else:
                print("\nNo suitable package found matching your requirements.")
        
        elif choice == "2":
            recommender.compare_packages()
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
