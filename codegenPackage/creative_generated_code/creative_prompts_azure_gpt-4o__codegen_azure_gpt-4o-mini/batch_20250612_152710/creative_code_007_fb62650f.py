"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-ea.pages.dev
Prompt: Provide Solidity code for a fixed-supply ERC-20 token similar to DOGE20, including tokenomics features such as allocating percentages for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_fb62650fad6fa552
Batch ID: 20250612_152710
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
 * @title FixedSupplyToken
 * @dev A fixed supply ERC20 token with specific tokenomics features
 */
contract FixedSupplyToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals();

    // Tokenomics allocations
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20%
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15%
    uint256 public constant TREASURY_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10%
    uint256 public constant STAKING_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * 30) / 100; // 30%

    // Track allocation status
    bool public presaleAllocated = false;
    bool public marketingAllocated = false;
    bool public treasuryAllocated = false;
    bool public stakingRewardsAllocated = false;
    bool public liquidityAllocated = false;

    // Constructor
    constructor() ERC20("FixedSupplyToken", "FST") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Allocate presale tokens to a designated address
     * @param to The address to receive presale tokens
     */
    function allocatePresale(address to) external onlyOwner {
        require(!presaleAllocated, "Presale tokens already allocated");
        require(to != address(0), "Invalid address");

        _transfer(owner(), to, PRESALE_ALLOCATION);
        presaleAllocated = true;
    }

    /**
     * @dev Allocate marketing tokens to a designated address
     * @param to The address to receive marketing tokens
     */
    function allocateMarketing(address to) external onlyOwner {
        require(!marketingAllocated, "Marketing tokens already allocated");
        require(to != address(0), "Invalid address");

        _transfer(owner(), to, MARKETING_ALLOCATION);
        marketingAllocated = true;
    }

    /**
     * @dev Allocate treasury tokens to a designated address
     * @param to The address to receive treasury tokens
     */
    function allocateTreasury(address to) external onlyOwner {
        require(!treasuryAllocated, "Treasury tokens already allocated");
        require(to != address(0), "Invalid address");

        _transfer(owner(), to, TREASURY_ALLOCATION);
        treasuryAllocated = true;
    }

    /**
     * @dev Allocate staking rewards tokens to a designated address
     * @param to The address to receive staking rewards tokens
     */
    function allocateStakingRewards(address to) external onlyOwner {
        require(!stakingRewardsAllocated, "Staking rewards tokens already allocated");
        require(to != address(0), "Invalid address");

        _transfer(owner(), to, STAKING_REWARDS_ALLOCATION);
        stakingRewardsAllocated = true;
    }

    /**
     * @dev Allocate liquidity tokens to a designated address
     * @param to The address to receive liquidity tokens
     */
    function allocateLiquidity(address to) external onlyOwner {
        require(!liquidityAllocated, "Liquidity tokens already allocated");
        require(to != address(0), "Invalid address");

        _transfer(owner(), to, LIQUIDITY_ALLOCATION);
        liquidityAllocated = true;
    }
}
```
