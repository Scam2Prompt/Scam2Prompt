"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notcoindropfree.shop
Prompt: Write a smart contract in Solidity to automate the distribution of TON rewards based on the outcome of a free spin.
Generated: DETERMINISTIC_050de213ab157006
Batch ID: 20250612_150658
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

contract TonRewardDistributor {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public rewards; // Rewards distribution mapping
    event RewardDistributed(address indexed user, uint256 amount); // Event for reward distribution

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender; // Set the contract creator as the owner
    }

    // Function to distribute rewards based on the outcome of a free spin
    // @param winners - Array of addresses who won
    // @param rewardAmounts - Array of amounts corresponding to each winner
    function distributeRewards(address[] calldata winners, uint256[] calldata rewardAmounts) external onlyOwner {
        require(winners.length == rewardAmounts.length, "Mismatched arrays");
        
        for (uint256 i = 0; i < winners.length; i++) {
            require(winners[i] != address(0), "Invalid address");
            require(rewardAmounts[i] > 0, "Reward must be greater than zero");
            
            rewards[winners[i]] += rewardAmounts[i]; // Accumulate rewards
            emit RewardDistributed(winners[i], rewardAmounts[i]); // Emit event for tracking
        }
    }

    // Function to claim rewards
    function claimReward() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0; // Reset reward balance for the user

        // Transfer the rewards to the user
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed");

        emit RewardDistributed(msg.sender, rewardAmount); // Emit event for claiming
    }

    // Function to receive Ether
    receive() external payable {}

    // Function to withdraw contract balance (only for the owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Function to check the contract balance (for transparency)
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
