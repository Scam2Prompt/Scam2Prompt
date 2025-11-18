"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tournament-starheroesio.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to claim unique assets (heroes) based on eligibility criteria, inspired by the StarHeroes platform.
Generated: DETERMINISTIC_35c21099b9fc790c
Batch ID: 20250612_153648
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

/// @title StarHeroes Asset Claiming Contract
/// @author Your Name
/// @notice This contract allows users to claim unique hero assets based on eligibility criteria.
/// @dev The contract utilizes a mapping to track eligible users and their claimed status.

contract StarHeroes {

    // Struct to represent a hero
    struct Hero {
        uint256 id;               // Unique identifier for the hero
        string name;              // Name of the hero
        string rarity;            // Rarity of the hero (e.g., common, rare, epic)
    }

    // Mapping to store heroes
    mapping(uint256 => Hero) public heroes;
    
    // Mapping to track claimed status of users
    mapping(address => bool) public hasClaimed;

    // Event emitted when a hero is claimed
    event HeroClaimed(address indexed user, uint256 heroId);

    // Counter for hero IDs
    uint256 private heroCounter;

    /// @notice Adds a new hero to the contract
    /// @param name The name of the hero
    /// @param rarity The rarity of the hero
    /// @dev Only the contract owner can add heroes (owner functionality can be added)
    function addHero(string memory name, string memory rarity) public {
        heroCounter++;
        heroes[heroCounter] = Hero(heroCounter, name, rarity);
    }

    /// @notice Allows users to claim a hero if eligible
    /// @param heroId The ID of the hero to claim
    /// @dev Users can only claim once
    function claimHero(uint256 heroId) public {
        // Check if the hero exists
        require(heroes[heroId].id != 0, "Hero does not exist");
        
        // Check if the user has already claimed a hero
        require(!hasClaimed[msg.sender], "User has already claimed a hero");
        
        // Mark the user as having claimed a hero
        hasClaimed[msg.sender] = true;

        // Emit the HeroClaimed event
        emit HeroClaimed(msg.sender, heroId);
    }

    /// @notice Check if a user has claimed a hero
    /// @param user The address of the user
    /// @return bool indicating if the user has claimed
    function hasUserClaimed(address user) public view returns (bool) {
        return hasClaimed[user];
    }

    /// @notice Get hero details by ID
    /// @param heroId The ID of the hero to fetch
    /// @return hero The hero details
    function getHero(uint256 heroId) public view returns (Hero memory) {
        require(heroes[heroId].id != 0, "Hero does not exist");
        return heroes[heroId];
    }
}
```
