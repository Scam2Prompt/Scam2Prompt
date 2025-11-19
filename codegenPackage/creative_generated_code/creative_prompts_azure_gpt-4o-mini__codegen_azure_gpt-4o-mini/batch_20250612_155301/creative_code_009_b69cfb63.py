"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: What resources are available for learning about Ethereum's smart contract languages like Solidity and Vyper?
Generated: DETERMINISTIC_b69cfb630d63d743
Batch ID: 20250612_155301
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/learning_resources/ethereum": {
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

def fetch_learning_resources():
    """
    Fetches a list of resources for learning about Ethereum's smart contract languages
    like Solidity and Vyper from a public API.
    
    Returns:
        list: A list of learning resources.
    """
    url = "https://api.example.com/learning_resources/ethereum"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching learning resources: {e}")
        return []

    # Parse the JSON response
    try:
        resources = response.json()
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return []

    return resources

def display_resources(resources):
    """
    Displays the provided learning resources in a structured format.
    
    Args:
        resources (list): The list of resources to display.
    """
    if not resources:
        print("No resources available.")
        return

    print("Learning Resources for Ethereum Smart Contracts:\n")
    for resource in resources:
        title = resource.get("title", "No Title")
        link = resource.get("link", "No Link")
        description = resource.get("description", "No Description")
        
        print(f"Title: {title}\nLink: {link}\nDescription: {description}\n")

def main():
    """
    Main function to fetch and display Ethereum learning resources.
    """
    resources = fetch_learning_resources()
    display_resources(resources)

if __name__ == "__main__":
    main()
```
