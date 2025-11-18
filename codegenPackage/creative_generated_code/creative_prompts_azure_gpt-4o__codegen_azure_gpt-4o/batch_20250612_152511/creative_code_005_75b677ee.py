"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-astrovault.pages.dev
Prompt: Create a script to filter participants based on country restrictions listed on TrustPad, ensuring compliance with the exclusion rules for IDOs.
Generated: DETERMINISTIC_75b677ee26efbaad
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_country_restrictions(file_path):
    """
    Load country restrictions from a JSON file.
    
    :param file_path: Path to the JSON file containing restricted countries.
    :return: A set of restricted countries.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Ensure the data is a list and convert it to a set for faster lookups
            restricted_countries = set(data.get("restricted_countries", []))
            return restricted_countries
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON file at path: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error while loading country restrictions: {str(e)}")


def filter_participants(participants, restricted_countries):
    """
    Filter participants based on country restrictions.
    
    :param participants: List of participant dictionaries, each containing 'name' and 'country'.
    :param restricted_countries: Set of restricted countries.
    :return: List of allowed participants (those not in restricted countries).
    """
    allowed_participants = []
    for participant in participants:
        try:
            country = participant.get('country')
            name = participant.get('name')
            
            # Ensure required fields exist and are valid
            if not country or not name:
                raise ValueError(f"Invalid participant data: {participant}")

            # Check if the participant's country is restricted
            if country not in restricted_countries:
                allowed_participants.append(participant)
        except Exception as e:
            print(f"Skipping participant due to error: {str(e)}")
    
    return allowed_participants


def main():
    """
    Main function to execute the participant filtering process.
    """
    # Path to the file containing restricted countries
    restrictions_file = 'restricted_countries.json'

    # Example participant list to filter
    participants = [
        {"name": "Alice", "country": "United States"},
        {"name": "Bob", "country": "Iran"},
        {"name": "Charlie", "country": "Canada"},
    ]

    try:
        # Load restricted countries
        restricted_countries = load_country_restrictions(restrictions_file)

        # Filter participants
        allowed_participants = filter_participants(participants, restricted_countries)

        # Display results
        print("Allowed Participants:")
        for participant in allowed_participants:
            print(f"Name: {participant['name']}, Country: {participant['country']}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
