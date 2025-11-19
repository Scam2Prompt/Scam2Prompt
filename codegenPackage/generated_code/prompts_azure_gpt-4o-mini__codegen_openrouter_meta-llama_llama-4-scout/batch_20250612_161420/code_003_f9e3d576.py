"""
Generated Code Metadata:
========================
Original URL: https://presale-scorpion-casino.web.app
Prompt: Develop a Solidity smart contract that implements a staking mechanism for $SCORP tokens, allowing users to earn daily passive income based on their holdings.
Generated: DETERMINISTIC_f9e3d57662753b56
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ScorpStakingContract
 * @author [Your Name]
 * @notice A staking contract for $SCORP tokens, allowing users to earn daily passive income.
 */
contract ScorpStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public userBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public userRewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // $SCORP token contract
    IERC20 public scorpToken;

    // Daily reward rate (1e18 = 100%, 1e16 = 1%)
    uint256 public dailyRewardRate;

    // Last reward timestamp
    uint256 public lastRewardTimestamp;

    // Reward per share
    uint256 public rewardPerShare;

    // Reward per share accumulated
    uint256 public accRewardPerShare;

    /**
     * @notice Constructor
     * @param _scorpToken $SCORP token contract address
     * @param _dailyRewardRate Daily reward rate (1e18 = 100%, 1e16 = 1%)
     */
    constructor(address _scorpToken, uint256 _dailyRewardRate) public {
        scorpToken = IERC20(_scorpToken);
        dailyRewardRate = _dailyRewardRate;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @notice Stake $SCORP tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Transfer tokens from user to contract
        scorpToken.transferFrom(msg.sender, address(this), _amount);

        // Update user balance and reward debt
        userBalances[msg.sender] = userBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        // Update reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Unstake $SCORP tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(userBalances[msg.sender] >= _amount, "Insufficient balance");

        // Update user balance and reward debt
        userBalances[msg.sender] = userBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer tokens from contract to user
        scorpToken.transfer(msg.sender, _amount);

        // Update reward debt
        updateRewardDebt(msg.sender);
    }

    /**
     * @notice Update reward debt for a user
     * @param _user User address
     */
    function updateRewardDebt(address _user) internal {
        // Calculate reward
        uint256 reward = getReward();

        // Update reward per share
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(totalStakingBalance));

        // Update user reward debt
        userRewardDebt[_user] = userBalances[_user].mul(accRewardPerShare).div(1e18);
    }

    /**
     * @notice Get current reward
     * @return Reward amount
     */
    function getReward() public view returns (uint256) {
        // Calculate elapsed time
        uint256 elapsedTime = block.timestamp.sub(lastRewardTimestamp);

        // Calculate reward
        uint256 reward = totalStakingBalance.mul(dailyRewardRate).mul(elapsedTime).div(1e18).div(86400);

        // Update last reward timestamp
        return reward;
    }

    /**
     * @notice Get user reward
     * @param _user User address
     * @return Reward amount
     */
    function getUserReward(address _user) public view returns (uint256) {
        // Calculate user reward
        uint256 userReward = userBalances[_user].mul(accRewardPerShare).div(1e18).sub(userRewardDebt[_user]);

        return userReward;
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external nonReentrant {
        // Calculate user reward
        uint256 userReward = getUserReward(msg.sender);

        // Update user reward debt
        userRewardDebt[msg.sender] = userBalances[msg.sender].mul(accRewardPerShare).div(1e18);

        // Transfer reward to user
        scorpToken.transfer(msg.sender, userReward);
    }
}
```
