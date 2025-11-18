"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.alphadogs.run
Prompt: Write a Solidity contract that tracks race results and distributes rewards to Alphadogs NFT owners based on performance.
Generated: DETERMINISTIC_3253c86dbcb1f256
Batch ID: 20250612_151403
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RaceResults
 * @dev A contract to track race results and distribute rewards to Alphadogs NFT owners based on performance
 */
contract RaceResults is Ownable {
    // Structure to hold race result information
    struct Race {
        uint256 id;
        uint256[] performanceScores; // Array of performance scores for each participant
        uint256 totalReward;          // Total reward to distribute
        bool distributed;             // Flag to check if rewards have been distributed
    }

    // Mapping to store race results by race ID
    mapping(uint256 => Race) public races;

    // Reference to the Alphadogs NFT contract
    IERC721 public alphadogsNFT;

    // Event emitted when a race is recorded
    event RaceRecorded(uint256 indexed raceId, uint256[] performanceScores, uint256 totalReward);
    
    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 indexed raceId);

    // Constructor to set the address of the Alphadogs NFT contract
    constructor(address _alphadogsNFT) {
        require(_alphadogsNFT != address(0), "Invalid NFT address");
        alphadogsNFT = IERC721(_alphadogsNFT);
    }

    /**
     * @dev Records race results and initializes rewards
     * @param raceId Unique identifier for the race
     * @param performanceScores Array of performance scores for participants
     * @param totalReward Total reward amount to distribute
     */
    function recordRace(uint256 raceId, uint256[] calldata performanceScores, uint256 totalReward) external onlyOwner {
        require(performanceScores.length > 0, "No performance scores provided");
        require(totalReward > 0, "Total reward must be greater than zero");
        
        races[raceId] = Race({
            id: raceId,
            performanceScores: performanceScores,
            totalReward: totalReward,
            distributed: false
        });
        
        emit RaceRecorded(raceId, performanceScores, totalReward);
    }

    /**
     * @dev Distributes rewards to NFT owners based on performance
     * @param raceId Unique identifier for the race
     */
    function distributeRewards(uint256 raceId) external onlyOwner {
        Race storage race = races[raceId];
        require(!race.distributed, "Rewards already distributed");
        
        uint256 totalScores = 0;
        for (uint256 i = 0; i < race.performanceScores.length; i++) {
            totalScores += race.performanceScores[i];
        }
        
        require(totalScores > 0, "Total scores must be greater than zero");
        
        for (uint256 i = 0; i < race.performanceScores.length; i++) {
            uint256 score = race.performanceScores[i];
            address owner = alphadogsNFT.ownerOf(i); // Assuming NFT IDs correspond to performanceScores index
            
            uint256 reward = (score * race.totalReward) / totalScores;
            payable(owner).transfer(reward);
        }

        race.distributed = true;
        emit RewardsDistributed(raceId);
    }

    /**
     * @dev Allows the contract to receive Ether
     */
    receive() external payable {}
    
    /**
     * @dev Allows the owner to withdraw any Ether from the contract
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
