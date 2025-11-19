"""
Generated Code Metadata:
========================
Original URL: https://anamalika.com
Prompt: Write a tutorial on how to apply مكياج الوجه (face makeup) using products from استي لودر (Estee Lauder) and فور ايفر (Forever).
Generated: DETERMINISTIC_02275b23cc6fa235
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python script that simulates a tutorial for applying face makeup using products from Estee Lauder and Forever. The script is designed to be clean, well-documented, and production-ready.

```python
"""
Face Makeup Tutorial Script
This script provides a step-by-step guide for applying face makeup using products from Estee Lauder and Forever.
The tutorial is interactive and allows users to follow along with prompts.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def display_step(step_number, description, product):
    """
    Displays a single step in the makeup tutorial.

    Args:
        step_number (int): The step number in the tutorial.
        description (str): The description of the step.
        product (str): The product recommended for the step.
    """
    print(f"\nStep {step_number}: {description}")
    print(f"Recommended Product: {product}")
    input("Press Enter to continue to the next step...")

def main():
    """
    Main function to run the face makeup tutorial.
    """
    try:
        print("Welcome to the Face Makeup Tutorial!")
        print("This tutorial uses products from Estee Lauder and Forever.")
        print("Follow the steps below to achieve a flawless look.\n")

        # Step-by-step tutorial
        steps = [
            {
                "step_number": 1,
                "description": "Cleanse your face thoroughly to remove any dirt or oil.",
                "product": "Estee Lauder Perfectly Clean Multi-Action Foam Cleanser"
            },
            {
                "step_number": 2,
                "description": "Apply a moisturizer to hydrate your skin.",
                "product": "Estee Lauder DayWear Multi-Protection Anti-Oxidant Moisturizer"
            },
            {
                "step_number": 3,
                "description": "Use a primer to create a smooth base for makeup.",
                "product": "Forever Skin Primer"
            },
            {
                "step_number": 4,
                "description": "Apply foundation evenly across your face.",
                "product": "Estee Lauder Double Wear Stay-in-Place Foundation"
            },
            {
                "step_number": 5,
                "description": "Conceal any blemishes or dark circles using a concealer.",
                "product": "Forever Ultra HD Concealer"
            },
            {
                "step_number": 6,
                "description": "Set your foundation and concealer with a setting powder.",
                "product": "Estee Lauder Perfecting Loose Powder"
            },
            {
                "step_number": 7,
                "description": "Add color to your cheeks using blush.",
                "product": "Forever Artist Face Color Blush"
            },
            {
                "step_number": 8,
                "description": "Define your eyebrows using an eyebrow pencil or gel.",
                "product": "Estee Lauder Brow Now Stay-in-Place Brow Gel"
            },
            {
                "step_number": 9,
                "description": "Apply eyeshadow to enhance your eyes.",
                "product": "Forever Artist Color Eye Shadow Palette"
            },
            {
                "step_number": 10,
                "description": "Use eyeliner to define your eyes.",
                "product": "Estee Lauder Double Wear Stay-in-Place Eye Pencil"
            },
            {
                "step_number": 11,
                "description": "Finish your eye makeup with mascara.",
                "product": "Estee Lauder Sumptuous Extreme Lash Multiplying Volume Mascara"
            },
            {
                "step_number": 12,
                "description": "Apply lipstick or lip gloss to complete the look.",
                "product": "Forever Rouge Artist Lipstick"
            }
        ]

        # Iterate through each step and display it
        for step in steps:
            display_step(step["step_number"], step["description"], step["product"])

        print("\nCongratulations! You have completed the face makeup tutorial.")
        print("Enjoy your flawless look!")

    except KeyboardInterrupt:
        print("\nTutorial interrupted by user. Exiting...")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```

This script is interactive and provides a step-by-step guide for applying face makeup. It uses Python's `input()` function to allow users to proceed through the tutorial at their own pace. Error handling is included to manage interruptions or unexpected issues.
