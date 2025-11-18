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

/// @title Reward Distribution Contract for Gamified FREE SPIN Feature
/// @author Your Name
/// @notice This contract manages reward distribution for users participating in the FREE SPIN feature.
/// @dev The contract ensures that rewards are fairly distributed and tracks user participation.

contract FreeSpinReward {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalRewards; // Total rewards pool for distribution
    mapping(address => uint256) public rewards; // Mapping of user addresses to their reward balances
    mapping(address => uint256) public spins; // Mapping of user addresses to their spin counts

    // Events
    event RewardDistributed(address indexed user, uint256 amount);
    event SpinPerformed(address indexed user, uint256 spinCount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function");
        _;
    }

    // Constructor to initialize the contract with the owner's address
    constructor() {
        owner = msg.sender;
    }

    // Function to set the total rewards pool
    function setTotalRewards(uint256 _totalRewards) external onlyOwner {
        totalRewards = _totalRewards;
    }

    // Function to perform a spin
    function performSpin() external {
        require(totalRewards > 0, "No rewards available for distribution");
        
        // Increment user's spin count
        spins[msg.sender] += 1;

        // Simple reward calculation (for demonstration purposes)
        uint256 rewardAmount = totalRewards / 100; // Reward is 1% of total rewards per spin
        rewards[msg.sender] += rewardAmount;
        totalRewards -= rewardAmount;

        emit SpinPerformed(msg.sender, spins[msg.sender]);
        emit RewardDistributed(msg.sender, rewardAmount);
    }

    // Function to withdraw rewards
    function withdrawRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to withdraw");

        // Reset user's rewards before transfer
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        payable(msg.sender).transfer(rewardAmount);
    }

    // Function to receive Ether. This is necessary to fund the rewards pool.
    receive() external payable {
        totalRewards += msg.value;
    }

    // Function to withdraw contract balance by the owner
    function withdrawContractBalance() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Function to check user's rewards
    function checkRewards(address user) external view returns (uint256) {
        return rewards[user];
    }

    // Function to check user's spin count
    function checkSpins(address user) external view returns (uint256) {
        return spins[user];
    }

    // Fallback function to prevent accidental Ether transfers
    fallback() external {
        revert("Direct transfers not allowed");
    }
}
```
