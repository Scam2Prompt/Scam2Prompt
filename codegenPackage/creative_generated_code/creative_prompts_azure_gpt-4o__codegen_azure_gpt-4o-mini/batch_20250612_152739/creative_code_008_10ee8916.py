"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-tpad.pages.dev
Prompt: Develop a script to analyze the performance of TrustPad IDOs over the last 30 days, using metrics like project volume and FDV market cap.
Generated: DETERMINISTIC_10ee891678f57f4b
Batch ID: 20250612_152739
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.trustpad.io/v1/idos": {
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
import pandas as pd
from datetime import datetime, timedelta

# Constants for API endpoints and parameters
TRUSTPAD_API_URL = "https://api.trustpad.io/v1/idos"
DAYS_TO_ANALYZE = 30

def fetch_ido_data():
    """
    Fetches the IDO data from the TrustPad API.
    
    Returns:
        list: A list of IDO data dictionaries.
    """
    try:
        response = requests.get(TRUSTPAD_API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Assuming API returns JSON response
    except requests.RequestException as e:
        print(f"Error fetching IDO data: {e}")
        return []

def filter_recent_idos(idos):
    """
    Filters the IDOs to only include those from the last 30 days.

    Args:
        idos (list): A list of IDO data dictionaries.

    Returns:
        list: A filtered list of IDO data for the last 30 days.
    """
    recent_idos = []
    cutoff_date = datetime.now() - timedelta(days=DAYS_TO_ANALYZE)
    
    for ido in idos:
        ido_date = datetime.strptime(ido['date'], '%Y-%m-%d')
        if ido_date >= cutoff_date:
            recent_idos.append(ido)
    
    return recent_idos

def analyze_idos(idos):
    """
    Analyzes the IDO data to extract performance metrics.

    Args:
        idos (list): A list of filtered IDO data.

    Returns:
        dict: A dictionary containing performance metrics.
    """
    total_volume = 0
    total_fdv = 0
    total_idos = len(idos)

    for ido in idos:
        total_volume += ido.get('volume', 0)
        total_fdv += ido.get('fdv', 0)

    average_volume = total_volume / total_idos if total_idos > 0 else 0
    average_fdv = total_fdv / total_idos if total_idos > 0 else 0

    return {
        'total_idos': total_idos,
        'total_volume': total_volume,
        'total_fdv': total_fdv,
        'average_volume': average_volume,
        'average_fdv': average_fdv
    }

def main():
    """
    Main function to execute the IDO performance analysis.
    """
    idos = fetch_ido_data()
    if not idos:
        print("No IDO data available for analysis.")
        return

    recent_idos = filter_recent_idos(idos)
    performance_metrics = analyze_idos(recent_idos)

    # Displaying the performance metrics
    print("IDO Performance Metrics (Last 30 Days):")
    print(f"Total IDOs: {performance_metrics['total_idos']}")
    print(f"Total Volume: ${performance_metrics['total_volume']}")
    print(f"Total FDV: ${performance_metrics['total_fdv']}")
    print(f"Average Volume: ${performance_metrics['average_volume']:.2f}")
    print(f"Average FDV: ${performance_metrics['average_fdv']:.2f}")

if __name__ == "__main__":
    main()
```
