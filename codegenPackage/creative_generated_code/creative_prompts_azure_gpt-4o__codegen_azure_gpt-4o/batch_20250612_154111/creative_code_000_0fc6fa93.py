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

/**
 * @title InvestmentPlatform
 * @dev A smart contract for an investment platform with referral commissions, daily profit bonuses, and hold bonuses.
 */
contract InvestmentPlatform {
    // State variables
    address public owner; // Contract owner
    uint256 public dailyProfitRate = 3; // Daily profit rate (3%)
    uint256 public holdBonusCap = 1; // Maximum hold bonus (1%)
    uint256 public referralCommissionRate = 5; // Referral commission rate (5%)

    struct User {
        uint256 investedAmount; // Amount invested by the user
        uint256 lastClaimTime; // Last time the user claimed their profit
        uint256 holdBonus; // Accumulated hold bonus capped at holdBonusCap
    }

    mapping(address => User) public users; // Tracking user data
    mapping(address => address) public referrals; // Referral relationships

    // Events
    event Invest(address indexed investor, uint256 amount);
    event Claim(address indexed investor, uint256 profit);
    event ReferralReward(address indexed referrer, address indexed referee, uint256 reward);

    constructor() {
        owner = msg.sender; // Set contract owner
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Invest function to deposit funds into the platform.
     * @param referrer The address of the referrer (if applicable).
     */
    function invest(address referrer) external payable {
        require(msg.value > 0, "Investment amount must be greater than 0");

        // Update user data
        User storage user = users[msg.sender];
        user.investedAmount += msg.value;

        // Handle referrals
        if (referrals[msg.sender] == address(0) && referrer != msg.sender && referrer != address(0)) {
            referrals[msg.sender] = referrer;
            uint256 referralReward = (msg.value * referralCommissionRate) / 100;
            payable(referrer).transfer(referralReward);
            emit ReferralReward(referrer, msg.sender, referralReward);
        }

        emit Invest(msg.sender, msg.value);
    }

    /**
     * @dev Claim function to withdraw daily profits and hold bonuses.
     */
    function claim() external {
        User storage user = users[msg.sender];
        require(user.investedAmount > 0, "No investment found");

        // Calculate daily profit
        uint256 timeElapsed = block.timestamp - user.lastClaimTime;
        uint256 dailyProfit = (user.investedAmount * dailyProfitRate * timeElapsed) / (100 * 1 days);

        // Calculate hold bonus (capped)
        uint256 holdBonus = user.holdBonus;
        if (holdBonus > holdBonusCap) {
            holdBonus = holdBonusCap;
        }

        // Total profit
        uint256 totalProfit = dailyProfit + ((user.investedAmount * holdBonus) / 100);
        require(totalProfit > 0, "No profit available to claim");

        // Update user claim time and reset hold bonus
        user.lastClaimTime = block.timestamp;
        user.holdBonus = 0;

        // Transfer profit to the user
        payable(msg.sender).transfer(totalProfit);
        emit Claim(msg.sender, totalProfit);
    }

    /**
     * @dev Function to update the hold bonus for a user.
     * This is called periodically to accumulate bonuses.
     */
    function updateHoldBonus(address userAddress) external onlyOwner {
        User storage user = users[userAddress];
        require(user.investedAmount > 0, "User has no investment");

        uint256 timeElapsed = block.timestamp - user.lastClaimTime;
        user.holdBonus += (timeElapsed * holdBonusCap) / (100 * 1 days);
    }

    /**
     * @dev Fallback function to accept Ether deposits.
     */
    receive() external payable {
        revert("Use the invest() function to deposit funds.");
    }

    /**
     * @dev Function to withdraw funds from the contract (Only owner).
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance in contract");
        payable(owner).transfer(amount);
    }
}
```
