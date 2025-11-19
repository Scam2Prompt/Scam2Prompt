"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.web.app
Prompt: Propose a smart contract upgrade to introduce a new feature for BTCETF, such as auto-compounding of staking rewards.
Generated: DETERMINISTIC_ef91804010e6f6cc
Batch ID: 20250622_205045
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCETF Auto-Compounding Staking Contract
 * @author [Your Name]
 * @notice This contract introduces auto-compounding of staking rewards for BTCETF.
 */
contract BTCETFStaking is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Staking token (BTCETF)
    IERC20 public stakingToken;

    // Reward token (same as staking token for auto-compounding)
    IERC20 public rewardToken;

    // Staking rewards per user
    mapping(address => uint256) public stakingRewards;

    // User staking balances
    mapping(address => uint256) public stakingBalances;

    // Auto-compounding interval in seconds
    uint256 public autoCompoundingInterval;

    // Timestamp of last auto-compounding
    uint256 public lastAutoCompounding;

    /**
     * @notice Constructor
     * @param _stakingToken Staking token address
     * @param _rewardToken Reward token address
     * @param _autoCompoundingInterval Auto-compounding interval in seconds
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _autoCompoundingInterval
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        autoCompoundingInterval = _autoCompoundingInterval;
        lastAutoCompounding = block.timestamp;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        stakingToken.safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Accrue staking rewards
     * @param _user User address
     */
    function accrueRewards(address _user) internal {
        uint256 stakingBalance = stakingBalances[_user];
        uint256 rewards = calculateRewards(stakingBalance);

        stakingRewards[_user] = stakingRewards[_user].add(rewards);
    }

    /**
     * @notice Calculate staking rewards
     * @param _stakingBalance Staking balance
     * @return Rewards
     */
    function calculateRewards(uint256 _stakingBalance) internal view returns (uint256) {
        // Implement your reward calculation logic here
        // For demonstration purposes, assume 10% APY
        uint256 apy = 10;
        uint256 rewards = _stakingBalance.mul(apy).div(100);
        return rewards;
    }

    /**
     * @notice Auto-compound staking rewards
     */
    function autoCompoundRewards() external onlyOwner {
        uint256 currentTimestamp = block.timestamp;
        require(currentTimestamp.sub(lastAutoCompounding) >= autoCompoundingInterval, "Auto-compounding interval not reached");

        for (address user in stakingBalances) {
            accrueRewards(user);
            uint256 rewards = stakingRewards[user];

            // Auto-compound rewards by restaking
            stakingToken.safeTransferFrom(address(rewardToken), address(this), rewards);
            stakingBalances[user] = stakingBalances[user].add(rewards);

            stakingRewards[user] = 0;
        }

        lastAutoCompounding = currentTimestamp;
    }

    /**
     * @notice Withdraw staking rewards
     */
    function withdrawRewards() external {
        accrueRewards(msg.sender);
        uint256 rewards = stakingRewards[msg.sender];

        stakingRewards[msg.sender] = 0;
        rewardToken.safeTransfer(msg.sender, rewards);
    }
}
```
