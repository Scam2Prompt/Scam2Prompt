"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ie.pages.dev
Prompt: Write a Solidity smart contract to implement tokenomics similar to WienerAI, including allocations for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_20de9232995ed124
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";

/**
 * @title TokenomicsToken
 * @dev Implementation of a standard ERC20 token with specific allocations for tokenomics.
 */
contract TokenomicsToken is ERC20, Ownable, ERC20Burnable {
    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_ALLOCATION = 30; // 30%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 25; // 25%
    uint256 public constant LIQUIDITY_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    // Mappings to track allocations
    mapping(address => uint256) public presaleWallets;
    mapping(address => uint256) public stakingWallets;
    mapping(address => uint256) public communityRewardWallets;
    mapping(address => uint256) public liquidityWallets;
    mapping(address => uint256) public marketingWallets;

    // Events for logging
    event TokensAllocated(address indexed to, uint256 amount);

    constructor() ERC20("TokenomicsToken", "TKT") {
        // Mint total supply to the owner
        _mint(msg.sender, TOTAL_SUPPLY);
        allocateTokens();
    }

    /**
     * @dev Allocates tokens to various wallet addresses based on the defined percentages.
     */
    function allocateTokens() internal onlyOwner {
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 stakingAmount = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        uint256 communityRewardsAmount = (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;

        // Allocate tokens to respective wallets (replace with actual addresses)
        presaleWallets[msg.sender] = presaleAmount; // Presale wallet of the owner for initial distribution
        stakingWallets[msg.sender] = stakingAmount; // Staking wallet of the owner
        communityRewardWallets[msg.sender] = communityRewardsAmount; // Community rewards wallet of the owner
        liquidityWallets[msg.sender] = liquidityAmount; // Liquidity wallet of the owner
        marketingWallets[msg.sender] = marketingAmount; // Marketing wallet of the owner

        emit TokensAllocated(msg.sender, presaleAmount);
        emit TokensAllocated(msg.sender, stakingAmount);
        emit TokensAllocated(msg.sender, communityRewardsAmount);
        emit TokensAllocated(msg.sender, liquidityAmount);
        emit TokensAllocated(msg.sender, marketingAmount);
    }

    /**
     * @dev Allows the owner to transfer tokens to a specified address.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function transferTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(amount <= balanceOf(msg.sender), "Insufficient balance");

        _transfer(msg.sender, recipient, amount);
    }

    /**
     * @dev Burns a specified amount of tokens from the owner's account.
     * @param amount The amount of tokens to be burned.
     */
    function burnTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(msg.sender), "Insufficient balance to burn");
        _burn(msg.sender, amount);
    }
}
```
