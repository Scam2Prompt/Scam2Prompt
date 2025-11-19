"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Develop a library function that formats and displays promotional offers for dining tables and chairs, referencing specific items like "Помощна масичка" and "Столове Eлдорадо."
Generated: DETERMINISTIC_d76f1b0c10e6d80f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def format_promotional_offers(dining_tables, chairs):
    """
    Formats and displays promotional offers for dining tables and chairs.
    
    Args:
        dining_tables (list): List of dictionaries containing dining table information.
                             Each dictionary should have 'name' and 'discount' keys.
        chairs (list): List of dictionaries containing chair information.
                       Each dictionary should have 'name' and 'discount' keys.
    
    Returns:
        str: Formatted promotional message with all offers.
    
    Raises:
        ValueError: If input is not in the expected format.
    """
    if not isinstance(dining_tables, list) or not isinstance(chairs, list):
        raise ValueError("Both dining_tables and chairs must be lists")
    
    for item in dining_tables + chairs:
        if not isinstance(item, dict) or 'name' not in item or 'discount' not in item:
            raise ValueError("Each item must be a dictionary with 'name' and 'discount' keys")
    
    promotional_message = "🌟 Специални промоционални оферти 🌟\n\n"
    
    if dining_tables:
        promotional_message += "🪑 Маси за вашата трапезария:\n"
        for table in dining_tables:
            promotional_message += f"- {table['name']}: {table['discount']}% отстъпка\n"
        promotional_message += "\n"
    
    if chairs:
        promotional_message += "💺 Удобни столове:\n"
        for chair in chairs:
            promotional_message += f"- {chair['name']}: {chair['discount']}% отстъпка\n"
    
    return promotional_message

# Example usage:
if __name__ == "__main__":
    try:
        dining_tables = [
            {"name": "Помощна масичка", "discount": 15},
            {"name": "Голяма маса за хранене", "discount": 20}
        ]
        
        chairs = [
            {"name": "Столове Eлдорадо", "discount": 25},
            {"name": "Модерни столове", "discount": 10}
        ]
        
        print(format_promotional_offers(dining_tables, chairs))
    except ValueError as e:
        print(f"Error: {e}")
```
