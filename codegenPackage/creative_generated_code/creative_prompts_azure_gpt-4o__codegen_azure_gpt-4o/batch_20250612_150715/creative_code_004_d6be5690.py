"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Generate a smart contract that enables Farcaster channels to issue programmatic rewards for followers who engage with specific content, using Moxie Reward functionality.
Generated: DETERMINISTIC_d6be56909411643a
Batch ID: 20250612_150715
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
 * @title FarcasterChannelReward
 * @dev Smart contract to issue programmatic rewards for followers engaging with specific content.
 * Utilizes Moxie Reward functionality for reward distribution.
 */
contract FarcasterChannelReward {
    // Owner of the contract (usually the Farcaster channel creator)
    address public owner;

    // Mapping to store engagement and reward details for specific content
    mapping(bytes32 => ContentReward) public contentRewards;

    // Struct to represent content and reward details
    struct ContentReward {
        uint256 rewardAmount; // Amount of reward for engagement
        bool active; // Whether the reward distribution is active
        mapping(address => bool) rewardedFollowers; // Tracks which followers already received rewards
    }

    // Event emitted when a reward is issued
    event RewardIssued(address follower, bytes32 contentHash, uint256 rewardAmount);

    // Event emitted when a new content reward is configured
    event ContentRewardConfigured(bytes32 contentHash, uint256 rewardAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check if the content reward is active
    modifier isActiveReward(bytes32 contentHash) {
        require(contentRewards[contentHash].active, "Reward is not active for this content");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Configure a reward for specific content.
     * @param contentHash Unique hash of the content (e.g., keccak256(content)).
     * @param rewardAmount Amount of reward to issue for engagement.
     */
    function configureReward(bytes32 contentHash, uint256 rewardAmount) external onlyOwner {
        ContentReward storage reward = contentRewards[contentHash];
        reward.rewardAmount = rewardAmount;
        reward.active = true;

        emit ContentRewardConfigured(contentHash, rewardAmount);
    }

    /**
     * @dev Disable reward distribution for specific content.
     * @param contentHash Unique hash of the content.
     */
    function disableReward(bytes32 contentHash) external onlyOwner {
        contentRewards[contentHash].active = false;
    }

    /**
     * @dev Issue a reward to a follower who engages with specific content.
     * @param contentHash Unique hash of the content.
     * @param follower Address of the follower to receive the reward.
     */
    function issueReward(bytes32 contentHash, address follower) external isActiveReward(contentHash) {
        ContentReward storage reward = contentRewards[contentHash];

        // Ensure the follower has not already received the reward
        require(!reward.rewardedFollowers[follower], "Follower has already been rewarded");

        // Ensure the contract has enough balance to issue the reward
        require(address(this).balance >= reward.rewardAmount, "Insufficient contract balance");

        // Mark the follower as rewarded
        reward.rewardedFollowers[follower] = true;

        // Transfer the reward to the follower
        payable(follower).transfer(reward.rewardAmount);

        emit RewardIssued(follower, contentHash, reward.rewardAmount);
    }

    /**
     * @dev Deposit Ether into the contract to fund rewards.
     */
    function depositFunds() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    /**
     * @dev Withdraw Ether from the contract (only owner can withdraw).
     * @param amount Amount to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {}

    /**
     * @dev Function to retrieve contract balance.
     * @return Contract balance in Wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
