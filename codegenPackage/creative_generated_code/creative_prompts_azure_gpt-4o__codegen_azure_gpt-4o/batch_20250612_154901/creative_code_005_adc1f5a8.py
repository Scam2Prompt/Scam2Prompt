"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msk-rk.ru
Prompt: Develop a script to calculate the time required for a token transfer between two networks using Hop Protocol, considering network congestion.
Generated: DETERMINISTIC_adc1f5a8801a8a5e
Batch ID: 20250612_154901
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.network-congestion.com/{network}/congestion`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.network-congestion.com/{network}/congestion": {
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
import time

def get_network_congestion(network):
    """
    Fetch current network congestion for the given network.
    
    Args:
        network (str): The name of the network (e.g., 'ethereum', 'polygon').
    
    Returns:
        float: Congestion level as a multiplier (e.g., 1.0 = normal speed, higher values = slower).
    """
    try:
        # Placeholder API endpoint (replace with actual congestion API for the network)
        api_url = f"https://api.network-congestion.com/{network}/congestion"
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data.get('congestion_multiplier', 1.0)  # Default multiplier if not found
    except requests.RequestException as e:
        print(f"Error fetching network congestion for {network}: {e}")
        return 1.0  # Assume normal speed if API fails


def calculate_transfer_time(source_network, destination_network, base_transfer_time):
    """
    Calculate the estimated transfer time for a token between two networks
    using the Hop Protocol, considering network congestion.
    
    Args:
        source_network (str): Source network name.
        destination_network (str): Destination network name.
        base_transfer_time (float): Base time for transfer in seconds under normal conditions.
    
    Returns:
        float: Estimated transfer time in seconds.
    """
    try:
        # Fetch congestion multipliers for both networks
        source_congestion = get_network_congestion(source_network)
        destination_congestion = get_network_congestion(destination_network)

        # Calculate adjusted transfer time
        adjusted_time = base_transfer_time * source_congestion * destination_congestion
        return adjusted_time
    except Exception as e:
        print(f"Error calculating transfer time: {e}")
        return base_transfer_time  # Default to base transfer time in case of an error


def main():
    """
    Main function to estimate token transfer time between two networks.
    """
    # User input for networks and base transfer time
    source_network = input("Enter source network name: ").strip().lower()
    destination_network = input("Enter destination network name: ").strip().lower()
    try:
        base_transfer_time = float(input("Enter base transfer time in seconds (e.g., 300): "))
    except ValueError:
        print("Invalid input for base transfer time. Please enter a numerical value.")
        return

    # Calculate estimated transfer time
    estimated_time = calculate_transfer_time(source_network, destination_network, base_transfer_time)
    print(f"Estimated token transfer time from {source_network} to {destination_network}: {estimated_time:.2f} seconds")


if __name__ == "__main__":
    # Measure script execution time
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Script executed in {end_time - start_time:.2f} seconds")
```

### Notes:
- Replace `https://api.network-congestion.com/{network}/congestion` with the actual API endpoint providing congestion data for the networks.
- Ensure the API key or authentication (if needed) is handled securely (e.g., via environment variables).
