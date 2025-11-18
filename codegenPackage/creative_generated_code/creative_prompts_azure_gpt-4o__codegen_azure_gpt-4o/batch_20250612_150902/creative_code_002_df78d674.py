"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fightout.vercel.app
Prompt: Provide an example of how to implement staking functionality in a DApp using MainnetSync, including the ability to lock tokens and calculate rewards.
Generated: DETERMINISTIC_df78d67473019831
Batch ID: 20250612_150902
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
 * @title StakingDApp
 * @dev Implements token staking functionality with lock periods and reward calculation.
 */
contract StakingDApp {
    // Address of the ERC20 token contract
    IERC20 public token;

    // Reward rate (e.g., 10% per year = 0.1)
    uint256 public rewardRate;

    // Minimum lock period in seconds
    uint256 public lockPeriod;

    // Struct to store staking details
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 startTime;    // Timestamp when staking started
        bool withdrawn;       // Flag to indicate if withdrawn
    }

    // Mapping to track stakes per user
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 startTime);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize token, reward rate, and lock period
    constructor(IERC20 _token, uint256 _rewardRate, uint256 _lockPeriod) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        require(_lockPeriod > 0, "Lock period must be greater than zero");

        token = _token;
        rewardRate = _rewardRate;
        lockPeriod = _lockPeriod;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(stakes[msg.sender].amount == 0, "Already staking");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Record staking details
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            withdrawn: false
        });

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens and rewards after the lock period.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");
        require(!userStake.withdrawn, "Stake already withdrawn");
        require(block.timestamp >= userStake.startTime + lockPeriod, "Lock period not yet over");

        // Calculate rewards
        uint256 reward = calculateReward(userStake.amount, userStake.startTime);

        // Withdraw staked tokens and rewards
        uint256 totalAmount = userStake.amount + reward;
        require(token.transfer(msg.sender, totalAmount), "Token transfer failed");

        // Update stake status
        userStake.withdrawn = true;

        emit Withdrawn(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Calculates rewards based on the staking amount and duration.
     * @param _amount Amount of tokens staked.
     * @param _startTime Timestamp when staking started.
     * @return Reward amount.
     */
    function calculateReward(uint256 _amount, uint256 _startTime) public view returns (uint256) {
        uint256 stakingDuration = block.timestamp - _startTime;
        uint256 reward = (_amount * rewardRate * stakingDuration) / (365 days);
        return reward;
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}
```
