"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Write a blockchain-based smart contract in Solidity to manage Astragoldbitx.org's investment plans, ensuring secure deposits, daily returns, and referral bonuses.
Generated: DETERMINISTIC_ef6e857c9bfc8323
Batch ID: 20250612_154601
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
 * @title Astragoldbitx Investment Contract
 * @dev Smart contract to manage investment plans with secure deposits,
 *      daily returns, and referral bonuses.
 */
contract AstragoldbitxInvestment {
    // Owner of the contract
    address public owner;

    // Investment structure
    struct Investment {
        uint256 amount;        // Amount invested
        uint256 startTime;     // Timestamp of investment
        uint256 referralBonus; // Referral bonus earned
        address referrer;      // Referrer address
    }

    // Mapping to store investments made by each user
    mapping(address => Investment) public investments;

    // Events
    event Invested(address indexed investor, uint256 amount, address indexed referrer);
    event ReferralBonusPaid(address indexed investor, uint256 bonus);
    event Withdrawal(address indexed investor, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier hasInvestment(address investor) {
        require(investments[investor].amount > 0, "No active investment");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to invest and optionally specify a referrer.
     * @param referrer Address of the referrer (optional).
     */
    function invest(address referrer) external payable {
        require(msg.value > 0, "Investment amount must be greater than zero");

        Investment storage userInvestment = investments[msg.sender];

        // If a new investment, initialize the structure
        if (userInvestment.amount == 0) {
            userInvestment.startTime = block.timestamp;
            userInvestment.referrer = referrer;
        }

        // Update investment details
        userInvestment.amount += msg.value;

        // Handle referral bonus
        if (referrer != address(0) && referrer != msg.sender) {
            uint256 referralBonus = msg.value / 10; // 10% referral bonus
            investments[referrer].referralBonus += referralBonus;
            emit ReferralBonusPaid(referrer, referralBonus);
        }

        emit Invested(msg.sender, msg.value, referrer);
    }

    /**
     * @dev Calculates daily returns for the investor based on the investment amount.
     * @param investor Address of the investor.
     * @return Returns the daily return amount.
     */
    function calculateDailyReturn(address investor) public view hasInvestment(investor) returns (uint256) {
        Investment storage userInvestment = investments[investor];
        uint256 dailyReturn = (userInvestment.amount * 5) / 100; // 5% daily return
        return dailyReturn;
    }

    /**
     * @dev Allows the investor to withdraw their returns including referral bonuses.
     */
    function withdraw() external hasInvestment(msg.sender) {
        Investment storage userInvestment = investments[msg.sender];

        // Calculate daily returns
        uint256 daysElapsed = (block.timestamp - userInvestment.startTime) / 1 days;
        uint256 totalReturn = daysElapsed * calculateDailyReturn(msg.sender);

        // Include referral bonus
        uint256 totalAmountWithdrawable = totalReturn + userInvestment.referralBonus;

        require(totalAmountWithdrawable > 0, "No returns to withdraw");

        // Reset referral bonus
        userInvestment.referralBonus = 0;

        // Transfer the funds
        payable(msg.sender).transfer(totalAmountWithdrawable);

        emit Withdrawal(msg.sender, totalAmountWithdrawable);
    }

    /**
     * @dev Allows the owner to withdraw contract balance.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Fallback function to accept ether.
     */
    receive() external payable {
        invest(address(0));
    }
}
```
