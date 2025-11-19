"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Compare and recommend the best CCTV cameras for home and business security in Kenya, considering factors like HD resolution, night vision, and secure cloud storage.
Generated: DETERMINISTIC_84244d4e45f9ac8b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests

def fetch_cctv_data():
    """
    Fetches CCTV camera data from an external API or database.
    This function simulates fetching data for demonstration purposes.
    Returns:
        list: A list of dictionaries containing CCTV camera details.
    """
    # Simulated data for demonstration purposes
    return [
        {
            "name": "Camera A",
            "resolution": "1080p",
            "night_vision": True,
            "cloud_storage": True,
            "price": 15000,
            "type": "Home"
        },
        {
            "name": "Camera B",
            "resolution": "720p",
            "night_vision": True,
            "cloud_storage": False,
            "price": 10000,
            "type": "Business"
        },
        {
            "name": "Camera C",
            "resolution": "4K",
            "night_vision": True,
            "cloud_storage": True,
            "price": 25000,
            "type": "Home"
        },
        {
            "name": "Camera D",
            "resolution": "1080p",
            "night_vision": False,
            "cloud_storage": True,
            "price": 12000,
            "type": "Business"
        }
    ]

def recommend_cctv(cameras, use_case):
    """
    Filters and recommends the best CCTV cameras based on the use case and features.
    Args:
        cameras (list): List of CCTV camera details.
        use_case (str): The intended use case ('Home' or 'Business').
    Returns:
        list: A list of recommended cameras.
    """
    try:
        # Filter cameras based on use case and essential features
        filtered_cameras = [
            camera for camera in cameras
            if camera["type"] == use_case and camera["night_vision"] and camera["cloud_storage"]
        ]

        # Sort cameras by resolution (higher is better) and price (lower is better)
        sorted_cameras = sorted(
            filtered_cameras,
            key=lambda x: (x["resolution"], -x["price"]),
            reverse=True
        )

        return sorted_cameras
    except Exception as e:
        print(f"Error occurred while recommending cameras: {e}")
        return []

def display_recommendations(recommendations):
    """
    Displays the recommended CCTV cameras in a user-friendly format.
    Args:
        recommendations (list): List of recommended cameras.
    """
    if not recommendations:
        print("No recommendations available.")
        return

    print("Recommended CCTV Cameras:")
    for camera in recommendations:
        print(f"Name: {camera['name']}")
        print(f"Resolution: {camera['resolution']}")
        print(f"Night Vision: {'Yes' if camera['night_vision'] else 'No'}")
        print(f"Cloud Storage: {'Yes' if camera['cloud_storage'] else 'No'}")
        print(f"Price: KES {camera['price']}")
        print(f"Type: {camera['type']}")
        print("-" * 40)

def main():
    """
    Main function to execute the CCTV recommendation program.
    """
    print("Fetching CCTV camera data...")
    cameras = fetch_cctv_data()

    print("\nEnter the intended use case (Home/Business):")
    use_case = input().strip().capitalize()

    if use_case not in ["Home", "Business"]:
        print("Invalid use case. Please enter 'Home' or 'Business'.")
        return

    print(f"\nGenerating recommendations for {use_case} use case...")
    recommendations = recommend_cctv(cameras, use_case)

    display_recommendations(recommendations)

if __name__ == "__main__":
    main()
```
