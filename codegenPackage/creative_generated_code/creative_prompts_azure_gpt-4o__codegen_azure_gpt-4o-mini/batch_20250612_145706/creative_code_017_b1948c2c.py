"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Develop a smart contract for a fixed total supply token with allocations for presale, staking, marketing, rewards, and liquidity, based on $FROP’s supply cap of 111,111,111,111 tokens.
Generated: DETERMINISTIC_b1948c2c95934709
Batch ID: 20250612_145706
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

// The FixedSupplyToken contract implements a fixed total supply ERC20 token
contract FixedSupplyToken is ERC20, Ownable {
    // Total supply cap
    uint256 public constant TOTAL_SUPPLY = 111111111111 * 10 ** 18; // 111,111,111,111 tokens with 18 decimals

    // Allocations as per specified percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant STAKING_ALLOCATION = 30; // 30%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant REWARDS_ALLOCATION = 25; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 15; // 15%

    // Allocation tracking
    uint256 public presaleTokens;
    uint256 public stakingTokens;
    uint256 public marketingTokens;
    uint256 public rewardsTokens;
    uint256 public liquidityTokens;

    // Events for tracking allocations
    event TokensAllocated(string allocationType, uint256 amount);

    constructor() ERC20("FixedSupplyToken", "FROP") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Calculate allocations based on total supply
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        stakingTokens = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        marketingTokens = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        rewardsTokens = (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 100;
        liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;

        // Emit allocation events
        emit TokensAllocated("Presale", presaleTokens);
        emit TokensAllocated("Staking", stakingTokens);
        emit TokensAllocated("Marketing", marketingTokens);
        emit TokensAllocated("Rewards", rewardsTokens);
        emit TokensAllocated("Liquidity", liquidityTokens);
    }

    // Function to withdraw tokens from the contract for the presale
    function allocatePresaleTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= presaleTokens, "Amount exceeds presale allocation");
        presaleTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to withdraw tokens for staking
    function allocateStakingTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= stakingTokens, "Amount exceeds staking allocation");
        stakingTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to withdraw tokens for marketing
    function allocateMarketingTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= marketingTokens, "Amount exceeds marketing allocation");
        marketingTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to withdraw tokens for rewards
    function allocateRewardsTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= rewardsTokens, "Amount exceeds rewards allocation");
        rewardsTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to withdraw tokens for liquidity
    function allocateLiquidityTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= liquidityTokens, "Amount exceeds liquidity allocation");
        liquidityTokens -= amount;
        _transfer(owner(), to, amount);
    }

    // Function to get the remaining allocation for presale
    function getRemainingPresaleAllocation() external view returns (uint256) {
        return presaleTokens;
    }

    // Function to get the remaining allocation for staking
    function getRemainingStakingAllocation() external view returns (uint256) {
        return stakingTokens;
    }

    // Function to get the remaining allocation for marketing
    function getRemainingMarketingAllocation() external view returns (uint256) {
        return marketingTokens;
    }

    // Function to get the remaining allocation for rewards
    function getRemainingRewardsAllocation() external view returns (uint256) {
        return rewardsTokens;
    }

    // Function to get the remaining allocation for liquidity
    function getRemainingLiquidityAllocation() external view returns (uint256) {
        return liquidityTokens;
    }
}
```
