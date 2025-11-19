"""
Generated Code Metadata:
========================
Original URL: https://npcs.pages.dev
Prompt: Implement a feature in a dApp that allows users to mint their custom NPC PFPs on the Base network, ensuring uniqueness and compliance with the ERC11 standard.
Generated: DETERMINISTIC_725efa2de83aa601
Batch ID: 20250612_151219
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

// Importing OpenZeppelin's ERC721 implementation for NFT standards
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Custom NFT contract for minting unique NPC PFPs
contract NPCPFP is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track if a token ID has been minted
    mapping(uint256 => bool) private _mintedTokens;

    // Event emitted when a new NPC PFP is minted
    event NPCMinted(address indexed owner, uint256 indexed tokenId);

    // Base URI for metadata
    string private _baseTokenURI;

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NPC PFP
    function mintNPCPFP() external {
        uint256 newTokenId = _tokenIdCounter.current();
        
        // Ensure the token ID is unique
        require(!_mintedTokens[newTokenId], "Token ID already minted");

        // Mint the NFT to the caller
        _mint(msg.sender, newTokenId);
        
        // Mark the token ID as minted
        _mintedTokens[newTokenId] = true;

        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Emit the minting event
        emit NPCMinted(msg.sender, newTokenId);
    }

    // Function to set a new base URI for metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override the baseURI function to return the custom base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to retrieve the total minted NPC PFPs
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to check if a token ID has been minted
    function isTokenMinted(uint256 tokenId) external view returns (bool) {
        return _mintedTokens[tokenId];
    }
}
```
