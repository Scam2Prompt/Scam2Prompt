"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://j-node.net
Prompt: Develop a smart contract to reward trusted validators for their contributions to blockchain security, inspired by J•Node's mission.
Generated: DETERMINISTIC_d112198d81554365
Batch ID: 20250612_153954
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
 * @title ValidatorRewardSystem
 * @dev A smart contract to reward trusted validators for their contributions to blockchain security.
 */
contract ValidatorRewardSystem {
    // Owner of the contract
    address public owner;

    // Mapping to store validator addresses and their respective balances
    mapping(address => uint256) public validatorBalances;

    // Event emitted when a validator is rewarded
    event ValidatorRewarded(address indexed validator, uint256 rewardAmount);

    // Event emitted when the contract owner withdraws funds
    event OwnerWithdrawal(address indexed owner, uint256 withdrawalAmount);

    // Modifier to restrict access to contract owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Sets the deployer as the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to reward a trusted validator.
     * @param validator The address of the validator to be rewarded.
     * @param rewardAmount The amount of reward to be sent to the validator.
     */
    function rewardValidator(address validator, uint256 rewardAmount) external onlyOwner {
        require(validator != address(0), "Invalid validator address");
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        require(address(this).balance >= rewardAmount, "Insufficient contract balance");

        // Update the validator's balance
        validatorBalances[validator] += rewardAmount;

        // Transfer the reward to the validator
        (bool success, ) = validator.call{value: rewardAmount}("");
        require(success, "Transfer to validator failed");

        // Emit the event
        emit ValidatorRewarded(validator, rewardAmount);
    }

    /**
     * @dev Allows the owner to withdraw funds from the contract.
     * @param amount The amount to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Transfer the funds to the owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Transfer to owner failed");

        // Emit the event
        emit OwnerWithdrawal(owner, amount);
    }

    /**
     * @dev Receives Ether into the contract.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle unexpected calls.
     */
    fallback() external payable {}
}
```
