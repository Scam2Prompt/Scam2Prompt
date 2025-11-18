"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogee1.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics that enforces the fixed supply and allocates tokens according to the presale, marketing, treasury, staking rewards, and liquidity provisions.
Generated: DETERMINISTIC_4a13bd1b8a82710d
Batch ID: 20250612_151626
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
 * @title DOGE20 Token Contract
 * @dev Implements a fixed supply ERC20 token with specific allocations.
 */
contract DOGE20 is ERC20, Ownable {
    // Total token supply set to 1 million tokens (1,000,000 DOGE20)
    uint256 private constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals();

    // Allocation percentages (in basis points, i.e., 10000 = 100%)
    uint256 public constant PRESALE_ALLOCATION = 3000;  // 30%
    uint256 public constant MARKETING_ALLOCATION = 2000; // 20%
    uint256 public constant TREASURY_ALLOCATION = 1500;  // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 2500; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 1000; // 10%

    // Addresses to receive allocated tokens
    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingRewardsWallet;
    address public liquidityWallet;

    /**
     * @dev Constructor that sets up the token and allocates the initial supply.
     * @param _presaleWallet Address to receive presale allocation.
     * @param _marketingWallet Address to receive marketing allocation.
     * @param _treasuryWallet Address to receive treasury allocation.
     * @param _stakingRewardsWallet Address to receive staking rewards allocation.
     * @param _liquidityWallet Address to receive liquidity allocation.
     */
    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) ERC20("DOGE20", "DOGE20") {
        // Set wallet addresses
        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Allocate tokens
        _mint(presaleWallet, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000);
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000);
        _mint(treasuryWallet, (TOTAL_SUPPLY * TREASURY_ALLOCATION) / 10000);
        _mint(stakingRewardsWallet, (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 10000);
        _mint(liquidityWallet, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 10000);
    }

    /**
     * @dev Function to update the presale wallet address.
     * @param newPresaleWallet New address for presale allocation.
     */
    function updatePresaleWallet(address newPresaleWallet) external onlyOwner {
        require(newPresaleWallet != address(0), "Invalid address");
        presaleWallet = newPresaleWallet;
    }

    /**
     * @dev Function to update the marketing wallet address.
     * @param newMarketingWallet New address for marketing allocation.
     */
    function updateMarketingWallet(address newMarketingWallet) external onlyOwner {
        require(newMarketingWallet != address(0), "Invalid address");
        marketingWallet = newMarketingWallet;
    }

    /**
     * @dev Function to update the treasury wallet address.
     * @param newTreasuryWallet New address for treasury allocation.
     */
    function updateTreasuryWallet(address newTreasuryWallet) external onlyOwner {
        require(newTreasuryWallet != address(0), "Invalid address");
        treasuryWallet = newTreasuryWallet;
    }

    /**
     * @dev Function to update the staking rewards wallet address.
     * @param newStakingRewardsWallet New address for staking rewards allocation.
     */
    function updateStakingRewardsWallet(address newStakingRewardsWallet) external onlyOwner {
        require(newStakingRewardsWallet != address(0), "Invalid address");
        stakingRewardsWallet = newStakingRewardsWallet;
    }

    /**
     * @dev Function to update the liquidity wallet address.
     * @param newLiquidityWallet New address for liquidity allocation.
     */
    function updateLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        require(newLiquidityWallet != address(0), "Invalid address");
        liquidityWallet = newLiquidityWallet;
    }
}
```
