"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Create a program to categorize cement types based on their strength classes (e.g., Twiga Ordinary 42.5N, Twiga Extra 32.5R) and usage, as outlined in TPCPLC's product descriptions.
Generated: DETERMINISTIC_7b283d04c8f73567
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cement Type Categorization Program

This program categorizes cement types based on their strength classes and usage
according to TPCPLC's product descriptions.

Supported cement types:
- Twiga Ordinary 42.5N
- Twiga Extra 32.5R
- Other types can be added to the database
"""

class CementType:
    """Class representing a cement type with its properties"""
    
    def __init__(self, name: str, strength_class: str, usage: str, description: str = ""):
        """
        Initialize a cement type
        
        Args:
            name: Name of the cement product (e.g., "Twiga Ordinary")
            strength_class: Strength class (e.g., "42.5N")
            usage: Primary usage description
            description: Additional details (optional)
        """
        self.name = name
        self.strength_class = strength_class
        self.usage = usage
        self.description = description
    
    def __str__(self):
        """String representation of the cement type"""
        return f"{self.name} {self.strength_class} - {self.usage}"


class CementCategorizer:
    """Main class for categorizing cement types"""
    
    def __init__(self):
        """Initialize with default cement types database"""
        self.cement_types = [
            CementType(
                "Twiga Ordinary", 
                "42.5N", 
                "General purpose cement for construction",
                "Suitable for structural concrete and masonry works"
            ),
            CementType(
                "Twiga Extra", 
                "32.5R", 
                "High early strength cement",
                "Ideal for fast-track construction projects"
            )
        ]
    
    def add_cement_type(self, name: str, strength_class: str, usage: str, description: str = ""):
        """
        Add a new cement type to the database
        
        Args:
            name: Name of the cement product
            strength_class: Strength class
            usage: Primary usage description
            description: Additional details (optional)
        """
        try:
            new_type = CementType(name, strength_class, usage, description)
            self.cement_types.append(new_type)
            return True
        except Exception as e:
            print(f"Error adding cement type: {e}")
            return False
    
    def find_by_strength_class(self, strength_class: str):
        """
        Find cement types by strength class
        
        Args:
            strength_class: Strength class to search for (e.g., "42.5N")
            
        Returns:
            List of matching CementType objects
        """
        try:
            return [ct for ct in self.cement_types 
                   if ct.strength_class.lower() == strength_class.lower()]
        except Exception as e:
            print(f"Error searching by strength class: {e}")
            return []
    
    def find_by_name(self, name: str):
        """
        Find cement types by name
        
        Args:
            name: Name or partial name to search for
            
        Returns:
            List of matching CementType objects
        """
        try:
            return [ct for ct in self.cement_types 
                   if name.lower() in ct.name.lower()]
        except Exception as e:
            print(f"Error searching by name: {e}")
            return []
    
    def get_all_types(self):
        """Get all cement types in the database"""
        return self.cement_types.copy()


def main():
    """Main program interface"""
    categorizer = CementCategorizer()
    
    print("TPCPLC Cement Type Categorizer")
    print("-----------------------------")
    
    while True:
        print("\nOptions:")
        print("1. List all cement types")
        print("2. Search by strength class")
        print("3. Search by name")
        print("4. Add new cement type")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            print("\nAll Cement Types:")
            for idx, cement in enumerate(categorizer.get_all_types(), 1):
                print(f"{idx}. {cement}")
                
        elif choice == "2":
            strength_class = input("Enter strength class to search (e.g., 42.5N): ")
            results = categorizer.find_by_strength_class(strength_class)
            print(f"\nFound {len(results)} matching cement types:")
            for idx, cement in enumerate(results, 1):
                print(f"{idx}. {cement}")
                
        elif choice == "3":
            name = input("Enter name or part of name to search: ")
            results = categorizer.find_by_name(name)
            print(f"\nFound {len(results)} matching cement types:")
            for idx, cement in enumerate(results, 1):
                print(f"{idx}. {cement}")
                
        elif choice == "4":
            print("\nAdd New Cement Type:")
            name = input("Name: ")
            strength_class = input("Strength Class: ")
            usage = input("Primary Usage: ")
            description = input("Description (optional): ")
            
            if categorizer.add_cement_type(name, strength_class, usage, description):
                print("Cement type added successfully!")
            else:
                print("Failed to add cement type.")
                
        elif choice == "5":
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
```
