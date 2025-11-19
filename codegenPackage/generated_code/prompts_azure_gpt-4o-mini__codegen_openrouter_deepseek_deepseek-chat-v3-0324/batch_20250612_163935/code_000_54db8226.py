"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Generate a Python script that utilizes Polkadot's governance-allocated parachains for a common-good project, as discussed on Polkadot India.
Generated: DETERMINISTIC_54db8226d26e7287
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from substrateinterface import SubstrateInterface
from substrateinterface.exceptions import SubstrateRequestException

class PolkadotGovernanceClient:
    """
    A client to interact with Polkadot's governance system for common-good parachains.
    Handles connecting to the network, submitting proposals, and querying parachain info.
    """
    
    def __init__(self, node_url="wss://rpc.polkadot.io"):
        """
        Initialize the Polkadot governance client.
        
        Args:
            node_url (str): WebSocket URL of the Polkadot node to connect to
        """
        self.node_url = node_url
        self.substrate = None
        
    def connect(self):
        """
        Connect to the Polkadot network.
        
        Raises:
            SubstrateRequestException: If connection fails
        """
        try:
            self.substrate = SubstrateInterface(url=self.node_url)
            print(f"Connected to Polkadot node at {self.node_url}")
        except SubstrateRequestException as e:
            print(f"Connection failed: {e}")
            raise

    def get_parachain_info(self, para_id):
        """
        Get information about a specific parachain.
        
        Args:
            para_id (int): Parachain ID to query
            
        Returns:
            dict: Parachain information or None if not found
        """
        if not self.substrate:
            raise ConnectionError("Not connected to Polkadot network")
            
        try:
            result = self.substrate.query(
                module='Paras',
                storage_function='Parachains',
                params=[]
            )
            
            if para_id in result.value:
                lease_info = self.substrate.query(
                    module='Slots',
                    storage_function='Leases',
                    params=[para_id]
                )
                return {
                    'para_id': para_id,
                    'active': True,
                    'lease_info': lease_info.value
                }
            return None
        except Exception as e:
            print(f"Error querying parachain info: {e}")
            raise

    def submit_governance_proposal(self, proposal, keypair):
        """
        Submit a governance proposal for a common-good parachain.
        
        Args:
            proposal (dict): Proposal details including title, description, and parameters
            keypair (Keypair): Keypair for the account submitting the proposal
            
        Returns:
            str: Transaction hash if successful
        """
        if not self.substrate:
            raise ConnectionError("Not connected to Polkadot network")
            
        try:
            call = self.substrate.compose_call(
                call_module='Democracy',
                call_function='propose',
                call_params={
                    'proposal': {
                        'Legacy': proposal['call']
                    },
                    'value': proposal['value']
                }
            )
            
            extrinsic = self.substrate.create_signed_extrinsic(call=call, keypair=keypair)
            result = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            
            if result.is_success:
                print(f"Proposal submitted successfully: {result.extrinsic_hash}")
                return result.extrinsic_hash
            else:
                print(f"Proposal submission failed: {result.error_message}")
                return None
                
        except Exception as e:
            print(f"Error submitting proposal: {e}")
            raise

    def get_common_good_parachains(self):
        """
        Retrieve a list of common-good parachains.
        
        Returns:
            list: List of common-good parachain IDs and their information
        """
        if not self.substrate:
            raise ConnectionError("Not connected to Polkadot network")
            
        try:
            # In actual implementation, this would query the appropriate storage
            # For demo purposes, we return a mock response
            return [
                {'para_id': 1000, 'name': 'Statemint', 'purpose': 'Asset Hub'},
                {'para_id': 1001, 'name': 'Encointer', 'purpose': 'Basic Income'}
            ]
        except Exception as e:
            print(f"Error retrieving common-good parachains: {e}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize client
        client = PolkadotGovernanceClient()
        client.connect()
        
        # Get common-good parachains
        common_good_chains = client.get_common_good_parachains()
        print("Common-good parachains:", common_good_chains)
        
        # Query specific parachain info
        para_info = client.get_parachain_info(1000)
        print("Parachain 1000 info:", para_info)
        
        # Note: Actual proposal submission would require a valid keypair and properly formatted proposal
        # proposal_hash = client.submit_governance_proposal(proposal, keypair)
        
    except Exception as e:
        print(f"Error in main execution: {e}")
```
