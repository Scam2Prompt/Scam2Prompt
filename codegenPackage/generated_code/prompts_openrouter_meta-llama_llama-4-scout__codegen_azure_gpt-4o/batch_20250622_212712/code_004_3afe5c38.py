"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Create a smart contract using Solidity to incentivize individuals to contribute their health data to a decentralized healthcare platform, promoting universal health coverage and basic income principles.
Generated: DETERMINISTIC_3afe5c38f71ed209
Batch ID: 20250622_212712
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

/**
 * @title HealthDataIncentive
 * @dev A smart contract to incentivize individuals to contribute their health data
 *      to a decentralized healthcare platform, promoting universal health coverage
 *      and basic income principles.
 */
contract HealthDataIncentive {
    // Owner of the contract
    address public owner;

    // Mapping to store contributors' health data hashes
    mapping(address => string) public healthData;

    // Mapping to store contributors' rewards
    mapping(address => uint256) public rewards;

    // Event emitted when health data is submitted
    event HealthDataSubmitted(address indexed contributor, string dataHash);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed contributor, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Submit health data to the platform.
     * @param dataHash The hash of the health data being submitted.
     */
    function submitHealthData(string memory dataHash) external {
        require(bytes(dataHash).length > 0, "Data hash cannot be empty");

        // Store the health data hash
        healthData[msg.sender] = dataHash;

        // Assign a reward to the contributor
        rewards[msg.sender] += 10; // Example reward amount

        // Emit an event for health data submission
        emit HealthDataSubmitted(msg.sender, dataHash);
    }

    /**
     * @dev Claim rewards for contributing health data.
     */
    function claimReward() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available to claim");

        // Reset the reward balance
        rewards[msg.sender] = 0;

        // Transfer the reward to the contributor
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");

        // Emit an event for reward claim
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Fund the contract to ensure rewards can be distributed.
     */
    function fundContract() external payable onlyOwner {
        require(msg.value > 0, "Funding amount must be greater than zero");
    }

    /**
     * @dev Get the balance of the contract.
     * @return The contract's balance in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Withdraw funds from the contract (only owner).
     * @param amount The amount to withdraw in wei.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Fallback function for other calls
    fallback() external payable {}
}
```
