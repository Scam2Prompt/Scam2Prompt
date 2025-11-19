"""
Generated Code Metadata:
========================
Original URL: https://thoreumdashboard.com
Prompt: Write a Solidity contract for a rewards distribution system that pays holders in top cryptocurrencies (e.g., BNB, BTCB, ETH) based on a percentage of ecosystem revenue, similar to Thoreum Bank.
Generated: DETERMINISTIC_ff0b2ebf87f48522
Batch ID: 20250612_152658
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Rewards Distribution System Contract
 * @author [Your Name]
 * @notice This contract distributes rewards to holders in top cryptocurrencies
 * based on a percentage of ecosystem revenue.
 */
contract RewardsDistributionSystem is Ownable {
    using SafeMath for uint256;

    // Mapping of reward tokens (e.g., BNB, BTCB, ETH)
    mapping(address => bool) public rewardTokens;

    // Mapping of user balances
    mapping(address => uint256) public userBalances;

    // Total ecosystem revenue
    uint256 public totalRevenue;

    // Percentage of revenue to distribute as rewards
    uint256 public rewardPercentage;

    // Mapping of user reward claims
    mapping(address => mapping(address => uint256)) public userRewardClaims;

    /**
     * @dev Constructor
     * @param _rewardPercentage Percentage of revenue to distribute as rewards
     */
    constructor(uint256 _rewardPercentage) {
        rewardPercentage = _rewardPercentage;
    }

    /**
     * @dev Add a reward token
     * @param _token Address of the reward token
     */
    function addRewardToken(address _token) public onlyOwner {
        rewardTokens[_token] = true;
    }

    /**
     * @dev Remove a reward token
     * @param _token Address of the reward token
     */
    function removeRewardToken(address _token) public onlyOwner {
        rewardTokens[_token] = false;
    }

    /**
     * @dev Update user balance
     * @param _user Address of the user
     * @param _balance New balance of the user
     */
    function updateUserBalance(address _user, uint256 _balance) public onlyOwner {
        userBalances[_user] = _balance;
    }

    /**
     * @dev Update total ecosystem revenue
     * @param _revenue New total ecosystem revenue
     */
    function updateTotalRevenue(uint256 _revenue) public onlyOwner {
        totalRevenue = _revenue;
    }

    /**
     * @dev Update reward percentage
     * @param _percentage New reward percentage
     */
    function updateRewardPercentage(uint256 _percentage) public onlyOwner {
        rewardPercentage = _percentage;
    }

    /**
     * @dev Claim rewards for a user
     * @param _user Address of the user
     * @param _rewardToken Address of the reward token
     * @return Reward amount
     */
    function claimRewards(address _user, address _rewardToken) public returns (uint256) {
        require(rewardTokens[_rewardToken], "Invalid reward token");

        uint256 userBalance = userBalances[_user];
        uint256 rewardAmount = calculateRewardAmount(userBalance);

        userRewardClaims[_user][_rewardToken] = userRewardClaims[_user][_rewardToken].add(rewardAmount);

        // Transfer reward to user
        IERC20(_rewardToken).transfer(_user, rewardAmount);

        return rewardAmount;
    }

    /**
     * @dev Calculate reward amount for a user
     * @param _userBalance Balance of the user
     * @return Reward amount
     */
    function calculateRewardAmount(uint256 _userBalance) internal view returns (uint256) {
        uint256 totalUserBalances = getTotalUserBalances();
        uint256 rewardPool = totalRevenue.mul(rewardPercentage) / 100;

        return rewardPool.mul(_userBalance) / totalUserBalances;
    }

    /**
     * @dev Get total user balances
     * @return Total user balances
     */
    function getTotalUserBalances() internal view returns (uint256) {
        uint256 totalBalances = 0;

        for (address user in userBalances) {
            totalBalances = totalBalances.add(userBalances[user]);
        }

        return totalBalances;
    }

    /**
     * @dev Get reward claim for a user and reward token
     * @param _user Address of the user
     * @param _rewardToken Address of the reward token
     * @return Reward claim amount
     */
    function getRewardClaim(address _user, address _rewardToken) public view returns (uint256) {
        return userRewardClaims[_user][_rewardToken];
    }
}
```
