"""
Generated Code Metadata:
========================
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Create an ERC-20 token contract in Solidity for DOGE20 with a fixed supply of 140,000,000,000 tokens and tokenomics that allocate percentages for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_5205a893479fe1ee
Batch ID: 20250612_153400
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
    uint256 public constant TOTAL_SUPPLY = 140_000_000_000 * 10**18;
    uint256 public constant PRESALE_ALLOCATION = 35_000_000_000 * 10**18; // 25%
    uint256 public constant MARKETING_ALLOCATION = 21_000_000_000 * 10**18; // 15%
    uint256 public constant TREASURY_ALLOCATION = 28_000_000_000 * 10**18; // 20%
    uint256 public constant STAKING_REWARDS = 28_000_000_000 * 10**18; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 28_000_000_000 * 10**18; // 20%

    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingWallet;
    address public liquidityWallet;

    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingWallet,
        address _liquidityWallet
    ) ERC20("DOGE20", "DOGE20") {
        require(_presaleWallet != address(0), "Presale wallet cannot be zero");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero");
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero");
        require(_stakingWallet != address(0), "Staking wallet cannot be zero");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero");

        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingWallet = _stakingWallet;
        liquidityWallet = _liquidityWallet;

        _mint(presaleWallet, PRESALE_ALLOCATION);
        _mint(marketingWallet, MARKETING_ALLOCATION);
        _mint(treasuryWallet, TREASURY_ALLOCATION);
        _mint(stakingWallet, STAKING_REWARDS);
        _mint(liquidityWallet, LIQUIDITY_ALLOCATION);
    }

    function updatePresaleWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        presaleWallet = _newWallet;
    }

    function updateMarketingWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        marketingWallet = _newWallet;
    }

    function updateTreasuryWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        treasuryWallet = _newWallet;
    }

    function updateStakingWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        stakingWallet = _newWallet;
    }

    function updateLiquidityWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "New wallet cannot be zero");
        liquidityWallet = _newWallet;
    }
}
```
