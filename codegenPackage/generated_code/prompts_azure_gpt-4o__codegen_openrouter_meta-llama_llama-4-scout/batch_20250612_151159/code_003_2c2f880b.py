"""
Generated Code Metadata:
========================
Original URL: https://web-wienerdog.pages.dev
Prompt: Develop a staking mechanism in Solidity that allows users to stake WienerAI ($WAI) tokens and earn rewards with an annual percentage yield (APY) of 120%.
Generated: DETERMINISTIC_2c2f880b84437e5c
Batch ID: 20250612_151159
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

/**
 * @title WienerAI Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake WienerAI ($WAI) tokens and earn rewards with an annual percentage yield (APY) of 120%.
 */
contract WienerAIS staking is ReentrancyGuard {
    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // WienerAI token contract
    ERC20 public token;

    // Reward token contract (same as WienerAI for simplicity)
    ERC20 public rewardToken;

    // APY in basis points (120% = 12000)
    uint256 public constant APY = 12000;

    // Seconds in a year
    uint256 public constant SECONDS_IN_YEAR = 365 days;

    // Reward per second
    uint256 public rewardPerSecond;

    // Last update timestamp
    uint256 public lastUpdateTimestamp;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _token WienerAI token contract address
     * @param _rewardToken Reward token contract address (same as WienerAI for simplicity)
     */
    constructor(address _token, address _rewardToken) {
        require(_token != address(0), "Token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        token = ERC20(_token);
        rewardToken = ERC20(_rewardToken);

        // Initialize reward per second (120% APY)
        rewardPerSecond = (APY * 1e18) / (SECONDS_IN_YEAR * 10000);

        lastUpdateTimestamp = block.timestamp;
    }

    /**
     * @notice Stake WienerAI tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from user to contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking balance and reward debt
        _updateStakingBalance(msg.sender, _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake WienerAI tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update staking balance and reward debt
        _updateStakingBalance(msg.sender, -_amount);

        // Transfer tokens from contract to user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update staking balance and reward debt for a user
     * @param _user User address
     * @param _amount Amount to add or subtract from staking balance
     */
    function _updateStakingBalance(address _user, uint256 _amount) internal {
        // Calculate rewards since last update
        uint256 rewards = _calculateRewards(_user);

        // Update last update timestamp
        uint256 currentTimestamp = block.timestamp;
        uint256 timeElapsed = currentTimestamp - lastUpdateTimestamp;
        lastUpdateTimestamp = currentTimestamp;

        // Update staking balance
        if (_amount > 0) {
            stakingBalances[_user] += _amount;
            totalStakingBalance += _amount;
        } else {
            stakingBalances[_user] -= _amount;
            totalStakingBalance -= _amount;
        }

        // Update reward debt
        rewardDebt[_user] = stakingBalances[_user] * 1e18 + rewards;

        // Distribute rewards
        if (rewards > 0) {
            require(rewardToken.transfer(_user, rewards), "Reward token transfer failed");
            emit RewardsDistributed(_user, rewards);
        }
    }

    /**
     * @notice Calculate rewards for a user since last update
     * @param _user User address
     * @return Rewards in wei
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        uint256 currentTimestamp = block.timestamp;
        uint256 timeElapsed = currentTimestamp - lastUpdateTimestamp;

        // Calculate total rewards
        uint256 totalRewards = rewardPerSecond * timeElapsed * totalStakingBalance / 1e18;

        // Calculate user's share of rewards
        uint256 userRewards = totalRewards * stakingBalances[_user] / totalStakingBalance;

        return userRewards;
    }

    /**
     * @notice Get user staking balance and reward debt
     * @param _user User address
     * @return Staking balance and reward debt
     */
    function getUserInfo(address _user) external view returns (uint256, uint256) {
        return (stakingBalances[_user], rewardDebt[_user]);
    }
}
```
