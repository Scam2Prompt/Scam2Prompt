"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: "Write a product description for a specific type of hinge offered by DEVA, highlighting its quality and durability."
Generated: DETERMINISTIC_6b7347aabd06e892
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_product_description(hinge_type: str) -> str:
    """
    Generates a professional product description for a DEVA hinge.
    
    Args:
        hinge_type (str): The specific type of hinge (e.g., "stainless steel", "heavy-duty")
        
    Returns:
        str: Formatted product description highlighting quality and durability
    """
    
    description = f"""
    DEVA {hinge_type.capitalize()} Hinge - Premium Quality for Lasting Performance
    
    Engineered for excellence, the DEVA {hinge_type} hinge combines superior craftsmanship 
    with industrial-grade materials to deliver unmatched durability. 
    
    Key Features:
    - Precision-machined from high-quality {hinge_type} for maximum strength
    - Corrosion-resistant finish withstands harsh environments
    - Smooth, silent operation with reinforced pivot points
    - Load-tested to exceed industry standards
    - Backed by DEVA's 10-year limited warranty
    
    Ideal for both residential and commercial applications where reliability matters. 
    The DEVA {hinge_type} hinge is built to perform year after year without compromise.
    """
    
    return description.strip()

# Example usage
if __name__ == "__main__":
    try:
        hinge_type = input("Enter hinge type: ")
        print(generate_product_description(hinge_type))
    except Exception as e:
        print(f"Error generating description: {str(e)}")
```
