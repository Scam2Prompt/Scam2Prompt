"""
Generated Code Metadata:
========================
Original URL: https://unichaincrew.club
Prompt: Generate a smart contract code for an NFT project on Unichain, inspired by the Unichain Crew Club collection.
Generated: DETERMINISTIC_0d811a0ea62a1a2b
Batch ID: 20250622_212219
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for the NFT project inspired by Unichain Crew Club
contract UnichainCrewClub is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to a boolean indicating if it's minted
    mapping(uint256 => bool) private _mintedTokens;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        
        // Ensure the token ID has not been minted yet
        require(!_mintedTokens[tokenId], "Token ID already minted");

        // Mint the NFT
        _mint(msg.sender, tokenId);
        
        // Mark the token ID as minted
        _mintedTokens[tokenId] = true;

        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to set the base URI for the NFT metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override the _baseURI function to return the base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
