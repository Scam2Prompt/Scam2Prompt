"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icursor.ai
Prompt: How can I create a writing tool that allows real-time collaboration with AI assistance, similar to the features of iCursor?
Generated: DETERMINISTIC_882376b66b129893
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import websockets
import json
from concurrent.futures import ThreadPoolExecutor
import openai

# Async server for real-time collaboration
class RealTimeCollaborationServer:
    def __init__(self, host='localhost', port=8765):
        self.host = host
        self.port = port
        self.clients = set()
        self.executor = ThreadPoolExecutor()
        openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API Key

    async def handler(self, websocket, path):
        """
        Main handler for WebSocket connections. Handles client messages and broadcasts updates.
        """
        self.clients.add(websocket)  # Add client to the active clients list
        try:
            async for message in websocket:
                data = json.loads(message)
                if data.get('type') == 'text_update':
                    # Broadcast the updated text to all connected clients
                    await self.broadcast(data)
                elif data.get('type') == 'ai_assist':
                    # Generate AI assistance based on the text
                    ai_response = await self.generate_ai_assistance(data.get('text', ''))
                    await websocket.send(json.dumps({"type": "ai_response", "response": ai_response}))
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            self.clients.remove(websocket)  # Remove client on disconnect

    async def broadcast(self, message):
        """
        Broadcasts message to all connected clients.
        """
        if self.clients:  # Ensure there are active clients
            await asyncio.wait([client.send(json.dumps(message)) for client in self.clients])

    async def generate_ai_assistance(self, text):
        """
        Generates AI assistance using OpenAI's GPT model.
        """
        try:
            # Delegate the work to a thread pool to avoid blocking the event loop
            response = await asyncio.get_event_loop().run_in_executor(self.executor, self.call_openai_api, text)
            return response
        except Exception as e:
            return f"Error generating AI assistance: {str(e)}"

    def call_openai_api(self, text):
        """
        Calls OpenAI GPT API to generate AI assistance.
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Replace with the desired GPT model
                prompt=f"Provide assistance for the following text: {text}",
                max_tokens=150,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error interacting with OpenAI API: {str(e)}"

    async def start(self):
        """
        Starts the WebSocket server.
        """
        async with websockets.serve(self.handler, self.host, self.port):
            print(f"Server started on ws://{self.host}:{self.port}. Waiting for connections...")
            await asyncio.Future()  # Run forever

# Entry point for the script
if __name__ == "__main__":
    try:
        server = RealTimeCollaborationServer()
        asyncio.run(server.start())
    except KeyboardInterrupt:
        print("Server shut down.")
```

### How it works:
1. This script sets up a WebSocket server to facilitate real-time collaboration.
2. AI assistance is provided using OpenAI's GPT model.
3. Error handling is present for WebSocket connections and API calls.
4. The server broadcasts updates to all connected clients and handles AI assistance requests individually. 

**Usage Notes:**
- Replace `"your_openai_api_key"` with a valid OpenAI API key.
- Test in a local environment with WebSocket clients to verify real-time functionality.
