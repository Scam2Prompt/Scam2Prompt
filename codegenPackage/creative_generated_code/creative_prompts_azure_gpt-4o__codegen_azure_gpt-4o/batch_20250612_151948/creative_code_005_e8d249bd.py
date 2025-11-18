"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.superstep.org
Prompt: Develop a Python program to analyze the efficiency of weapons in "Myth of Empires," based on the game insights shared on Superstep.org.
Generated: DETERMINISTIC_e8d249bdccfdb28d
Batch ID: 20250612_151948
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

def load_weapon_data(file_path):
    """
    Load weapon data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing weapon efficiency data.
    
    Returns:
        dict: Dictionary containing weapon data.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return {}


def analyze_efficiency(weapon_data):
    """
    Analyze efficiency of weapons based on their stats.
    
    Args:
        weapon_data (dict): Dictionary containing weapon stats.
    
    Returns:
        dict: Dictionary containing weapons sorted by efficiency in descending order.
    """
    try:
        efficiency_scores = {}
        
        for weapon, stats in weapon_data.items():
            # Ensure required keys exist in stats
            if not all(key in stats for key in ['damage', 'speed', 'durability']):
                print(f"Warning: Missing keys in stats for weapon: {weapon}")
                continue
            
            # Calculate efficiency score (example formula)
            efficiency = stats['damage'] * stats['speed'] * (stats['durability'] / 100)
            efficiency_scores[weapon] = efficiency
            
        # Sort weapons by efficiency in descending order
        sorted_efficiency = dict(sorted(efficiency_scores.items(), key=lambda x: x[1], reverse=True))
        return sorted_efficiency
    
    except Exception as e:
        print(f"Error analyzing weapon efficiency: {e}")
        return {}


def display_efficiency(efficiency_data):
    """
    Display the efficiency scores of weapons.
    
    Args:
        efficiency_data (dict): Dictionary containing weapons and their efficiency scores.
    """
    if not efficiency_data:
        print("No efficiency data available to display.")
        return
    
    print("\nWeapon Efficiency Rankings:")
    print("---------------------------")
    for rank, (weapon, score) in enumerate(efficiency_data.items(), start=1):
        print(f"{rank}. {weapon}: {score:.2f}")


def main():
    """
    Main function to execute the weapon efficiency analysis.
    """
    # Path to the JSON file containing weapon data
    weapon_data_file = os.path.join(os.getcwd(), 'weapon_data.json')
    
    print("Loading weapon data...")
    weapon_data = load_weapon_data(weapon_data_file)
    
    if not weapon_data:
        print("No weapon data found. Exiting program.")
        return
    
    print("Analyzing weapon efficiency...")
    efficiency_data = analyze_efficiency(weapon_data)
    
    display_efficiency(efficiency_data)


if __name__ == "__main__":
    main()
```

### Notes:
- This program expects a JSON file named `weapon_data.json` in the current working directory.
- The JSON file should contain weapon stats structured similarly:
    ```json
    {
        "Sword": {"damage": 50, "speed": 1.2, "durability": 80},
        "Axe": {"damage": 65, "speed": 0.9, "durability": 90}
    }
    ```
