"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Generate a code snippet that formats a list of items for labeling, suitable for use in a nursery or kindergarten, based on LabelMyStuff.com’s offerings.
Generated: DETERMINISTIC_d03e2d5b7b037579
Batch ID: 20250612_155944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Label Formatter for Nursery/Kindergarten Items

This script formats a list of items for labeling, suitable for use in a nursery or kindergarten.
The output follows LabelMyStuff.com's formatting standards.
"""

def format_labels(items, font_size=14, bold=True, uppercase=True, max_length=30):
    """
    Formats a list of items for labeling according to specified parameters.
    
    Args:
        items (list): List of strings representing items to be labeled
        font_size (int): Font size for labels (default 14)
        bold (bool): Whether to make labels bold (default True)
        uppercase (bool): Whether to convert labels to uppercase (default True)
        max_length (int): Maximum character length for each label (default 30)
    
    Returns:
        list: Formatted labels ready for printing
    
    Raises:
        ValueError: If items is not a list or contains non-string elements
    """
    if not isinstance(items, list):
        raise ValueError("Items must be provided as a list")
    
    formatted_labels = []
    
    for item in items:
        if not isinstance(item, str):
            raise ValueError(f"All items must be strings. Found: {type(item)}")
        
        # Process the label text
        label = item.strip()
        
        # Apply transformations
        if uppercase:
            label = label.upper()
        
        # Truncate if necessary
        if len(label) > max_length:
            label = label[:max_length-3] + "..."
        
        # Add formatting metadata
        formatted_label = {
            'text': label,
            'font_size': font_size,
            'bold': bold
        }
        
        formatted_labels.append(formatted_label)
    
    return formatted_labels


def print_formatted_labels(formatted_labels):
    """
    Prints formatted labels in a user-friendly way.
    
    Args:
        formatted_labels (list): List of formatted label dictionaries
    """
    print("\n--- FORMATTED LABELS ---")
    for i, label in enumerate(formatted_labels, 1):
        bold_text = "BOLD" if label['bold'] else "normal"
        print(f"{i}. {label['text']} (Size: {label['font_size']}, Weight: {bold_text})")


# Example usage
if __name__ == "__main__":
    try:
        sample_items = [
            "crayons",
            "construction paper",
            "building blocks",
            "story books",
            "paint brushes",
            "This is a very long label that will be truncated"
        ]
        
        labels = format_labels(sample_items)
        print_formatted_labels(labels)
        
    except ValueError as e:
        print(f"Error: {e}")
```
