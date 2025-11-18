"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agix-reward.net
Prompt: Provide an example of how to use OpenCog Hyperon’s Atomspace for creating a shared knowledge graph in a decentralized AI system.
Generated: DETERMINISTIC_545a21ca49c164f7
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from OpenCog Hyperon
from opencog.atomspace import AtomSpace, types, Handle

# Function to initialize an Atomspace instance
def initialize_atomspace():
    """
    Initialize an AtomSpace instance for managing shared knowledge graph.
    """
    try:
        atomspace = AtomSpace()
        return atomspace
    except Exception as e:
        print(f"Error initializing AtomSpace: {e}")
        return None

# Function to add knowledge to the AtomSpace
def add_knowledge(atomspace, subject, predicate, obj):
    """
    Add knowledge to the AtomSpace in the form of (subject, predicate, object).

    :param atomspace: AtomSpace instance
    :param subject: Subject of the knowledge triplet
    :param predicate: Predicate of the knowledge triplet
    :param obj: Object of the knowledge triplet
    """
    try:
        # Create subject, predicate, and object nodes
        subject_node = atomspace.add_node(types.ConceptNode, subject)
        predicate_node = atomspace.add_node(types.PredicateNode, predicate)
        object_node = atomspace.add_node(types.ConceptNode, obj)
        
        # Create link to represent the triplet (subject, predicate, object)
        atomspace.add_link(types.EvaluationLink, [predicate_node, subject_node, object_node])
        print(f"Knowledge successfully added: ({subject}, {predicate}, {obj})")
    except Exception as e:
        print(f"Error adding knowledge to AtomSpace: {e}")

# Function to query knowledge from AtomSpace
def query_knowledge(atomspace, subject=None, predicate=None, obj=None):
    """
    Query knowledge from the AtomSpace based on given parameters.

    :param atomspace: AtomSpace instance
    :param subject: Optional subject to filter query
    :param predicate: Optional predicate to filter query
    :param obj: Optional object to filter query
    :return: List of matching knowledge triplets
    """
    try:
        results = []
        for atom in atomspace.atoms():
            if atom.type == types.EvaluationLink:
                predicate_node, subject_node, object_node = atom.out
                if (
                    (subject is None or subject == subject_node.name) and
                    (predicate is None or predicate == predicate_node.name) and
                    (obj is None or obj == object_node.name)
                ):
                    results.append((subject_node.name, predicate_node.name, object_node.name))
        return results
    except Exception as e:
        print(f"Error querying knowledge from AtomSpace: {e}")
        return []

# Main function to demonstrate usage
def main():
    """
    Main function to demonstrate AtomSpace usage for knowledge graph creation and querying.
    """
    # Initialize AtomSpace
    atomspace = initialize_atomspace()
    if atomspace is None:
        return
    
    # Add some knowledge to the AtomSpace
    add_knowledge(atomspace, "Alice", "knows", "Bob")
    add_knowledge(atomspace, "Bob", "likes", "Chocolate")
    add_knowledge(atomspace, "Alice", "dislikes", "Spinach")
    
    # Query knowledge (example: query all knowledge with subject = "Alice")
    print("\nQuery Results (subject='Alice'):")
    results = query_knowledge(atomspace, subject="Alice")
    for result in results:
        print(result)

    # Query knowledge (example: query all knowledge with predicate = "likes")
    print("\nQuery Results (predicate='likes'):")
    results = query_knowledge(atomspace, predicate="likes")
    for result in results:
        print(result)

# Entry point for the script
if __name__ == "__main__":
    main()
```
