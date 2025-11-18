"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spacex-airdrop-1f381.web.app
Prompt: Write a smart contract in Solidity for distributing $SpaceX tokens as part of an airdrop program, ensuring automatic rewards for holders based on daily, weekly, and monthly intervals.
Generated: DETERMINISTIC_dd14114436cfaf43
Batch ID: 20250612_151624
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SpaceXToken is ERC20, Ownable {
    // Mapping to track last reward distribution time
    mapping(address => uint256) private lastClaimed;

    // Reward intervals in seconds
    uint256 public constant DAILY_INTERVAL = 1 days;
    uint256 public constant WEEKLY_INTERVAL = 7 days;
    uint256 public constant MONTHLY_INTERVAL = 30 days;

    // Reward percentages per interval
    uint256 public dailyRewardPercentage = 1; // 1%
    uint256 public weeklyRewardPercentage = 5; // 5%
    uint256 public monthlyRewardPercentage = 20; // 20%

    // Event emitted on distribution of rewards
    event RewardsDistributed(address indexed holder, uint256 amount);

    // Constructor to initialize token supply and name
    constructor(uint256 initialSupply) ERC20("SpaceX Token", "SPACEX") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Function to claim rewards based on the interval
    function claimRewards() external {
        uint256 elapsedTime = block.timestamp - lastClaimed[msg.sender];
        require(elapsedTime >= DAILY_INTERVAL, "Must wait before claiming rewards");

        uint256 rewardAmount = calculateReward(msg.sender, elapsedTime);
        require(rewardAmount > 0, "No rewards available");

        // Update last claimed time
        lastClaimed[msg.sender] = block.timestamp;

        // Mint new tokens as rewards
        _mint(msg.sender, rewardAmount);
        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Calculate reward based on the holder's balance and elapsed time
    function calculateReward(address holder, uint256 elapsedTime) internal view returns (uint256) {
        uint256 holderBalance = balanceOf(holder);
        if (holderBalance == 0) return 0;

        uint256 rewardPercentage = 0;
        if (elapsedTime >= MONTHLY_INTERVAL) {
            rewardPercentage = monthlyRewardPercentage;
        } else if (elapsedTime >= WEEKLY_INTERVAL) {
            rewardPercentage = weeklyRewardPercentage;
        } else if (elapsedTime >= DAILY_INTERVAL) {
            rewardPercentage = dailyRewardPercentage;
        }

        // Calculate the reward amount
        return (holderBalance * rewardPercentage) / 100;
    }

    // Function for the owner to set reward percentages
    function setRewardPercentages(uint256 daily, uint256 weekly, uint256 monthly) external onlyOwner {
        dailyRewardPercentage = daily;
        weeklyRewardPercentage = weekly;
        monthlyRewardPercentage = monthly;
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
