"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Develop a program that organizes label orders for different use cases, such as student travel, daycare, and retirement homes, based on the categories described on Etiquettetout.com.
Generated: DETERMINISTIC_41f1473eb960caa3
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Label Order Organizer for Etiquettetout.com

This program organizes label orders based on different use cases such as student travel,
daycare, and retirement homes. It allows users to select a category, specify order details,
and generates an organized order summary.

Features:
- Supports multiple label categories
- Validates user input
- Generates a formatted order summary
"""

class LabelOrder:
    """Represents a label order with category and details."""
    
    CATEGORIES = {
        'student_travel': {
            'name': 'Student Travel',
            'fields': ['student_name', 'class_grade', 'emergency_contact', 'allergies'],
            'description': 'Labels for student belongings during travel.'
        },
        'daycare': {
            'name': 'Daycare',
            'fields': ['child_name', 'parent_name', 'contact_number', 'special_instructions'],
            'description': 'Labels for daycare items and children.'
        },
        'retirement_home': {
            'name': 'Retirement Home',
            'fields': ['resident_name', 'room_number', 'medication_info', 'contact_person'],
            'description': 'Labels for personal belongings in retirement homes.'
        }
    }
    
    def __init__(self, category):
        """Initialize a label order with the specified category."""
        if category not in self.CATEGORIES:
            raise ValueError(f"Invalid category. Available categories: {list(self.CATEGORIES.keys())}")
        
        self.category = category
        self.details = {}
    
    def set_details(self, **kwargs):
        """Set order details based on category requirements."""
        required_fields = self.CATEGORIES[self.category]['fields']
        
        for field in required_fields:
            if field not in kwargs:
                raise ValueError(f"Missing required field: {field}")
            
            if not kwargs[field]:
                raise ValueError(f"Field '{field}' cannot be empty")
        
        self.details = kwargs
    
    def generate_summary(self):
        """Generate a formatted order summary."""
        category_info = self.CATEGORIES[self.category]
        summary = [
            f"\n--- Label Order Summary ---",
            f"Category: {category_info['name']}",
            f"Description: {category_info['description']}",
            "\nDetails:"
        ]
        
        for field, value in self.details.items():
            summary.append(f"- {field.replace('_', ' ').title()}: {value}")
        
        return '\n'.join(summary)


def get_user_input(prompt, required=True):
    """Helper function to get validated user input."""
    while True:
        user_input = input(prompt).strip()
        if not user_input and required:
            print("This field is required. Please try again.")
            continue
        return user_input


def main():
    """Main program function to handle user interaction."""
    print("Label Order Organizer")
    print("=====================\n")
    
    # Display available categories
    print("Available label categories:")
    for i, (key, category) in enumerate(LabelOrder.CATEGORIES.items(), 1):
        print(f"{i}. {category['name']} - {category['description']}")
    
    # Get category selection
    while True:
        try:
            selection = input("\nEnter the number of your category: ")
            category_key = list(LabelOrder.CATEGORIES.keys())[int(selection)-1]
            break
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")
    
    # Create order
    order = LabelOrder(category_key)
    
    # Get order details
    print(f"\nEnter details for {order.CATEGORIES[category_key]['name']} labels:")
    details = {}
    for field in order.CATEGORIES[category_key]['fields']:
        prompt = f"{field.replace('_', ' ').title()}: "
        details[field] = get_user_input(prompt)
    
    try:
        order.set_details(**details)
        print(order.generate_summary())
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
