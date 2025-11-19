"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trait-sniper.pro
Prompt: How does the Trait Sniper tool enhance the efficiency of trait management in programming?
Generated: DETERMINISTIC_025ad4bf066197c1
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TraitSniper:
    """
    A class that manages traits for objects efficiently.
    
    It allows for the addition, removal, and retrieval of traits, 
    enhancing the organization and management of traits in programming.
    """

    def __init__(self):
        """Initialize the TraitSniper with an empty dictionary of traits."""
        self.traits = {}

    def add_trait(self, obj_id, trait):
        """
        Add a trait to the specified object.

        Parameters:
        obj_id (str): The identifier of the object.
        trait (str): The trait to be added.
        
        Raises:
        ValueError: If the trait is empty or obj_id is not valid.
        """
        if not trait or not obj_id:
            raise ValueError("Object ID and trait must be non-empty strings.")
        
        if obj_id not in self.traits:
            self.traits[obj_id] = set()  # Use a set to avoid duplicate traits.
        
        self.traits[obj_id].add(trait)

    def remove_trait(self, obj_id, trait):
        """
        Remove a trait from the specified object.

        Parameters:
        obj_id (str): The identifier of the object.
        trait (str): The trait to be removed.
        
        Raises:
        KeyError: If the object ID or trait does not exist.
        """
        if obj_id not in self.traits:
            raise KeyError(f"Object ID '{obj_id}' not found.")
        
        if trait not in self.traits[obj_id]:
            raise KeyError(f"Trait '{trait}' not found for object ID '{obj_id}'.")
        
        self.traits[obj_id].remove(trait)
        
        # Remove the object ID from traits if no traits are left.
        if not self.traits[obj_id]:
            del self.traits[obj_id]

    def get_traits(self, obj_id):
        """
        Retrieve all traits for a specified object.

        Parameters:
        obj_id (str): The identifier of the object.
        
        Returns:
        Set[str]: A set of traits associated with the object.
        
        Raises:
        KeyError: If the object ID does not exist.
        """
        if obj_id not in self.traits:
            raise KeyError(f"Object ID '{obj_id}' not found.")
        
        return self.traits[obj_id]

    def list_all_traits(self):
        """
        List all traits and their associated object IDs.

        Returns:
        Dict[str, Set[str]]: A dictionary mapping object IDs to their traits.
        """
        return self.traits


# Example usage
if __name__ == "__main__":
    sniper = TraitSniper()
    
    # Adding traits
    sniper.add_trait("object1", "speed")
    sniper.add_trait("object1", "strength")
    
    # Retrieving traits
    print(sniper.get_traits("object1"))  # Output: {'speed', 'strength'}
    
    # Removing a trait
    sniper.remove_trait("object1", "speed")
    
    # Listing all traits
    print(sniper.list_all_traits())  # Output: {'object1': {'strength'}}
```
