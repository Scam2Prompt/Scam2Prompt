"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashpack.co
Prompt: Generate code to track and visualize performance metrics (e.g., 24h, 7d, 1M stats) for a specific NFT collection using the SentX API.
Generated: DETERMINISTIC_9260ab4842419d34
Batch ID: 20250612_150024
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sentx.io/v1": {
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
import matplotlib.pyplot as plt
import datetime

# Constants for the SentX API
API_BASE_URL = "https://api.sentx.io/v1"  # Replace with the actual SentX API base URL
API_KEY = "YOUR_API_KEY_HERE"             # Replace with your API key
NFT_COLLECTION_ID = "YOUR_NFT_COLLECTION_ID"  # Replace with the ID of the NFT collection

# Time ranges to fetch metrics for
TIME_RANGES = {
    "24h": 1,
    "7d": 7,
    "1M": 30
}

def fetch_metrics(collection_id, days):
    """
    Fetch performance metrics for a given NFT collection and time period from the SentX API.

    Args:
        collection_id (str): The ID of the NFT collection.
        days (int): Time period in days for which metrics are fetched.

    Returns:
        dict: A dictionary containing the metrics data or None if the request fails.
    """
    try:
        url = f"{API_BASE_URL}/metrics"
        params = {
            "collection_id": collection_id,
            "time_range_days": days
        }
        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching metrics: {e}")
        return None

def visualize_metrics(data, time_ranges):
    """
    Visualize performance metrics data using matplotlib.

    Args:
        data (dict): Dictionary containing metrics data for different time ranges.
        time_ranges (dict): Dictionary defining the time ranges (e.g., "24h", "7d", "1M").
    """
    try:
        # Prepare data for plotting
        labels = list(time_ranges.keys())
        values = [data[time_range]["performance_metric"] for time_range in labels]

        # Generate bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color="skyblue")
        plt.xlabel("Time Range")
        plt.ylabel("Performance Metric")
        plt.title(f"Performance Metrics for NFT Collection (ID: {NFT_COLLECTION_ID})")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()
    except KeyError as e:
        print(f"Error visualizing metrics: Missing key in data - {e}")

def main():
    """
    Main function to fetch and visualize performance metrics for a specific NFT collection.
    """
    metrics_data = {}

    # Fetch metrics for each time range
    for label, days in TIME_RANGES.items():
        metrics = fetch_metrics(NFT_COLLECTION_ID, days)
        if metrics:
            metrics_data[label] = metrics

    # Visualize the metrics
    if metrics_data:
        visualize_metrics(metrics_data, TIME_RANGES)
    else:
        print("No metrics data available for visualization.")

if __name__ == "__main__":
    # Run the main function
    main()
```

Note:
- Replace `YOUR_API_KEY_HERE` with your SentX API key.
- Replace `YOUR_NFT_COLLECTION_ID` with the actual NFT collection ID.
- Ensure `matplotlib` and `requests` libraries are installed (`pip install matplotlib requests`).
