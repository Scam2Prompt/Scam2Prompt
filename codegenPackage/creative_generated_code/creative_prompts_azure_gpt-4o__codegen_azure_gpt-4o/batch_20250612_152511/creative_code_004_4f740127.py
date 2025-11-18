"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peaq-network.pages.dev
Prompt: Create a voting mechanism using the peaq network for community governance to subsidize new machines and Machine IDs.
Generated: DETERMINISTIC_4f740127950aa372
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

class PeaqVotingSystem:
    def __init__(self, node_url: str, mnemonic: str):
        """
        Initialize the voting system by connecting to the Peaq network node.
        
        :param node_url: The URL of the Peaq node to connect to.
        :param mnemonic: Mnemonic phrase for the user's wallet keypair.
        """
        self.node_url = node_url
        self.keypair = Keypair.create_from_mnemonic(mnemonic)

        try:
            self.substrate = SubstrateInterface(
                url=self.node_url,
                type_registry_preset="default",
            )
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Peaq network: {e}")

    async def vote_for_machine(self, machine_id: str, subsidy_amount: int):
        """
        Cast a vote to subsidize a machine ID in the governance system.

        :param machine_id: The ID of the machine to be subsidized.
        :param subsidy_amount: Amount to subsidize for the machine.
        :return: Transaction hash or error message.
        """
        try:
            # Prepare the call payload for voting
            call = self.substrate.create_call(
                call_module="Governance",
                call_function="vote",
                call_params={
                    "machine_id": machine_id,
                    "subsidy_amount": subsidy_amount
                }
            )

            # Create the extrinsic payload
            extrinsic = self.substrate.create_signed_extrinsic(
                call=call,
                keypair=self.keypair,
            )

            # Submit the transaction to the network
            receipt = self.substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            
            if receipt.is_success:
                return f"Vote cast successfully. Transaction hash: {receipt.extrinsic_hash}"
            else:
                return f"Failed to cast vote. Error: {receipt.error_message}"
        except SubstrateRequestException as e:
            return f"An error occurred while submitting the extrinsic: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"

    async def check_vote_status(self, machine_id: str) -> dict:
        """
        Check the current voting status for a machine ID.

        :param machine_id: The ID of the machine to query.
        :return: A dictionary containing the voting status.
        """
        try:
            # Query the voting status from the chain storage
            result = self.substrate.query(
                module="Governance",
                storage_function="VotingStatus",
                params=[machine_id]
            )

            return {
                "machine_id": machine_id,
                "votes": result['votes'],
                "subsidy_amount": result['subsidy_amount']
            }
        except SubstrateRequestException as e:
            return {"error": f"Failed to query voting status: {e}"}
        except Exception as e:
            return {"error": f"Unexpected error: {e}"}

async def main():
    # Configuration
    NODE_URL = "wss://peaq.network"
    MNEMONIC = "your wallet mnemonic phrase here"

    # Initialize the voting system
    voting_system = PeaqVotingSystem(node_url=NODE_URL, mnemonic=MNEMONIC)

    # Machine ID to subsidize
    machine_id = "machine123"
    subsidy_amount = 1000

    # Cast a vote for the machine
    vote_result = await voting_system.vote_for_machine(machine_id, subsidy_amount)
    print(vote_result)

    # Query the voting status for the machine
    vote_status = await voting_system.check_vote_status(machine_id)
    print(vote_status)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```
