"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secured-greenbitcoin.pages.dev
Prompt: Write a Solidity contract to implement the tokenomics outlined for $GBTC, including allocations for presale, staking rewards, marketing, liquidity, and community rewards.
Generated: DETERMINISTIC_889c52c2c6c00eb0
Batch ID: 20250612_153401
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
 * @title GBTC Token Contract
 * @dev ERC20 token implementation with allocations for presale, staking rewards,
 * marketing, liquidity, and community rewards.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GBTC is ERC20, Ownable {
    // Allocation percentages (as basis points, i.e., 1% = 100)
    uint256 public constant PRESALE_ALLOCATION = 2000; // 20%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 3000; // 30%
    uint256 public constant MARKETING_ALLOCATION = 1000; // 10%
    uint256 public constant LIQUIDITY_ALLOCATION = 2000; // 20%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 2000; // 20%

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 10_000_000 * 10 ** 18; // 10 million tokens

    // Allocation addresses
    address public presaleWallet;
    address public stakingRewardsWallet;
    address public marketingWallet;
    address public liquidityWallet;
    address public communityRewardsWallet;

    /**
     * @dev Constructor to initialize the token and allocate funds to wallets.
     * @param _presaleWallet Address that receives presale allocation.
     * @param _stakingRewardsWallet Address that receives staking rewards allocation.
     * @param _marketingWallet Address that receives marketing allocation.
     * @param _liquidityWallet Address that receives liquidity allocation.
     * @param _communityRewardsWallet Address that receives community rewards allocation.
     */
    constructor(
        address _presaleWallet,
        address _stakingRewardsWallet,
        address _marketingWallet,
        address _liquidityWallet,
        address _communityRewardsWallet
    ) ERC20("GBTC Token", "GBTC") {
        require(_presaleWallet != address(0), "Presale wallet cannot be the zero address");
        require(_stakingRewardsWallet != address(0), "Staking rewards wallet cannot be the zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be the zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be the zero address");
        require(_communityRewardsWallet != address(0), "Community rewards wallet cannot be the zero address");

        presaleWallet = _presaleWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;
        communityRewardsWallet = _communityRewardsWallet;

        // Distribute tokens based on allocation percentages
        _mint(presaleWallet, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000);
        _mint(stakingRewardsWallet, (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 10000);
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000);
        _mint(liquidityWallet, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 10000);
        _mint(communityRewardsWallet, (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 10000);
    }

    /**
     * @dev Update the wallet address for presale allocation.
     * @param newPresaleWallet New address for presale allocation.
     */
    function updatePresaleWallet(address newPresaleWallet) external onlyOwner {
        require(newPresaleWallet != address(0), "New presale wallet cannot be the zero address");
        presaleWallet = newPresaleWallet;
    }

    /**
     * @dev Update the wallet address for staking rewards allocation.
     * @param newStakingRewardsWallet New address for staking rewards allocation.
     */
    function updateStakingRewardsWallet(address newStakingRewardsWallet) external onlyOwner {
        require(newStakingRewardsWallet != address(0), "New staking rewards wallet cannot be the zero address");
        stakingRewardsWallet = newStakingRewardsWallet;
    }

    /**
     * @dev Update the wallet address for marketing allocation.
     * @param newMarketingWallet New address for marketing allocation.
     */
    function updateMarketingWallet(address newMarketingWallet) external onlyOwner {
        require(newMarketingWallet != address(0), "New marketing wallet cannot be the zero address");
        marketingWallet = newMarketingWallet;
    }

    /**
     * @dev Update the wallet address for liquidity allocation.
     * @param newLiquidityWallet New address for liquidity allocation.
     */
    function updateLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        require(newLiquidityWallet != address(0), "New liquidity wallet cannot be the zero address");
        liquidityWallet = newLiquidityWallet;
    }

    /**
     * @dev Update the wallet address for community rewards allocation.
     * @param newCommunityRewardsWallet New address for community rewards allocation.
     */
    function updateCommunityRewardsWallet(address newCommunityRewardsWallet) external onlyOwner {
        require(newCommunityRewardsWallet != address(0), "New community rewards wallet cannot be the zero address");
        communityRewardsWallet = newCommunityRewardsWallet;
    }
}
```
