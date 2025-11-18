"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npcs.pages.dev
Prompt: Implement a feature in a dApp that allows users to mint their custom NPC PFPs on the Base network, ensuring uniqueness and compliance with the ERC11 standard.
Generated: DETERMINISTIC_725efa2de83aa601
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the necessary OpenZeppelin contracts for ERC721
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NPCPFP
 * @dev Contract for minting unique NPC Profile Pictures (PFPs) on the Base network.
 */
contract NPCPFP is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of minted tokens
    Counters.Counter private _tokenIdCounter;

    // Mapping to ensure uniqueness of each NFT based on a unique identifier
    mapping(uint256 => bool) private _existingIdentifiers;

    // Event emitted when a new NPC PFP is minted
    event NPCMinted(uint256 indexed tokenId, address owner);

    // Base URI for the metadata of the NFTs
    string private _baseTokenURI;

    /**
     * @dev Constructor to initialize the NFT contract
     * @param name Name of the NFT collection
     * @param symbol Symbol of the NFT collection
     * @param baseTokenURI Base URI for the metadata
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to mint a new NPC PFP
     * @param uniqueIdentifier A unique identifier for the NPC PFP
     */
    function mintNPCPFP(uint256 uniqueIdentifier) external {
        // Check if the unique identifier has already been used
        require(!_existingIdentifiers[uniqueIdentifier], "Unique identifier already exists.");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new token to the caller's address
        _safeMint(msg.sender, tokenId);

        // Store the unique identifier to ensure uniqueness
        _existingIdentifiers[uniqueIdentifier] = true;

        // Emit the minting event
        emit NPCMinted(tokenId, msg.sender);
    }

    /**
     * @dev Function to set the base token URI
     * @param baseTokenURI New base URI for the metadata
     */
    function setBaseTokenURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function that returns the base URI for the NFT metadata
     * @return The base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
    
    /**
     * @dev Function to retrieve the total number of minted tokens
     * @return The total supply of NFTs minted
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
