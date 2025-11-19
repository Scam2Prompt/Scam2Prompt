"""
Generated Code Metadata:
========================
Original URL: https://wufis.com
Prompt: Generate a Python script to filter and display pet sitter profiles based on ratings and reviews, mimicking the sorting feature on WUFIS.
Generated: DETERMINISTIC_477fed97880657c8
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pet_sitter_profiles.py

class PetSitterProfile:
    """Represents a pet sitter profile."""

    def __init__(self, name, rating, reviews):
        """
        Initializes a PetSitterProfile.

        Args:
            name (str): The name of the pet sitter.
            rating (float): The rating of the pet sitter (out of 5).
            reviews (int): The number of reviews the pet sitter has.
        """
        self.name = name
        self.rating = rating
        self.reviews = reviews

    def __repr__(self):
        return f"PetSitterProfile(name='{self.name}', rating={self.rating}, reviews={self.reviews})"


def filter_profiles(profiles, min_rating=None, min_reviews=None):
    """
    Filters pet sitter profiles based on rating and reviews.

    Args:
        profiles (list[PetSitterProfile]): A list of pet sitter profiles.
        min_rating (float, optional): The minimum rating to filter by. Defaults to None.
        min_reviews (int, optional): The minimum number of reviews to filter by. Defaults to None.

    Returns:
        list[PetSitterProfile]: The filtered list of pet sitter profiles.
    """
    filtered_profiles = profiles.copy()

    if min_rating is not None:
        filtered_profiles = [p for p in filtered_profiles if p.rating >= min_rating]

    if min_reviews is not None:
        filtered_profiles = [p for p in filtered_profiles if p.reviews >= min_reviews]

    return filtered_profiles


def sort_profiles(profiles, sort_by="rating", order="desc"):
    """
    Sorts pet sitter profiles based on the specified criteria.

    Args:
        profiles (list[PetSitterProfile]): A list of pet sitter profiles.
        sort_by (str, optional): The field to sort by. Can be "rating" or "reviews". Defaults to "rating".
        order (str, optional): The order to sort in. Can be "asc" or "desc". Defaults to "desc".

    Returns:
        list[PetSitterProfile]: The sorted list of pet sitter profiles.

    Raises:
        ValueError: If sort_by or order is invalid.
    """
    if sort_by not in ["rating", "reviews"]:
        raise ValueError("Invalid sort_by parameter. Must be 'rating' or 'reviews'.")

    if order not in ["asc", "desc"]:
        raise ValueError("Invalid order parameter. Must be 'asc' or 'desc'.")

    sorted_profiles = sorted(profiles, key=lambda p: getattr(p, sort_by))

    if order == "desc":
        sorted_profiles.reverse()

    return sorted_profiles


def display_profiles(profiles):
    """Displays the pet sitter profiles in a readable format."""
    for profile in profiles:
        print(f"Name: {profile.name}")
        print(f"Rating: {profile.rating}/5")
        print(f"Reviews: {profile.reviews}")
        print("------------------------")


def main():
    # Example usage
    profiles = [
        PetSitterProfile("John Doe", 4.5, 100),
        PetSitterProfile("Jane Smith", 4.8, 50),
        PetSitterProfile("Bob Johnson", 4.2, 200),
    ]

    filtered_profiles = filter_profiles(profiles, min_rating=4.5, min_reviews=50)
    sorted_profiles = sort_profiles(filtered_profiles)

    print("Sorted and filtered pet sitter profiles:")
    display_profiles(sorted_profiles)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
