"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibasaga-io.web.app
Prompt: Write a smart contract in Solidity that integrates staking functionality for $SHIA tokens, ensuring reward multipliers for early stakers and voting power based on the amount staked.
Generated: DETERMINISTIC_0ab46c4dd96e9fe4
Batch ID: 20250612_152827
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
 * @title SHIAStaking
 * @dev A staking contract for SHIA tokens with reward multipliers for early stakers and voting power allocation.
 */
contract SHIAStaking {
    // ERC20 token interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // SHIA token address
    IERC20 public immutable shiaToken;

    // Staker information
    struct StakerInfo {
        uint256 amountStaked;  // Amount of tokens staked
        uint256 rewardMultiplier;  // Reward multiplier (1x, 2x, etc.)
        uint256 votingPower;  // Voting power based on staked amount
        uint256 lastStakeTime;  // Timestamp of the last stake
    }

    // Mapping of staker addresses to their staking information
    mapping(address => StakerInfo) public stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Constants for reward multipliers
    uint256 constant EARLY_STAKER_MULTIPLIER = 2; // Early staker 2x reward
    uint256 constant BASE_MULTIPLIER = 1;        // Regular staker 1x reward
    uint256 constant EARLY_STAKER_TIMEFRAME = 30 days; // Time window for early staking

    // Events
    event Staked(address indexed staker, uint256 amount, uint256 votingPower);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 reward);

    /**
     * @dev Constructor initializes the SHIA token address.
     * @param _shiaToken Address of the SHIA token contract.
     */
    constructor(IERC20 _shiaToken) {
        shiaToken = _shiaToken;
    }

    /**
     * @dev Stake SHIA tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from staker to the contract
        require(shiaToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate reward multiplier
        uint256 multiplier = block.timestamp <= EARLY_STAKER_TIMEFRAME ? EARLY_STAKER_MULTIPLIER : BASE_MULTIPLIER;

        // Calculate voting power (simple 1:1 ratio for voting power)
        uint256 votingPower = amount * multiplier;

        // Update staker information
        StakerInfo storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.rewardMultiplier = multiplier;
        staker.votingPower += votingPower;
        staker.lastStakeTime = block.timestamp;

        // Update total staked tokens
        totalStaked += amount;

        emit Staked(msg.sender, amount, votingPower);
    }

    /**
     * @dev Unstake SHIA tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= amount;
        staker.votingPower -= amount * staker.rewardMultiplier;

        // Update total staked tokens
        totalStaked -= amount;

        // Transfer tokens back to the staker
        require(shiaToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on staked tokens and reward multiplier.
     */
    function claimRewards() external {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No staked tokens to claim rewards");

        // Calculate reward (simple example: reward = amountStaked * rewardMultiplier)
        uint256 reward = staker.amountStaked * staker.rewardMultiplier;

        // Transfer reward tokens to the staker
        require(shiaToken.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Get the voting power of a staker.
     * @param staker Address of the staker.
     * @return Voting power of the staker.
     */
    function getVotingPower(address staker) external view returns (uint256) {
        return stakers[staker].votingPower;
    }
}
```
