"""
Generated Code Metadata:
========================
Original URL: https://somnia.pages.dev
Prompt: "Develop a use case for Somnia's 300k+tps EVM Layer 1 blockchain in a gaming or NFT application, focusing on its benefits and implementation details."
Generated: DETERMINISTIC_4a77d5012e573858
Batch ID: 20250622_204726
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/nft/1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.somnia.network": {
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
"""
Use Case: NFT-based Gaming Application on Somnia's 300k+ TPS EVM Layer 1 Blockchain

This code demonstrates a simple implementation of an NFT-based gaming application
where players can mint, trade, and use NFTs as in-game assets. The high throughput
of Somnia's blockchain ensures smooth gameplay and fast transactions.
"""

from web3 import Web3
from solcx import compile_source

# Connect to Somnia's EVM-compatible blockchain
SOMNIA_RPC_URL = "https://rpc.somnia.network"  # Replace with actual RPC URL
web3 = Web3(Web3.HTTPProvider(SOMNIA_RPC_URL))

# Check connection
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Somnia blockchain.")

# Set up account (use environment variables or secure storage for private keys in production)
PRIVATE_KEY = "your_private_key_here"  # Replace with your private key
ACCOUNT = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)

# Compile the NFT smart contract
contract_source_code = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GameNFT is ERC721, Ownable {
    uint256 public nextTokenId;
    mapping(uint256 => string) private _tokenURIs;

    constructor() ERC721("GameNFT", "GNFT") {}

    function mint(address to, string memory tokenURI) external onlyOwner {
        uint256 tokenId = nextTokenId;
        nextTokenId++;
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
    }

    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        return _tokenURIs[tokenId];
    }
}
"""

compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:GameNFT']

# Deploy the contract
GameNFT = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
nonce = web3.eth.getTransactionCount(ACCOUNT.address)

transaction = GameNFT.constructor().buildTransaction({
    'chainId': web3.eth.chain_id,
    'gas': 3000000,
    'gasPrice': web3.toWei('10', 'gwei'),
    'nonce': nonce
})

signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Get deployed contract address
contract_address = tx_receipt.contractAddress
print(f"Contract deployed at address: {contract_address}")

# Interact with the contract
game_nft = web3.eth.contract(address=contract_address, abi=contract_interface['abi'])

# Mint an NFT
def mint_nft(to_address, token_uri):
    """
    Mint a new NFT for the given address with the specified token URI.
    """
    nonce = web3.eth.getTransactionCount(ACCOUNT.address)
    transaction = game_nft.functions.mint(to_address, token_uri).buildTransaction({
        'chainId': web3.eth.chain_id,
        'gas': 3000000,
        'gasPrice': web3.toWei('10', 'gwei'),
        'nonce': nonce
    })

    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"NFT minted successfully. Transaction hash: {tx_hash.hex()}")

# Example usage
PLAYER_ADDRESS = "0xPlayerAddressHere"  # Replace with actual player address
TOKEN_URI = "https://example.com/nft/1"  # Replace with actual metadata URI

try:
    mint_nft(PLAYER_ADDRESS, TOKEN_URI)
except Exception as e:
    print(f"Error minting NFT: {e}")
```
