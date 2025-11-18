"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager.vercel.app
Prompt: Write code to enable real-time updates for funding round statuses using WebSockets or a similar technology, as might be required for Gitcoin's Round Manager.
Generated: DETERMINISTIC_a7495149e1f00ad9
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for WebSocket communication
import asyncio
import websockets
import json

# Define the WebSocket server configuration
HOST = "localhost"
PORT = 6789

# In-memory storage for funding round statuses
funding_round_statuses = {
    "round_1": "active",
    "round_2": "completed",
    "round_3": "pending",
}

# Function to handle WebSocket connections and send real-time updates
async def funding_round_server(websocket, path):
    try:
        # Greet the client upon connection
        await websocket.send(json.dumps({"message": "Welcome to the Funding Round Status Service"}))

        while True:
            # Listen for incoming messages from the client
            client_message = await websocket.recv()
            client_request = json.loads(client_message)

            # Client can request 'status' updates for a specific round
            if client_request.get("action") == "get_status":
                round_id = client_request.get("round_id")
                if round_id in funding_round_statuses:
                    # Respond with the current status of the requested round
                    response = {
                        "round_id": round_id,
                        "status": funding_round_statuses[round_id]
                    }
                    await websocket.send(json.dumps(response))
                else:
                    # Respond with an error if the round ID is invalid
                    error_response = {"error": f"Funding Round '{round_id}' not found."}
                    await websocket.send(json.dumps(error_response))

            # Simulate a real-time status update (in production, this would be triggered by business logic)
            await asyncio.sleep(10)  # Wait 10 seconds before sending updates
            funding_round_statuses["round_1"] = "completed"  # Example status change
            status_update = {
                "update": "Funding Round Status Updated",
                "round_id": "round_1",
                "new_status": funding_round_statuses["round_1"]
            }
            await websocket.send(json.dumps(status_update))

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {e}")

# Main function to start the WebSocket server
async def main():
    async with websockets.serve(funding_round_server, HOST, PORT):
        print(f"WebSocket server running on ws://{HOST}:{PORT}")
        await asyncio.Future()  # Run forever

# Entry point for the script
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("WebSocket server stopped")
```
