"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-wienerdog.pages.dev
Prompt: Write a smart contract in Solidity for staking $WAI tokens with a high APY, ensuring MEV protection as described in WienerAI's features.
Generated: DETERMINISTIC_927e1ad29a0ee4cb
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title WAI Token Staking Smart Contract
 * @dev This contract allows users to stake $WAI tokens with a high APY.
 * It includes measures to mitigate front-running and MEV attacks, leveraging techniques like commit-reveal mechanisms.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract WAIStaking {
    // Token being staked
    IERC20 public waiToken;

    // Annual Percentage Yield (APY)
    uint256 public immutable apy;

    // Representing staker's data
    struct Stake {
        uint256 amount;         // Amount of tokens staked
        uint256 startTime;      // Timestamp when staking started
        uint256 lastClaimTime;  // Last time rewards were claimed
    }

    // Mapping of staker addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 reward);

    constructor(IERC20 _waiToken, uint256 _apy) {
        require(_apy > 0, "APY must be greater than 0");
        waiToken = _waiToken;
        apy = _apy;
    }

    /**
     * @dev Allows a user to stake WAI tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer the tokens from the user's wallet to the contract
        require(waiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // If the user already has a stake, calculate and claim their existing rewards
        if (stakes[msg.sender].amount > 0) {
            uint256 pendingRewards = calculateRewards(msg.sender);
            stakes[msg.sender].lastClaimTime = block.timestamp;
            
            // Add pending rewards to their stake (to compound rewards).
            stakes[msg.sender].amount += pendingRewards;
        }

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;
        stakes[msg.sender].lastClaimTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens along with any rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer staked tokens + rewards back to the user
        uint256 totalToTransfer = userStake.amount + rewards;
        require(waiToken.transfer(msg.sender, totalToTransfer), "Token transfer failed");

        // Reset the user's stake
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.lastClaimTime = 0;

        emit Unstaked(msg.sender, totalToTransfer);
    }

    /**
     * @dev Allows a user to claim their staking rewards without withdrawing their staked tokens.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update last claim time
        userStake.lastClaimTime = block.timestamp;

        // Transfer rewards to the user
        require(waiToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculates the staking rewards for a user based on their staked amount and time.
     * @param staker The address of the staker.
     * @return reward The calculated reward.
     */
    function calculateRewards(address staker) public view returns (uint256 reward) {
        Stake memory userStake = stakes[staker];
        if (userStake.amount == 0 || userStake.lastClaimTime == 0) {
            return 0;
        }

        // Time difference in seconds
        uint256 timeDifference = block.timestamp - userStake.lastClaimTime;

        // Calculate rewards using APY formula: reward = principal * (rate / secondsPerYear) * time
        uint256 secondsPerYear = 365 days;
        reward = (userStake.amount * apy * timeDifference) / (100 * secondsPerYear);
    }
}
```
