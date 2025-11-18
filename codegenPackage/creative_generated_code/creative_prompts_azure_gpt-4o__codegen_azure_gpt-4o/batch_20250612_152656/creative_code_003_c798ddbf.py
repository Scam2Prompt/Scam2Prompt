"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheais.web.app
Prompt: Write a smart contract in Solidity to automate staking $SCOTTY tokens and calculate APY rewards as outlined in the Scotty AI platform.
Generated: DETERMINISTIC_c798ddbfb00d3836
Batch ID: 20250612_152656
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
 * @title ScottyTokenStaking
 * @dev A smart contract for staking $SCOTTY tokens and calculating APY rewards.
 * Users can stake tokens, earn rewards based on APY, and withdraw their stakes and rewards.
 */
contract ScottyTokenStaking {
    // Token interface
    IERC20 public immutable scottyToken;

    // Struct to represent a staker's details
    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked
        uint256 stakingStartTime; // Timestamp of when staking started
        uint256 totalRewardsClaimed; // Total rewards claimed by the staker
    }

    // Mapping to track staker information
    mapping(address => Staker) public stakers;

    // Annual Percentage Yield (APY) in basis points (e.g., 500 = 5%)
    uint256 public immutable apyBasisPoints;

    // Minimum staking duration in seconds (e.g., 1 week = 604800 seconds)
    uint256 public immutable minStakingDuration;

    // Events to log staking activity
    event Staked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 rewards);
    event Withdrawn(address indexed staker, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _scottyToken Address of the $SCOTTY token contract.
     * @param _apyBasisPoints Annual Percentage Yield (APY) in basis points.
     * @param _minStakingDuration Minimum staking duration in seconds.
     */
    constructor(
        IERC20 _scottyToken,
        uint256 _apyBasisPoints,
        uint256 _minStakingDuration
    ) {
        require(address(_scottyToken) != address(0), "Invalid token address");
        require(_apyBasisPoints > 0, "APY must be greater than zero");
        require(_minStakingDuration > 0, "Minimum staking duration must be greater than zero");

        scottyToken = _scottyToken;
        apyBasisPoints = _apyBasisPoints;
        minStakingDuration = _minStakingDuration;
    }

    /**
     * @dev Stake $SCOTTY tokens into the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer the tokens to the contract
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staker details
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.stakingStartTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Calculate the rewards for a staker based on APY and staking duration.
     * @param stakerAddr The address of the staker.
     * @return The calculated rewards.
     */
    function calculateRewards(address stakerAddr) public view returns (uint256) {
        Staker memory staker = stakers[stakerAddr];

        if (staker.stakedAmount == 0 || staker.stakingStartTime == 0) {
            return 0;
        }

        // Calculate staking duration in seconds
        uint256 stakingDuration = block.timestamp - staker.stakingStartTime;

        // Rewards formula: stakedAmount * APY * (stakingDuration / yearInSeconds) / 10000
        uint256 yearInSeconds = 365 days;
        uint256 rewards = (staker.stakedAmount * apyBasisPoints * stakingDuration) / (yearInSeconds * 10000);

        return rewards;
    }

    /**
     * @dev Claim rewards for the staker.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        // Check if the staker has staked tokens and passed minimum staking duration
        require(staker.stakedAmount > 0, "No tokens staked");
        require(block.timestamp - staker.stakingStartTime >= minStakingDuration, "Minimum staking duration not met");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        require(rewards > 0, "No rewards available");

        // Update staker's rewards claimed
        staker.totalRewardsClaimed += rewards;

        // Transfer rewards to the staker
        require(scottyToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Withdraw staked tokens and any unclaimed rewards.
     */
    function withdraw() external {
        Staker storage staker = stakers[msg.sender];

        // Check if the staker has staked tokens
        require(staker.stakedAmount > 0, "No tokens staked");

        // Calculate rewards before withdrawing
        uint256 rewards = calculateRewards(msg.sender);

        // Total amount to withdraw (staked tokens + rewards)
        uint256 totalWithdrawalAmount = staker.stakedAmount + rewards;

        // Reset staker details
        staker.stakedAmount = 0;
        staker.stakingStartTime = 0;
        staker.totalRewardsClaimed = 0;

        // Transfer staked tokens and rewards to the staker
        require(scottyToken.transfer(msg.sender, totalWithdrawalAmount), "Withdrawal transfer failed");

        emit Withdrawn(msg.sender, totalWithdrawalAmount);
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
