"""
Generated Code Metadata:
========================
Original URL: https://neonlabs.org
Prompt: Write a code snippet to interact with Neon EVM and execute a smart contract on Solana using Ethereum-compatible tools.
Generated: DETERMINISTIC_0a2f5b3da70deb61
Batch ID: 20250612_151119
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://neon-proxy-mainnet.solana.p2p.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from web3 import Web3
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.system_program import TransferParams, transfer
from solana.rpc.types import TxOpts

# Configuration for Neon EVM (Ethereum-compatible layer on Solana)
NEON_RPC_URL = "https://neon-proxy-mainnet.solana.p2p.org"
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

# Initialize Web3 for Neon EVM
w3 = Web3(Web3.HTTPProvider(NEON_RPC_URL))

# Initialize Solana client
solana_client = Client(SOLANA_RPC_URL)

# Smart contract ABI and address (example)
CONTRACT_ABI = json.loads("""
    [
        {
            "inputs": [],
            "name": "exampleFunction",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]
""")
CONTRACT_ADDRESS = "0xYourContractAddressHere"

def execute_neon_evm_contract(private_key, contract_address, abi):
    """Execute a smart contract on Neon EVM"""
    try:
        # Set up account
        account = w3.eth.account.from_key(private_key)
        
        # Create contract instance
        contract = w3.eth.contract(address=contract_address, abi=abi)
        
        # Build transaction
        tx = contract.functions.exampleFunction().build_transaction({
            'chainId': w3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': w3.eth.gas_price,
            'nonce': w3.eth.get_transaction_count(account.address),
        })
        
        # Sign and send transaction
        signed_tx = account.sign_transaction(tx)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for transaction receipt
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt
    
    except Exception as e:
        print(f"Error executing Neon EVM contract: {e}")
        raise

def execute_solana_transaction(private_key, program_id, instruction_data):
    """Execute a transaction on Solana"""
    try:
        # Convert private key to keypair
        keypair = Keypair.from_secret_key(bytes.fromhex(private_key))
        
        # Get recent blockhash
        recent_blockhash = solana_client.get_recent_blockhash()["result"]["value"]["blockhash"]
        
        # Create transaction
        transaction = Transaction(
            fee_payer=keypair.public_key,
            recent_blockhash=recent_blockhash
        )
        
        # Add instruction (example: transfer SOL)
        transaction.add(
            transfer(
                TransferParams(
                    from_pubkey=keypair.public_key,
                    to_pubkey=PublicKey(program_id),
                    lamports=1000  # Amount in lamports (1 SOL = 1,000,000,000 lamports)
                )
            )
        )
        
        # Sign transaction
        transaction.sign(keypair)
        
        # Send transaction
        txid = solana_client.send_transaction(transaction, opts=TxOpts(skip_preflight=False))
        
        # Confirm transaction
        solana_client.confirm_transaction(txid["result"])
        return txid
    
    except Exception as e:
        print(f"Error executing Solana transaction: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # WARNING: Never hardcode private keys in production code
    neon_private_key = "your_neon_private_key_here"
    solana_private_key = "your_solana_private_key_here"
    
    # Execute Neon EVM contract
    print("Executing Neon EVM contract...")
    receipt = execute_neon_evm_contract(neon_private_key, CONTRACT_ADDRESS, CONTRACT_ABI)
    print(f"Neon EVM transaction receipt: {receipt}")
    
    # Execute Solana transaction
    print("\nExecuting Solana transaction...")
    program_id = "YourSolanaProgramIdHere"
    txid = execute_solana_transaction(solana_private_key, program_id, b"")
    print(f"Solana transaction ID: {txid}")
```
