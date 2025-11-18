"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethir.ai
Prompt: Develop a program to track GPU usage and costs using Aethir’s GPU Dashboard API for a decentralized cloud gaming project.
Generated: DETERMINISTIC_3765b307930dea26
Batch ID: 20250612_145121
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aethir.io/v1/gpu-dashboard": {
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
import json
from datetime import datetime

# Constants
API_BASE_URL = "https://api.aethir.io/v1/gpu-dashboard"
API_KEY = "your_api_key_here"  # Replace with your actual API key
COST_PER_HOUR = 0.50  # Example cost per GPU usage hour in dollars

# Function to fetch GPU usage data from the Aethir API
def fetch_gpu_usage():
    """
    Fetch GPU usage statistics from the Aethir GPU Dashboard API.
    
    Returns:
        dict: GPU usage data (in JSON format).
    Raises:
        Exception: If the API request fails or an error occurs.
    """
    url = f"{API_BASE_URL}/usage"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()  # Return JSON response
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch GPU usage data: {e}")

# Function to calculate costs based on GPU usage
def calculate_costs(gpu_data):
    """
    Calculate the total cost based on GPU usage hours.
    
    Args:
        gpu_data (dict): JSON data containing GPU usage hours.
    
    Returns:
        dict: A summary of costs per GPU and total cost.
    """
    costs_summary = {}
    total_cost = 0.0
    
    # Iterate through GPU data and compute costs
    for gpu in gpu_data.get("gpus", []):
        gpu_id = gpu["id"]
        usage_hours = gpu["usage_hours"]
        cost = usage_hours * COST_PER_HOUR
        costs_summary[gpu_id] = cost
        total_cost += cost
    
    # Final summary
    return {
        "costs_per_gpu": costs_summary,
        "total_cost": total_cost
    }

# Main function
def main():
    """
    Main function to track GPU usage and costs.
    """
    try:
        print("Fetching GPU usage data...")
        gpu_data = fetch_gpu_usage()
        
        print("Calculating costs...")
        costs_summary = calculate_costs(gpu_data)
        
        # Display results
        print("\nGPU Usage Costs Summary:")
        print(json.dumps(costs_summary, indent=4))
        
        # Save summary to file
        output_filename = f"gpu_usage_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_filename, 'w') as output_file:
            json.dump(costs_summary, output_file, indent=4)
        
        print(f"\nSummary saved to {output_filename}")
    
    except Exception as e:
        print(f"Error: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
