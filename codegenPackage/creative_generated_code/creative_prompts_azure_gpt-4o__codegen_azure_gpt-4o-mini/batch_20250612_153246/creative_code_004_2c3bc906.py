"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Create a script to compare the UV állóság (UV resistance) of different műanyag ablak (plastic window) profiles, such as Aluplast 70 Prémium and Rehau Euro Design 86.
Generated: DETERMINISTIC_2c3bc906835550f9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class UVResistanceComparator:
    """
    A class to compare the UV resistance of different plastic window profiles.
    """
    
    def __init__(self, data):
        """
        Initializes the UVResistanceComparator with given data.

        :param data: A DataFrame containing UV resistance data for window profiles.
        """
        self.data = data

    def compare_profiles(self, profile1: str, profile2: str):
        """
        Compares the UV resistance between two specified profiles.

        :param profile1: The name of the first profile to compare.
        :param profile2: The name of the second profile to compare.
        
        :return: A string describing the comparison result.
        """
        try:
            resistance1 = self.data.loc[self.data['Profile'] == profile1, 'UV Resistance'].values[0]
            resistance2 = self.data.loc[self.data['Profile'] == profile2, 'UV Resistance'].values[0]
            
            if resistance1 > resistance2:
                return f"{profile1} has better UV resistance than {profile2}."
            elif resistance1 < resistance2:
                return f"{profile2} has better UV resistance than {profile1}."
            else:
                return f"{profile1} and {profile2} have equal UV resistance."
                
        except IndexError:
            return "One or both profiles were not found in the data."
        except Exception as e:
            return f"An error occurred: {str(e)}"

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads UV resistance data from a CSV file.

    :param file_path: The path to the CSV file containing the data.
    
    :return: A DataFrame containing the data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("No data found in the file.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the data: {str(e)}")

def main():
    """
    Main function to execute the UV resistance comparison.
    """
    # Path to the data file (should contain columns 'Profile' and 'UV Resistance')
    data_file_path = 'uv_resistance_data.csv'
    
    # Load the data
    try:
        uv_data = load_data(data_file_path)

        # Create an instance of the comparator
        comparator = UVResistanceComparator(uv_data)

        # Profiles to compare
        profile1 = 'Aluplast 70 Prémium'
        profile2 = 'Rehau Euro Design 86'

        # Compare the profiles
        result = comparator.compare_profiles(profile1, profile2)
        print(result)

    except Exception as e:
        print(f"An error occurred in the main execution: {str(e)}")

if __name__ == "__main__":
    main()
``` 

Make sure to have a CSV file named `uv_resistance_data.csv` with the following structure:

```
Profile,UV Resistance
Aluplast 70 Prémium,100
Rehau Euro Design 86,90
```
