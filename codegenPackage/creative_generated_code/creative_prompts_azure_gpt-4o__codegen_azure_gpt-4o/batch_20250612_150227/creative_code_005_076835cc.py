"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fortunecapitals.net
Prompt: Write a smart contract in Solidity to manage referral bonuses and daily returns for investment plans like those on fortunecapitals.net.
Generated: DETERMINISTIC_076835cc516c31c8
Batch ID: 20250612_150227
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
 * @title InvestmentReferralContract
 * @dev A smart contract to manage referral bonuses and daily returns for investment plans.
 */
contract InvestmentReferralContract {
    // State variables
    address public owner; // Owner of the contract
    uint256 public dailyReturnPercent; // Daily return percentage (e.g., 2% daily return)
    uint256 public referralBonusPercent; // Referral bonus percentage (e.g., 5%)

    struct Investment {
        uint256 amount;
        uint256 lastWithdrawalTime;
    }

    mapping(address => Investment) public investments; // Tracks investments of each user
    mapping(address => address) public referrals; // Stores referrer for each user
    mapping(address => uint256) public referralBonuses; // Tracks accumulated referral bonuses for each user

    // Events
    event Invest(address indexed investor, uint256 amount);
    event Withdraw(address indexed investor, uint256 amount);
    event ReferralBonusPaid(address indexed referrer, address indexed referee, uint256 bonus);

    /**
     * @dev Sets the owner and initializes percentages.
     * @param _dailyReturnPercent Daily return percentage (e.g., 2 for 2%).
     * @param _referralBonusPercent Referral bonus percentage (e.g., 5 for 5%).
     */
    constructor(uint256 _dailyReturnPercent, uint256 _referralBonusPercent) {
        require(_dailyReturnPercent > 0 && _referralBonusPercent > 0, "Percentages must be greater than 0");
        owner = msg.sender;
        dailyReturnPercent = _dailyReturnPercent;
        referralBonusPercent = _referralBonusPercent;
    }

    /**
     * @dev Invests an amount in the contract. Optionally includes a referrer address.
     * @param referrer Address of the referrer (can be zero address if no referrer).
     */
    function invest(address referrer) external payable {
        require(msg.value > 0, "Investment amount must be greater than 0");

        // Update investment details for the investor
        investments[msg.sender].amount += msg.value;
        investments[msg.sender].lastWithdrawalTime = block.timestamp;

        // Handle referral bonuses if referrer is valid
        if (referrer != address(0) && referrer != msg.sender && referrals[msg.sender] == address(0)) {
            referrals[msg.sender] = referrer;
            uint256 referralBonus = (msg.value * referralBonusPercent) / 100;
            referralBonuses[referrer] += referralBonus;

            emit ReferralBonusPaid(referrer, msg.sender, referralBonus);
        }

        emit Invest(msg.sender, msg.value);
    }

    /**
     * @dev Withdraws the accumulated daily returns for the investor.
     */
    function withdraw() external {
        Investment storage userInvestment = investments[msg.sender];
        require(userInvestment.amount > 0, "No active investment found");

        // Calculate the daily returns since last withdrawal
        uint256 timeElapsed = block.timestamp - userInvestment.lastWithdrawalTime;
        uint256 returns = (userInvestment.amount * dailyReturnPercent * timeElapsed) / (100 * 1 days);

        require(returns > 0, "No returns available to withdraw");

        // Update last withdrawal time
        userInvestment.lastWithdrawalTime = block.timestamp;

        // Transfer returns to the investor
        payable(msg.sender).transfer(returns);

        emit Withdraw(msg.sender, returns);
    }

    /**
     * @dev Allows the owner to withdraw the contract's balance.
     */
    function ownerWithdraw(uint256 amount) external {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(amount <= address(this).balance, "Insufficient contract balance");

        payable(owner).transfer(amount);
    }

    /**
     * @dev Gets the contract's balance.
     * @return The balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
