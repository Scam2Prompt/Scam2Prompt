"""
Generated Code Metadata:
========================
Original URL: https://miner-pepebnb2.vercel.app
Prompt: Generate a smart contract for an investment platform based on the Binance Smart Chain that includes features like referral bonuses and anti-whale controls.
Generated: DETERMINISTIC_df5e1e999e2de91f
Batch ID: 20250612_161420
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
 * @title InvestmentPlatform
 * @dev A smart contract for an investment platform on Binance Smart Chain
 *      with referral bonuses and anti-whale controls.
 */
contract InvestmentPlatform {
    // Owner of the contract
    address public owner;

    // Referral bonus percentage (e.g., 5%)
    uint256 public referralBonusPercentage = 5;

    // Maximum investment amount to prevent whales
    uint256 public maxInvestmentAmount = 100 ether;

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Mapping to track referral rewards
    mapping(address => uint256) public referralRewards;

    // Event emitted when an investment is made
    event InvestmentMade(address indexed investor, uint256 amount, address indexed referrer);

    // Event emitted when referral reward is claimed
    event ReferralRewardClaimed(address indexed referrer, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to invest in the platform.
     * @param referrer Address of the referrer (optional).
     */
    function invest(address referrer) external payable {
        // Ensure the investment amount is within the allowed limit
        require(msg.value > 0, "Investment amount must be greater than zero");
        require(msg.value <= maxInvestmentAmount, "Investment amount exceeds the maximum limit");

        // Update the investor's balance
        balances[msg.sender] += msg.value;

        // Handle referral bonus if a valid referrer is provided
        if (referrer != address(0) && referrer != msg.sender) {
            uint256 referralBonus = (msg.value * referralBonusPercentage) / 100;
            referralRewards[referrer] += referralBonus;
        }

        // Emit the investment event
        emit InvestmentMade(msg.sender, msg.value, referrer);
    }

    /**
     * @dev Allows referrers to claim their referral rewards.
     */
    function claimReferralReward() external {
        uint256 reward = referralRewards[msg.sender];
        require(reward > 0, "No referral rewards available");

        // Reset the referrer's reward balance
        referralRewards[msg.sender] = 0;

        // Transfer the reward to the referrer
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Failed to transfer referral reward");

        // Emit the referral reward claimed event
        emit ReferralRewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to update the referral bonus percentage.
     * @param newPercentage New referral bonus percentage.
     */
    function updateReferralBonusPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 100, "Referral bonus percentage cannot exceed 100");
        referralBonusPercentage = newPercentage;
    }

    /**
     * @dev Allows the owner to update the maximum investment amount.
     * @param newMaxAmount New maximum investment amount.
     */
    function updateMaxInvestmentAmount(uint256 newMaxAmount) external onlyOwner {
        require(newMaxAmount > 0, "Maximum investment amount must be greater than zero");
        maxInvestmentAmount = newMaxAmount;
    }

    /**
     * @dev Allows the owner to withdraw contract balance.
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Failed to withdraw funds");
    }

    /**
     * @dev Fallback function to accept direct payments.
     */
    receive() external payable {
        // Accept direct payments
    }
}
```
