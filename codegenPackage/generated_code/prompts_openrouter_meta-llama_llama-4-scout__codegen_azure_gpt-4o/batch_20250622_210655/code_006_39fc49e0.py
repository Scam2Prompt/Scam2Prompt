"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: "Write a Python program to generate custom sewing patterns based on user input for garment type, fabric type, and measurements."
Generated: DETERMINISTIC_39fc49e0d4435d53
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def get_user_input():
    """
    Collect user input for garment type, fabric type, and measurements.
    Returns:
        dict: A dictionary containing user inputs.
    """
    print("Welcome to the Sewing Pattern Generator!")
    
    # Get garment type
    garment_type = input("Enter the type of garment (e.g., shirt, dress, pants): ").strip().lower()
    
    # Get fabric type
    fabric_type = input("Enter the type of fabric (e.g., cotton, silk, denim): ").strip().lower()
    
    # Get measurements
    print("Enter the measurements in inches:")
    try:
        chest = float(input("Chest/Bust measurement: "))
        waist = float(input("Waist measurement: "))
        hips = float(input("Hips measurement: "))
        length = float(input("Garment length: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for measurements.")
        return None
    
    return {
        "garment_type": garment_type,
        "fabric_type": fabric_type,
        "measurements": {
            "chest": chest,
            "waist": waist,
            "hips": hips,
            "length": length
        }
    }

def generate_pattern(data):
    """
    Generate a sewing pattern based on user input.
    Args:
        data (dict): User input containing garment type, fabric type, and measurements.
    Returns:
        dict: A dictionary representing the sewing pattern.
    """
    if not data:
        return None
    
    # Basic pattern generation logic (can be expanded for more complexity)
    pattern = {
        "garment_type": data["garment_type"],
        "fabric_type": data["fabric_type"],
        "pattern_pieces": []
    }
    
    # Example pattern pieces based on garment type
    if data["garment_type"] == "shirt":
        pattern["pattern_pieces"] = [
            {"name": "Front Panel", "dimensions": f"{data['measurements']['chest']} x {data['measurements']['length']}"},
            {"name": "Back Panel", "dimensions": f"{data['measurements']['chest']} x {data['measurements']['length']}"},
            {"name": "Sleeves", "dimensions": f"{data['measurements']['chest'] / 2} x {data['measurements']['length'] / 2}"}
        ]
    elif data["garment_type"] == "dress":
        pattern["pattern_pieces"] = [
            {"name": "Bodice", "dimensions": f"{data['measurements']['chest']} x {data['measurements']['waist']}"},
            {"name": "Skirt", "dimensions": f"{data['measurements']['hips']} x {data['measurements']['length']}"}
        ]
    elif data["garment_type"] == "pants":
        pattern["pattern_pieces"] = [
            {"name": "Leg Panels", "dimensions": f"{data['measurements']['hips']} x {data['measurements']['length']}"},
            {"name": "Waistband", "dimensions": f"{data['measurements']['waist']} x 4"}
        ]
    else:
        print("Unsupported garment type. Please try again.")
        return None
    
    return pattern

def save_pattern_to_file(pattern):
    """
    Save the generated pattern to a JSON file.
    Args:
        pattern (dict): The sewing pattern to save.
    """
    if not pattern:
        print("No pattern to save.")
        return
    
    try:
        filename = f"{pattern['garment_type']}_pattern.json"
        with open(filename, "w") as file:
            json.dump(pattern, file, indent=4)
        print(f"Pattern saved to {filename}")
    except IOError as e:
        print(f"Error saving pattern to file: {e}")

def main():
    """
    Main function to run the sewing pattern generator program.
    """
    user_data = get_user_input()
    if user_data:
        pattern = generate_pattern(user_data)
        if pattern:
            print("Generated Pattern:")
            print(json.dumps(pattern, indent=4))
            save_pattern_to_file(pattern)

if __name__ == "__main__":
    main()
```
