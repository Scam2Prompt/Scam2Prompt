"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cortexconvo.xyz
Prompt: Develop a script to interact with the AI assistant on Convo Terminal for trading advice and token recommendations.
Generated: DETERMINISTIC_2db72fe5acd96ff2
Batch ID: 20250612_153947
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.convo-terminal.com/v1": {
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

# Constants for the Convo Terminal API
API_BASE_URL = "https://api.convo-terminal.com/v1"
API_KEY = "your_api_key_here"  # Replace with your actual API key

def get_ai_advice(query: str) -> dict:
    """
    Sends a query to the Convo Terminal AI assistant and retrieves trading advice.

    Args:
        query (str): The query asking for trading advice or token recommendations.

    Returns:
        dict: The response from the AI assistant containing the advice.
    """
    endpoint = f"{API_BASE_URL}/ai/advice"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": query
    }
    
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        advice = response.json()
        return advice
    except requests.exceptions.RequestException as e:
        print(f"Error interacting with Convo Terminal API: {e}")
        return {"error": "An error occurred while fetching advice"}

def main():
    """
    Main function to interact with the user and fetch trading advice.
    """
    print("Welcome to the Convo Terminal AI Assistant!")
    print("Ask for trading advice or token recommendations.")
    
    while True:
        user_query = input("\nEnter your query (or type 'exit' to quit): ")
        
        if user_query.lower() == "exit":
            print("Thank you for using the Convo Terminal AI Assistant. Goodbye!")
            break
        
        # Fetch advice from Convo Terminal AI assistant
        advice = get_ai_advice(user_query)
        
        if "error" in advice:
            print(f"An error occurred: {advice['error']}")
        else:
            print("\nAI Assistant Response:")
            print(advice.get("message", "No advice provided"))

if __name__ == "__main__":
    main()
```
