"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Develop a step-by-step algorithm to create fingerprint keepsakes for toddlers, referencing Craft Intra's tutorial for heart-shaped crafts.
Generated: DETERMINISTIC_dcc02486312bf34d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code representing the algorithm for creating fingerprint keepsakes for toddlers based on Craft Intra's tutorial for heart-shaped crafts. This is a simulation of the process, since physical crafting steps cannot be directly executed in code.

```python
import os

def create_fingerprint_keepsake():
    """Function to create a virtual fingerprint keepsake for toddlers."""
    try:
        print("Welcome to the Fingerprint Keepsake Creator!")
        
        # Step 1: Collect User Input
        toddler_name = input("Enter the toddler's name: ").strip()
        if not toddler_name:
            raise ValueError("Toddler's name cannot be empty.")
        
        print("\nLet's create a heart-shaped keepsake.")
        print("Use washable paint to capture the fingerprints on paper.")
        print("Press the toddler's finger gently into the paint and apply to paper in a heart shape.")

        # Step 2: Simulate Heart Shape Creation
        heart_shape = """
           **    **
         ******  ******
       ******************
        ****************
         **************
          ************
           **********
            ********
             ******
              ****
               **
        """
        print("\nHere is your virtual heart-shaped keepsake with fingerprints:")
        print(heart_shape)

        # Step 3: Save Keepsake to File
        directory = "keepsakes"
        if not os.path.exists(directory):
            os.mkdir(directory)
        
        filename = f"{directory}/{toddler_name}_fingerprint_keepsake.txt"
        with open(filename, "w") as keepsake_file:
            keepsake_file.write(f"Toddler's Name: {toddler_name}\n\n")
            keepsake_file.write("Heart-Shaped Fingerprint Keepsake:\n")
            keepsake_file.write(heart_shape)
        
        print(f"\nThe keepsake has been successfully saved to {filename}!")
        print("You can now physically replicate this on craft paper, using the tutorial steps.")
    
    except ValueError as ve:
        print(f"Error: {ve}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_fingerprint_keepsake()
```
