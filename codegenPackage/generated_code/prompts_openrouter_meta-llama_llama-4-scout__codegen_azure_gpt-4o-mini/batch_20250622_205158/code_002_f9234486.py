"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: "Design a smart contract using Solidity that interacts with the Rangers Protocol's NFT protocol, allowing users to create, transfer, and manage NFTs on the platform, and provide a detailed explanation of the contract's functionality."
Generated: DETERMINISTIC_f923448669e1bc61
Batch ID: 20250622_205158
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

// Importing the ERC721 interface for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// RangersNFT is a smart contract that allows users to create, transfer, and manage NFTs
contract RangersNFT is ERC721, ERC721Burnable, Ownable {
    // Mapping from token ID to the token's metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Counter for tracking the next token ID
    uint256 private _nextTokenId;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string tokenURI, address indexed owner);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("RangersNFT", "RNGNFT") {
        _nextTokenId = 1; // Start token IDs from 1
    }

    // Function to create a new NFT
    function createNFT(string memory tokenURI) external onlyOwner {
        uint256 tokenId = _nextTokenId; // Get the current token ID
        _mint(msg.sender, tokenId); // Mint the NFT to the contract owner
        _setTokenURI(tokenId, tokenURI); // Set the token's metadata URI
        emit NFTCreated(tokenId, tokenURI, msg.sender); // Emit the NFT creation event
        _nextTokenId++; // Increment the token ID for the next NFT
    }

    // Function to set the token URI for a specific token ID
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist"); // Ensure the token exists
        _tokenURIs[tokenId] = tokenURI; // Set the token URI
    }

    // Function to retrieve the token URI for a specific token ID
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist"); // Ensure the token exists
        return _tokenURIs[tokenId]; // Return the token URI
    }

    // Function to transfer an NFT from one address to another
    function transferNFT(address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved"); // Check ownership
        _transfer(msg.sender, to, tokenId); // Transfer the NFT
    }

    // Function to burn an NFT, removing it from circulation
    function burnNFT(uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved"); // Check ownership
        _burn(tokenId); // Burn the NFT
    }

    // Function to get the total number of NFTs created
    function totalSupply() external view returns (uint256) {
        return _nextTokenId - 1; // Return the total number of NFTs created
    }
}
```
