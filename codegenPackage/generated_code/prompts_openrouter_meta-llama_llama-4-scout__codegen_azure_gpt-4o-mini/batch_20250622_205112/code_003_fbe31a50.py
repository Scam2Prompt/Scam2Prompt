"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Develop a use case for using LayerZero's ONFT (Omnichain Non-Fungible Token) standard for gaming applications.
Generated: DETERMINISTIC_fbe31a502de70b59
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing LayerZero's ONFT interface
import "@layerzero/ONFT.sol";

// Contract for a gaming application using LayerZero's ONFT standard
contract GameNFT is ONFT {
    // Mapping from token ID to the owner address
    mapping(uint256 => address) private _owners;

    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the ONFT contract with a name and symbol
    constructor(string memory name, string memory symbol) ONFT(name, symbol) {}

    // Function to mint a new NFT
    function mintNFT(address to, uint256 tokenId) external {
        require(to != address(0), "Invalid address: zero address");
        require(!_exists(tokenId), "Token already exists");

        // Mint the NFT
        _mint(to, tokenId);
        _owners[tokenId] = to;

        emit Minted(to, tokenId);
    }

    // Function to check if a token exists
    function _exists(uint256 tokenId) internal view returns (bool) {
        return _owners[tokenId] != address(0);
    }

    // Function to transfer an NFT to another address
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(from == _owners[tokenId], "Transfer not authorized");
        require(to != address(0), "Invalid address: zero address");

        // Transfer the NFT
        _transfer(from, to, tokenId);
        _owners[tokenId] = to;
    }

    // Function to get the owner of a specific token
    function ownerOf(uint256 tokenId) external view returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "Token does not exist");
        return owner;
    }

    // Function to handle cross-chain transfers
    function crossChainTransfer(address to, uint256 tokenId, uint16 destinationChainId) external {
        require(_owners[tokenId] == msg.sender, "Not the token owner");
        require(destinationChainId != 0, "Invalid destination chain ID");

        // Logic for cross-chain transfer using LayerZero's functionality
        // This is a placeholder for the actual implementation
        // _sendCrossChain(to, tokenId, destinationChainId);
    }

    // Function to receive tokens from other chains
    function receiveCrossChainNFT(address from, uint256 tokenId) external {
        // Logic to handle receiving NFTs from other chains
        // This is a placeholder for the actual implementation
        // _receiveCrossChain(from, tokenId);
    }
}
```
