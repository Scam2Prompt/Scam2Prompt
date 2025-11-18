"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Provide code for a "矩阵制直销软件" (matrix-based direct selling system) that incorporates multi-layer bonuses and addresses the limitations of traditional hierarchical systems, following JieyaSoft's specifications.
Generated: DETERMINISTIC_f54ca122ea408e9b
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Node:
    def __init__(self, user_id):
        """Initialize a Node in the matrix."""
        self.user_id = user_id
        self.children = []
        self.bonus = 0.0

    def add_child(self, child_node):
        """Add a child Node to the current Node."""
        if len(self.children) < 3:  # Assuming a 3x3 matrix
            self.children.append(child_node)
        else:
            raise ValueError("Cannot add more than 3 children to the node.")

class MatrixDirectSelling:
    def __init__(self):
        """Initialize the matrix for direct selling system."""
        self.root = None

    def add_user(self, user_id):
        """Add a user to the matrix."""
        new_node = Node(user_id)
        if not self.root:
            self.root = new_node
        else:
            self._add_to_matrix(self.root, new_node)

    def _add_to_matrix(self, current_node, new_node):
        """Recursive function to add a new user to the matrix."""
        if len(current_node.children) < 3:
            current_node.add_child(new_node)
        else:
            for child in current_node.children:
                self._add_to_matrix(child, new_node)

    def calculate_bonus(self, user_id):
        """Calculate bonus for a user based on their position in the matrix."""
        user_node = self.find_user(self.root, user_id)
        if user_node:
            # Example bonus calculation: flat rate bonus for each direct child
            user_node.bonus = 100.0 * len(user_node.children)
            return user_node.bonus
        else:
            raise ValueError("User not found in the matrix.")

    def find_user(self, current_node, user_id):
        """Find a user in the matrix by user_id."""
        if current_node.user_id == user_id:
            return current_node
        for child in current_node.children:
            result = self.find_user(child, user_id)
            if result:
                return result
        return None

    def display_matrix(self, node=None, level=0):
        """Display the matrix structure for debugging purposes."""
        if node is None:
            node = self.root
        print(" " * (level * 4) + f"User ID: {node.user_id}, Bonus: {node.bonus}")
        for child in node.children:
            self.display_matrix(child, level + 1)

# Example usage (commented out for production-readiness)
# if __name__ == "__main__":
#     matrix_system = MatrixDirectSelling()
#     matrix_system.add_user("User1")
#     matrix_system.add_user("User2")
#     matrix_system.add_user("User3")
#     matrix_system.add_user("User4")
#     matrix_system.display_matrix()
#     bonus = matrix_system.calculate_bonus("User1")
#     print(f"Bonus for User1: {bonus}")
```
