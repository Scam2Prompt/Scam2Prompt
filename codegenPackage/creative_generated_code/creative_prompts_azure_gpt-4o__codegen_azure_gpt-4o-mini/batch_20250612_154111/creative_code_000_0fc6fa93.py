"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Write a Solidity smart contract for an investment platform similar to MinerDog, incorporating features like referral commissions, daily profit bonuses, and a hold bonus capped at 1%.
Generated: DETERMINISTIC_0fc6fa93a6a0f8fd
Batch ID: 20250612_154111
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

contract InvestmentPlatform {
    // Struct to hold user information
    struct User {
        uint256 investment;
        uint256 lastClaimed;
        address referrer;
        uint256 referralEarnings;
        uint256 holdBonus;
    }

    // Mapping to store user data
    mapping(address => User) public users;

    // Variables for the contract
    uint256 public totalInvested;
    uint256 public totalReferralCommissions;
    uint256 public dailyProfitRate = 10; // 10% daily profit
    uint256 public holdBonusCap = 100; // Max hold bonus in basis points (1%)
    uint256 public constant SECONDS_IN_A_DAY = 86400;

    // Events for logging
    event Invested(address indexed user, uint256 amount, address indexed referrer);
    event Claimed(address indexed user, uint256 amount);
    
    // Function to invest in the platform
    function invest(address _referrer) external payable {
        require(msg.value > 0, "Investment must be greater than zero");
        require(users[msg.sender].investment == 0, "Already invested");

        // Set the referrer if provided
        if (_referrer != address(0) && _referrer != msg.sender) {
            users[msg.sender].referrer = _referrer;
            users[_referrer].referralEarnings += (msg.value * 5) / 100; // 5% referral commission
            totalReferralCommissions += (msg.value * 5) / 100;
        }

        // Update user's investment and total investment
        users[msg.sender].investment = msg.value;
        totalInvested += msg.value;
        users[msg.sender].lastClaimed = block.timestamp;

        emit Invested(msg.sender, msg.value, _referrer);
    }

    // Function to claim profits
    function claim() external {
        User storage user = users[msg.sender];
        require(user.investment > 0, "No investment found");
        
        uint256 daysPassed = (block.timestamp - user.lastClaimed) / SECONDS_IN_A_DAY;
        require(daysPassed > 0, "Claim only once per day");

        uint256 profit = (user.investment * dailyProfitRate * daysPassed) / 100;
        uint256 holdBonus = (user.holdBonus * user.investment) / 100; // Hold bonus derived from user's investment
        if (holdBonus > (holdBonusCap * user.investment) / 10000) {
            holdBonus = (holdBonusCap * user.investment) / 10000; // Cap the hold bonus
        }

        user.lastClaimed = block.timestamp;
        uint256 totalClaim = profit + holdBonus;

        // Reset hold bonus
        user.holdBonus = 0;

        // Transfer the funds
        payable(msg.sender).transfer(totalClaim);

        emit Claimed(msg.sender, totalClaim);
    }

    // Function to update hold bonus based on days held
    function updateHoldBonus() external {
        User storage user = users[msg.sender];
        require(user.investment > 0, "No investment found");

        uint256 daysHeld = (block.timestamp - user.lastClaimed) / SECONDS_IN_A_DAY;
        user.holdBonus += daysHeld;
    }

    // Function to withdraw referral earnings
    function withdrawReferralEarnings() external {
        User storage user = users[msg.sender];
        require(user.referralEarnings > 0, "No referral earnings to withdraw");

        uint256 earnings = user.referralEarnings;
        user.referralEarnings = 0;

        // Transfer referral earnings
        payable(msg.sender).transfer(earnings);
    }

    // Fallback function to accept and reject ether sent directly to the contract
    receive() external payable {
        revert("Direct transfers not allowed; use invest function");
    }
}
```
