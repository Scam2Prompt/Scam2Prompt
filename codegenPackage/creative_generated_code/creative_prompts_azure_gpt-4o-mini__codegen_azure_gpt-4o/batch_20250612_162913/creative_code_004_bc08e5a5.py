"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstcrackcoffeeroasters.com
Prompt: Illustrate how to use First Crack Coffee Roasters' manual brewing equipment with a step-by-step guide in Markdown format.
Generated: DETERMINISTIC_bc08e5a557a71922
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# brew_guide.py
"""
Generate a brewing guide for First Crack Coffee Roasters' manual brewing equipment.

This script outputs the brewing guide in Markdown format. The guide provides
step-by-step instructions for each stage of the brewing process.

Usage:
Run the script to produce a Markdown file named `brewing_guide.md`.
"""

import os

def generate_markdown_guide(file_name="brewing_guide.md"):
    """
    Generates a step-by-step guide for manual coffee brewing in Markdown format.

    Args:
        file_name (str): The name of the Markdown file to save the guide.
    
    Returns:
        None
    """
    # Step-by-step guide in Markdown format
    guide_content = """
# First Crack Coffee Roasters Manual Brewing Guide

Welcome to First Crack Coffee Roasters' manual brewing guide! Follow these steps to brew the perfect cup of coffee using our equipment.

---

## Equipment Checklist
Before you start, make sure you have the following:
- Freshly roasted coffee beans
- Burr grinder
- Scale
- Timer
- Kettle (preferably with temperature control)
- Brewing device (e.g., pour-over dripper, French press, or AeroPress)
- Filter paper (if applicable)
- Mug or carafe

---

## Step-by-Step Guide

### 1. Prepare the Equipment
- Clean all your brewing equipment.
- Ensure your kettle is filled with fresh water.

### 2. Heat the Water
- Heat the water to a temperature of 195°F to 205°F (90°C to 96°C).
- Use a thermometer or a temperature-controlled kettle for accuracy.

### 3. Measure and Grind Coffee
- Weigh your coffee beans. Use a coffee-to-water ratio of 1:16 for optimal flavor (e.g., 25 grams of coffee for 400 grams of water).
- Grind the beans to the appropriate coarseness:
  - **Pour-over dripper:** Medium grind, similar to sea salt.
  - **French press:** Coarse grind, similar to breadcrumbs.
  - **AeroPress:** Fine grind, similar to table salt.

### 4. Pre-wet the Filter (if applicable)
- Place the filter in the brewing device and pour hot water over it.
- This removes any paper taste and preheats the equipment. Discard the rinse water.

### 5. Add Coffee Grounds
- Place the ground coffee into your brewing device.
- Level the grounds for even extraction.

### 6. Start Brewing
#### For Pour-over:
1. Begin with a bloom: Pour 2-3 times the weight of coffee in water (e.g., 50 grams for 25 grams of coffee) and let it sit for 30–45 seconds.
2. Continue pouring in slow, concentric circles until the desired water amount is reached.

#### For French Press:
1. Pour all the water over the coffee grounds.
2. Stir gently to ensure even saturation.
3. Place the lid on and let it steep for 4 minutes.
4. Slowly press the plunger down.

#### For AeroPress:
1. Add water, stir, and let it steep for about 1 minute.
2. Insert the plunger and press down gently.

### 7. Serve and Enjoy
- Pour the brewed coffee into your mug or carafe.
- Allow it to cool slightly and enjoy!

---

## Tips for Best Results
- Use freshly roasted coffee beans for maximum flavor.
- Adjust grind size and brewing time to suit your taste preferences.
- Clean your equipment thoroughly after each use.

---

Thank you for choosing First Crack Coffee Roasters. Happy brewing!
"""

    try:
        # Write the guide to a Markdown file
        with open(file_name, "w") as file:
            file.write(guide_content)
        print(f"Brewing guide successfully written to '{file_name}'")
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")


if __name__ == "__main__":
    # Generate the brewing guide
    generate_markdown_guide()
```
