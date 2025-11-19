"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spacex-airdrop-1f381.web.app
Prompt: Generate a smart contract for a token airdrop mechanism similar to the one described on the SpaceX DAO website, including features for daily, weekly, and monthly rewards for token holders.
Generated: DETERMINISTIC_add47448df6fb932
Batch ID: 20250612_135637
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

/**
 * @title AirdropMechanism
 * @dev This contract implements an airdrop mechanism for distributing rewards to token holders
 */
contract AirdropMechanism is Ownable {
    // Token to be distributed
    IERC20 public token;

    // Mapping of user addresses to their last reward claim times
    mapping(address => uint256) public lastClaimed;

    // Reward intervals
    uint256 public dailyRewardInterval = 1 days;
    uint256 public weeklyRewardInterval = 7 days;
    uint256 public monthlyRewardInterval = 30 days;

    // Total rewards for different intervals
    uint256 public dailyRewardAmount;
    uint256 public weeklyRewardAmount;
    uint256 public monthlyRewardAmount;

    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token and reward amounts
     * @param _token Address of the ERC20 token
     * @param _dailyReward Amount of daily reward
     * @param _weeklyReward Amount of weekly reward
     * @param _monthlyReward Amount of monthly reward
     */
    constructor(
        address _token,
        uint256 _dailyReward,
        uint256 _weeklyReward,
        uint256 _monthlyReward
    ) {
        token = IERC20(_token);
        dailyRewardAmount = _dailyReward;
        weeklyRewardAmount = _weeklyReward;
        monthlyRewardAmount = _monthlyReward;
    }

    /**
     * @dev Allows users to claim their rewards based on the time elapsed since their last claim
     */
    function claimRewards() external {
        uint256 currentTime = block.timestamp;
        uint256 lastClaim = lastClaimed[msg.sender];
        uint256 rewardAmount = 0;

        // Daily rewards
        if (currentTime >= lastClaim + dailyRewardInterval) {
            rewardAmount += dailyRewardAmount;
        }

        // Weekly rewards
        if (currentTime >= lastClaim + weeklyRewardInterval) {
            rewardAmount += weeklyRewardAmount;
        }

        // Monthly rewards
        if (currentTime >= lastClaim + monthlyRewardInterval) {
            rewardAmount += monthlyRewardAmount;
        }

        require(rewardAmount > 0, "No rewards available to claim");

        // Update last claimed time
        lastClaimed[msg.sender] = currentTime;

        // Transfer tokens to the user
        require(token.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");
        token.transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows the contract owner to withdraw tokens from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance");
        token.transfer(owner(), _amount);
    }

    /**
     * @dev Update reward amounts (only callable by owner)
     * @param _dailyReward New daily reward amount
     * @param _weeklyReward New weekly reward amount
     * @param _monthlyReward New monthly reward amount
     */
    function updateRewards(
        uint256 _dailyReward,
        uint256 _weeklyReward,
        uint256 _monthlyReward
    ) external onlyOwner {
        dailyRewardAmount = _dailyReward;
        weeklyRewardAmount = _weeklyReward;
        monthlyRewardAmount = _monthlyReward;
    }
}
```
