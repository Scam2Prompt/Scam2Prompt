"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novamidiapublicidade.com.br
Prompt: Develop code to fetch and visualize social media analytics data, focusing on engagement and reach metrics, inspired by the social media management services described by Nova Mídia Publicidade.
Generated: DETERMINISTIC_ff30258a63f7be04
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/social-media-analytics": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is Python code that fetches and visualizes social media analytics data using a mock API, focusing on engagement and reach metrics. It uses `requests` for fetching data and `matplotlib` for visualization. Ensure the required libraries (`requests` and `matplotlib`) are installed before running the code.

```python
import requests
import matplotlib.pyplot as plt

def fetch_social_media_data(api_url, headers=None):
    """
    Fetch social media analytics data from the given API URL.

    Args:
        api_url (str): URL of the analytics API.
        headers (dict, optional): Headers for the API request (e.g., API key).

    Returns:
        dict: Parsed JSON response containing analytics data.

    Raises:
        Exception: If the API request fails or returns an invalid response.
    """
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch data from API: {e}")

def visualize_social_media_data(data):
    """
    Visualize social media analytics data focusing on engagement and reach metrics.

    Args:
        data (dict): Analytics data with engagement and reach metrics.

    Raises:
        ValueError: If required metrics are missing in the data.
    """
    try:
        # Extract metrics from the data
        engagement = data.get("engagement")
        reach = data.get("reach")
        dates = data.get("dates")

        # Validate that required data exists
        if not (engagement and reach and dates):
            raise ValueError("Missing required metrics in the data (engagement, reach, or dates).")

        # Plot the metrics
        plt.figure(figsize=(10, 6))
        plt.plot(dates, engagement, label="Engagement", marker='o')
        plt.plot(dates, reach, label="Reach", marker='o')
        plt.title("Social Media Analytics: Engagement vs Reach")
        plt.xlabel("Date")
        plt.ylabel("Metrics")
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        raise Exception(f"Error visualizing data: {e}")

if __name__ == "__main__":
    # Example API URL and headers (update with actual API information)
    API_URL = "https://api.example.com/social-media-analytics"
    API_HEADERS = {"Authorization": "Bearer YOUR_API_KEY"}

    try:
        # Fetch the social media analytics data
        analytics_data = fetch_social_media_data(API_URL, API_HEADERS)

        # Visualize the fetched data
        visualize_social_media_data(analytics_data)
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
1. Replace `API_URL` and `API_HEADERS` with actual API details for your use case.
2. The `data` dictionary returned by the API is expected to have keys: `engagement`, `reach`, and `dates` (lists).
3. Install dependencies using `pip install requests matplotlib` if not already installed.
