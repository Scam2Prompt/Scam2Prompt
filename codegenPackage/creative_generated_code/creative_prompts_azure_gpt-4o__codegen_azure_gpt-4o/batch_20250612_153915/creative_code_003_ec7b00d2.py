"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-spin.web.app
Prompt: Create a smart contract in Solidity that handles reward distribution for a gamified system like the "FREE SPIN" feature described on the TON SPIN website.
Generated: DETERMINISTIC_ec7b00d26f0a5fb4
Batch ID: 20250612_153915
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
 * @title RewardDistribution
 * @dev A smart contract for gamified reward distribution (e.g., "FREE SPIN").
 */
contract RewardDistribution {
    // Owner of the contract
    address public owner;

    // Mapping to store balances of rewards for each user
    mapping(address => uint256) public userRewards;

    // Event for logging reward distribution
    event RewardDistributed(address indexed user, uint256 amount);

    // Event for logging reward claim
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Distribute rewards to a user.
     * @param _user Address of the user receiving the reward.
     * @param _amount Amount of reward to distribute.
     */
    function distributeReward(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Reward amount must be greater than zero");

        // Update user's reward balance
        userRewards[_user] += _amount;

        emit RewardDistributed(_user, _amount);
    }

    /**
     * @dev Allow users to claim their rewards.
     */
    function claimReward() external {
        uint256 rewardAmount = userRewards[msg.sender];
        require(rewardAmount > 0, "No rewards available to claim");

        // Reset the user's reward balance before transferring
        userRewards[msg.sender] = 0;

        // Transfer the reward to the user
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Failed to transfer reward");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Fallback function to receive Ether for reward distribution.
     */
    receive() external payable {}

    /**
     * @dev Allow the owner to withdraw excess Ether from the contract.
     * @param _amount Amount of Ether to withdraw.
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");

        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Failed to withdraw Ether");
    }

    /**
     * @dev Get the contract balance.
     * @return The Ether balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
