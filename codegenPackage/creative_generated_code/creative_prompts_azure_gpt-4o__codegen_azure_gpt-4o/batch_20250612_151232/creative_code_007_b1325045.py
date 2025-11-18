"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kuratedao.xyz
Prompt: Explain how to use DBDAO to give data ownership to contributors by minting NFTs for their data entries.
Generated: DETERMINISTIC_b13250458a382d25
Batch ID: 20250612_151232
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from web3 import Web3
from solcx import compile_source
import json
import os
import sqlite3

# Connect to Ethereum node (update with proper RPC endpoint)
ETH_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))

# Check connection to Ethereum node
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum node.")

# Contract source code for minting NFTs (simplified example)
CONTRACT_SOURCE_CODE = """
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DataOwnershipNFT is ERC721, Ownable {
    uint256 private _currentTokenId;

    struct DataEntry {
        string metadata;
        address contributor;
    }

    mapping(uint256 => DataEntry) public dataEntries;

    constructor() ERC721("DataOwnershipNFT", "DONFT") {}

    function mintDataOwnershipNFT(address contributor, string memory metadata) public onlyOwner returns (uint256) {
        _currentTokenId++;
        uint256 newTokenId = _currentTokenId;

        _mint(contributor, newTokenId);
        dataEntries[newTokenId] = DataEntry(metadata, contributor);

        return newTokenId;
    }

    function getDataEntry(uint256 tokenId) public view returns (string memory, address) {
        require(_exists(tokenId), "NFT does not exist.");
        DataEntry memory entry = dataEntries[tokenId];
        return (entry.metadata, entry.contributor);
    }
}
"""

# Compile the contract
def compile_contract(source_code):
    compiled_sol = compile_source(source_code)
    contract_id, contract_interface = compiled_sol.popitem()
    return contract_interface

contract_interface = compile_contract(CONTRACT_SOURCE_CODE)

# Deploy the contract
def deploy_contract(web3, contract_interface, deployer_private_key):
    deployer_account = web3.eth.account.privateKeyToAccount(deployer_private_key)
    contract = web3.eth.contract(abi=contract_interface["abi"], bytecode=contract_interface["bin"])

    # Build transaction
    transaction = contract.constructor().buildTransaction({
        'from': deployer_account.address,
        'nonce': web3.eth.getTransactionCount(deployer_account.address),
        'gas': 2000000,
        'gasPrice': web3.toWei('20', 'gwei')
    })

    # Sign and send transaction
    signed_txn = web3.eth.account.sign_transaction(transaction, deployer_private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    # Wait for transaction receipt
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return web3.eth.contract(address=receipt.contractAddress, abi=contract_interface["abi"])

# Initialize SQLite database to store data entries
DB_FILE = "data_entries.db"
if not os.path.exists(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE data_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        metadata TEXT NOT NULL,
        contributor_address TEXT NOT NULL,
        nft_token_id INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Interact with the contract
def mint_data_ownership_nft(contract, contributor_address, metadata, private_key):
    # Build transaction
    transaction = contract.functions.mintDataOwnershipNFT(contributor_address, metadata).buildTransaction({
        'from': web3.eth.account.privateKeyToAccount(private_key).address,
        'nonce': web3.eth.getTransactionCount(web3.eth.account.privateKeyToAccount(private_key).address),
        'gas': 2000000,
        'gasPrice': web3.toWei('20', 'gwei')
    })

    # Sign and send transaction
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    # Wait for transaction receipt
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    # Fetch the minted token ID (simplified logic, assuming event data exists)
    logs = contract.events.Transfer().processReceipt(receipt)
    token_id = logs[0]["args"]["tokenId"]

    # Store the data entry in the SQLite database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data_entries (metadata, contributor_address, nft_token_id) VALUES (?, ?, ?)", 
                   (metadata, contributor_address, token_id))
    conn.commit()
    conn.close()

    return token_id

# Example usage
if __name__ == '__main__':
    # Replace with appropriate private key for deployment
    DEPLOYER_PRIVATE_KEY = "YOUR_PRIVATE_KEY"

    # Deploy the contract
    nft_contract = deploy_contract(web3, contract_interface, DEPLOYER_PRIVATE_KEY)
    print(f"Contract deployed at address: {nft_contract.address}")

    # Mint NFT for a data contributor (replace with real contributor address and private key)
    CONTRIBUTOR_PRIVATE_KEY = "CONTRIBUTOR_PRIVATE_KEY"
    CONTRIBUTOR_ADDRESS = web3.eth.account.privateKeyToAccount(CONTRIBUTOR_PRIVATE_KEY).address
    METADATA = "Contributor's data entry metadata"

    token_id = mint_data_ownership_nft(nft_contract, CONTRIBUTOR_ADDRESS, METADATA, DEPLOYER_PRIVATE_KEY)
    print(f"NFT minted with token ID: {token_id}")
```
