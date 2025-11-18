"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: Write a Solidity contract that generates NFTs with 170+ traits and varying rarity, similar to the algorithmic generation process described for Robotos on the Robots NFT Minting website.
Generated: DETERMINISTIC_72dd87c33d4fe582
Batch ID: 20250612_153606
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract TraitNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent traits and their rarity
    struct Trait {
        string name;
        uint8 rarity; // Rarity percentage (0-100)
    }

    // Mapping from tokenId to its traits
    mapping(uint256 => Trait[]) private _tokenTraits;

    // Example traits pool (replace with 170+ traits)
    Trait[] public traitsPool;

    // Events
    event NFTMinted(uint256 indexed tokenId, Trait[] traits);

    // Constructor to initialize the NFT contract
    constructor() ERC721("TraitNFT", "TNFT") {
        // Initialize the traits pool (Example)
        traitsPool.push(Trait("Red Hat", 10));
        traitsPool.push(Trait("Blue Hat", 20));
        // Add more traits as needed...
    }

    // Function to mint a new NFT with random traits
    function mintNFT() external onlyOwner {
        uint256 newTokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Generate random traits for the NFT
        Trait[] memory generatedTraits = _generateRandomTraits();

        // Assign the traits to the new token
        _tokenTraits[newTokenId] = generatedTraits;

        // Mint the NFT
        _mint(msg.sender, newTokenId);

        // Emit an event with the minted NFT's details
        emit NFTMinted(newTokenId, generatedTraits);
    }

    // Function to generate random traits based on rarity
    function _generateRandomTraits() internal view returns (Trait[] memory) {
        // Example of random trait generation logic
        Trait[] memory randomTraits = new Trait[](3); // Limit to 3 traits for simplicity
        for (uint8 i = 0; i < randomTraits.length; i++) {
            // Simple random selection based on rarity (Replace with better randomness)
            uint256 randomIndex = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender, i))) % traitsPool.length;
            randomTraits[i] = traitsPool[randomIndex];
        }
        return randomTraits;
    }

    // Function to view traits of a tokenId
    function getTokenTraits(uint256 tokenId) external view returns (Trait[] memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenTraits[tokenId];
    }

    // Function to get the total supply of NFTs
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to withdraw contract balance to owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
