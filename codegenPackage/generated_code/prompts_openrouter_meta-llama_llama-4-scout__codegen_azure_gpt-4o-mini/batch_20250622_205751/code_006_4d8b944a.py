"""
Generated Code Metadata:
========================
Original URL: https://dao-nftt.web.app
Prompt: Develop a smart contract in Solidity (or equivalent) for creating and managing NFT collections on Solana, inspired by the features of this platform.
Generated: DETERMINISTIC_4d8b944a9abb7b19
Batch ID: 20250622_205751
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

// Importing necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for managing NFT collections
contract NFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to token metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to create a new NFT
    function createNFT(string memory tokenURI) external onlyOwner {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter and assign it to a new token
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Mint the NFT to the owner
        _mint(msg.sender, tokenId);
        
        // Set the token URI
        _setTokenURI(tokenId, tokenURI);
        
        // Emit the NFT creation event
        emit NFTCreated(tokenId, tokenURI);
    }

    // Function to set the token URI for a specific token
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to retrieve the token URI for a specific token
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    // Function to withdraw contract balance (if any)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
