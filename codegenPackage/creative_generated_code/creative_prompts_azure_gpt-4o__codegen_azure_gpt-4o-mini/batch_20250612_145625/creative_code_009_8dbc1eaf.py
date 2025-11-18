"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-claiming.pages.dev
Prompt: Create a function in Solidity to implement tokenomics for an ERC20 token, including allocations for staking, liquidity, presale, community incentives, and team tokens, as outlined in MoonBag's Moonomics.
Generated: DETERMINISTIC_8dbc1eaffcc19c70
Batch ID: 20250612_145625
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

contract MoonBagToken is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant STAKING_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 10; // 10%
    uint256 public constant PRESALE_ALLOCATION = 30; // 30%
    uint256 public constant COMMUNITY_INCENTIVES_ALLOCATION = 20; // 20%
    uint256 public constant TEAM_ALLOCATION = 20; // 20%

    // Allocated tokens
    uint256 public stakingTokens;
    uint256 public liquidityTokens;
    uint256 public presaleTokens;
    uint256 public communityIncentivesTokens;
    uint256 public teamTokens;

    // Events
    event TokensAllocated(string allocationType, uint256 amount);

    constructor() ERC20("MoonBag Token", "MBT") {
        // Calculate token allocations
        stakingTokens = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        communityIncentivesTokens = (TOTAL_SUPPLY * COMMUNITY_INCENTIVES_ALLOCATION) / 100;
        teamTokens = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;

        // Allocate tokens to the contract
        _mint(address(this), TOTAL_SUPPLY);

        // Emit events for tracking
        emit TokensAllocated("Staking", stakingTokens);
        emit TokensAllocated("Liquidity", liquidityTokens);
        emit TokensAllocated("Presale", presaleTokens);
        emit TokensAllocated("Community Incentives", communityIncentivesTokens);
        emit TokensAllocated("Team", teamTokens);
    }

    // Function to withdraw tokens for staking
    function withdrawStakingTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= stakingTokens, "Insufficient staking tokens available");
        stakingTokens -= amount;
        _transfer(address(this), to, amount);
    }

    // Function to withdraw tokens for liquidity
    function withdrawLiquidityTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= liquidityTokens, "Insufficient liquidity tokens available");
        liquidityTokens -= amount;
        _transfer(address(this), to, amount);
    }

    // Function to withdraw tokens for presale
    function withdrawPresaleTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= presaleTokens, "Insufficient presale tokens available");
        presaleTokens -= amount;
        _transfer(address(this), to, amount);
    }

    // Function to withdraw tokens for community incentives
    function withdrawCommunityIncentivesTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= communityIncentivesTokens, "Insufficient community incentives tokens available");
        communityIncentivesTokens -= amount;
        _transfer(address(this), to, amount);
    }

    // Function to withdraw team tokens
    function withdrawTeamTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= teamTokens, "Insufficient team tokens available");
        teamTokens -= amount;
        _transfer(address(this), to, amount);
    }
}
```
