"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9eth.eu
Prompt: Provide an example of a staking mechanism in Solidity that offers flexible lock periods and a fixed annual yield, inspired by the staking features on the site.
Generated: DETERMINISTIC_b81cc94e3d3bc19e
Batch ID: 20250612_154829
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
 * @title Flexible Staking Contract
 * @dev Implements staking mechanism with flexible lock periods and fixed annual yield.
 */
contract FlexibleStaking {
    // Token address for staking (ERC20 compatible)
    IERC20 public stakingToken;

    // Annual Yield (e.g., 10% yield would be 0.1 * 10^18 -> 100000000000000000)
    uint256 public annualYieldRate;

    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Timestamp when staking started
        uint256 lockPeriod; // Lock period in seconds
        bool claimed; // Flag indicating whether rewards were claimed
    }

    // Mapping from staker address to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Event emitted when a user withdraws their stake
    event StakeWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking contract.
     * @param _stakingToken Address of the ERC20 token to be staked.
     * @param _annualYieldRate Fixed annual yield rate in wei (e.g., 10% = 0.1 * 10^18).
     */
    constructor(IERC20 _stakingToken, uint256 _annualYieldRate) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_annualYieldRate > 0, "Yield rate must be positive");
        stakingToken = _stakingToken;
        annualYieldRate = _annualYieldRate;
    }

    /**
     * @dev Allows users to stake tokens with a specified lock period.
     * @param _amount Amount of tokens to stake.
     * @param _lockPeriod Lock period in seconds.
     */
    function stake(uint256 _amount, uint256 _lockPeriod) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(_lockPeriod > 0, "Lock period must be greater than zero");

        // Transfer staking tokens to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Record stake details
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            lockPeriod: _lockPeriod,
            claimed: false
        });

        emit Staked(msg.sender, _amount, _lockPeriod);
    }

    /**
     * @dev Calculates rewards for a given stake.
     * @param user Address of the staker.
     * @return Rewards amount in tokens.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory stakeData = stakes[user];
        if (stakeData.amount == 0 || stakeData.claimed) {
            return 0;
        }

        // Calculate staking duration in seconds
        uint256 stakingDuration = block.timestamp - stakeData.startTime;

        // Convert annual yield rate to per-second rate
        uint256 perSecondRate = annualYieldRate / (365 days);

        // Calculate rewards based on duration and staking amount
        uint256 rewards = (stakeData.amount * stakingDuration * perSecondRate) / 1e18;

        return rewards;
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount > 0, "No active stake found");
        require(!stakeData.claimed, "Rewards already claimed");
        require(block.timestamp >= stakeData.startTime + stakeData.lockPeriod, "Lock period not yet ended");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Mark rewards as claimed
        stakeData.claimed = true;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Allows users to withdraw their staked tokens after the lock period.
     */
    function withdrawStake() external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount > 0, "No active stake found");
        require(block.timestamp >= stakeData.startTime + stakeData.lockPeriod, "Lock period not yet ended");

        uint256 amount = stakeData.amount;

        // Reset stake data
        stakeData.amount = 0;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit StakeWithdrawn(msg.sender, amount);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
