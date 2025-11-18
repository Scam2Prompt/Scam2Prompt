"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainlywallet.web.app
Prompt: Develop a staking pool smart contract that supports decentralized wallets, based on the staking pool functionality described on the Multichainly Wallet platform.
Generated: DETERMINISTIC_b446e273c01e2225
Batch ID: 20250612_153849
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title StakingPool
 * @dev A smart contract for a simple staking pool that allows users to stake ERC20 tokens.
 */
contract StakingPool is Ownable {
    IERC20 public stakingToken; // Token that users will stake
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastUpdateBlock; // Last block number rewards were calculated
    mapping(address => uint256) public balances; // User staking balances
    mapping(address => uint256) public rewards; // Accumulated rewards for each user

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @param _stakingToken Address of the ERC20 token to be staked
     * @param _rewardRate Rate of reward distribution
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    /**
     * @dev Modifier to update rewards before any staking or unstaking actions
     */
    modifier updateRewards() {
        if (totalStaked > 0) {
            // Calculate rewards for all stakers
            uint256 blocksPassed = block.number - lastUpdateBlock;
            rewards[msg.sender] += (balances[msg.sender] * blocksPassed * rewardRate) / 1e18; // Adjust reward calculation
        }
        lastUpdateBlock = block.number; // Update the last update block
        _;
    }

    /**
     * @dev Stake tokens in the pool
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Staking amount must be greater than zero");
        
        // Transfer tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user balance and total staked amount
        balances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the pool
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external updateRewards {
        require(amount > 0, "Unstaking amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user balance and total staked amount
        balances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Withdraw accumulated rewards
     */
    function withdrawRewards() external updateRewards {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to withdraw");

        // Reset user's rewards
        rewards[msg.sender] = 0;

        // Transfer rewards to the user (e.g., could be in the same stakingToken or a different reward token)
        stakingToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Get the user's staked amount
     * @param user Address of the user
     * @return Amount staked by the user
     */
    function stakedAmount(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Get the user's accumulated rewards
     * @param user Address of the user
     * @return Accumulated rewards of the user
     */
    function accumulatedRewards(address user) external view returns (uint256) {
        uint256 blocksPassed = block.number - lastUpdateBlock;
        return rewards[user] + (balances[user] * blocksPassed * rewardRate) / 1e18;
    }
}
```
