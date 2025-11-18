"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muzikoin.pages.dev
Prompt: Create a Solidity function for staking MuziKoin tokens, ensuring rewards are distributed fairly to participants in the ecosystem.
Generated: DETERMINISTIC_97f98da21f3ba898
Batch ID: 20250612_145731
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
 * @title MuziKoinStaking
 * @dev A contract for staking MuziKoin tokens and distributing rewards fairly.
 */
contract MuziKoinStaking {
    // ERC-20 token interface
    IERC20 public muziKoin;

    // Struct representing each staker's information
    struct Staker {
        uint256 stakedAmount; // Total staked amount
        uint256 rewardDebt;   // Reward debt (used in fair reward calculation)
    }

    // Mapping of stakers to their info
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Rewards per token (scaled to avoid precision issues)
    uint256 public rewardsPerTokenScaled;

    // Scaling factor for precision calculations
    uint256 private constant SCALE = 1e18;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 reward);

    /**
     * @dev Constructor initializing the MuziKoin token.
     * @param _muziKoin Address of the MuziKoin token contract.
     */
    constructor(address _muziKoin) {
        require(_muziKoin != address(0), "Invalid token address");
        muziKoin = IERC20(_muziKoin);
    }

    /**
     * @dev Modifier to ensure the staker has a non-zero staked amount.
     */
    modifier hasStake(address _staker) {
        require(stakers[_staker].stakedAmount > 0, "No stake found");
        _;
    }

    /**
     * @dev Function to allow staking MuziKoin tokens into the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update rewards before modifying state
        updateRewards();

        Staker storage staker = stakers[msg.sender];

        // Transfer MuziKoin tokens from the sender to the contract
        require(muziKoin.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update staker data
        staker.stakedAmount += _amount;
        staker.rewardDebt = (staker.stakedAmount * rewardsPerTokenScaled) / SCALE;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to allow unstaking MuziKoin tokens from the contract.
     * @param _amount The amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external hasStake(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Amount must be greater than zero");
        require(staker.stakedAmount >= _amount, "Insufficient staked amount");

        // Update rewards before modifying state
        updateRewards();

        // Claim outstanding rewards first
        claimRewards();

        // Update staker data
        staker.stakedAmount -= _amount;
        staker.rewardDebt = (staker.stakedAmount * rewardsPerTokenScaled) / SCALE;

        // Update total staked amount
        totalStaked -= _amount;

        // Transfer MuziKoin tokens back to the sender
        require(muziKoin.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimRewards() public hasStake(msg.sender) {
        updateRewards();

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards
        uint256 pendingRewards = ((staker.stakedAmount * rewardsPerTokenScaled) / SCALE) - staker.rewardDebt;

        require(pendingRewards > 0, "No rewards available");

        // Update reward debt
        staker.rewardDebt = (staker.stakedAmount * rewardsPerTokenScaled) / SCALE;

        // Transfer rewards to the staker (assuming rewards are distributed from the contract's balance)
        require(muziKoin.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Internal function to update the rewards per token.
     */
    function updateRewards() internal {
        // Logic to increase `rewardsPerTokenScaled` based on external reward distribution mechanism.
        // This function should be called periodically or triggered by another function (e.g., a reward distribution event).
        // For simplicity, it is left empty here.
    }
}

/**
 * @dev Minimal IERC20 interface.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
