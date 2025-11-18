"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpkinspicebirds.xyz
Prompt: Write a function in Solidity to randomly assign rare traits to NFTs during minting, inspired by the rare traits mentioned in Pumpkin Spice Moonbirds.
Generated: DETERMINISTIC_e49181fbfdaed75c
Batch ID: 20250612_151550
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

/// @title NFT Rare Trait Assignment Contract
/// @dev This contract assigns random rare traits to NFTs during minting
/// @notice Ensure the contract is integrated with a secure random number source (e.g., Chainlink VRF)

contract RareTraitAssignment {
    // Structure to define traits
    struct Trait {
        string name;  // Name of the trait
        uint rarity;  // Rarity percentage (0-100)
    }

    // List of possible traits
    Trait[] public traits;

    // Mapping to store assigned traits for each tokenId
    mapping(uint256 => Trait) public tokenTraits;

    // Event emitted when a rare trait is assigned
    event RareTraitAssigned(uint256 indexed tokenId, string traitName);

    /// @notice Constructor initializes trait options
    constructor() {
        // Add traits with names and rarity percentages
        traits.push(Trait("Moon Hat", 5));       // 5% rarity
        traits.push(Trait("Pumpkin Spice Drink", 10)); // 10% rarity
        traits.push(Trait("Golden Feathers", 1));    // 1% rarity
        traits.push(Trait("Spooky Glow", 15));       // 15% rarity
    }

    /// @notice Function to mint an NFT and assign a random rare trait
    /// @param tokenId The ID of the NFT being minted
    function mintNFT(uint256 tokenId) external {
        require(tokenTraits[tokenId].rarity == 0, "Trait already assigned."); // Ensure trait isn't already assigned
        
        // Generate a random number for trait assignment
        uint256 randomNumber = _generateRandomNumber(tokenId);

        // Assign a rare trait based on the random number
        Trait memory assignedTrait = _assignTrait(randomNumber);
        tokenTraits[tokenId] = assignedTrait;

        // Emit an event for the assigned trait
        emit RareTraitAssigned(tokenId, assignedTrait.name);
    }

    /// @notice Internal function to assign a trait based on randomness
    /// @param randomNumber Random number for selecting a trait
    /// @return Trait The assigned trait
    function _assignTrait(uint256 randomNumber) internal view returns (Trait memory) {
        uint256 cumulativeRarity = 0;

        // Iterate through traits and assign one based on rarity
        for (uint256 i = 0; i < traits.length; i++) {
            cumulativeRarity += traits[i].rarity;
            if (randomNumber % 100 < cumulativeRarity) {
                return traits[i];
            }
        }

        // Default fallback (no rare trait assigned)
        return Trait("None", 0);
    }

    /// @notice Internal function to generate a pseudo-random number
    /// @param seed A value to seed the randomness
    /// @return uint256 A pseudo-random number
    function _generateRandomNumber(uint256 seed) internal view returns (uint256) {
        // Basic pseudo-random number; replace with Chainlink VRF in production
        return uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, seed)));
    }
}
```
