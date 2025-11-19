"""
Generated Code Metadata:
========================
Original URL: https://panther-ai.pages.dev
Prompt: Generate a smart contract for the PantherAI token using BEP20 standards, ensuring it includes features for staking and liquidity management.
Generated: DETERMINISTIC_4daaa70eb87f350d
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PantherAI Token
 * @author [Your Name]
 * @notice BEP20 compliant token with staking and liquidity management features
 */
contract PantherAI is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker's information
    mapping(address => Staker) public stakers;

    // Mapping of liquidity provider's information
    mapping(address => LiquidityProvider) public liquidityProviders;

    // Total staked tokens
    uint256 public totalStaked;

    // Total liquidity provided
    uint256 public totalLiquidity;

    // Staking and liquidity management variables
    uint256 public stakingRewardRate;
    uint256 public liquidityRewardRate;
    uint256 public stakingCooldownPeriod;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event LiquidityProvided(address indexed provider, uint256 amount);
    event LiquidityRemoved(address indexed provider, uint256 amount);

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initialize staking and liquidity management variables
        stakingRewardRate = 100; // 1%
        liquidityRewardRate = 50; // 0.5%
        stakingCooldownPeriod = 30 days;

        // Mint initial tokens
        _mint(msg.sender, 1e9 * 10**18); // 1 billion tokens
    }

    /**
     * @notice Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Invalid stake amount");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update staker's information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(amount);
        stakers[msg.sender].lastStakedTime = block.timestamp;

        // Update total staked tokens
        totalStaked = totalStaked.add(amount);

        // Transfer tokens from staker to contract
        _transfer(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     */
    function unstake() external nonReentrant {
        require(stakers[msg.sender].stakedAmount > 0, "No staked tokens");

        // Calculate unstake amount with reward
        uint256 unstakeAmount = stakers[msg.sender].stakedAmount;
        uint256 reward = calculateStakingReward(unstakeAmount);

        // Update staker's information
        stakers[msg.sender].stakedAmount = 0;
        stakers[msg.sender].lastStakedTime = 0;

        // Update total staked tokens
        totalStaked = totalStaked.sub(unstakeAmount);

        // Transfer tokens to staker
        _transfer(address(this), msg.sender, unstakeAmount.add(reward));

        emit Unstaked(msg.sender, unstakeAmount);
    }

    /**
     * @notice Provide liquidity
     * @param amount Amount to provide
     */
    function provideLiquidity(uint256 amount) external {
        require(amount > 0, "Invalid liquidity amount");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update liquidity provider's information
        liquidityProviders[msg.sender].liquidityAmount = liquidityProviders[msg.sender].liquidityAmount.add(amount);

        // Update total liquidity
        totalLiquidity = totalLiquidity.add(amount);

        // Transfer tokens from provider to contract
        _transfer(msg.sender, address(this), amount);

        emit LiquidityProvided(msg.sender, amount);
    }

    /**
     * @notice Remove liquidity
     */
    function removeLiquidity() external nonReentrant {
        require(liquidityProviders[msg.sender].liquidityAmount > 0, "No liquidity provided");

        // Calculate remove amount with reward
        uint256 removeAmount = liquidityProviders[msg.sender].liquidityAmount;
        uint256 reward = calculateLiquidityReward(removeAmount);

        // Update liquidity provider's information
        liquidityProviders[msg.sender].liquidityAmount = 0;

        // Update total liquidity
        totalLiquidity = totalLiquidity.sub(removeAmount);

        // Transfer tokens to provider
        _transfer(address(this), msg.sender, removeAmount.add(reward));

        emit LiquidityRemoved(msg.sender, removeAmount);
    }

    /**
     * @notice Calculate staking reward
     * @param amount Staked amount
     * @return Reward amount
     */
    function calculateStakingReward(uint256 amount) internal view returns (uint256) {
        return amount.mul(stakingRewardRate).div(100);
    }

    /**
     * @notice Calculate liquidity reward
     * @param amount Liquidity amount
     * @return Reward amount
     */
    function calculateLiquidityReward(uint256 amount) internal view returns (uint256) {
        return amount.mul(liquidityRewardRate).div(100);
    }

    // Structs
    struct Staker {
        uint256 stakedAmount;
        uint256 lastStakedTime;
    }

    struct LiquidityProvider {
        uint256 liquidityAmount;
    }
}
```
