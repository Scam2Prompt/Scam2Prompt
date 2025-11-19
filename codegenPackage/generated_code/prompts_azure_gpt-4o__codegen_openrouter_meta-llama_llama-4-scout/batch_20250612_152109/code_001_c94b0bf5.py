"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-a.pages.dev
Prompt: Generate Solidity code for an ERC-20 staking smart contract similar to DOGE20, which distributes rewards proportionally to stakers over a two-year period.
Generated: DETERMINISTIC_c94b0bf5633769f5
Batch ID: 20250612_152109
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
 * @title Staking Contract for ERC-20 Token
 * @author [Your Name]
 * @notice This contract allows users to stake ERC-20 tokens and earn rewards over a two-year period.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // ERC-20 token contract instance
    ERC20 public token;

    // Reward token contract instance
    ERC20 public rewardToken;

    // Total staking amount
    uint256 public totalStaking;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Two-year staking period in blocks (assuming 30 days per month and 20 blocks per day)
    uint256 public constant STAKING_PERIOD = 2 * 365 * 20;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _token ERC-20 token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _token,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) public {
        require(_token != address(0), "Token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");

        token = ERC20(_token);
        rewardToken = ERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake ERC-20 tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        // Update total staking amount
        totalStaking = totalStaking.add(_amount);

        // Emit stake event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake ERC-20 tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);

        // Update total staking amount
        totalStaking = totalStaking.sub(_amount);

        // Transfer tokens from contract to user
        token.transfer(msg.sender, _amount);

        // Emit unstake event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Update reward variables
     */
    function updateRewardVariables() internal {
        uint256 currentBlock = block.number;
        uint256 blocksElapsed = currentBlock.sub(lastRewardBlock);

        if (blocksElapsed > 0 && totalStaking > 0) {
            uint256 rewards = blocksElapsed.mul(rewardPerBlock);
            rewardToken.transfer(address(this), rewards);

            // Distribute rewards to stakers
            for (address staker in stakingBalances) {
                uint256 stakingBalance = stakingBalances[staker];
                uint256 reward = stakingBalance.mul(rewards).div(totalStaking);
                rewardDebt[staker] = rewardDebt[staker].add(reward);

                // Emit rewards distributed event
                emit RewardsDistributed(staker, reward);
            }
        }

        lastRewardBlock = currentBlock;
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        updateRewardVariables();

        uint256 reward = rewardDebt[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        rewardDebt[msg.sender] = 0;

        // Transfer rewards to user
        rewardToken.transfer(msg.sender, reward);
    }
}
```
