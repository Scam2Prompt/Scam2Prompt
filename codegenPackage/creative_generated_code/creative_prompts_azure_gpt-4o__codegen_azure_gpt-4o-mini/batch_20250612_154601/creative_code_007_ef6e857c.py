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

contract AstragoldbitxInvestment {
    // Struct to hold investment details
    struct Investment {
        uint256 amount;        // Amount invested
        uint256 startTime;     // Time when investment was made
        uint256 dailyReturn;   // Daily return amount
        address referrer;      // Referral address
        uint256 referralBonus; // Referral bonus earned
    }

    // Mapping of investors' addresses to their investments
    mapping(address => Investment) public investments;

    // Total amount of deposits in the contract
    uint256 public totalDeposits;

    // Referral bonus percentage
    uint256 public referralBonusPercentage = 10; // 10% of the investment

    // Event to emit when a new investment is made
    event InvestmentMade(address indexed investor, uint256 amount, address indexed referrer);

    // Modifier to check for valid investments
    modifier validInvestment() {
        require(msg.value > 0, "Investment must be greater than 0");
        _;
    }

    // Function to make an investment
    function invest(address _referrer) external payable validInvestment {
        // Calculate daily return (1% of investment)
        uint256 dailyReturn = (msg.value * 1) / 100;
        
        // Create an investment record
        investments[msg.sender] = Investment({
            amount: msg.value,
            startTime: block.timestamp,
            dailyReturn: dailyReturn,
            referrer: _referrer,
            referralBonus: 0
        });

        // Update total deposits
        totalDeposits += msg.value;

        // Calculate and assign referral bonus if referrer is not zero address
        if (_referrer != address(0) && _referrer != msg.sender) {
            uint256 referralBonus = (msg.value * referralBonusPercentage) / 100;
            investments[_referrer].referralBonus += referralBonus;
        }

        // Emit investment event
        emit InvestmentMade(msg.sender, msg.value, _referrer);
    }

    // Function to calculate the daily returns for an investor
    function calculateReturns(address _investor) public view returns (uint256) {
        Investment memory investment = investments[_investor];
        uint256 daysInvested = (block.timestamp - investment.startTime) / 1 days;
        return investment.dailyReturn * daysInvested;
    }

    // Function to withdraw returns
    function withdrawReturns() external {
        Investment storage investment = investments[msg.sender];
        uint256 returns = calculateReturns(msg.sender);

        require(returns > 0, "No returns to withdraw");

        // Reset the investment start time to the current time
        investment.startTime = block.timestamp;

        // Transfer returns to the investor
        payable(msg.sender).transfer(returns);
    }

    // Function to withdraw referral bonuses
    function withdrawReferralBonus() external {
        Investment storage investment = investments[msg.sender];
        uint256 bonus = investment.referralBonus;

        require(bonus > 0, "No referral bonus to withdraw");

        // Reset the referral bonus
        investment.referralBonus = 0;

        // Transfer the bonus to the invetor
        payable(msg.sender).transfer(bonus);
    }

    // Fallback function for receiving ether
    receive() external payable {
        // Accept ether sent to the contract
    }

    // Function to get the investment details of an investor
    function getInvestmentDetails(address _investor) external view returns (uint256 amount, uint256 startTime, uint256 dailyReturn, address referrer, uint256 referralBonus) {
        Investment memory investment = investments[_investor];
        return (investment.amount, investment.startTime, investment.dailyReturn, investment.referrer, investment.referralBonus);
    }
}
```
