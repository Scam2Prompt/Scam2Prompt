"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miner-pepebnb2.vercel.app
Prompt: Generate a smart contract for an investment platform based on the Binance Smart Chain that includes features like referral bonuses and anti-whale controls.
Generated: DETERMINISTIC_df5e1e999e2de91f
Batch ID: 20250612_161420
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// InvestmentPlatform contract allows users to invest and earn rewards through referrals
contract InvestmentPlatform is Ownable {
    using SafeMath for uint256;

    // Token used for investments
    IERC20 public investmentToken;

    // Referral structure to store referral information
    struct Referral {
        address referrer;
        uint256 rewards;
    }

    // Mapping of user addresses to their referral information
    mapping(address => Referral) public referrals;

    // Mapping to track total investments by address
    mapping(address => uint256) public investments;

    // Maximum investment allowed to prevent whale manipulation
    uint256 public constant MAX_INVESTMENT = 1000 * 10**18; // Example value, adjust accordingly

    // Event emitted when a user invests
    event Invested(address indexed investor, uint256 amount, address indexed referrer);

    // Constructor to initialize the contract with the investment token address
    constructor(IERC20 _investmentToken) {
        investmentToken = _investmentToken;
    }

    // Function to invest in the platform
    function invest(uint256 amount, address referrer) external {
        require(amount > 0, "Investment amount must be greater than 0");
        require(amount <= MAX_INVESTMENT, "Investment exceeds maximum limit");

        // Transfer investment tokens from the user to the contract
        investmentToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's total investments
        investments[msg.sender] = investments[msg.sender].add(amount);

        // Implement referral system
        if (referrer != address(0) && referrer != msg.sender) {
            // Update referral information
            referrals[msg.sender].referrer = referrer;
            referrals[referrer].rewards = referrals[referrer].rewards.add(amount.mul(5).div(100)); // 5% bonus for referrer
        }

        emit Invested(msg.sender, amount, referrer);
    }

    // Function for the owner to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(investmentToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        investmentToken.transfer(msg.sender, amount);
    }

    // Function to check total investments of a user
    function getInvestment(address user) external view returns (uint256) {
        return investments[user];
    }

    // Function to check referral rewards of a user
    function getReferralRewards(address user) external view returns (uint256) {
        return referrals[user].rewards;
    }

    // Function to claim referral rewards
    function claimReferralRewards() external {
        uint256 rewards = referrals[msg.sender].rewards;
        require(rewards > 0, "No rewards to claim");

        // Reset the user's referral rewards after claiming
        referrals[msg.sender].rewards = 0;

        investmentToken.transfer(msg.sender, rewards);
    }
}
```
