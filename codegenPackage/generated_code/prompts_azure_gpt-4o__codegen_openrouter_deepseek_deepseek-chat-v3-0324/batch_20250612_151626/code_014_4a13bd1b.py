"""
Generated Code Metadata:
========================
Original URL: https://dogee1.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics that enforces the fixed supply and allocates tokens according to the presale, marketing, treasury, staking rewards, and liquidity provisions.
Generated: DETERMINISTIC_4a13bd1b8a82710d
Batch ID: 20250612_151626
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract DOGE20 is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 100_000_000_000 * 10**18; // 100 billion tokens
    uint256 public constant PRESALE_ALLOCATION = 30_000_000_000 * 10**18; // 30%
    uint256 public constant MARKETING_ALLOCATION = 10_000_000_000 * 10**18; // 10%
    uint256 public constant TREASURY_ALLOCATION = 20_000_000_000 * 10**18; // 20%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 20_000_000_000 * 10**18; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 20_000_000_000 * 10**18; // 20%

    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingRewardsWallet;
    address public liquidityWallet;

    bool private _allocated = false;

    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) ERC20("DOGE20", "DOGE20") {
        require(
            _presaleWallet != address(0) &&
            _marketingWallet != address(0) &&
            _treasuryWallet != address(0) &&
            _stakingRewardsWallet != address(0) &&
            _liquidityWallet != address(0),
            "Zero address not allowed"
        );

        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;
    }

    function allocateTokens() external onlyOwner {
        require(!_allocated, "Tokens already allocated");
        require(totalSupply() == 0, "Tokens already minted");

        _mint(presaleWallet, PRESALE_ALLOCATION);
        _mint(marketingWallet, MARKETING_ALLOCATION);
        _mint(treasuryWallet, TREASURY_ALLOCATION);
        _mint(stakingRewardsWallet, STAKING_REWARDS_ALLOCATION);
        _mint(liquidityWallet, LIQUIDITY_ALLOCATION);

        _allocated = true;
    }

    function burn(uint256 amount) external {
        _burn(_msgSender(), amount);
    }

    function updatePresaleWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Zero address not allowed");
        presaleWallet = newWallet;
    }

    function updateMarketingWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Zero address not allowed");
        marketingWallet = newWallet;
    }

    function updateTreasuryWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Zero address not allowed");
        treasuryWallet = newWallet;
    }

    function updateStakingRewardsWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Zero address not allowed");
        stakingRewardsWallet = newWallet;
    }

    function updateLiquidityWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Zero address not allowed");
        liquidityWallet = newWallet;
    }
}
```
