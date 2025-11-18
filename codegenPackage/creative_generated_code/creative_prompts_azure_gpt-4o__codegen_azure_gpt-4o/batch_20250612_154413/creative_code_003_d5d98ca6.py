"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Write a program in Python to parse and organize fabric data from Shaoxing Eagles Textile Co., Ltd., grouping items like "French Terry," "Hacci," and "Two Face Waffle Cloth" into categories.
Generated: DETERMINISTIC_d5d98ca629857ee7
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample fabric data (replace with actual data source, e.g., a file or database)
fabric_data = [
    {"name": "French Terry", "material": "Cotton", "weight_gsm": 250},
    {"name": "Hacci", "material": "Polyester", "weight_gsm": 200},
    {"name": "Two Face Waffle Cloth", "material": "Cotton", "weight_gsm": 300},
    {"name": "Jersey Knit", "material": "Cotton", "weight_gsm": 180},
    {"name": "French Terry", "material": "Polyester", "weight_gsm": 230},
    {"name": "Hacci", "material": "Rayon", "weight_gsm": 210},
]

def categorize_fabrics(fabric_list):
    """
    Categorizes fabric data into groups based on the fabric name.
    
    Args:
        fabric_list (list): List of dictionaries containing fabric data.
    
    Returns:
        dict: Dictionary with fabric names as keys and lists of fabric data as values.
    """
    categorized = {}
    for fabric in fabric_list:
        try:
            # Extract fabric name
            name = fabric.get("name")
            if not name:
                raise ValueError("Fabric entry is missing a name.")
            
            # Add fabric to the appropriate category
            if name not in categorized:
                categorized[name] = []
            categorized[name].append(fabric)
        
        except Exception as e:
            print(f"Error processing fabric data: {e}")
    
    return categorized

def main():
    """
    Main function to parse and organize fabric data.
    """
    try:
        # Group fabrics into categories
        grouped_fabrics = categorize_fabrics(fabric_data)
        
        # Print organized data in JSON format for readability
        print("Organized Fabric Data:")
        print(json.dumps(grouped_fabrics, indent=4))
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point for the program
    main()
```
