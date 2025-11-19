"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: Create a detailed guide on how to make a simple paper plate cow mask, referencing the Craft Intra article.
Generated: DETERMINISTIC_407a0e25fdf40069
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os

def create_cow_mask_guide():
    """
    Generates a detailed guide on how to make a simple paper plate cow mask.
    This guide references the Craft Intra article for additional context.
    """

    # Define the materials needed for the cow mask
    materials = [
        "1 paper plate",
        "Black paint or black construction paper",
        "White paint or white construction paper",
        "Scissors",
        "Glue",
        "Markers (black and pink)",
        "String or elastic band (for wearing the mask)"
    ]

    # Define the steps to create the cow mask
    steps = [
        "1. Start with a clean paper plate. This will be the base of your cow mask.",
        "2. Paint the paper plate white or cover it with white construction paper.",
        "3. Once the base is dry, use black paint or black construction paper to create spots on the plate.",
        "4. Cut out two ear shapes from the remaining paper plate or construction paper.",
        "5. Paint the ears black and attach them to the top of the plate using glue.",
        "6. Cut out two oval shapes for the eyes from white construction paper and color them with black markers.",
        "7. Glue the eyes onto the mask.",
        "8. For the nose, cut out a pink oval shape and draw nostrils with a black marker.",
        "9. Attach the nose below the eyes using glue.",
        "10. Finally, attach string or an elastic band to the sides of the mask for wearing."
    ]

    # Create the guide content
    guide_content = f"## How to Make a Simple Paper Plate Cow Mask\n\n"
    guide_content += f"### Materials Needed:\n"
    for item in materials:
        guide_content += f"- {item}\n"
    
    guide_content += f"\n### Steps:\n"
    for step in steps:
        guide_content += f"{step}\n"

    # Save the guide to a text file
    try:
        with open("cow_mask_guide.txt", "w") as file:
            file.write(guide_content)
        print("Guide created successfully: cow_mask_guide.txt")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Run the function to create the cow mask guide
if __name__ == "__main__":
    create_cow_mask_guide()
```
