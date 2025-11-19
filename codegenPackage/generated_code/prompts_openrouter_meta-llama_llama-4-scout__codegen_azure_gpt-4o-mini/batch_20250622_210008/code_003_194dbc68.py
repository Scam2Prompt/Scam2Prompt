"""
Generated Code Metadata:
========================
Original URL: https://molly-a5h.pages.dev
Prompt: Design a simple smart contract using Solidity to create and manage NFTs on the Molly platform, including functions for minting and transferring NFTs.
Generated: DETERMINISTIC_194dbc68f16be6c1
Batch ID: 20250622_210008
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

// Importing the ERC721 interface and the Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for managing NFTs on the Molly platform
contract MollyNFT is ERC721, Ownable {
    // Counter for tracking the token IDs
    uint256 private _tokenIdCounter;

    // Mapping from token ID to the token's metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("MollyNFT", "MNFT") {
        _tokenIdCounter = 1; // Start token IDs from 1
    }

    // Function to mint a new NFT
    // @param to The address that will own the minted NFT
    // @param tokenURI The metadata URI for the NFT
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Invalid address: cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "Invalid token URI: cannot be empty");

        uint256 tokenId = _tokenIdCounter; // Get the current token ID
        _mint(to, tokenId); // Mint the NFT
        _setTokenURI(tokenId, tokenURI); // Set the token URI

        emit NFTMinted(to, tokenId, tokenURI); // Emit the NFTMinted event

        _tokenIdCounter++; // Increment the token ID counter for the next mint
    }

    // Function to transfer an NFT from one address to another
    // @param from The current owner of the NFT
    // @param to The new owner of the NFT
    // @param tokenId The ID of the NFT to transfer
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Invalid address: cannot transfer to the zero address");

        _transfer(from, to, tokenId); // Transfer the NFT
    }

    // Internal function to set the token URI
    // @param tokenId The ID of the NFT
    // @param tokenURI The metadata URI for the NFT
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI; // Store the token URI
    }

    // Function to retrieve the token URI for a given token ID
    // @param tokenId The ID of the NFT
    // @return The metadata URI of the NFT
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _tokenURIs[tokenId]; // Return the token URI
    }
}
```
