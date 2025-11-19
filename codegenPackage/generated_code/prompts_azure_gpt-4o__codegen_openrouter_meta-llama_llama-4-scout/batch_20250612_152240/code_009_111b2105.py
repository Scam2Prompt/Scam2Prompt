"""
Generated Code Metadata:
========================
Original URL: https://claim-wienerdogs.pages.dev
Prompt: Create a Solidity contract for WienerAI tokenomics, ensuring proper allocation for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_111b21059f9ec905
Batch ID: 20250612_152240
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
 * @title WienerAI Tokenomics Contract
 * @author [Your Name]
 * @notice This contract manages the tokenomics of WienerAI, including presale, staking, community rewards, liquidity, and marketing allocations.
 */
contract WienerAITokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective roles
    mapping(address => bool) public isPresaleAllocator;
    mapping(address => bool) public isStakingAllocator;
    mapping(address => bool) public isCommunityRewardsAllocator;
    mapping(address => bool) public isLiquidityAllocator;
    mapping(address => bool) public isMarketingAllocator;

    // Token allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 15;
    uint256 public constant STAKING_ALLOCATION = 20;
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 20;
    uint256 public constant LIQUIDITY_ALLOCATION = 20;
    uint256 public constant MARKETING_ALLOCATION = 15;

    // Token allocation amounts
    uint256 public presaleAllocationAmount;
    uint256 public stakingAllocationAmount;
    uint256 public communityRewardsAllocationAmount;
    uint256 public liquidityAllocationAmount;
    uint256 public marketingAllocationAmount;

    // Total token supply
    uint256 public constant TOTAL_SUPPLY = 1000 * 10**6 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @notice Constructor for WienerAITokenomics contract
     * @param presaleAllocatorAddress Address for presale allocation
     * @param stakingAllocatorAddress Address for staking allocation
     * @param communityRewardsAllocatorAddress Address for community rewards allocation
     * @param liquidityAllocatorAddress Address for liquidity allocation
     * @param marketingAllocatorAddress Address for marketing allocation
     */
    constructor(
        address presaleAllocatorAddress,
        address stakingAllocatorAddress,
        address communityRewardsAllocatorAddress,
        address liquidityAllocatorAddress,
        address marketingAllocatorAddress
    ) ERC20("WienerAI", "WAI") {
        // Initialize token allocations
        presaleAllocationAmount = TOTAL_SUPPLY.mul(PRESALE_ALLOCATION).div(100);
        stakingAllocationAmount = TOTAL_SUPPLY.mul(STAKING_ALLOCATION).div(100);
        communityRewardsAllocationAmount = TOTAL_SUPPLY.mul(COMMUNITY_REWARDS_ALLOCATION).div(100);
        liquidityAllocationAmount = TOTAL_SUPPLY.mul(LIQUIDITY_ALLOCATION).div(100);
        marketingAllocationAmount = TOTAL_SUPPLY.mul(MARKETING_ALLOCATION).div(100);

        // Mint tokens for each allocation
        _mint(presaleAllocatorAddress, presaleAllocationAmount);
        _mint(stakingAllocatorAddress, stakingAllocationAmount);
        _mint(communityRewardsAllocatorAddress, communityRewardsAllocationAmount);
        _mint(liquidityAllocatorAddress, liquidityAllocationAmount);
        _mint(marketingAllocatorAddress, marketingAllocationAmount);

        // Set role mappings
        isPresaleAllocator[presaleAllocatorAddress] = true;
        isStakingAllocator[stakingAllocatorAddress] = true;
        isCommunityRewardsAllocator[communityRewardsAllocatorAddress] = true;
        isLiquidityAllocator[liquidityAllocatorAddress] = true;
        isMarketingAllocator[marketingAllocatorAddress] = true;
    }

    /**
     * @notice Presale token allocation function
     * @param amount Amount of tokens to allocate for presale
     */
    function allocatePresaleTokens(uint256 amount) external {
        require(isPresaleAllocator[msg.sender], "Only presale allocator can allocate tokens");
        require(amount <= presaleAllocationAmount, "Allocation amount exceeds available tokens");
        presaleAllocationAmount = presaleAllocationAmount.sub(amount);
        _mint(msg.sender, amount);
    }

    /**
     * @notice Staking token allocation function
     * @param amount Amount of tokens to allocate for staking
     */
    function allocateStakingTokens(uint256 amount) external {
        require(isStakingAllocator[msg.sender], "Only staking allocator can allocate tokens");
        require(amount <= stakingAllocationAmount, "Allocation amount exceeds available tokens");
        stakingAllocationAmount = stakingAllocationAmount.sub(amount);
        _mint(msg.sender, amount);
    }

    /**
     * @notice Community rewards token allocation function
     * @param amount Amount of tokens to allocate for community rewards
     */
    function allocateCommunityRewardsTokens(uint256 amount) external {
        require(isCommunityRewardsAllocator[msg.sender], "Only community rewards allocator can allocate tokens");
        require(amount <= communityRewardsAllocationAmount, "Allocation amount exceeds available tokens");
        communityRewardsAllocationAmount = communityRewardsAllocationAmount.sub(amount);
        _mint(msg.sender, amount);
    }

    /**
     * @notice Liquidity token allocation function
     * @param amount Amount of tokens to allocate for liquidity
     */
    function allocateLiquidityTokens(uint256 amount) external {
        require(isLiquidityAllocator[msg.sender], "Only liquidity allocator can allocate tokens");
        require(amount <= liquidityAllocationAmount, "Allocation amount exceeds available tokens");
        liquidityAllocationAmount = liquidityAllocationAmount.sub(amount);
        _mint(msg.sender, amount);
    }

    /**
     * @notice Marketing token allocation function
     * @param amount Amount of tokens to allocate for marketing
     */
    function allocateMarketingTokens(uint256 amount) external {
        require(isMarketingAllocator[msg.sender], "Only marketing allocator can allocate tokens");
        require(amount <= marketingAllocationAmount, "Allocation amount exceeds available tokens");
        marketingAllocationAmount = marketingAllocationAmount.sub(amount);
        _mint(msg.sender, amount);
    }
}
```
