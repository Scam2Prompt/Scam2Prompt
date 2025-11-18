"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis2020.com
Prompt: Create a Python script to automate the calculation of "slot gacor maxwin" probabilities based on game data, referencing Satria4D's focus on high-winning slots.
Generated: DETERMINISTIC_bdbf528597ddcb98
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
import logging

# Configure logging to log errors and information
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_game_data(file_path):
    """
    Load game data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing game data.
    
    Returns:
        dict: Parsed game data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logging.info("Game data loaded successfully.")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        raise

def calculate_gacor_probability(game_data):
    """
    Calculate 'slot gacor maxwin' probabilities based on game data.
    
    Args:
        game_data (dict): Dictionary containing slot game data.
    
    Returns:
        dict: Probabilities for each slot.
    """
    probabilities = {}
    try:
        for slot, stats in game_data.items():
            # Ensure required keys are present
            if 'total_games' in stats and 'maxwin_count' in stats:
                total_games = stats['total_games']
                maxwin_count = stats['maxwin_count']
                
                # Avoid division by zero
                if total_games > 0:
                    probability = maxwin_count / total_games
                else:
                    probability = 0.0
                
                probabilities[slot] = round(probability, 4)  # Round to 4 decimal places
            else:
                logging.warning(f"Missing data for slot: {slot}")
                probabilities[slot] = None  # Mark as undefined
        logging.info("Probabilities calculated successfully.")
    except Exception as e:
        logging.error(f"Error during calculation: {e}")
        raise
    return probabilities

def save_probabilities(probabilities, output_path):
    """
    Save probabilities to a JSON file.
    
    Args:
        probabilities (dict): Calculated probabilities for each slot.
        output_path (str): Path to save the JSON file.
    """
    try:
        with open(output_path, 'w') as file:
            json.dump(probabilities, file, indent=4)
            logging.info(f"Probabilities saved to {output_path}")
    except Exception as e:
        logging.error(f"Error saving probabilities: {e}")
        raise

def main():
    """
    Main function to load game data, calculate probabilities, and save results.
    """
    input_file = "game_data.json"  # Input file containing game data
    output_file = "probabilities.json"  # Output file for saving probabilities

    try:
        # Load game data
        game_data = load_game_data(input_file)
        
        # Calculate probabilities
        probabilities = calculate_gacor_probability(game_data)
        
        # Save probabilities to file
        save_probabilities(probabilities, output_file)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
