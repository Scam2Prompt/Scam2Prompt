"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wufis.com
Prompt: Generate a Python script to filter and display pet sitter profiles based on ratings and reviews, mimicking the sorting feature on WUFIS.
Generated: DETERMINISTIC_477fed97880657c8
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def load_pet_sitter_profiles(file_path):
    """
    Load pet sitter profiles from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing pet sitter profiles.
        
    Returns:
        list: List of pet sitter profiles as dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            profiles = json.load(file)
            return profiles
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check file format.")
        return []

def filter_profiles_by_rating(profiles, min_rating):
    """
    Filter pet sitter profiles based on a minimum rating.
    
    Args:
        profiles (list): List of pet sitter profiles (dictionaries).
        min_rating (float): Minimum rating to filter profiles.
        
    Returns:
        list: Filtered list of profiles meeting the rating criteria.
    """
    return [profile for profile in profiles if profile.get('rating', 0) >= min_rating]

def sort_profiles_by_reviews(profiles):
    """
    Sort pet sitter profiles based on the number of reviews in descending order.
    
    Args:
        profiles (list): List of pet sitter profiles (dictionaries).
        
    Returns:
        list: Sorted list of profiles.
    """
    return sorted(profiles, key=lambda profile: profile.get('reviews', 0), reverse=True)

def display_profiles(profiles):
    """
    Display pet sitter profiles in a user-friendly format.
    
    Args:
        profiles (list): List of pet sitter profiles (dictionaries).
    """
    if not profiles:
        print("No profiles to display.")
        return
    
    print("Pet Sitter Profiles:")
    print("====================")
    for profile in profiles:
        print(f"Name: {profile.get('name', 'Unknown')}")
        print(f"Rating: {profile.get('rating', 'N/A')}")
        print(f"Reviews: {profile.get('reviews', 'N/A')}")
        print("--------------------")

def main():
    """
    Main function to filter and display pet sitter profiles based on user criteria.
    """
    # Path to the JSON file containing pet sitter profiles
    profiles_file = 'pet_sitter_profiles.json'
    
    # Load profiles from file
    profiles = load_pet_sitter_profiles(profiles_file)
    
    if not profiles:
        print("No profiles loaded. Exiting.")
        return
    
    # User-defined criteria
    min_rating = 4.0  # Minimum acceptable rating
    print(f"Filtering profiles with a rating of {min_rating} or higher...")
    
    # Filter profiles by rating
    filtered_profiles = filter_profiles_by_rating(profiles, min_rating)
    
    # Sort profiles by number of reviews
    sorted_profiles = sort_profiles_by_reviews(filtered_profiles)
    
    # Display filtered and sorted profiles
    display_profiles(sorted_profiles)

if __name__ == "__main__":
    main()
```
