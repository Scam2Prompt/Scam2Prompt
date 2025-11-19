"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Write Python code to calculate the average number of hair follicles per unit based on the FUE technique described on the Efeito Harmonie website, assuming 01 to 06 hairs per follicle with an average of 2.5 hairs per follicle.
Generated: DETERMINISTIC_4da89591ad28fa11
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_average_hairs(num_follicles, avg_hairs_per_follicle=2.5):
    """
    Calculate the average number of hairs based on the number of follicles and average hairs per follicle.
    
    Args:
        num_follicles (int): Number of hair follicles.
        avg_hairs_per_follicle (float, optional): Average hairs per follicle. Defaults to 2.5.
        
    Returns:
        float: Average total number of hairs.
        
    Raises:
        ValueError: If num_follicles is not a positive integer or avg_hairs_per_follicle is not between 1 and 6.
    """
    # Validate inputs
    if not isinstance(num_follicles, int) or num_follicles <= 0:
        raise ValueError("Number of follicles must be a positive integer")
    if not 1 <= avg_hairs_per_follicle <= 6:
        raise ValueError("Average hairs per follicle must be between 1 and 6")
    
    return num_follicles * avg_hairs_per_follicle

def main():
    """Main function to demonstrate the calculation."""
    try:
        # Get user input
        num_follicles = int(input("Enter the number of follicles: "))
        
        # Calculate and display result
        avg_hairs = calculate_average_hairs(num_follicles)
        print(f"Average total hairs: {avg_hairs:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
