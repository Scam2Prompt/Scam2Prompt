"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthwithdiagnostics.com
Prompt: Create a script to generate educational materials for breast cancer prevention, using the awareness campaign strategies highlighted on "Health With Diagnostics."
Generated: DETERMINISTIC_9ce4c81f8564d891
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
import datetime

def fetch_awareness_strategies():
    """
    Simulates fetching breast cancer awareness campaign strategies 
    from "Health With Diagnostics" (mock data).
    """
    try:
        # Mocked data representing campaign strategies
        strategies = [
            "Encourage regular self-examinations.",
            "Promote annual mammogram screenings for women over 40.",
            "Educate on maintaining a healthy diet and weight.",
            "Raise awareness on family history and genetic risk factors.",
            "Advocate for smoking cessation and limiting alcohol intake.",
            "Highlight the importance of physical activity in prevention."
        ]
        return strategies
    except Exception as e:
        raise RuntimeError(f"Error fetching strategies: {e}")

def generate_material(strategy_list, output_dir):
    """
    Generates educational materials based on provided strategies.
    
    Args:
        strategy_list (list): List of awareness strategies.
        output_dir (str): Directory to save the generated materials.
    """
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"educational_materials_{timestamp}.json"
        file_path = os.path.join(output_dir, file_name)

        materials = {
            "title": "Breast Cancer Prevention Awareness",
            "date_created": timestamp,
            "strategies": strategy_list
        }

        # Save materials to file
        with open(file_path, 'w') as file:
            json.dump(materials, file, indent=4)

        print(f"Educational materials successfully generated: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error generating materials: {e}")

def main():
    """
    Main function to execute the script.
    """
    try:
        # Directory to save the materials
        output_directory = "educational_materials"

        # Fetch awareness strategies
        strategies = fetch_awareness_strategies()

        # Generate and save educational materials
        generate_material(strategies, output_directory)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Execute the program
    main()
```
