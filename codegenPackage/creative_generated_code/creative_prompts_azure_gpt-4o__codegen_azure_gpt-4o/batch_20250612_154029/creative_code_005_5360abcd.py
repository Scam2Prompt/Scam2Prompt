"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-apps.web.app
Prompt: Explain how to cancel a connection via a light client on the Astar Network and provide sample code for implementation.
Generated: DETERMINISTIC_5360abcdb02b54ad
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from substrateinterface import SubstrateInterface, Keypair, SubstrateRequestException

# Configuration
ASTAR_NODE_URL = "wss://rpc.astar.network"  # URL of the Astar Network node
MNEMONIC = "your mnemonic phrase here"  # Replace with your light client's mnemonic phrase
CONNECTION_ID = "connection_id_to_cancel"  # Replace with the connection ID you want to cancel

def cancel_connection():
    """
    Function to cancel a connection using a light client on the Astar Network.
    """
    try:
        # Establish connection to the Astar Network node
        substrate = SubstrateInterface(
            url=ASTAR_NODE_URL,
            type_registry_preset='astar'
        )
        
        # Generate keypair from mnemonic
        keypair = Keypair.create_from_mnemonic(MNEMONIC)
        
        # Prepare extrinsic call details
        call = substrate.compose_call(
            call_module='ConnectionManagement',  # Replace with the actual module name if it differs
            call_function='cancel_connection',  # Replace with the actual function name
            call_params={
                'connection_id': CONNECTION_ID  # Pass the connection ID to cancel
            }
        )
        
        # Create and sign extrinsic
        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
        
        # Submit extrinsic to the network
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        
        # Check receipt status
        if receipt.is_success:
            print(f"Connection {CONNECTION_ID} has been successfully canceled!")
        else:
            print(f"Failed to cancel connection {CONNECTION_ID}. Error: {receipt.error_message}")
    
    except SubstrateRequestException as e:
        print(f"Substrate request error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Execute the function
if __name__ == "__main__":
    cancel_connection()
```
