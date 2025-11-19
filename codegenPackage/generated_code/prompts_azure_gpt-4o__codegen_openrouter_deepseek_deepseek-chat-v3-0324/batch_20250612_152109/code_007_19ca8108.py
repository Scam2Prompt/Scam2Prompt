"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-a.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics, ensuring fixed supply allocation: 25% presale, 25% marketing, 25% treasury, 15% staking rewards, and 10% liquidity.
Generated: DETERMINISTIC_19ca8108ad663341
Batch ID: 20250612_152109
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
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 private constant PRESALE_ALLOCATION = 25_00; // 25% (using basis points)
    uint256 private constant MARKETING_ALLOCATION = 25_00; // 25%
    uint256 private constant TREASURY_ALLOCATION = 25_00; // 25%
    uint256 private constant STAKING_ALLOCATION = 15_00; // 15%
    uint256 private constant LIQUIDITY_ALLOCATION = 10_00; // 10%
    
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

        _mint(presaleWallet, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100_00);
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100_00);
        _mint(treasuryWallet, (TOTAL_SUPPLY * TREASURY_ALLOCATION) / 100_00);
        _mint(stakingWallet, (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100_00);
        _mint(liquidityWallet, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100_00);
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
