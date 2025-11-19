"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: How can I implement a search function in a genealogy application to find ancestors by first name and surname, inspired by the search features on Apperley.ca?
Generated: DETERMINISTIC_029e9dc4c9180f98
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
import re

class Person:
    """Represents a person in the genealogy tree."""
    
    def __init__(self, first_name: str, surname: str, birth_year: Optional[int] = None):
        """
        Initialize a Person object.
        
        Args:
            first_name: First name of the person
            surname: Surname of the person
            birth_year: Optional birth year
        """
        self.first_name = first_name.strip()
        self.surname = surname.strip()
        self.birth_year = birth_year
        self.parents: List[Person] = []
        self.children: List[Person] = []
    
    def add_parent(self, parent: 'Person') -> None:
        """Add a parent to this person."""
        if parent not in self.parents:
            self.parents.append(parent)
            parent.children.append(self)
    
    def __repr__(self) -> str:
        return f"{self.first_name} {self.surname} ({self.birth_year})" if self.birth_year else f"{self.first_name} {self.surname}"

class GenealogyTree:
    """Represents a genealogy tree with search functionality."""
    
    def __init__(self):
        """Initialize an empty genealogy tree."""
        self.people: List[Person] = []
    
    def add_person(self, person: Person) -> None:
        """Add a person to the genealogy tree."""
        if person not in self.people:
            self.people.append(person)
    
    def search_ancestors(
        self, 
        first_name: str, 
        surname: str, 
        current_person: Person, 
        max_generations: int = 10
    ) -> List[Person]:
        """
        Search for ancestors of a person matching the given name.
        
        Args:
            first_name: First name to search for (case insensitive)
            surname: Surname to search for (case insensitive)
            current_person: Person to start search from
            max_generations: Maximum generations to search back
        
        Returns:
            List of matching ancestors ordered by generation (closest first)
        """
        matches = []
        visited = set()
        
        def _search(person: Person, generations: int) -> None:
            if generations > max_generations or person in visited:
                return
            
            visited.add(person)
            
            # Check if current person matches the search criteria
            if (re.match(first_name, person.first_name, re.IGNORECASE) and 
                re.match(surname, person.surname, re.IGNORECASE)):
                matches.append(person)
            
            # Recursively search parents
            for parent in person.parents:
                _search(parent, generations + 1)
        
        _search(current_person, 0)
        return matches
    
    def fuzzy_search(
        self,
        first_name: str = "",
        surname: str = "",
        birth_year: Optional[int] = None,
        threshold: float = 0.7
    ) -> List[Dict[str, any]]:
        """
        Perform a fuzzy search across all people in the tree.
        
        Args:
            first_name: Partial first name to search for
            surname: Partial surname to search for
            birth_year: Optional birth year to match exactly
            threshold: Similarity threshold (0-1)
        
        Returns:
            List of dictionaries with person info and match score
        """
        from difflib import SequenceMatcher
        
        results = []
        
        for person in self.people:
            score = 0
            matches = 0
            total = 0
            
            if first_name:
                ratio = SequenceMatcher(None, first_name.lower(), person.first_name.lower()).ratio()
                score += ratio
                total += 1
                if ratio >= threshold:
                    matches += 1
            
            if surname:
                ratio = SequenceMatcher(None, surname.lower(), person.surname.lower()).ratio()
                score += ratio
                total += 1
                if ratio >= threshold:
                    matches += 1
            
            if birth_year is not None:
                total += 1
                if person.birth_year == birth_year:
                    score += 1
                    matches += 1
            
            if total > 0:
                avg_score = score / total
                if matches > 0 or avg_score >= threshold:
                    results.append({
                        'person': person,
                        'score': avg_score,
                        'matches': matches
                    })
        
        # Sort by best matches first
        results.sort(key=lambda x: (-x['matches'], -x['score']))
        return results

# Example usage
if __name__ == "__main__":
    # Create a sample family tree
    tree = GenealogyTree()
    
    # Add people
    john = Person("John", "Smith", 1950)
    mary = Person("Mary", "Johnson", 1952)
    tree.add_person(john)
    tree.add_person(mary)
    
    # Add their child
    bob = Person("Bob", "Smith", 1980)
    bob.add_parent(john)
    bob.add_parent(mary)
    tree.add_person(bob)
    
    # Add John's parents
    william = Person("William", "Smith", 1920)
    elizabeth = Person("Elizabeth", "Brown", 1925)
    william.add_parent(Person("George", "Smith", 1890))
    tree.add_person(william)
    tree.add_person(elizabeth)
    john.add_parent(william)
    john.add_parent(elizabeth)
    
    # Search for ancestors
    print("Searching for ancestors of Bob Smith named John Smith:")
    ancestors = tree.search_ancestors("John", "Smith", bob)
    for ancestor in ancestors:
        print(f"Found ancestor: {ancestor}")
    
    # Fuzzy search example
    print("\nFuzzy search for 'Joh' in first names:")
    results = tree.fuzzy_search(first_name="Joh")
    for result in results:
        print(f"Match: {result['person']} (score: {result['score']:.2f})")
```
