"""
Generated Code Metadata:
========================
Original URL: https://zksync-6-1.nfts2.me
Prompt: What are the steps to create a smart contract that manages referral fees for NFT mints on ZKsync, ensuring users can claim their rewards?
Generated: DETERMINISTIC_6d91c7a567f7111d
Batch ID: 20250612_162744
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
 * @title ReferralFeeManager
 * @dev A smart contract to manage referral fees for NFT mints on ZKsync.
 *      Referrers can earn rewards, and users can claim their accumulated fees.
 */
contract ReferralFeeManager {
    // Events
    event ReferralRecorded(address indexed referrer, address indexed buyer, uint256 amount);
    event RewardClaimed(address indexed referrer, uint256 amount);

    // State variables
    address public owner; // Contract owner
    uint256 public referralFeePercentage; // Fee percentage for referrals
    mapping(address => uint256) public rewards; // Mapping to track rewards for referrers

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor
    constructor(uint256 _referralFeePercentage) {
        require(_referralFeePercentage > 0 && _referralFeePercentage <= 100, "Invalid referral fee percentage");
        owner = msg.sender;
        referralFeePercentage = _referralFeePercentage;
    }

    /**
     * @dev Records a referral and distributes the referral fee.
     * @param referrer The address of the referrer.
     * @param buyer The address of the buyer.
     * @param mintPrice The price of the NFT mint.
     */
    function recordReferral(address referrer, address buyer, uint256 mintPrice) external payable {
        require(referrer != address(0), "Referrer address cannot be zero");
        require(buyer != address(0), "Buyer address cannot be zero");
        require(mintPrice > 0, "Mint price must be greater than zero");
        require(msg.value == mintPrice, "Incorrect payment amount");

        // Calculate referral fee
        uint256 referralFee = (mintPrice * referralFeePercentage) / 100;

        // Update rewards for the referrer
        rewards[referrer] += referralFee;

        // Emit event
        emit ReferralRecorded(referrer, buyer, referralFee);

        // Transfer remaining funds to the owner
        uint256 remainingFunds = mintPrice - referralFee;
        (bool success, ) = owner.call{value: remainingFunds}("");
        require(success, "Transfer to owner failed");
    }

    /**
     * @dev Allows referrers to claim their accumulated rewards.
     */
    function claimReward() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Reset the reward balance
        rewards[msg.sender] = 0;

        // Transfer the reward to the referrer
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");

        // Emit event
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Updates the referral fee percentage. Only callable by the owner.
     * @param _newPercentage The new referral fee percentage.
     */
    function updateReferralFeePercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage > 0 && _newPercentage <= 100, "Invalid referral fee percentage");
        referralFeePercentage = _newPercentage;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraws all funds from the contract. Only callable by the owner.
     */
    function withdrawAll() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
