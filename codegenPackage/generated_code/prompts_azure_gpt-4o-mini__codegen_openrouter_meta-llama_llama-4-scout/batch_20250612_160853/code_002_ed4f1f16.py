"""
Generated Code Metadata:
========================
Original URL: https://bitcoinetf-chain.pages.dev
Prompt: Create a Solidity smart contract that implements the staking mechanism for Bitcoin ETF Token, allowing users to earn rewards based on their staked amount.
Generated: DETERMINISTIC_ed4f1f16bab762d8
Batch ID: 20250612_160853
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
 * @title Bitcoin ETF Token Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake Bitcoin ETF Tokens and earn rewards.
 */
contract BitcoinETFTokenStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking amount
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Last block number that rewards were distributed
    uint256 public lastRewardBlock;

    // Bitcoin ETF Token contract
    ERC20 public bitcoinETFToken;

    // Reward token contract
    ERC20 public rewardToken;

    /**
     * @notice Constructor
     * @param _bitcoinETFToken Bitcoin ETF Token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _bitcoinETFToken,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) public {
        bitcoinETFToken = ERC20(_bitcoinETFToken);
        rewardToken = ERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake Bitcoin ETF Tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(bitcoinETFToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        updateReward(msg.sender);
    }

    /**
     * @notice Unstake Bitcoin ETF Tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        require(bitcoinETFToken.transfer(msg.sender, _amount), "Token transfer failed");

        updateReward(msg.sender);
    }

    /**
     * @notice Update reward for user
     * @param _user User address
     */
    function updateReward(address _user) internal {
        uint256 currentBlock = block.number;
        if (currentBlock <= lastRewardBlock) {
            return;
        }

        uint256 reward = 0;
        if (totalStaked > 0) {
            reward = currentBlock.sub(lastRewardBlock).mul(rewardPerBlock);
            accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(totalStaked));
        }

        lastRewardBlock = currentBlock;

        if (_user != address(0)) {
            uint256 userReward = stakingBalances[_user].mul(accRewardPerShare).div(1e18).sub(rewardDebt[_user]);
            if (userReward > 0) {
                rewardDebt[_user] = stakingBalances[_user].mul(accRewardPerShare).div(1e18);
                require(rewardToken.transfer(_user, userReward), "Reward token transfer failed");
            }
        }
    }

    /**
     * @notice Get user staking information
     * @param _user User address
     * @return staking balance, reward debt, and pending reward
     */
    function getStakingInfo(address _user) external view returns (uint256, uint256, uint256) {
        uint256 pendingReward = stakingBalances[_user].mul(accRewardPerShare).div(1e18).sub(rewardDebt[_user]);
        return (stakingBalances[_user], rewardDebt[_user], pendingReward);
    }
}
```
