"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-ea.pages.dev
Prompt: Design a smart contract using Solidity to distribute staking rewards to DOGE20 token holders over a period of two years, according to their percentage of the staking pool, and provide a code example of how to implement this functionality.
Generated: DETERMINISTIC_865b2093160f5193
Batch ID: 20250622_210243
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
 * @title Doge20StakingContract
 * @author [Your Name]
 * @notice A smart contract to distribute staking rewards to DOGE20 token holders over a period of two years.
 */
contract Doge20StakingContract is ReentrancyGuard {
    // Mapping of user staking balance
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebts;

    // DOGE20 token contract
    ERC20 public doge20Token;

    // Total staking pool
    uint256 public totalStakingPool;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block (2 years, assuming 13,680 blocks per day and 365 days per year)
    uint256 public stakingEndBlock;

    // Reward distribution start block (after 1 year)
    uint256 public rewardDistributionStartBlock;

    // Reward distribution end block (after 2 years)
    uint256 public rewardDistributionEndBlock;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _doge20TokenAddress Address of the DOGE20 token contract
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     */
    constructor(
        address _doge20TokenAddress,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock
    ) {
        doge20Token = ERC20(_doge20TokenAddress);
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingStartBlock + (2 * 365 * 13680); // 2 years
        rewardDistributionStartBlock = _stakingStartBlock + (1 * 365 * 13680); // 1 year
        rewardDistributionEndBlock = _stakingStartBlock + (2 * 365 * 13680); // 2 years
        lastRewardBlock = _stakingStartBlock;
    }

    /**
     * @notice Stake DOGE20 tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(msg.sender != address(0), "Invalid address");
        require(_amount > 0, "Invalid amount");
        require(block.number >= stakingStartBlock && block.number <= stakingEndBlock, "Staking period is over");

        // Transfer tokens from user to contract
        doge20Token.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] += _amount;

        // Update total staking pool
        totalStakingPool += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake DOGE20 tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(msg.sender != address(0), "Invalid address");
        require(_amount > 0, "Invalid amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] -= _amount;

        // Update total staking pool
        totalStakingPool -= _amount;

        // Transfer tokens from contract to user
        doge20Token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward variables
     */
    function updateRewardVariables() internal {
        uint256 currentBlock = block.number;
        if (currentBlock <= lastRewardBlock) return;

        uint256 rewards = 0;
        if (currentBlock > rewardDistributionEndBlock) {
            currentBlock = rewardDistributionEndBlock;
        }

        if (currentBlock > rewardDistributionStartBlock) {
            rewards = (currentBlock - lastRewardBlock) * rewardPerBlock;
        }

        lastRewardBlock = currentBlock;

        // Distribute rewards to all stakers
        for (address user in stakingBalances) {
            uint256 userStakingBalance = stakingBalances[user];
            if (userStakingBalance > 0) {
                uint256 userReward = (userStakingBalance * rewards) / totalStakingPool;
                rewardDebts[user] += userReward;

                emit RewardsDistributed(user, userReward);
            }
        }
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        updateRewardVariables();

        uint256 userReward = rewardDebts[msg.sender];

        require(userReward > 0, "No rewards to claim");

        rewardDebts[msg.sender] = 0;

        // Transfer rewards to user
        doge20Token.transfer(msg.sender, userReward);
    }
}
```
