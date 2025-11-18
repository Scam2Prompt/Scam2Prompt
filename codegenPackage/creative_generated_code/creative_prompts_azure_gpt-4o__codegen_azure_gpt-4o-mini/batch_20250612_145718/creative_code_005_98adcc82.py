"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonlucky.top
Prompt: Generate a script that multiplies rewards by a factor of X3 for NFT owners, as mentioned in the TON Lucky reward system.
Generated: DETERMINISTIC_98adcc82cba2fc83
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class NFTRewardMultiplier:
    def __init__(self, multiplier: float):
        """
        Initializes the NFTRewardMultiplier with a specified multiplier.

        Args:
            multiplier (float): The multiplier factor to apply to rewards.
        """
        if multiplier <= 0:
            raise ValueError("Multiplier must be a positive number.")
        self.multiplier = multiplier

    def load_rewards(self, file_path: str) -> dict:
        """
        Loads the rewards data from a specified JSON file.

        Args:
            file_path (str): The path to the JSON file containing rewards data.

        Returns:
            dict: The rewards data loaded from the file.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                rewards = json.load(file)
                return rewards
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error: The file {file_path} was not found.") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"Error: The file {file_path} contains invalid JSON.") from e

    def multiply_rewards(self, rewards: dict) -> dict:
        """
        Applies the multiplier to the rewards of NFT owners.

        Args:
            rewards (dict): A dictionary containing NFT owners and their current rewards.

        Returns:
            dict: A new dictionary with updated rewards.
        """
        updated_rewards = {}
        for owner, reward in rewards.items():
            if not isinstance(reward, (int, float)):
                raise ValueError(f"Invalid reward for owner {owner}: {reward}. Must be a number.")
            updated_rewards[owner] = reward * self.multiplier
        return updated_rewards

    def save_rewards(self, rewards: dict, file_path: str):
        """
        Saves the updated rewards data to a specified JSON file.

        Args:
            rewards (dict): The updated rewards data to save.
            file_path (str): The path to the JSON file to save the data.

        Raises:
            IOError: If an error occurs while writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(rewards, file, indent=4)
        except IOError as e:
            raise IOError(f"Error: Unable to write to file {file_path}.") from e

def main():
    # Set the multiplier for NFT owners
    multiplier_factor = 3.0
    multiplier = NFTRewardMultiplier(multiplier_factor)

    # Load current rewards from a JSON file
    input_file_path = 'rewards.json'
    output_file_path = 'updated_rewards.json'
    
    try:
        rewards = multiplier.load_rewards(input_file_path)

        # Multiply rewards by the defined multiplier
        updated_rewards = multiplier.multiply_rewards(rewards)

        # Save the updated rewards to a new JSON file
        multiplier.save_rewards(updated_rewards, output_file_path)
        print(f"Updated rewards saved to {output_file_path}.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
