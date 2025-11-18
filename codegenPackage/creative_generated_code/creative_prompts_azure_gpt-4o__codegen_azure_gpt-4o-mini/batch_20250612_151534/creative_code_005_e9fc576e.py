"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apk20.com
Prompt: Develop a function to compare app ratings from APK20 with another APK repository and highlight discrepancies.
Generated: DETERMINISTIC_e9fc576e89f8ba9a
Batch ID: 20250612_151534
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.otherrepo.com/ratings/{app_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.apk20.com/ratings/{app_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from typing import List, Dict, Tuple

class RatingComparisonError(Exception):
    """Custom exception for rating comparison errors."""
    pass

def fetch_ratings_from_apk20(app_ids: List[str]) -> Dict[str, float]:
    """
    Fetch app ratings from APK20.
    
    Parameters:
        app_ids (List[str]): List of application IDs to fetch ratings for.
    
    Returns:
        Dict[str, float]: A dictionary mapping app IDs to their ratings.
    """
    ratings = {}
    for app_id in app_ids:
        try:
            # Simulated API request to fetch ratings; replace with actual URL
            response = requests.get(f"https://api.apk20.com/ratings/{app_id}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            ratings[app_id] = data['rating']  # Assuming JSON response contains a 'rating' field
        except (requests.RequestException, KeyError) as e:
            raise RatingComparisonError(f"Error fetching rating for {app_id}: {str(e)}")
    return ratings

def fetch_ratings_from_other_repo(app_ids: List[str]) -> Dict[str, float]:
    """
    Fetch app ratings from another APK repository.
    
    Parameters:
        app_ids (List[str]): List of application IDs to fetch ratings for.
    
    Returns:
        Dict[str, float]: A dictionary mapping app IDs to their ratings.
    """
    ratings = {}
    for app_id in app_ids:
        try:
            # Simulated API request to fetch ratings; replace with actual URL
            response = requests.get(f"https://api.otherrepo.com/ratings/{app_id}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            ratings[app_id] = data['rating']  # Assuming JSON response contains a 'rating' field
        except (requests.RequestException, KeyError) as e:
            raise RatingComparisonError(f"Error fetching rating for {app_id}: {str(e)}")
    return ratings

def compare_ratings(apk20_ratings: Dict[str, float], other_repo_ratings: Dict[str, float]) -> List[Tuple[str, float, float]]:
    """
    Compare ratings from APK20 and another repository and highlight discrepancies.
    
    Parameters:
        apk20_ratings (Dict[str, float]): Ratings from APK20.
        other_repo_ratings (Dict[str, float]): Ratings from another repository.
    
    Returns:
        List[Tuple[str, float, float]]: A list of discrepancies with app ID, APK20 rating, and other repo rating.
    """
    discrepancies = []
    for app_id in apk20_ratings:
        if app_id in other_repo_ratings:
            apk20_rating = apk20_ratings[app_id]
            other_repo_rating = other_repo_ratings[app_id]
            if apk20_rating != other_repo_rating:
                discrepancies.append((app_id, apk20_rating, other_repo_rating))

    return discrepancies

def main(app_ids: List[str]):
    """
    Main function to orchestrate the fetching and comparison of app ratings.
    
    Parameters:
        app_ids (List[str]): List of application IDs to compare ratings for.
    """
    try:
        # Fetch ratings from both repositories
        apk20_ratings = fetch_ratings_from_apk20(app_ids)
        other_repo_ratings = fetch_ratings_from_other_repo(app_ids)

        # Compare ratings and find discrepancies
        discrepancies = compare_ratings(apk20_ratings, other_repo_ratings)

        # Output discrepancies
        if discrepancies:
            print("Discrepancies found:")
            for app_id, apk20_rating, other_repo_rating in discrepancies:
                print(f"App ID: {app_id}, APK20 Rating: {apk20_rating}, Other Repo Rating: {other_repo_rating}")
        else:
            print("No discrepancies found.")

    except RatingComparisonError as e:
        print(f"Error during rating comparison: {str(e)}")

# Example usage
if __name__ == "__main__":
    app_ids_to_compare = ["app1", "app2", "app3"]  # Replace with actual app IDs
    main(app_ids_to_compare)
```
