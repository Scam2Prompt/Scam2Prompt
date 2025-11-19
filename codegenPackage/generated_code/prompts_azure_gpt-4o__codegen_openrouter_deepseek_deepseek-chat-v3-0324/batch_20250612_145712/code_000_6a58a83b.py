"""
Generated Code Metadata:
========================
Original URL: https://meyerseim.com
Prompt: Write Python code to extract genealogical data from a database and organize it into family trees, referencing the Meyer/Seim families as an example.
Generated: DETERMINISTIC_6a58a83b66ea7eda
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional, Tuple
from collections import defaultdict

class FamilyTreeBuilder:
    """
    A class to extract genealogical data from a database and organize it into family trees.
    """
    
    def __init__(self, db_path: str = "genealogy.db"):
        """
        Initialize the FamilyTreeBuilder with a database connection.
        
        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        
    def connect(self) -> None:
        """Establish a connection to the database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            raise Exception(f"Database connection failed: {e}")
    
    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()
    
    def get_families(self, family_names: List[str] = ["Meyer", "Seim"]) -> Dict[str, Dict]:
        """
        Retrieve family data for specified family names.
        
        Args:
            family_names: List of family names to query.
            
        Returns:
            Dictionary containing family trees for each family name.
        """
        if not self.conn:
            self.connect()
            
        family_trees = {}
        
        try:
            for family_name in family_names:
                # Get all individuals with this family name
                self.cursor.execute(
                    "SELECT id, first_name, last_name, birth_date, death_date, gender "
                    "FROM individuals WHERE last_name = ?", 
                    (family_name,)
                )
                individuals = self.cursor.fetchall()
                
                # Get all relationships
                self.cursor.execute(
                    "SELECT id, individual1_id, individual2_id, relationship_type "
                    "FROM relationships WHERE individual1_id IN "
                    "(SELECT id FROM individuals WHERE last_name = ?) "
                    "OR individual2_id IN (SELECT id FROM individuals WHERE last_name = ?)",
                    (family_name, family_name)
                )
                relationships = self.cursor.fetchall()
                
                # Build family tree structure
                family_tree = self._build_family_tree(individuals, relationships)
                family_trees[family_name] = family_tree
                
        except sqlite3.Error as e:
            raise Exception(f"Database query failed: {e}")
            
        return family_trees
    
    def _build_family_tree(
        self, 
        individuals: List[Tuple], 
        relationships: List[Tuple]
    ) -> Dict:
        """
        Build a family tree structure from individuals and relationships.
        
        Args:
            individuals: List of individual records from database.
            relationships: List of relationship records from database.
            
        Returns:
            Dictionary representing the family tree structure.
        """
        # Create individual nodes
        tree = {}
        individuals_by_id = {}
        
        for ind in individuals:
            ind_id = ind[0]
            individuals_by_id[ind_id] = {
                "id": ind_id,
                "first_name": ind[1],
                "last_name": ind[2],
                "birth_date": ind[3],
                "death_date": ind[4],
                "gender": ind[5],
                "parents": [],
                "children": [],
                "spouses": []
            }
            tree[ind_id] = individuals_by_id[ind_id]
        
        # Process relationships
        for rel in relationships:
            rel_id, ind1_id, ind2_id, rel_type = rel
            
            if rel_type == "parent_child":
                # ind1 is parent of ind2
                tree[ind1_id]["children"].append(ind2_id)
                tree[ind2_id]["parents"].append(ind1_id)
            elif rel_type == "marriage":
                # ind1 and ind2 are spouses
                tree[ind1_id]["spouses"].append(ind2_id)
                tree[ind2_id]["spouses"].append(ind1_id)
                
        return tree
    
    def find_roots(self, family_tree: Dict) -> List[int]:
        """
        Find root individuals in a family tree (those with no parents).
        
        Args:
            family_tree: Family tree structure.
            
        Returns:
            List of root individual IDs.
        """
        roots = []
        for ind_id, ind_data in family_tree.items():
            if not ind_data["parents"]:
                roots.append(ind_id)
        return roots
    
    def print_family_tree(
        self, 
        family_tree: Dict, 
        current_id: int, 
        level: int = 0, 
        visited: Optional[set] = None
    ) -> None:
        """
        Print a family tree starting from a given individual.
        
        Args:
            family_tree: Family tree structure.
            current_id: ID of the current individual to print.
            level: Current depth in the tree (for indentation).
            visited: Set of already visited individuals to prevent cycles.
        """
        if visited is None:
            visited = set()
            
        if current_id in visited:
            return
            
        visited.add(current_id)
        person = family_tree[current_id]
        
        # Print current person with proper indentation
        indent = "  " * level
        print(f"{indent}- {person['first_name']} {person['last_name']} "
              f"({person['birth_date']} - {person['death_date']})")
        
        # Print spouses
        for spouse_id in person["spouses"]:
            if spouse_id not in visited:
                spouse = family_tree[spouse_id]
                print(f"{indent}  m. {spouse['first_name']} {spouse['last_name']}")
        
        # Recursively print children
        for child_id in person["children"]:
            self.print_family_tree(family_tree, child_id, level + 1, visited)


# Example usage
if __name__ == "__main__":
    try:
        builder = FamilyTreeBuilder()
        family_trees = builder.get_families(["Meyer", "Seim"])
        
        for family_name, family_tree in family_trees.items():
            print(f"\nFamily Tree for {family_name}:")
            roots = builder.find_roots(family_tree)
            for root_id in roots:
                builder.print_family_tree(family_tree, root_id)
                
    except Exception as e:
        print(f"Error: {e}")
    finally:
        builder.close()
```
