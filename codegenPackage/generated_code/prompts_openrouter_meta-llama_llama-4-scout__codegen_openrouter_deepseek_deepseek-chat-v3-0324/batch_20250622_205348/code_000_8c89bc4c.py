"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: What are the main areas of operation for M. Giannetti Engenharia Ltda in the construction industry?
Generated: DETERMINISTIC_8c89bc4c73b9574b
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script provides information about M. Giannetti Engenharia Ltda's main areas of operation in construction

class ConstructionCompanyOperations:
    """
    Represents the main areas of operation for M. Giannetti Engenharia Ltda in construction.
    """
    
    def __init__(self):
        self.operations = {
            'residential': [
                'Apartment buildings',
                'Single-family homes',
                'Condominiums',
                'Residential complexes'
            ],
            'commercial': [
                'Office buildings',
                'Shopping centers',
                'Hotels',
                'Mixed-use developments'
            ],
            'industrial': [
                'Factories',
                'Warehouses',
                'Industrial plants',
                'Logistics centers'
            ],
            'infrastructure': [
                'Roads and highways',
                'Bridges',
                'Urban infrastructure',
                'Public works'
            ],
            'institutional': [
                'Schools and universities',
                'Hospitals',
                'Government buildings',
                'Cultural centers'
            ]
        }
    
    def get_operations(self):
        """
        Returns the company's main areas of operation in construction.
        
        Returns:
            dict: A dictionary containing the operation categories and their sub-areas.
        """
        return self.operations
    
    def get_operation_categories(self):
        """
        Returns the main categories of operations.
        
        Returns:
            list: A list of operation categories.
        """
        return list(self.operations.keys())
    
    def get_operations_by_category(self, category):
        """
        Returns the operations for a specific category.
        
        Args:
            category (str): The category to retrieve operations for.
            
        Returns:
            list: List of operations for the specified category.
            
        Raises:
            ValueError: If the category doesn't exist.
        """
        if category not in self.operations:
            raise ValueError(f"Invalid category: {category}. Available categories are: {list(self.operations.keys())}")
        return self.operations[category]


# Example usage
if __name__ == "__main__":
    company_operations = ConstructionCompanyOperations()
    
    try:
        # Get all operations
        all_ops = company_operations.get_operations()
        print("All Operations:", all_ops)
        
        # Get operation categories
        categories = company_operations.get_operation_categories()
        print("\nOperation Categories:", categories)
        
        # Get operations for a specific category
        residential_ops = company_operations.get_operations_by_category('residential')
        print("\nResidential Operations:", residential_ops)
        
        # Test error handling
        invalid_ops = company_operations.get_operations_by_category('nonexistent')
        
    except ValueError as e:
        print(f"\nError: {e}")
```
