"""
Generated Code Metadata:
========================
Original URL: https://j-node.net
Prompt: Develop a smart contract to reward trusted validators for their contributions to blockchain security, inspired by J•Node's mission.
Generated: DETERMINISTIC_d112198d81554365
Batch ID: 20250612_153954
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

/// @title Validator Reward Smart Contract
/// @author Your Name
/// @notice This contract rewards trusted validators for their contributions to blockchain security
/// @dev This contract implements a simple reward mechanism for validators

contract ValidatorReward {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public rewards; // Mapping of validator addresses to their rewards
    mapping(address => bool) public trustedValidators; // Mapping of trusted validators
    uint256 public totalRewards; // Total rewards distributed

    // Events
    event ValidatorAdded(address indexed validator);
    event ValidatorRemoved(address indexed validator);
    event RewardDistributed(address indexed validator, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier onlyTrustedValidator() {
        require(trustedValidators[msg.sender], "Not a trusted validator");
        _;
    }

    /// @notice Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Add a trusted validator
    /// @param validator The address of the validator to add
    function addTrustedValidator(address validator) external onlyOwner {
        require(validator != address(0), "Invalid address");
        require(!trustedValidators[validator], "Validator already trusted");

        trustedValidators[validator] = true;
        emit ValidatorAdded(validator);
    }

    /// @notice Remove a trusted validator
    /// @param validator The address of the validator to remove
    function removeTrustedValidator(address validator) external onlyOwner {
        require(trustedValidators[validator], "Validator not found");

        trustedValidators[validator] = false;
        emit ValidatorRemoved(validator);
    }

    /// @notice Distribute rewards to trusted validators
    /// @param validator The address of the validator to reward
    /// @param amount The amount of reward to distribute
    function distributeReward(address validator, uint256 amount) external onlyOwner {
        require(trustedValidators[validator], "Validator not trusted");
        require(amount > 0, "Reward amount must be greater than zero");

        rewards[validator] += amount;
        totalRewards += amount;

        emit RewardDistributed(validator, amount);
    }

    /// @notice Withdraw rewards for the caller
    function withdrawRewards() external onlyTrustedValidator {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to withdraw");

        // Reset the reward before transferring to prevent re-entrancy attacks
        rewards[msg.sender] = 0;

        // Transfer the reward to the validator
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Transfer failed");
    }

    /// @notice Fallback function to receive Ether
    receive() external payable {}

    /// @notice Get the reward balance of a validator
    /// @param validator The address of the validator
    /// @return The reward balance of the validator
    function getRewardBalance(address validator) external view returns (uint256) {
        return rewards[validator];
    }
}
```
