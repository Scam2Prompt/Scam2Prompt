"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appsmuhdorepositoryhub.pages.dev
Prompt: Generate a smart contract that supports staking DNA tokens in the Genesis Staking Pool, following the MuhdoHub ecosystem requirements.
Generated: DETERMINISTIC_a2dcec7ec3ab3616
Batch ID: 20250612_153712
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

/**
 * @title Genesis Staking Pool for DNA Tokens
 * @dev A staking contract that allows users to stake DNA tokens and earn rewards.
 *      Follows MuhdoHub ecosystem requirements.
 */
contract GenesisStakingPool {
    // Token interface to interact with the DNA token contract.
    IERC20 public immutable dnaToken;

    // Struct to track staker's information.
    struct Staker {
        uint256 amountStaked; // Amount of DNA tokens staked by the user.
        uint256 rewardDebt;   // Rewards owed to the staker.
    }

    // Mapping of user addresses to their staking data.
    mapping(address => Staker) public stakers;

    // Total DNA tokens staked in the pool.
    uint256 public totalStaked;

    // Reward rate per block (example: 0.01 DNA per block, adjustable later).
    uint256 public rewardRatePerBlock;

    // Last recorded block for reward calculation.
    uint256 public lastRewardBlock;

    // Accumulated rewards per staked token (scaled by 1e18).
    uint256 public accRewardPerShare;

    // Event declarations for transparency.
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking pool contract.
     * @param _dnaToken Address of the DNA token contract.
     * @param _rewardRatePerBlock Reward rate per block for staking.
     */
    constructor(IERC20 _dnaToken, uint256 _rewardRatePerBlock) {
        require(address(_dnaToken) != address(0), "Invalid DNA token address");
        require(_rewardRatePerBlock > 0, "Reward rate must be greater than zero");

        dnaToken = _dnaToken;
        rewardRatePerBlock = _rewardRatePerBlock;
        lastRewardBlock = block.number; // Set initial reward block.
    }

    /**
     * @dev Internal function to update the reward variables.
     */
    function updatePool() internal {
        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        uint256 blocksSinceLastReward = block.number - lastRewardBlock;
        uint256 reward = blocksSinceLastReward * rewardRatePerBlock;
        accRewardPerShare += (reward * 1e18) / totalStaked;

        lastRewardBlock = block.number;
    }

    /**
     * @dev Function to stake DNA tokens into the pool.
     * @param _amount Amount of DNA tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        updatePool();
        Staker storage staker = stakers[msg.sender];

        // Transfer tokens from the user to the contract.
        dnaToken.transferFrom(msg.sender, address(this), _amount);

        // Calculate pending rewards.
        uint256 pendingReward = (staker.amountStaked * accRewardPerShare) / 1e18 - staker.rewardDebt;

        // Update staker's information.
        staker.amountStaked += _amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 1e18;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake DNA tokens from the pool.
     * @param _amount Amount of DNA tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Unstake amount exceeds staked balance");

        updatePool();

        // Calculate pending rewards.
        uint256 pendingReward = (staker.amountStaked * accRewardPerShare) / 1e18 - staker.rewardDebt;

        // Update staker's information.
        staker.amountStaked -= _amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 1e18;

        totalStaked -= _amount;

        // Transfer unstaked tokens back to the user.
        dnaToken.transfer(msg.sender, _amount);

        // Transfer pending rewards (if any).
        if (pendingReward > 0) {
            dnaToken.transfer(msg.sender, pendingReward);
            emit RewardClaimed(msg.sender, pendingReward);
        }

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Function to claim pending rewards without unstaking.
     */
    function claimRewards() external {
        updatePool();

        Staker storage staker = stakers[msg.sender];

        uint256 pendingReward = (staker.amountStaked * accRewardPerShare) / 1e18 - staker.rewardDebt;
        require(pendingReward > 0, "No rewards available");

        // Update reward debt.
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 1e18;

        // Transfer rewards to the user.
        dnaToken.transfer(msg.sender, pendingReward);

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Function to set a new reward rate per block.
     * @param _rewardRatePerBlock Reward rate per block to be set.
     */
    function setRewardRate(uint256 _rewardRatePerBlock) external {
        require(_rewardRatePerBlock > 0, "Reward rate must be greater than zero");
        
        updatePool();
        rewardRatePerBlock = _rewardRatePerBlock;
    }
}

// Minimal ERC20 interface to interact with the DNA token contract.
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
