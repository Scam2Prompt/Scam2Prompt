"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-io-dashborad.pages.dev
Prompt: Design a basic smart contract in Solidity for distributing staking rewards to DOGE20 token holders over a period of two years, utilizing Ethereum's smart contract capabilities.
Generated: DETERMINISTIC_333ff13b0c1bca3a
Batch ID: 20250622_210914
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DOGE20 Staking Rewards Contract
 * @author [Your Name]
 * @notice Distributes staking rewards to DOGE20 token holders over a period of two years.
 */
contract DOGE20StakingRewards is ReentrancyGuard {
    using SafeMath for uint256;

    // Token contract instance
    ERC20 public token;

    // Reward token instance
    ERC20 public rewardToken;

    // Total reward amount
    uint256 public totalRewards;

    // Reward duration in seconds (2 years)
    uint256 public rewardDuration;

    // Reward start time
    uint256 public rewardStartTime;

    // Reward end time
    uint256 public rewardEndTime;

    // User staking balance
    mapping(address => uint256) public stakingBalances;

    // User reward debt
    mapping(address => uint256) public rewardDebts;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _token DOGE20 token contract address
     * @param _rewardToken Reward token contract address
     * @param _totalRewards Total reward amount
     */
    constructor(
        address _token,
        address _rewardToken,
        uint256 _totalRewards
    ) public {
        require(_token != address(0), "Token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_totalRewards > 0, "Total rewards must be greater than zero");

        token = ERC20(_token);
        rewardToken = ERC20(_rewardToken);
        totalRewards = _totalRewards;
        rewardDuration = 2 years;
        rewardStartTime = block.timestamp;
        rewardEndTime = rewardStartTime.add(rewardDuration);
    }

    /**
     * @notice Stake DOGE20 tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        token.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake DOGE20 tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Get user staking balance
     * @param _user User address
     * @return User staking balance
     */
    function getStakingBalance(address _user) external view returns (uint256) {
        return stakingBalances[_user];
    }

    /**
     * @notice Get user reward debt
     * @param _user User address
     * @return User reward debt
     */
    function getRewardDebt(address _user) external view returns (uint256) {
        return rewardDebts[_user];
    }

    /**
     * @notice Distribute rewards to users
     */
    function distributeRewards() external {
        require(block.timestamp >= rewardStartTime && block.timestamp <= rewardEndTime, "Rewards are not available yet");

        uint256 rewardPerBlock = totalRewards.div(rewardDuration);
        uint256 userReward = stakingBalances[msg.sender].mul(rewardPerBlock).sub(rewardDebts[msg.sender]);

        if (userReward > 0) {
            rewardDebts[msg.sender] = rewardDebts[msg.sender].add(userReward);
            rewardToken.transfer(msg.sender, userReward);

            emit RewardsDistributed(msg.sender, userReward);
        }
    }

    /**
     * @notice Get reward rate
     * @return Reward rate
     */
    function getRewardRate() external view returns (uint256) {
        return totalRewards.div(rewardDuration);
    }
}
```
