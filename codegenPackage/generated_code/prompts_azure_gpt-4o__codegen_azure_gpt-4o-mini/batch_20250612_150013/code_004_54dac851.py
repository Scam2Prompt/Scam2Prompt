"""
Generated Code Metadata:
========================
Original URL: https://popofrogs.pages.dev
Prompt: Write a Solidity contract for a fixed total supply token like $FROP, with allocations for presale, staking, marketing, rewards, and liquidity as outlined in the tokenomics section.
Generated: DETERMINISTIC_54dac851669b0c01
Batch ID: 20250612_150013
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// FROP Token Contract
contract FROPToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_ALLOCATION = 25; // 25%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 30; // 30%

    // Mappings to track allocations
    mapping(address => uint256) public presaleWallets;
    mapping(address => uint256) public stakingWallets;
    mapping(address => uint256) public marketingWallets;
    mapping(address => uint256) public rewardsWallets;
    mapping(address => uint256) public liquidityWallets;

    // Events for tracking allocations
    event TokensAllocated(address indexed to, uint256 amount, string allocationType);

    // Constructor to mint the total supply to the contract owner
    constructor() ERC20("FROP Token", "FROP") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to allocate tokens for presale
    function allocatePresale(address to, uint256 amount) external onlyOwner {
        require(amount <= (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100, "Exceeds presale allocation");
        presaleWallets[to] += amount;
        emit TokensAllocated(to, amount, "Presale");
    }

    // Function to allocate tokens for staking
    function allocateStaking(address to, uint256 amount) external onlyOwner {
        require(amount <= (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100, "Exceeds staking allocation");
        stakingWallets[to] += amount;
        emit TokensAllocated(to, amount, "Staking");
    }

    // Function to allocate tokens for marketing
    function allocateMarketing(address to, uint256 amount) external onlyOwner {
        require(amount <= (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100, "Exceeds marketing allocation");
        marketingWallets[to] += amount;
        emit TokensAllocated(to, amount, "Marketing");
    }

    // Function to allocate tokens for rewards
    function allocateRewards(address to, uint256 amount) external onlyOwner {
        require(amount <= (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 100, "Exceeds rewards allocation");
        rewardsWallets[to] += amount;
        emit TokensAllocated(to, amount, "Rewards");
    }

    // Function to allocate tokens for liquidity
    function allocateLiquidity(address to, uint256 amount) external onlyOwner {
        require(amount <= (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100, "Exceeds liquidity allocation");
        liquidityWallets[to] += amount;
        emit TokensAllocated(to, amount, "Liquidity");
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Insufficient balance");
        _transfer(address(this), to, amount);
    }
}
```
