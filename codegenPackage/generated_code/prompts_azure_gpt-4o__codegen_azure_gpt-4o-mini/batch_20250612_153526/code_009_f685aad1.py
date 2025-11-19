"""
Generated Code Metadata:
========================
Original URL: https://doge20-claimyourdoge20.pages.dev
Prompt: Write a Solidity contract to implement fixed tokenomics for DOGE20, ensuring no inflation and proper allocation of tokens for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_f685aad1f8e6e0c2
Batch ID: 20250612_153526
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

/**
 * @title DOGE20 Token
 * @dev Implementation of a fixed supply ERC20 token with defined tokenomics.
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant TREASURY_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 25; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 30; // 30%

    // Allocated amounts
    uint256 public presaleTokens;
    uint256 public marketingTokens;
    uint256 public treasuryTokens;
    uint256 public stakingRewardsTokens;
    uint256 public liquidityTokens;

    // Events
    event TokensAllocated(address indexed to, uint256 amount);

    /**
     * @dev Constructor that initializes the token and allocates tokens according to the defined tokenomics.
     */
    constructor() ERC20("DOGE20", "DOGE20") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Calculate allocations
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        marketingTokens = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        treasuryTokens = (TOTAL_SUPPLY * TREASURY_ALLOCATION) / 100;
        stakingRewardsTokens = (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 100;
        liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;

        // Emit allocation events
        emit TokensAllocated(msg.sender, presaleTokens);
        emit TokensAllocated(msg.sender, marketingTokens);
        emit TokensAllocated(msg.sender, treasuryTokens);
        emit TokensAllocated(msg.sender, stakingRewardsTokens);
        emit TokensAllocated(msg.sender, liquidityTokens);
    }

    /**
     * @dev Function to withdraw tokens from the contract for presale, marketing, treasury, staking rewards, and liquidity.
     * @param to The address to which the tokens will be sent.
     * @param amount The amount of tokens to withdraw.
     * @param allocationType The type of allocation (1: presale, 2: marketing, 3: treasury, 4: staking rewards, 5: liquidity).
     */
    function withdrawTokens(address to, uint256 amount, uint8 allocationType) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        if (allocationType == 1) {
            require(amount <= presaleTokens, "Insufficient presale tokens");
            presaleTokens -= amount;
        } else if (allocationType == 2) {
            require(amount <= marketingTokens, "Insufficient marketing tokens");
            marketingTokens -= amount;
        } else if (allocationType == 3) {
            require(amount <= treasuryTokens, "Insufficient treasury tokens");
            treasuryTokens -= amount;
        } else if (allocationType == 4) {
            require(amount <= stakingRewardsTokens, "Insufficient staking rewards tokens");
            stakingRewardsTokens -= amount;
        } else if (allocationType == 5) {
            require(amount <= liquidityTokens, "Insufficient liquidity tokens");
            liquidityTokens -= amount;
        } else {
            revert("Invalid allocation type");
        }

        // Transfer tokens to the specified address
        _transfer(owner(), to, amount);
    }

    /**
     * @dev Function to get the remaining tokens for a specific allocation type.
     * @param allocationType The type of allocation (1: presale, 2: marketing, 3: treasury, 4: staking rewards, 5: liquidity).
     * @return The remaining tokens for the specified allocation type.
     */
    function getRemainingTokens(uint8 allocationType) external view returns (uint256) {
        if (allocationType == 1) {
            return presaleTokens;
        } else if (allocationType == 2) {
            return marketingTokens;
        } else if (allocationType == 3) {
            return treasuryTokens;
        } else if (allocationType == 4) {
            return stakingRewardsTokens;
        } else if (allocationType == 5) {
            return liquidityTokens;
        } else {
            revert("Invalid allocation type");
        }
    }
}
```
