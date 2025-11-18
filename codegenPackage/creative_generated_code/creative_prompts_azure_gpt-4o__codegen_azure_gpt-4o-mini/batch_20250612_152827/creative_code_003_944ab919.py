"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub-en.pages.dev
Prompt: Create a smart contract in Solidity to manage the tokenomics of $0DOG, including the 90% token distribution and automatic removal of unsold tokens after 30 days.
Generated: DETERMINISTIC_944ab91939db00a3
Batch ID: 20250612_152827
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
 * @title 0DOG Token Contract
 * @dev A token contract for $0DOG that manages tokenomics,
 * including distribution and automatic removal of unsold tokens.
 */
contract DogToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 ether;  // 1 million tokens

    // Distribution percentages
    uint256 public constant TEAM_ALLOCATION = 10; // 10% for team
    uint256 public constant LIQUIDITY_ALLOCATION = 30; // 30% for liquidity
    uint256 public constant MARKETING_ALLOCATION = 20; // 20% for marketing
    uint256 public constant COMMUNITY_ALLOCATION = 30; // 30% for community incentives

    // Allocation amounts
    uint256 public teamTokens;
    uint256 public liquidityTokens;
    uint256 public marketingTokens;
    uint256 public communityTokens;

    // Timestamp for unsold token removal
    uint256 public unsoldTokenRemovalTimestamp;

    // Event for token distribution
    event TokensDistributed(uint256 team, uint256 liquidity, uint256 marketing, uint256 community);

    // Constructor to set up the token and its allocations
    constructor() ERC20("0DOG", "0DOG") {
        // Calculate token allocations
        teamTokens = TOTAL_SUPPLY.mul(TEAM_ALLOCATION).div(100);
        liquidityTokens = TOTAL_SUPPLY.mul(LIQUIDITY_ALLOCATION).div(100);
        marketingTokens = TOTAL_SUPPLY.mul(MARKETING_ALLOCATION).div(100);
        communityTokens = TOTAL_SUPPLY.mul(COMMUNITY_ALLOCATION).div(100);

        // Mint total tokens to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Set the timestamp for unsold token removal (30 days from deployment)
        unsoldTokenRemovalTimestamp = block.timestamp + 30 days;

        emit TokensDistributed(teamTokens, liquidityTokens, marketingTokens, communityTokens);
    }

    /**
     * @dev Function to burn unsold tokens after 30 days.
     * Can only be called by the owner of the contract.
     */
    function burnUnsoldTokens() external onlyOwner {
        require(block.timestamp >= unsoldTokenRemovalTimestamp, "Tokens can only be burned after 30 days");
        
        uint256 unsoldTokens = balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to burn");

        _burn(address(this), unsoldTokens);
    }

    /**
     * @dev Function to withdraw tokens allocated to the team.
     * Can only be called by the owner.
     */
    function withdrawTeamTokens() external onlyOwner {
        require(teamTokens > 0, "No team tokens remaining");
        uint256 amount = teamTokens;
        teamTokens = 0; // Prevent re-entrancy
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Function to withdraw liquidity tokens.
     * Can only be called by the owner.
     */
    function withdrawLiquidityTokens() external onlyOwner {
        require(liquidityTokens > 0, "No liquidity tokens remaining");
        uint256 amount = liquidityTokens;
        liquidityTokens = 0; // Prevent re-entrancy
        _transfer(address(this), msg.sender, amount);
    }

    // Additional functions for marketing and community token withdrawals can be added here...
}
```
