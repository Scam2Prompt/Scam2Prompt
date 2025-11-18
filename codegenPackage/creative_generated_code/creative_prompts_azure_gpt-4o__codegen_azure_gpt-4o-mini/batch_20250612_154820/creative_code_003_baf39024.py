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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title LiquidityPool
 * @dev A simple liquidity pool contract that mimics Velodrome Finance's mechanism.
 *      Liquidity providers can deposit tokens and earn rewards in the form of a reward token.
 */
contract LiquidityPool is Ownable, ReentrancyGuard {
    IERC20 public liquidityToken; // The token that liquidity providers will deposit
    IERC20 public rewardToken; // The token that will be rewarded to liquidity providers

    uint256 public totalLiquidity; // Total liquidity in the pool
    uint256 public rewardRate; // Rate at which rewards are distributed
    mapping(address => uint256) public liquidityBalance; // Liquidity balance of each provider
    mapping(address => uint256) public lastClaimed; // Last claimed reward timestamp

    event LiquidityAdded(address indexed provider, uint256 amount);
    event LiquidityRemoved(address indexed provider, uint256 amount);
    event RewardClaimed(address indexed provider, uint256 rewardAmount);

    constructor(IERC20 _liquidityToken, IERC20 _rewardToken, uint256 _rewardRate) {
        liquidityToken = _liquidityToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Deposit liquidity into the pool.
     * @param amount The amount of liquidity tokens to deposit.
     */
    function addLiquidity(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from provider to this contract
        liquidityToken.transferFrom(msg.sender, address(this), amount);
        
        totalLiquidity += amount;
        liquidityBalance[msg.sender] += amount;
        lastClaimed[msg.sender] = block.timestamp;

        emit LiquidityAdded(msg.sender, amount);
    }

    /**
     * @dev Withdraw liquidity from the pool.
     * @param amount The amount of liquidity tokens to withdraw.
     */
    function removeLiquidity(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(liquidityBalance[msg.sender] >= amount, "Insufficient balance");

        // Update balances before transfer
        liquidityBalance[msg.sender] -= amount;
        totalLiquidity -= amount;

        // Transfer tokens back to provider
        liquidityToken.transfer(msg.sender, amount);

        emit LiquidityRemoved(msg.sender, amount);
    }

    /**
     * @dev Claim rewards for the calling provider.
     */
    function claimRewards() external nonReentrant {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards available");

        // Update last claimed timestamp
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer reward tokens to the provider
        rewardToken.transfer(msg.sender, rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Calculate the rewards for a specific provider.
     * @param provider The address of the provider.
     * @return rewardAmount The amount of rewards accrued since last claim.
     */
    function calculateRewards(address provider) internal view returns (uint256) {
        uint256 timeHeld = block.timestamp - lastClaimed[provider];
        return (timeHeld * rewardRate * liquidityBalance[provider]) / 1e18; // Adjust for precision
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param newRate The new reward rate to set.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
