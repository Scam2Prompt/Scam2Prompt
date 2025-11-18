"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thesoniclabs.pages.dev
Prompt: Provide an example of how to use SonicDB for low-latency blockchain applications, including RPC, validator, and observer node configurations.
Generated: DETERMINISTIC_d0eaafeb4f26073a
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import json
import websockets
from typing import Any, Dict, List

class SonicDBClient:
    """
    A client for interacting with a SonicDB instance using WebSocket RPC calls.
    """

    def __init__(self, uri: str):
        """
        Initializes the SonicDBClient.

        Args:
            uri (str): The WebSocket URI of the SonicDB instance.
        """
        self.uri = uri

    async def connect(self) -> websockets.WebSocketClientProtocol:
        """
        Connects to the SonicDB WebSocket server.

        Returns:
            websockets.WebSocketClientProtocol: The connected WebSocket client.
        """
        try:
            return await websockets.connect(self.uri)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to SonicDB: {e}")

    async def send_request(self, websocket: websockets.WebSocketClientProtocol, method: str, params: List[Any]) -> Dict[str, Any]:
        """
        Sends a JSON-RPC request to SonicDB.

        Args:
            websocket (websockets.WebSocketClientProtocol): The connected WebSocket client.
            method (str): The RPC method to call.
            params (List[Any]): The parameters for the RPC call.

        Returns:
            Dict[str, Any]: The response from the SonicDB server.

        Raises:
            Exception: Raises an exception if the request fails or response is not valid.
        """
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        await websocket.send(json.dumps(request))
        response = await websocket.recv()
        response_data = json.loads(response)

        if 'error' in response_data:
            raise Exception(f"Error in RPC call: {response_data['error']}")
        
        return response_data

    async def run(self):
        """
        Main method to connect to SonicDB and make test RPC calls.
        """
        async with websockets.connect(self.uri) as websocket:
            # Example RPC call to get blockchain status
            try:
                status = await self.send_request(websocket, "getBlockchainStatus", [])
                print("Blockchain Status:", status)

                # Example RPC call to get validator nodes
                validators = await self.send_request(websocket, "getValidators", [])
                print("Validators:", validators)

                # Example RPC call to observe node information
                observers = await self.send_request(websocket, "getObservers", [])
                print("Observers:", observers)

            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with your SonicDB WebSocket URI
    sonicdb_uri = "ws://localhost:8080"

    # Run the SonicDB client
    client = SonicDBClient(sonicdb_uri)
    
    try:
        asyncio.run(client.run())
    except KeyboardInterrupt:
        print("Client stopped by user.")
```
