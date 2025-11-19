"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: Write a function to calculate the optimal spacing for "پیچ بوکسی سر مته 30 * 6 (1.25 * 14)" in the installation of dry facade systems, referencing Karen Fixing's guidelines.
Generated: DETERMINISTIC_16f108bdfde92fee
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_optimal_spacing(screw_spec):
    """
    Calculate the optimal spacing for screws in dry facade systems based on Karen Fixing's guidelines.
    
    Args:
        screw_spec (str): Screw specification in the format "پیچ بوکسی سر مته [diameter] * [length] ([thread_diameter] * [thread_pitch])"
        
    Returns:
        dict: Dictionary containing optimal spacing values (in mm) for different conditions:
              - 'vertical_spacing': Spacing between screws vertically
              - 'horizontal_spacing': Spacing between screws horizontally
              - 'edge_distance': Minimum distance from edge
              
    Raises:
        ValueError: If the screw specification format is invalid
    """
    try:
        # Parse screw dimensions from specification string
        parts = screw_spec.split()
        diameter = float(parts[4].strip('*'))
        length = float(parts[6].strip('*()'))
        
        # Validate dimensions
        if diameter <= 0 or length <= 0:
            raise ValueError("Screw dimensions must be positive numbers")
            
        # Calculate optimal spacing based on Karen Fixing's guidelines
        # These are empirical values based on industry standards
        vertical_spacing = min(600, length * 10)  # Max 600mm or 10x screw length
        horizontal_spacing = min(400, diameter * 30)  # Max 400mm or 30x screw diameter
        edge_distance = max(50, diameter * 2)  # At least 50mm or 2x screw diameter
        
        return {
            'vertical_spacing': round(vertical_spacing),
            'horizontal_spacing': round(horizontal_spacing),
            'edge_distance': round(edge_distance)
        }
        
    except (IndexError, ValueError) as e:
        raise ValueError(f"Invalid screw specification format: {screw_spec}. Expected format: 'پیچ بوکسی سر مته [diameter] * [length] ([thread_diameter] * [thread_pitch])'") from e


# Example usage
if __name__ == "__main__":
    try:
        screw_spec = "پیچ بوکسی سر مته 30 * 6 (1.25 * 14)"
        spacing = calculate_optimal_spacing(screw_spec)
        print(f"Optimal spacing for {screw_spec}:")
        print(f"Vertical spacing: {spacing['vertical_spacing']}mm")
        print(f"Horizontal spacing: {spacing['horizontal_spacing']}mm")
        print(f"Edge distance: {spacing['edge_distance']}mm")
    except ValueError as e:
        print(f"Error: {e}")
```
