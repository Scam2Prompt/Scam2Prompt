"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maetamsklogi.talentlms.com
Prompt: "Generate a script that uses TalentLMS's AI-powered course generator to create a training module with text, images, and tests based on a given topic."
Generated: DETERMINISTIC_e1c6342855a1651b
Batch ID: 20250612_151752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.talentlms.com/v1/": {
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

# Constants
API_BASE_URL = "https://api.talentlms.com/v1/"
API_KEY = "your_api_key_here"  # Replace with your TalentLMS API key
COURSE_GENERATOR_ENDPOINT = "course-generator"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def create_training_module(topic):
    """
    Function to create a training module using TalentLMS AI-powered course generator.
    
    Args:
        topic (str): The topic for the training module.
        
    Returns:
        dict: Response containing the details of the created module or an error message.
    """
    payload = {
        "topic": topic,
        "include_text": True,
        "include_images": True,
        "include_tests": True
    }
    
    try:
        # Make the API request
        response = requests.post(
            API_BASE_URL + COURSE_GENERATOR_ENDPOINT,
            json=payload,
            headers=HEADERS
        )
        
        # Raise an error for HTTP request issues
        response.raise_for_status()
        
        # Parse the response JSON
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Handle exceptions related to the HTTP request
        return {"error": f"HTTP Request failed: {e}"}
    except Exception as e:
        # Handle any other exceptions
        return {"error": f"An unexpected error occurred: {e}"}

def main():
    """
    Main function to execute the script. Prompts the user for a topic and creates a training module.
    """
    print("Welcome to the AI-Powered Training Module Creator!")
    
    # Prompt user for the topic
    topic = input("Enter the topic for the training module: ").strip()
    
    if not topic:
        print("Error: Topic cannot be empty.")
        return
    
    # Generate the training module
    result = create_training_module(topic)
    
    if "error" in result:
        print(f"Failed to create training module: {result['error']}")
    else:
        print("Training module created successfully!")
        print("Module Details:")
        print(result)

if __name__ == "__main__":
    main()
```

**Note:**
- Replace the `your_api_key_here` placeholder with your actual TalentLMS API key. 
- Ensure that the TalentLMS API is enabled and the endpoint `/course-generator` exists and is accessible.
- Adjust the URL or payload format if the API specifications differ.
