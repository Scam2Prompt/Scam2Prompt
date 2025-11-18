"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: Recommend APIs for creating immersive AI art experiences, like those showcased in Refik Anadol's projects, and write code to integrate these APIs into a virtual reality application.
Generated: DETERMINISTIC_9f7edb77322bd8a4
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to integrate immersive AI art APIs into a Virtual Reality (VR) application.

This script uses OpenAI's DALL·E for AI art generation and Unity's WebSocket API to integrate
art into a VR environment. Ensure you have the required API keys and software installed before running.
"""

import openai
import websocket
import json

# API keys (replace with your own keys)
OPENAI_API_KEY = 'your_openai_api_key'
UNITY_VR_SERVER_URL = 'ws://your_vr_server_url'

# Function to generate AI art using OpenAI's DALL·E
def generate_ai_art(prompt):
    """
    Generates AI art based on a text prompt using OpenAI's DALL·E.

    Args:
        prompt (str): Description of the art to generate.

    Returns:
        str: URL to the generated art image.
    """
    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        # Extract the URL of the generated image
        return response['data'][0]['url']
    except Exception as e:
        print(f"Error generating AI art: {e}")
        return None

# Function to send data to the Unity VR application using WebSocket
def send_to_vr_server(image_url):
    """
    Sends generated AI art image URL to Unity VR application via WebSocket.

    Args:
        image_url (str): URL of the AI-generated image.
    """
    try:
        ws = websocket.create_connection(UNITY_VR_SERVER_URL)
        payload = json.dumps({"image_url": image_url})
        ws.send(payload)
        response = ws.recv()
        print(f"Server response: {response}")
        ws.close()
    except Exception as e:
        print(f"Error connecting to Unity VR server: {e}")

# Main application workflow
if __name__ == "__main__":
    # User input for art prompt
    art_prompt = input("Enter the description for the AI art: ")

    # Generate AI art
    image_url = generate_ai_art(art_prompt)
    if image_url:
        print(f"Generated AI art URL: {image_url}")

        # Integrate art into Unity VR application
        send_to_vr_server(image_url)
    else:
        print("Failed to generate AI art.")
```

**Requirements:**
1. Install the OpenAI Python SDK: `pip install openai`
2. Install WebSocket client: `pip install websocket-client`
3. Ensure the Unity VR application is set up to receive WebSocket messages containing image URLs.

**Best Practices followed:**
- Modular code structure for scalability.
- Proper error handling in API requests and WebSocket connections.
- Clear inline comments to explain functionality.
- Separation of concerns: AI art generation and VR application integration are handled in distinct functions.
