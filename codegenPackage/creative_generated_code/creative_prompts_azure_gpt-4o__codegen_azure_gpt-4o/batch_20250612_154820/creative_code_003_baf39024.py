"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cruas.ru
Prompt: Create a Solidity smart contract that mimics the liquidity pool mechanism of Velodrome Finance, including token rewards for liquidity providers.
Generated: DETERMINISTIC_baf390242b70fe76
Batch ID: 20250612_154820
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
 * @title LiquidityPool
 * @dev Smart contract mimicking a basic liquidity pool mechanism with reward distribution for liquidity providers.
 */
contract LiquidityPool {
    // Structure to hold liquidity provider's info
    struct LiquidityProvider {
        uint256 amountDeposited; // Amount of tokens deposited by the provider
        uint256 rewardDebt;      // Rewards debt (used for accurate reward calculations)
    }

    // Events
    event LiquidityAdded(address indexed provider, uint256 amount);
    event LiquidityRemoved(address indexed provider, uint256 amount);
    event RewardsClaimed(address indexed provider, uint256 rewardAmount);

    // State variables
    IERC20 public immutable token; // Token used in the liquidity pool
    uint256 public totalLiquidity; // Total liquidity in the pool
    uint256 public rewardPerToken; // Accumulated rewards per token
    uint256 public lastRewardTimestamp; // Timestamp of last reward distribution
    uint256 public rewardRate; // Reward rate per second

    mapping(address => LiquidityProvider) public liquidityProviders; // Liquidity providers' data

    // Constructor
    constructor(IERC20 _token, uint256 _rewardRate) {
        require(address(_token) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        token = _token;
        rewardRate = _rewardRate;
        lastRewardTimestamp = block.timestamp; // Initialize last reward timestamp
    }

    /**
     * @notice Updates pool rewards. Should be called during every transaction affecting the pool.
     */
    function updatePool() internal {
        if (totalLiquidity > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
            rewardPerToken += (timeElapsed * rewardRate) / totalLiquidity;
        }
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @notice Add liquidity to the pool and earn rewards.
     * @param amount Amount of tokens to deposit into the pool.
     */
    function addLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        updatePool();

        LiquidityProvider storage provider = liquidityProviders[msg.sender];

        // If provider already exists, calculate pending rewards and update reward debt
        if (provider.amountDeposited > 0) {
            uint256 pendingReward = _calculateReward(provider);
            provider.rewardDebt += pendingReward;
        }

        // Transfer tokens from the provider to the pool
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update provider's data
        provider.amountDeposited += amount;
        provider.rewardDebt = provider.amountDeposited * rewardPerToken;

        // Update total liquidity
        totalLiquidity += amount;

        emit LiquidityAdded(msg.sender, amount);
    }

    /**
     * @notice Withdraw liquidity from the pool and claim rewards.
     * @param amount Amount of tokens to withdraw from the pool.
     */
    function removeLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        LiquidityProvider storage provider = liquidityProviders[msg.sender];
        require(provider.amountDeposited >= amount, "Insufficient liquidity");

        updatePool();

        // Calculate pending rewards and reset reward debt
        uint256 pendingReward = _calculateReward(provider);
        provider.rewardDebt += pendingReward;

        // Update provider's data
        provider.amountDeposited -= amount;
        provider.rewardDebt = provider.amountDeposited * rewardPerToken;

        // Update total liquidity
        totalLiquidity -= amount;

        // Transfer tokens back to the provider
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit LiquidityRemoved(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards.
     */
    function claimRewards() external {
        updatePool();

        LiquidityProvider storage provider = liquidityProviders[msg.sender];
        uint256 pendingReward = _calculateReward(provider);

        require(pendingReward > 0, "No rewards available");

        provider.rewardDebt = provider.amountDeposited * rewardPerToken;

        // Transfer reward tokens to the provider
        require(token.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Internal function to calculate pending rewards for a provider.
     * @param provider Liquidity provider object.
     * @return pendingReward Amount of rewards that can be claimed.
     */
    function _calculateReward(LiquidityProvider storage provider) internal view returns (uint256) {
        return (provider.amountDeposited * rewardPerToken) - provider.rewardDebt;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
