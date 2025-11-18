"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-a.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics, ensuring fixed supply allocation: 25% presale, 25% marketing, 25% treasury, 15% staking rewards, and 10% liquidity.
Generated: DETERMINISTIC_19ca8108ad663341
Batch ID: 20250612_152109
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
 * @title DOGE20 Tokenomics Contract
 * @dev Implements a fixed-supply ERC20 token with specific allocations for presale, marketing, treasury, staking rewards, and liquidity.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DOGE20Token is ERC20, Ownable {
    // Total Fixed Supply: 1,000,000 tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18;

    // Allocations (Percentage-based)
    uint256 public constant PRESALE_ALLOCATION = TOTAL_SUPPLY * 25 / 100; // 25%
    uint256 public constant MARKETING_ALLOCATION = TOTAL_SUPPLY * 25 / 100; // 25%
    uint256 public constant TREASURY_ALLOCATION = TOTAL_SUPPLY * 25 / 100; // 25%
    uint256 public constant STAKING_ALLOCATION = TOTAL_SUPPLY * 15 / 100; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = TOTAL_SUPPLY * 10 / 100; // 10%

    // Allocation Addresses
    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingRewardsWallet;
    address public liquidityWallet;

    /**
     * @dev Constructor initializes the ERC20 token and allocates tokens to specific wallets.
     */
    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) ERC20("DOGE20 Token", "DOGE20") {
        require(
            _presaleWallet != address(0) &&
            _marketingWallet != address(0) &&
            _treasuryWallet != address(0) &&
            _stakingRewardsWallet != address(0) &&
            _liquidityWallet != address(0),
            "Wallet addresses cannot be zero."
        );

        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Mint tokens to respective wallets based on allocations
        _mint(presaleWallet, PRESALE_ALLOCATION);
        _mint(marketingWallet, MARKETING_ALLOCATION);
        _mint(treasuryWallet, TREASURY_ALLOCATION);
        _mint(stakingRewardsWallet, STAKING_ALLOCATION);
        _mint(liquidityWallet, LIQUIDITY_ALLOCATION);
    }

    /**
     * @dev Override for the decimals function to use 18 decimal places.
     */
    function decimals() public pure override returns (uint8) {
        return 18;
    }

    /**
     * @dev Prevent ownership renunciation, ensuring contract control.
     */
    function renounceOwnership() public override onlyOwner {
        revert("Ownership cannot be renounced.");
    }
}
```
