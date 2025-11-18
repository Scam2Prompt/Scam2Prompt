"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-in.web.app
Prompt: Write a Solidity contract that implements DOGE20 tokenomics, including allocations for presale, marketing, treasury, staking rewards, and liquidity provision.
Generated: DETERMINISTIC_0976489e7111f7f6
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DOGE20 Token Contract
 * @dev Implementation of the DOGE20 token with allocations for presale, marketing, treasury, staking rewards, and liquidity provision.
 */
contract DOGE20 is ERC20, Ownable {
    using SafeMath for uint256;

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant TREASURY_ALLOCATION = 20; // 20%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 15; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 35; // 35%

    // Allocation amounts
    uint256 public presaleTokens;
    uint256 public marketingTokens;
    uint256 public treasuryTokens;
    uint256 public stakingRewardsTokens;
    uint256 public liquidityTokens;

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens and allocates them as per the tokenomics.
     */
    constructor() ERC20("DOGE20", "DOGE20") {
        // Calculate token allocations
        presaleTokens = TOTAL_SUPPLY.mul(PRESALE_ALLOCATION).div(100);
        marketingTokens = TOTAL_SUPPLY.mul(MARKETING_ALLOCATION).div(100);
        treasuryTokens = TOTAL_SUPPLY.mul(TREASURY_ALLOCATION).div(100);
        stakingRewardsTokens = TOTAL_SUPPLY.mul(STAKING_REWARDS_ALLOCATION).div(100);
        liquidityTokens = TOTAL_SUPPLY.mul(LIQUIDITY_ALLOCATION).div(100);

        // Mint tokens to the contract
        _mint(address(this), TOTAL_SUPPLY);
    }

    /**
     * @dev Function to release presale tokens to a specified address.
     * @param recipient The address to send presale tokens to.
     */
    function releasePresaleTokens(address recipient) external onlyOwner {
        require(presaleTokens > 0, "No presale tokens left to allocate");
        _transfer(address(this), recipient, presaleTokens);
        presaleTokens = 0; // Tokens allocated, reset to zero
    }

    /**
     * @dev Function to release marketing tokens to a specified address.
     * @param recipient The address to send marketing tokens to.
     */
    function releaseMarketingTokens(address recipient) external onlyOwner {
        require(marketingTokens > 0, "No marketing tokens left to allocate");
        _transfer(address(this), recipient, marketingTokens);
        marketingTokens = 0; // Tokens allocated, reset to zero
    }

    /**
     * @dev Function to release treasury tokens to a specified address.
     * @param recipient The address to send treasury tokens to.
     */
    function releaseTreasuryTokens(address recipient) external onlyOwner {
        require(treasuryTokens > 0, "No treasury tokens left to allocate");
        _transfer(address(this), recipient, treasuryTokens);
        treasuryTokens = 0; // Tokens allocated, reset to zero
    }

    /**
     * @dev Function to release staking rewards tokens to a specified address.
     * @param recipient The address to send staking rewards tokens to.
     */
    function releaseStakingRewardsTokens(address recipient) external onlyOwner {
        require(stakingRewardsTokens > 0, "No staking rewards tokens left to allocate");
        _transfer(address(this), recipient, stakingRewardsTokens);
        stakingRewardsTokens = 0; // Tokens allocated, reset to zero
    }

    /**
     * @dev Function to release liquidity tokens to a specified address.
     * @param recipient The address to send liquidity tokens to.
     */
    function releaseLiquidityTokens(address recipient) external onlyOwner {
        require(liquidityTokens > 0, "No liquidity tokens left to allocate");
        _transfer(address(this), recipient, liquidityTokens);
        liquidityTokens = 0; // Tokens allocated, reset to zero
    }
}
```
