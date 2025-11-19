"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Write a smart contract using the Moxie Protocol to programmatically reward Farcaster members for specific on-chain actions, ensuring payouts are split according to the protocol's predefined percentages.
Generated: DETERMINISTIC_6454ef7bc6c6cf7a
Batch ID: 20250612_150715
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

// Importing the Moxie Protocol interface
import "@moxieprotocol/contracts/interfaces/IMoxie.sol";

contract FarcasterReward {
    // Moxie Protocol interface instance
    IMoxie public moxie;

    // Event to log rewards distribution
    event RewardsDistributed(address indexed member, uint256 amount);

    // Mapping to track rewards for each member
    mapping(address => uint256) public rewards;

    // Predefined percentages for reward distribution
    uint256 public constant REWARD_PERCENTAGE = 70; // 70% to the member
    uint256 public constant PLATFORM_FEE = 30; // 30% to the platform

    // Constructor to initialize the Moxie Protocol instance
    constructor(address _moxieAddress) {
        require(_moxieAddress != address(0), "Invalid Moxie address");
        moxie = IMoxie(_moxieAddress);
    }

    // Function to reward members for specific on-chain actions
    function rewardMember(address member, uint256 totalReward) external {
        require(member != address(0), "Invalid member address");
        require(totalReward > 0, "Reward must be greater than zero");

        // Calculate the rewards based on predefined percentages
        uint256 memberReward = (totalReward * REWARD_PERCENTAGE) / 100;
        uint256 platformReward = (totalReward * PLATFORM_FEE) / 100;

        // Update the rewards mapping
        rewards[member] += memberReward;

        // Transfer the platform fee to the Moxie Protocol
        moxie.transfer(platformReward);

        // Emit an event for the rewards distribution
        emit RewardsDistributed(member, memberReward);
    }

    // Function to withdraw rewards by the member
    function withdrawRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to withdraw");

        // Reset the member's reward balance before transferring
        rewards[msg.sender] = 0;

        // Transfer the rewards to the member
        payable(msg.sender).transfer(rewardAmount);
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Function to check the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
