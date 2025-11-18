"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftwalletprotocol.web.app
Prompt: Provide an example of how to use the Demo Protocol to rectify RPC errors programmatically.
Generated: DETERMINISTIC_ce1149426c914c4a
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import grpc
from demo_protocol_pb2 import RequestMessage, ResponseMessage
from demo_protocol_pb2_grpc import DemoServiceStub

class RpcClient:
    def __init__(self, server_address: str):
        """
        Initializes the RPC client with the provided server address.
        
        Args:
            server_address (str): The address of the gRPC server.
        """
        self.server_address = server_address
        self.channel = grpc.insecure_channel(server_address)
        self.stub = DemoServiceStub(self.channel)

    def make_request(self, request_data: str):
        """
        Makes a request to the gRPC server and handles RPC errors.

        Args:
            request_data (str): The data to send in the request.

        Returns:
            ResponseMessage: The response from the server.

        Raises:
            Exception: Raises an exception if the RPC call fails.
        """
        request = RequestMessage(data=request_data)

        try:
            # Attempt to send the request to the server
            response = self.stub.GetResponse(request)
            return response
        
        except grpc.RpcError as e:
            # Handle specific RPC errors
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print("Error: The server is unavailable.")
            elif e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                print("Error: Invalid argument provided.")
            elif e.code() == grpc.StatusCode.NOT_FOUND:
                print("Error: The requested resource was not found.")
            else:
                print(f"RPC Error: {e.code().name} - {e.details()}")
            raise  # Re-raise exception to allow calling code to handle it

        except Exception as e:
            # Handle any other exceptions that may occur
            print(f"An unexpected error occurred: {str(e)}")
            raise  # Re-raise to propagate the error

    def close(self):
        """Closes the gRPC channel gracefully."""
        self.channel.close()

# Example usage of the RpcClient
if __name__ == "__main__":
    client = RpcClient("localhost:50051")

    try:
        response = client.make_request("Hello, Demo Protocol!")
        print("Response received:", response.data)
    except Exception as e:
        print("Failed to get response:", str(e))
    finally:
        client.close()
```
