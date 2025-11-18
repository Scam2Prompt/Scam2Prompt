"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webex.net.cn
Prompt: Generate code to implement Webex's dual-mode whiteboard functionality for real-time brainstorming and idea sharing during a virtual meeting.
Generated: DETERMINISTIC_b0013f6932d06c29
Batch ID: 20250612_150651
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
import uuid

# Constants for WebSocket server
HOST = 'localhost'
PORT = 8765

# In-memory storage to keep track of whiteboard state
whiteboard_data = {}

# Error handling and logging utility
def log_error(message):
    print(f"[ERROR] {message}")

def log_info(message):
    print(f"[INFO] {message}")

async def handle_connection(websocket, path):
    """
    Handles incoming WebSocket connections and processes messages related to the whiteboard.
    """
    try:
        async for message in websocket:
            log_info(f"Received message: {message}")
            
            # Parse the incoming message
            try:
                data = json.loads(message)
            except json.JSONDecodeError as e:
                await websocket.send(json.dumps({"error": "Invalid JSON format"}))
                log_error(f"JSON Decode Error: {e}")
                continue
            
            action = data.get("action")
            board_id = data.get("board_id")
            
            # Validate required fields
            if not action:
                await websocket.send(json.dumps({"error": "Missing 'action' field"}))
                continue
            
            # Handle different actions
            if action == "create":
                # Create a new whiteboard and return its ID
                board_id = str(uuid.uuid4())
                whiteboard_data[board_id] = []
                log_info(f"Created new whiteboard with ID: {board_id}")
                await websocket.send(json.dumps({"status": "success", "board_id": board_id}))
            
            elif action == "update":
                # Update an existing whiteboard with new data
                if not board_id or board_id not in whiteboard_data:
                    await websocket.send(json.dumps({"error": "Invalid or missing 'board_id'"}))
                    continue
                
                updates = data.get("updates")
                if not isinstance(updates, list):
                    await websocket.send(json.dumps({"error": "'updates' must be a list"}))
                    continue
                
                whiteboard_data[board_id].extend(updates)  # Append updates to the whiteboard
                log_info(f"Updated whiteboard {board_id}. Current data: {whiteboard_data[board_id]}")
                await websocket.send(json.dumps({"status": "success", "message": "Whiteboard updated"}))
            
            elif action == "retrieve":
                # Retrieve the current state of the whiteboard
                if not board_id or board_id not in whiteboard_data:
                    await websocket.send(json.dumps({"error": "Invalid or missing 'board_id'"}))
                    continue
                
                current_state = whiteboard_data[board_id]
                log_info(f"Retrieved whiteboard {board_id}. Current state: {current_state}")
                await websocket.send(json.dumps({"status": "success", "data": current_state}))
            
            else:
                await websocket.send(json.dumps({"error": "Unknown action"}))
    
    except websockets.exceptions.ConnectionClosedError as e:
        log_error(f"Connection closed abruptly: {e}")
    except Exception as e:
        log_error(f"Unexpected error: {e}")

async def main():
    """
    Start the WebSocket server for dual-mode whiteboard functionality.
    """
    async with websockets.serve(handle_connection, HOST, PORT):
        log_info(f"WebSocket server started on ws://{HOST}:{PORT}")
        await asyncio.Future()  # Run forever

# Entry point for the WebSocket server
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log_info("Server stopped manually.")
    except Exception as e:
        log_error(f"Failed to start server: {e}")
```
