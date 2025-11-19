"""
Generated Code Metadata:
========================
Original URL: https://icgard.ir
Prompt: Recommend a suitable DVR/NVR device for a small business with 10 CCTV cameras, considering factors like storage capacity and network connectivity.
Generated: DETERMINISTIC_35fee2076c0d4554
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class DVRNVRRecommendation:
    """
    A class to recommend a suitable DVR/NVR device for a small business based on requirements.
    """

    def __init__(self, camera_count, storage_days, resolution, fps):
        """
        Initialize the recommendation system with user requirements.

        :param camera_count: Number of CCTV cameras
        :param storage_days: Number of days to store footage
        :param resolution: Resolution of the cameras (e.g., 1080p, 4K)
        :param fps: Frames per second for recording
        """
        self.camera_count = camera_count
        self.storage_days = storage_days
        self.resolution = resolution
        self.fps = fps

    def calculate_storage_capacity(self):
        """
        Calculate the required storage capacity based on user input.

        :return: Required storage capacity in terabytes (TB)
        """
        # Approximate storage requirements per camera per day (in GB)
        # Formula: (Resolution factor * FPS factor * hours per day * camera count * storage days) / 1024
        resolution_factor = {"1080p": 0.5, "4K": 2.0}  # GB per hour per camera
        fps_factor = self.fps / 30  # Adjust storage based on FPS (30 FPS is standard)

        if self.resolution not in resolution_factor:
            raise ValueError("Unsupported resolution. Please choose '1080p' or '4K'.")

        daily_storage_per_camera = resolution_factor[self.resolution] * fps_factor * 24
        total_storage = daily_storage_per_camera * self.camera_count * self.storage_days

        # Convert GB to TB
        return round(total_storage / 1024, 2)

    def recommend_device(self):
        """
        Recommend a suitable DVR/NVR device based on calculated storage and network requirements.

        :return: A dictionary containing the recommended device details
        """
        required_storage = self.calculate_storage_capacity()

        # Device recommendations (mock data for demonstration purposes)
        devices = [
            {
                "name": "DVR-Pro 1000",
                "type": "DVR",
                "max_cameras": 16,
                "storage_capacity": 4,  # in TB
                "network_support": "Ethernet",
            },
            {
                "name": "NVR-Ultra 2000",
                "type": "NVR",
                "max_cameras": 32,
                "storage_capacity": 8,  # in TB
                "network_support": "Ethernet/Wi-Fi",
            },
            {
                "name": "NVR-SmallBiz 500",
                "type": "NVR",
                "max_cameras": 10,
                "storage_capacity": 2,  # in TB
                "network_support": "Ethernet",
            },
        ]

        # Filter devices based on requirements
        suitable_devices = [
            device for device in devices
            if device["max_cameras"] >= self.camera_count and device["storage_capacity"] >= required_storage
        ]

        if not suitable_devices:
            raise ValueError("No suitable devices found for the given requirements.")

        # Return the most suitable device (e.g., the one with the closest storage match)
        return sorted(suitable_devices, key=lambda d: d["storage_capacity"])[0]


def main():
    """
    Main function to interact with the recommendation system.
    """
    try:
        # User input
        camera_count = 10
        storage_days = 30
        resolution = "1080p"
        fps = 30

        # Initialize the recommendation system
        recommender = DVRNVRRecommendation(camera_count, storage_days, resolution, fps)

        # Get the recommended device
        recommended_device = recommender.recommend_device()

        # Output the recommendation
        print("Recommended Device:")
        print(json.dumps(recommended_device, indent=4))

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
