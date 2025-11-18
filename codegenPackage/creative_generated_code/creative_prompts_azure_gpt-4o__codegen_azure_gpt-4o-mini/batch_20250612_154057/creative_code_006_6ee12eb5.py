"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwstayloud.io
Prompt: Provide code to integrate Meteora's fee split mechanism into a decentralized application (dApp) for managing Loud rewards.
Generated: DETERMINISTIC_6ee12eb5b32c5d4d
Batch ID: 20250612_154057
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
 * @title LoudRewards
 * @dev A dApp for managing Loud rewards with Meteora's fee split mechanism.
 */
contract LoudRewards {
    address public owner; // Owner of the contract
    address payable public meteoraFeeRecipient; // Address to receive the fee
    uint256 public feePercentage; // Fee percentage for splitting rewards

    event RewardDistributed(address indexed user, uint256 amount, uint256 fee);
    event FeeRecipientUpdated(address indexed newRecipient);
    event FeePercentageUpdated(uint256 newPercentage);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _feeRecipient Address to receive the fee.
     * @param _feePercentage Percentage of fee to split.
     */
    constructor(address payable _feeRecipient, uint256 _feePercentage) {
        require(_feeRecipient != address(0), "Invalid fee recipient address");
        require(_feePercentage <= 100, "Fee percentage must be 0-100");

        owner = msg.sender;
        meteoraFeeRecipient = _feeRecipient;
        feePercentage = _feePercentage;
    }

    /**
     * @dev Function to distribute rewards to a user.
     * @param user Address of the user to receive the reward.
     * @param amount Total amount of reward to distribute.
     */
    function distributeReward(address payable user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Calculate fee and net amount
        uint256 fee = (amount * feePercentage) / 100;
        uint256 netReward = amount - fee;

        // Transfer fee to Meteora's fee recipient
        (bool feeSent, ) = meteoraFeeRecipient.call{value: fee}("");
        require(feeSent, "Failed to send fee");

        // Transfer the net reward to the user
        (bool rewardSent, ) = user.call{value: netReward}("");
        require(rewardSent, "Failed to send reward");

        emit RewardDistributed(user, netReward, fee);
    }

    /**
     * @dev Function to update the fee recipient address.
     * @param newRecipient New fee recipient address.
     */
    function updateFeeRecipient(address payable newRecipient) external onlyOwner {
        require(newRecipient != address(0), "Invalid fee recipient address");
        meteoraFeeRecipient = newRecipient;
        emit FeeRecipientUpdated(newRecipient);
    }

    /**
     * @dev Function to update the fee percentage.
     * @param newPercentage New fee percentage to set.
     */
    function updateFeePercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "Fee percentage must be 0-100");
        feePercentage = newPercentage;
        emit FeePercentageUpdated(newPercentage);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}
}
```
