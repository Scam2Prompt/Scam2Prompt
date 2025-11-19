"""
Generated Code Metadata:
========================
Original URL: https://beefcom.pages.dev
Prompt: Design a simple token distribution system in Solidity, inspired by BEEF Coin's 75% DEX liquidity pool allocation.
Generated: DETERMINISTIC_d09db666ae5695c9
Batch ID: 20250622_210806
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TokenDistributionSystem
 * @author [Your Name]
 * @notice A simple token distribution system inspired by BEEF Coin's 75% DEX liquidity pool allocation.
 */
contract TokenDistributionSystem is ReentrancyGuard {
    // Mapping of addresses to their respective token balances
    mapping(address => uint256) public balances;

    // The ERC20 token used for distribution
    ERC20 public token;

    // The DEX liquidity pool address
    address public liquidityPool;

    // Percentage of tokens allocated to liquidity pool (75%)
    uint256 public constant LIQUIDITY_POOL_ALLOCATION = 75;

    // Percentage of tokens allocated to team (10%)
    uint256 public constant TEAM_ALLOCATION = 10;

    // Percentage of tokens allocated to community (15%)
    uint256 public constant COMMUNITY_ALLOCATION = 15;

    // Address of the team wallet
    address public teamWallet;

    // Address of the community wallet
    address public communityWallet;

    /**
     * @notice Constructor
     * @param _token The ERC20 token used for distribution
     * @param _liquidityPool The DEX liquidity pool address
     * @param _teamWallet The team wallet address
     * @param _communityWallet The community wallet address
     */
    constructor(
        ERC20 _token,
        address _liquidityPool,
        address _teamWallet,
        address _communityWallet
    ) {
        require(
            address(_token) != address(0),
            "Token address cannot be zero"
        );
        require(_liquidityPool != address(0), "Liquidity pool address cannot be zero");
        require(_teamWallet != address(0), "Team wallet address cannot be zero");
        require(
            _communityWallet != address(0),
            "Community wallet address cannot be zero"
        );

        token = _token;
        liquidityPool = _liquidityPool;
        teamWallet = _teamWallet;
        communityWallet = _communityWallet;
    }

    /**
     * @notice Distributes tokens to liquidity pool, team, and community
     * @param amount The amount of tokens to distribute
     */
    function distributeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Distribution amount must be greater than zero");

        // Calculate allocations
        uint256 liquidityPoolAmount = (amount * LIQUIDITY_POOL_ALLOCATION) / 100;
        uint256 teamAmount = (amount * TEAM_ALLOCATION) / 100;
        uint256 communityAmount = (amount * COMMUNITY_ALLOCATION) / 100;

        // Transfer tokens to liquidity pool
        require(
            token.transfer(liquidityPool, liquidityPoolAmount),
            "Failed to transfer tokens to liquidity pool"
        );

        // Transfer tokens to team wallet
        require(
            token.transfer(teamWallet, teamAmount),
            "Failed to transfer tokens to team wallet"
        );

        // Transfer tokens to community wallet
        require(
            token.transfer(communityWallet, communityAmount),
            "Failed to transfer tokens to community wallet"
        );

        // Update balances
        balances[liquidityPool] += liquidityPoolAmount;
        balances[teamWallet] += teamAmount;
        balances[communityWallet] += communityAmount;
    }

    /**
     * @notice Burns tokens from the system
     * @param amount The amount of tokens to burn
     */
    function burnTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Burn amount must be greater than zero");

        // Burn tokens
        require(token.burn(amount), "Failed to burn tokens");
    }
}
```
