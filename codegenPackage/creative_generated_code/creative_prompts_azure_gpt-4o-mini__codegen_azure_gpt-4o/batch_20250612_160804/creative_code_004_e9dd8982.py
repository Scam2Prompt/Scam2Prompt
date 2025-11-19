"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visit-aevo-21z.pages.dev
Prompt: Illustrate how to implement a feature that displays the operational status of AEVO systems in real-time.
Generated: DETERMINISTIC_e9dd8982283efee9
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure, here's the code for real-time operational status monitoring of AEVO systems using Python with WebSocket for real-time updates:

```python
import asyncio
import websockets
import json
from datetime import datetime

# Mock function to simulate AEVO system status retrieval
def get_aevo_system_status():
    # In a real-world scenario, this would query the system's API or database
    return {
        "system_name": "AEVO",
        "status": "Operational",
        "uptime": "99.99%",
        "last_checked": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# WebSocket server to broadcast AEVO system status in real-time
async def broadcast_status(websocket, path):
    try:
        while True:
            # Retrieve the current system status
            system_status = get_aevo_system_status()
            
            # Convert the status to JSON format for transmission
            status_json = json.dumps(system_status)
            
            # Send the system status to the connected client
            await websocket.send(status_json)
            
            # Wait before sending the next update (simulating real-time monitoring)
            await asyncio.sleep(5)  # Adjust this interval as needed
    except websockets.exceptions.ConnectionClosed:
        print("Client connection closed")
    except Exception as e:
        print(f"Error occurred: {e}")

# Entry point: Start the WebSocket server
async def main():
    # WebSocket server listens on localhost and port 6789
    server = await websockets.serve(broadcast_status, "localhost", 6789)
    print("WebSocket server is running on ws://localhost:6789")
    
    # Keep the server running indefinitely
    await server.wait_closed()

# Run the WebSocket server
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server shut down gracefully")
```

### Key Notes in the Code:
- **WebSocket Implementation**: The `websockets` library is used for real-time communication.
- **Error Handling**: Handles client disconnection and general errors gracefully.
- **Mock Status Retrieval**: The `get_aevo_system_status` function simulates status retrieval, which should be replaced with actual logic to query the AEVO system's operational status in a production environment.
- **Real-Time Updates**: Server broadcasts updates every 5 seconds; this interval can be adjusted based on requirements.
- **Documentation**: Inline comments explain key parts of the code comprehensively.
