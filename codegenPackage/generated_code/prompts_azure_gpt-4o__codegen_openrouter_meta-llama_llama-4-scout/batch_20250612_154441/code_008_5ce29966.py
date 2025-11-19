"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Write a smart contract that integrates a reward system for NFT holders based on their category (e.g., Alien, Golden Alien), inspired by Clone Force™.
Generated: DETERMINISTIC_5ce29966d6d084e6
Batch ID: 20250612_154441
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title CloneForceRewardSystem
 * @author [Your Name]
 * @notice A smart contract that integrates a reward system for NFT holders based on their category.
 */
contract CloneForceRewardSystem is Ownable {
    // Mapping of NFT categories to their respective reward amounts
    mapping(string => uint256) public rewards;

    // Mapping of NFT holders to their category and reward balance
    mapping(address => mapping(string => uint256)) public holderRewards;

    // Mapping of NFTs to their respective categories
    mapping(uint256 => string) public nftCategories;

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed holder, string category, uint256 amount);

    // Event emitted when an NFT is added to the system
    event NftAdded(uint256 tokenId, string category);

    // Event emitted when a reward is updated
    event RewardUpdated(string category, uint256 newRewardAmount);

    /**
     * @dev Initializes the contract with default reward amounts for each category.
     */
    constructor() public {
        // Initialize reward amounts for each category
        rewards["Alien"] = 100;
        rewards["Golden Alien"] = 500;
    }

    /**
     * @dev Adds an NFT to the system with its respective category.
     * @param tokenId The ID of the NFT.
     * @param category The category of the NFT (e.g., Alien, Golden Alien).
     */
    function addNft(uint256 tokenId, string memory category) public onlyOwner {
        require(bytes(category).length > 0, "Category cannot be empty");
        nftCategories[tokenId] = category;
        emit NftAdded(tokenId, category);
    }

    /**
     * @dev Updates the reward amount for a specific category.
     * @param category The category to update the reward for.
     * @param newRewardAmount The new reward amount for the category.
     */
    function updateReward(string memory category, uint256 newRewardAmount) public onlyOwner {
        require(newRewardAmount > 0, "Reward amount must be greater than 0");
        rewards[category] = newRewardAmount;
        emit RewardUpdated(category, newRewardAmount);
    }

    /**
     * @dev Claims a reward for an NFT holder based on their category.
     * @param tokenId The ID of the NFT.
     */
    function claimReward(uint256 tokenId) public {
        require(nftCategories[tokenId].length > 0, "NFT not found in the system");
        string memory category = nftCategories[tokenId];
        uint256 rewardAmount = rewards[category];
        require(rewardAmount > 0, "No reward available for this category");
        require(holderRewards[msg.sender][category] == 0, "Reward already claimed for this NFT");

        // Transfer reward to the holder
        payable(msg.sender).transfer(rewardAmount);

        // Update holder's reward balance
        holderRewards[msg.sender][category] = rewardAmount;

        emit RewardClaimed(msg.sender, category, rewardAmount);
    }

    /**
     * @dev Gets the reward balance for an NFT holder and category.
     * @param holder The address of the NFT holder.
     * @param category The category to get the reward balance for.
     * @return The reward balance for the holder and category.
     */
    function getRewardBalance(address holder, string memory category) public view returns (uint256) {
        return holderRewards[holder][category];
    }
}
```
