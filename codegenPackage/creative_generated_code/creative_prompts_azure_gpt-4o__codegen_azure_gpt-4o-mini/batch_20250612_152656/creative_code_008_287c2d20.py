"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greens-bitcoins.pages.dev
Prompt: Write a Solidity contract to implement the Green Bitcoin tokenomics, including allocations for presale, staking rewards, marketing, liquidity, and community rewards.
Generated: DETERMINISTIC_287c2d20395277c2
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GreenBitcoinToken
 * @dev Implementation of the Green Bitcoin Token with specific tokenomics
 */
contract GreenBitcoinToken is ERC20, Ownable {
    // Tokenomics allocations
    uint256 public constant PRESALE_ALLOCATION = 200_000_000 * 10**decimals(); // 20%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 150_000_000 * 10**decimals(); // 15%
    uint256 public constant MARKETING_ALLOCATION = 100_000_000 * 10**decimals(); // 10%
    uint256 public constant LIQUIDITY_ALLOCATION = 150_000_000 * 10**decimals(); // 15%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 200_000_000 * 10**decimals(); // 20%
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**decimals(); // 100%

    // Track allocated tokens
    uint256 public presaleAllocated;
    uint256 public stakingRewardsAllocated;
    uint256 public marketingAllocated;
    uint256 public liquidityAllocated;
    uint256 public communityRewardsAllocated;

    // Events for allocation
    event TokensAllocated(address indexed to, uint256 amount, string allocationType);

    /**
     * @dev Constructor that mints the total supply to the owner's address
     */
    constructor() ERC20("Green Bitcoin Token", "GBT") {
        // Mint total supply to the owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Allocate presale tokens to the specified address
     * @param _to The address to receive the presale tokens
     */
    function allocatePresaleTokens(address _to) external onlyOwner {
        require(presaleAllocated < PRESALE_ALLOCATION, "Presale allocation limit reached");
        uint256 amount = PRESALE_ALLOCATION - presaleAllocated;
        presaleAllocated += amount;
        _transfer(owner(), _to, amount);
        emit TokensAllocated(_to, amount, "Presale");
    }

    /**
     * @dev Allocate staking rewards to the specified address
     * @param _to The address to receive staking rewards
     */
    function allocateStakingRewards(address _to) external onlyOwner {
        require(stakingRewardsAllocated < STAKING_REWARDS_ALLOCATION, "Staking rewards allocation limit reached");
        uint256 amount = STAKING_REWARDS_ALLOCATION - stakingRewardsAllocated;
        stakingRewardsAllocated += amount;
        _transfer(owner(), _to, amount);
        emit TokensAllocated(_to, amount, "Staking Rewards");
    }

    /**
     * @dev Allocate marketing tokens to the specified address
     * @param _to The address to receive marketing tokens
     */
    function allocateMarketingTokens(address _to) external onlyOwner {
        require(marketingAllocated < MARKETING_ALLOCATION, "Marketing allocation limit reached");
        uint256 amount = MARKETING_ALLOCATION - marketingAllocated;
        marketingAllocated += amount;
        _transfer(owner(), _to, amount);
        emit TokensAllocated(_to, amount, "Marketing");
    }

    /**
     * @dev Allocate liquidity tokens to the specified address
     * @param _to The address to receive liquidity tokens
     */
    function allocateLiquidityTokens(address _to) external onlyOwner {
        require(liquidityAllocated < LIQUIDITY_ALLOCATION, "Liquidity allocation limit reached");
        uint256 amount = LIQUIDITY_ALLOCATION - liquidityAllocated;
        liquidityAllocated += amount;
        _transfer(owner(), _to, amount);
        emit TokensAllocated(_to, amount, "Liquidity");
    }

    /**
     * @dev Allocate community rewards to the specified address
     * @param _to The address to receive community rewards
     */
    function allocateCommunityRewards(address _to) external onlyOwner {
        require(communityRewardsAllocated < COMMUNITY_REWARDS_ALLOCATION, "Community rewards allocation limit reached");
        uint256 amount = COMMUNITY_REWARDS_ALLOCATION - communityRewardsAllocated;
        communityRewardsAllocated += amount;
        _transfer(owner(), _to, amount);
        emit TokensAllocated(_to, amount, "Community Rewards");
    }
}
```
