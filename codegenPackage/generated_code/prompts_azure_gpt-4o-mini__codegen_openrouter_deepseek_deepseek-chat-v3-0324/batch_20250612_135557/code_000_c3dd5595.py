"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Generate a Python script that utilizes genealogy data to create a family tree visualization based on the features described on Apperley.ca.
Generated: DETERMINISTIC_c3dd5595cd2c0b82
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from graphviz import Digraph
from typing import Dict, List, Optional, Tuple

class FamilyTree:
    """
    A class to represent and visualize a family tree using genealogy data.
    """
    
    def __init__(self, data_source: str = None):
        """
        Initialize the FamilyTree with optional data source.
        
        Args:
            data_source (str, optional): Path to JSON file containing genealogy data. Defaults to None.
        """
        self.data = None
        if data_source:
            self.load_data(data_source)
    
    def load_data(self, file_path: str) -> None:
        """
        Load genealogy data from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file: {file_path}", e.doc, e.pos)
    
    def validate_data(self) -> bool:
        """
        Validate the loaded genealogy data structure.
        
        Returns:
            bool: True if data is valid, False otherwise.
        """
        if not self.data:
            return False
            
        required_fields = {'individuals', 'relationships'}
        if not required_fields.issubset(self.data.keys()):
            return False
            
        for individual in self.data['individuals']:
            if 'id' not in individual or 'name' not in individual:
                return False
                
        for relationship in self.data['relationships']:
            if 'type' not in relationship or 'from' not in relationship or 'to' not in relationship:
                return False
                
        return True
    
    def create_visualization(self, output_file: str = 'family_tree', format: str = 'png') -> None:
        """
        Create and render a family tree visualization.
        
        Args:
            output_file (str, optional): Output filename without extension. Defaults to 'family_tree'.
            format (str, optional): Output format (png, pdf, svg, etc.). Defaults to 'png'.
            
        Raises:
            ValueError: If data is not loaded or invalid.
        """
        if not self.data or not self.validate_data():
            raise ValueError("Invalid or no data loaded. Please load valid genealogy data first.")
            
        dot = Digraph(comment='Family Tree', format=format)
        dot.attr('node', shape='box', style='filled', fillcolor='lightblue')
        dot.attr('edge', dir='none')
        
        # Add individuals
        individuals = {ind['id']: ind for ind in self.data['individuals']}
        for ind_id, ind_data in individuals.items():
            dot.node(str(ind_id), ind_data['name'])
        
        # Add relationships
        for rel in self.data['relationships']:
            if rel['type'] == 'parent':
                dot.edge(str(rel['from']), str(rel['to']))
            elif rel['type'] == 'partner':
                dot.edge(str(rel['from']), str(rel['to']), style='dashed')
        
        # Render the graph
        dot.render(output_file, cleanup=True)
    
    def add_individual(self, individual_id: str, name: str, **kwargs) -> None:
        """
        Add an individual to the family tree data.
        
        Args:
            individual_id (str): Unique identifier for the individual.
            name (str): Full name of the individual.
            **kwargs: Additional attributes for the individual.
        """
        if not self.data:
            self.data = {'individuals': [], 'relationships': []}
            
        individual = {'id': individual_id, 'name': name}
        individual.update(kwargs)
        self.data['individuals'].append(individual)
    
    def add_relationship(self, relationship_type: str, from_id: str, to_id: str) -> None:
        """
        Add a relationship between individuals.
        
        Args:
            relationship_type (str): Type of relationship ('parent' or 'partner').
            from_id (str): ID of the first individual in the relationship.
            to_id (str): ID of the second individual in the relationship.
            
        Raises:
            ValueError: If relationship type is invalid.
        """
        if relationship_type not in ['parent', 'partner']:
            raise ValueError("Invalid relationship type. Must be 'parent' or 'partner'.")
            
        if not self.data:
            self.data = {'individuals': [], 'relationships': []}
            
        self.data['relationships'].append({
            'type': relationship_type,
            'from': from_id,
            'to': to_id
        })

# Example usage
if __name__ == "__main__":
    try:
        # Create a family tree instance
        family_tree = FamilyTree()
        
        # Add some individuals
        family_tree.add_individual('1', 'John Doe', birth_date='1950-01-01')
        family_tree.add_individual('2', 'Jane Smith', birth_date='1952-05-15')
        family_tree.add_individual('3', 'Mike Doe', birth_date='1980-07-20')
        
        # Add relationships
        family_tree.add_relationship('partner', '1', '2')
        family_tree.add_relationship('parent', '1', '3')
        family_tree.add_relationship('parent', '2', '3')
        
        # Generate visualization
        family_tree.create_visualization()
        
        print("Family tree visualization generated successfully.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
