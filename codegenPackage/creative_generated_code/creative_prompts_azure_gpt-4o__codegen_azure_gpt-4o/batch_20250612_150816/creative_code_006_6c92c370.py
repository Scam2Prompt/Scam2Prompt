"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdgift.top
Prompt: Write a smart contract that facilitates reward distribution upon wallet connection, inspired by "Reward Portal v2."
Generated: DETERMINISTIC_6c92c3704bc49f90
Batch ID: 20250612_150816
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
 * @title RewardPortalV2
 * @dev A smart contract that facilitates reward distribution upon wallet connection.
 */
contract RewardPortalV2 {
    // Mapping to track whether a wallet has claimed the reward
    mapping(address => bool) private claimedRewards;

    // Address of the contract owner
    address public owner;

    // Reward amount
    uint256 public rewardAmount;

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict function access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardAmount The amount of reward to distribute.
     */
    constructor(uint256 _rewardAmount) {
        owner = msg.sender; // Set the contract creator as the owner
        rewardAmount = _rewardAmount; // Initialize the reward amount
    }

    /**
     * @dev Function to allow users to connect their wallet and claim rewards.
     */
    function claimReward() external {
        require(!claimedRewards[msg.sender], "Reward already claimed."); // Ensure the user hasn't claimed a reward yet
        require(address(this).balance >= rewardAmount, "Insufficient contract balance."); // Ensure contract has enough balance

        // Mark the reward as claimed
        claimedRewards[msg.sender] = true;

        // Send the reward to the user
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed."); // Handle transfer failure

        // Emit the RewardClaimed event
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function for the owner to deposit Ether into the contract.
     */
    function depositFunds() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
    }

    /**
     * @dev Function for the owner to withdraw Ether from the contract.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance.");
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
