"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-xai-games.pages.dev
Prompt: Create a smart contract that implements staking tiers and reward multipliers for esXAI tokens, ensuring compatibility with self-custody wallets and Ledger hardware wallets, as outlined on the Xai Staking webpage.
Generated: DETERMINISTIC_5e2653b02c5db674
Batch ID: 20250612_152527
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
 * @title StakingContract
 * @dev Implements staking tiers and reward multipliers for esXAI tokens.
 * Compatible with self-custody wallets and Ledger hardware wallets.
 */
contract StakingContract {
    // Token interface
    IERC20 public esXAIToken;

    // Struct to represent a staking tier
    struct StakingTier {
        uint256 minStake;
        uint256 rewardMultiplier; // Multiplier expressed as a percentage (e.g., 200 = 2.0x rewards)
    }

    // List of staking tiers
    StakingTier[] public stakingTiers;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Mapping to track last claim timestamp
    mapping(address => uint256) public lastClaim;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 rewards);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _esXAIToken Address of the esXAI token contract.
     * @param _tiers Array of tuples defining staking tiers (minStake, rewardMultiplier).
     */
    constructor(address _esXAIToken, StakingTier[] memory _tiers) {
        require(_esXAIToken != address(0), "Invalid token address");
        esXAIToken = IERC20(_esXAIToken);

        for (uint256 i = 0; i < _tiers.length; i++) {
            stakingTiers.push(
                StakingTier({
                    minStake: _tiers[i].minStake,
                    rewardMultiplier: _tiers[i].rewardMultiplier
                })
            );
        }
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to contract
        require(esXAIToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake
        stakes[msg.sender] += amount;

        // Update last claim timestamp
        lastClaim[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user stake
        stakes[msg.sender] -= amount;

        // Transfer tokens back to user
        require(esXAIToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on staked tokens and time elapsed.
     */
    function claimRewards() external {
        require(stakes[msg.sender] > 0, "No staked balance");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update last claim timestamp
        lastClaim[msg.sender] = block.timestamp;

        // Transfer rewards to user
        require(esXAIToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user based on staked tokens and tiers.
     * @param user Address of the user.
     * @return rewards Amount of rewards earned.
     */
    function calculateRewards(address user) public view returns (uint256 rewards) {
        uint256 stakedAmount = stakes[user];
        uint256 timeElapsed = block.timestamp - lastClaim[user];

        // Determine the user's reward multiplier based on staking tiers
        uint256 multiplier = 100; // Default multiplier (1.0x rewards)
        for (uint256 i = 0; i < stakingTiers.length; i++) {
            if (stakedAmount >= stakingTiers[i].minStake) {
                multiplier = stakingTiers[i].rewardMultiplier;
            }
        }

        // Rewards = stakedAmount * timeElapsed * multiplier / 100
        rewards = (stakedAmount * timeElapsed * multiplier) / (100 * 1 days); // Normalize by 1 day
    }

    /**
     * @dev View function to get user's staked balance.
     * @param user Address of the user.
     * @return Staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @dev View function to get staking tiers.
     * @return Array of staking tiers (minStake, rewardMultiplier).
     */
    function getStakingTiers() external view returns (StakingTier[] memory) {
        return stakingTiers;
    }
}

// Minimal ERC20 interface for token interaction
interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}
```
