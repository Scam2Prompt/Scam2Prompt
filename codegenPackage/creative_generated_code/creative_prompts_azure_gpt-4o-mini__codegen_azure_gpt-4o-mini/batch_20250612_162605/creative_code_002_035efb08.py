"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-portal.vercel.app
Prompt: What are the steps to implement a light client connection in the Astar Portal, and how can I handle cancellations?
Generated: DETERMINISTIC_035efb08b7054f2e
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import logging

class AstarPortalLightClient:
    """
    A class to implement a light client connection to the Astar Portal.
    """

    def __init__(self, endpoint):
        """
        Initializes the light client with the given endpoint.
        
        :param endpoint: The URL of the Astar Portal to connect to.
        """
        self.endpoint = endpoint
        self.session = None

    async def connect(self):
        """
        Establishes a connection to the Astar Portal.
        """
        try:
            self.session = await asyncio.open_connection(self.endpoint, 80)
            logging.info(f"Connected to Astar Portal at {self.endpoint}")
        except Exception as e:
            logging.error(f"Failed to connect to Astar Portal: {e}")
            raise

    async def send_request(self, request):
        """
        Sends a request to the Astar Portal and awaits the response.
        
        :param request: The request to send.
        :return: The response from the portal.
        """
        if self.session is None:
            raise ConnectionError("Light client is not connected.")

        try:
            writer = self.session[1]
            reader = self.session[0]

            # Send the request
            writer.write(request.encode())
            await writer.drain()
            logging.info(f"Request sent: {request}")

            # Await the response
            response = await reader.read(100)  # Read up to 100 bytes
            logging.info(f"Response received: {response.decode()}")
            return response.decode()
        except asyncio.CancelledError:
            logging.warning("Request was cancelled.")
            raise
        except Exception as e:
            logging.error(f"Error sending request: {e}")
            raise

    async def close(self):
        """
        Closes the connection to the Astar Portal.
        """
        if self.session:
            self.session[1].close()
            await self.session[1].wait_closed()
            self.session = None
            logging.info("Connection to Astar Portal closed.")

async def main():
    """
    Main function to run the light client connection example.
    """
    client = AstarPortalLightClient("example.astar.portal")

    try:
        await client.connect()
        
        # Example request handling with cancellation
        request_task = asyncio.create_task(client.send_request("GET /data"))

        # Simulate cancellation after a short delay
        await asyncio.sleep(1)
        request_task.cancel()  # This will cancel the send_request task

        try:
            await request_task
        except asyncio.CancelledError:
            logging.info("The request task was cancelled.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Set logging level
    asyncio.run(main())
```
