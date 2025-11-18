"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20en.pages.dev
Prompt: Create a Solidity contract for DOGE20 tokenomics that ensures a fixed supply distribution: 25% presale, 25% marketing, 25% treasury, 15% staking rewards, and 10% liquidity.
Generated: DETERMINISTIC_09eff41073bbfe5d
Batch ID: 20250612_152924
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
 * @title DOGE20 Token Contract
 * @dev ERC20 token with fixed supply and pre-defined distribution
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DOGE20 is ERC20, Ownable {
    // Fixed total supply: 1,000,000 tokens (1 million scaled to 10^18 for decimals)
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * (10**18);

    // Distribution percentages
    uint256 public constant PRESALE_PERCENTAGE = 25;
    uint256 public constant MARKETING_PERCENTAGE = 25;
    uint256 public constant TREASURY_PERCENTAGE = 25;
    uint256 public constant STAKING_REWARDS_PERCENTAGE = 15;
    uint256 public constant LIQUIDITY_PERCENTAGE = 10;

    // Distribution addresses
    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingRewardsWallet;
    address public liquidityWallet;

    /**
     * @dev Contract constructor initializes token and performs distribution.
     */
    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) ERC20("DOGE20", "DOGE") {
        require(_presaleWallet != address(0), "Presale wallet cannot be zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(_stakingRewardsWallet != address(0), "Staking rewards wallet cannot be zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");

        // Set wallet addresses
        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Perform token distribution
        _distributeTokens();
    }

    /**
     * @dev Internal function to distribute tokens based on fixed percentages.
     */
    function _distributeTokens() internal {
        // Calculate token allocations
        uint256 presaleTokens = (TOTAL_SUPPLY * PRESALE_PERCENTAGE) / 100;
        uint256 marketingTokens = (TOTAL_SUPPLY * MARKETING_PERCENTAGE) / 100;
        uint256 treasuryTokens = (TOTAL_SUPPLY * TREASURY_PERCENTAGE) / 100;
        uint256 stakingRewardsTokens = (TOTAL_SUPPLY * STAKING_REWARDS_PERCENTAGE) / 100;
        uint256 liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_PERCENTAGE) / 100;

        // Mint tokens to respective wallets
        _mint(presaleWallet, presaleTokens);
        _mint(marketingWallet, marketingTokens);
        _mint(treasuryWallet, treasuryTokens);
        _mint(stakingRewardsWallet, stakingRewardsTokens);
        _mint(liquidityWallet, liquidityTokens);
    }

    /**
     * @dev Allows the owner to update wallet addresses if necessary.
     * Proper checks ensure no address can be set to zero.
     */
    function updateWalletAddresses(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) external onlyOwner {
        require(_presaleWallet != address(0), "Presale wallet cannot be zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(_stakingRewardsWallet != address(0), "Staking rewards wallet cannot be zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");

        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;
    }
}
```
