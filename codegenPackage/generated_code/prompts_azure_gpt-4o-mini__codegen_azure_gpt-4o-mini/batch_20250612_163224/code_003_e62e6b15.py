"""
Generated Code Metadata:
========================
Original URL: https://tayloud.io
Prompt: Generate a Solidity smart contract that implements the fee split mechanism described on the Loud platform, allocating 4% to the system and distributing rewards to contributors.
Generated: DETERMINISTIC_e62e6b1521621fa8
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FeeSplit {
    // State variables
    address public owner;
    uint256 public totalFeesCollected;
    uint256 public constant SYSTEM_FEE_PERCENTAGE = 4; // 4% fee for the system
    mapping(address => uint256) public contributorRewards;

    // Events
    event FeesCollected(uint256 amount);
    event RewardsDistributed(address contributor, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to collect fees
    function collectFees() external payable {
        require(msg.value > 0, "Must send some ether");

        // Calculate system fee
        uint256 systemFee = (msg.value * SYSTEM_FEE_PERCENTAGE) / 100;
        uint256 contributorShare = msg.value - systemFee;

        // Update total fees collected
        totalFeesCollected += msg.value;

        // Emit event for fees collected
        emit FeesCollected(msg.value);

        // Distribute rewards to contributors
        distributeRewards(contributorShare);
    }

    // Internal function to distribute rewards to contributors
    function distributeRewards(uint256 amount) internal {
        // For simplicity, we assume a single contributor for this example
        // In a real-world scenario, you would have a more complex distribution logic
        address contributor = msg.sender; // Assuming the sender is the contributor
        contributorRewards[contributor] += amount;

        // Emit event for rewards distributed
        emit RewardsDistributed(contributor, amount);
    }

    // Function to withdraw rewards for a contributor
    function withdrawRewards() external {
        uint256 rewardAmount = contributorRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to withdraw");

        // Reset the contributor's reward balance
        contributorRewards[msg.sender] = 0;

        // Transfer the reward amount to the contributor
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed");

        // Emit event for withdrawal
        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Function to withdraw system fees by the owner
    function withdrawSystemFees() external onlyOwner {
        uint256 systemBalance = address(this).balance;
        require(systemBalance > 0, "No funds to withdraw");

        // Transfer the system balance to the owner
        (bool success, ) = owner.call{value: systemBalance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to accept ether
    receive() external payable {
        collectFees();
    }
}
```
