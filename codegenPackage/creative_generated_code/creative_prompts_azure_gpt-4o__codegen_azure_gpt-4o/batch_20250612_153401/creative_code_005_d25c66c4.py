"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nextearths-ap.web.app
Prompt: Generate a Solidity contract for a tier system that rewards Next Earth users based on the number of Land NFTs they hold.
Generated: DETERMINISTIC_d25c66c468c92330
Batch ID: 20250612_153401
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

/**
 * @title TierSystem
 * @dev A contract that rewards users based on the number of Land NFTs they hold.
 * Users are assigned to tiers based on their NFT holdings, and tiers determine their rewards.
 */
contract TierSystem {
    // Owner of the contract
    address public owner;

    // Mapping to store the number of Land NFTs each user holds
    mapping(address => uint256) public userLandNFTs;

    // Tier thresholds
    uint256 public tier1Threshold = 10; // Tier 1: 10 or more NFTs
    uint256 public tier2Threshold = 5;  // Tier 2: 5-9 NFTs
    uint256 public tier3Threshold = 1;  // Tier 3: 1-4 NFTs

    // Events
    event OwnerUpdated(address indexed oldOwner, address indexed newOwner);
    event UserNFTCountUpdated(address indexed user, uint256 nftCount);
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the contract's owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to update the owner of the contract.
     * @param newOwner The address of the new owner.
     */
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnerUpdated(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to update the number of Land NFTs a user holds.
     * @param user The address of the user.
     * @param nftCount The number of Land NFTs the user holds.
     */
    function updateUserLandNFTs(address user, uint256 nftCount) external onlyOwner {
        require(user != address(0), "User address cannot be zero");
        userLandNFTs[user] = nftCount;
        emit UserNFTCountUpdated(user, nftCount);
    }

    /**
     * @dev Function to get the tier of a user based on their Land NFT holdings.
     * @param user The address of the user.
     * @return The tier of the user.
     *         Tier 1: 10 or more NFTs
     *         Tier 2: 5-9 NFTs
     *         Tier 3: 1-4 NFTs
     *         Tier 0: No NFTs
     */
    function getUserTier(address user) public view returns (uint8) {
        uint256 nftCount = userLandNFTs[user];
        if (nftCount >= tier1Threshold) {
            return 1; // Tier 1
        } else if (nftCount >= tier2Threshold) {
            return 2; // Tier 2
        } else if (nftCount >= tier3Threshold) {
            return 3; // Tier 3
        } else {
            return 0; // Tier 0
        }
    }

    /**
     * @dev Function for a user to claim rewards based on their tier.
     * Rewards can be distributed off-chain or calculated based on certain criteria.
     * For simplicity, we assume each tier has a fixed reward amount in this example.
     */
    function claimReward() external {
        uint8 tier = getUserTier(msg.sender);
        require(tier > 0, "User is not eligible for any rewards");

        uint256 rewardAmount;
        if (tier == 1) {
            rewardAmount = 100; // Example reward for Tier 1
        } else if (tier == 2) {
            rewardAmount = 50;  // Example reward for Tier 2
        } else if (tier == 3) {
            rewardAmount = 20;  // Example reward for Tier 3
        }

        // Emit an event for reward claiming. Actual reward distribution logic would depend on the implementation.
        emit RewardClaimed(msg.sender, rewardAmount);
    }
}
```
