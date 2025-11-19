"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: How can I implement a rewards system for an ETH-based application that supports EVM wallets, similar to the one described on de-agent.com?
Generated: DETERMINISTIC_e2e202ab4e6bf13a
Batch ID: 20250612_155153
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
 * @title RewardsSystem
 * @dev A contract for implementing a reward system that supports EVM-compatible wallets.
 * Users can earn and claim rewards based on their participation or activities.
 */
contract RewardsSystem {
    // Mapping to store rewards for each user (address).
    mapping(address => uint256) private rewards;

    // Owner of the contract (administrator).
    address private owner;

    // Events for logging important actions.
    event RewardAdded(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add rewards to a user's account.
     * @param _user Address of the user.
     * @param _amount Amount of rewards to add.
     */
    function addReward(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Reward amount must be greater than zero");

        rewards[_user] += _amount;
        emit RewardAdded(_user, _amount);
    }

    /**
     * @dev Function to view the reward balance of a user.
     * @param _user Address of the user.
     * @return Reward balance of the user.
     */
    function viewRewards(address _user) external view returns (uint256) {
        require(_user != address(0), "Invalid user address");
        return rewards[_user];
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimRewards() external {
        uint256 userRewards = rewards[msg.sender];
        require(userRewards > 0, "No rewards to claim");

        rewards[msg.sender] = 0; // Reset rewards to zero after claiming.

        // Transfer rewards to the user. 
        // Assuming rewards are distributed in ETH (native currency).
        (bool sent, ) = msg.sender.call{value: userRewards}("");
        require(sent, "Failed to send rewards");

        emit RewardClaimed(msg.sender, userRewards);
    }

    /**
     * @dev Fallback function to accept ETH deposits into the contract.
     * This is needed to hold ETH for rewards distribution.
     */
    receive() external payable {}

    /**
     * @dev Function for the owner to withdraw any remaining contract balance.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        (bool sent, ) = owner.call{value: contractBalance}("");
        require(sent, "Failed to withdraw balance");
    }
}
```
