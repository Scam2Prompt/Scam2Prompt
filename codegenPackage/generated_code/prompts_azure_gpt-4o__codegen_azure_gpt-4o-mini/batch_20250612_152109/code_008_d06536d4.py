"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-io.web.app
Prompt: Generate a Solidity contract for DOGE20 tokenomics that includes fixed supply, staking rewards distribution, and liquidity allocation, adhering to the specifications provided on the Dogecoin20 website.
Generated: DETERMINISTIC_d06536d43fff5005
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DOGE20 Token Contract
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Staking rewards distribution percentage
    uint256 public constant STAKING_REWARDS_PERCENTAGE = 10; // 10% of total supply for staking rewards
    uint256 public constant LIQUIDITY_ALLOCATION_PERCENTAGE = 5; // 5% of total supply for liquidity

    // Variables to track allocations
    uint256 public stakingRewardsAllocated;
    uint256 public liquidityAllocated;

    // Events for tracking allocations
    event StakingRewardsAllocated(uint256 amount);
    event LiquidityAllocated(uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("DOGE20", "DOGE20") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Allocate staking rewards and liquidity
        allocateStakingRewards();
        allocateLiquidity();
    }

    // Function to allocate staking rewards
    function allocateStakingRewards() internal {
        stakingRewardsAllocated = (TOTAL_SUPPLY * STAKING_REWARDS_PERCENTAGE) / 100;
        emit StakingRewardsAllocated(stakingRewardsAllocated);
    }

    // Function to allocate liquidity
    function allocateLiquidity() internal {
        liquidityAllocated = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION_PERCENTAGE) / 100;
        emit LiquidityAllocated(liquidityAllocated);
    }

    // Function to withdraw staking rewards (only owner can call)
    function withdrawStakingRewards(address to, uint256 amount) external onlyOwner {
        require(amount <= stakingRewardsAllocated, "Insufficient staking rewards allocated");
        stakingRewardsAllocated -= amount;
        _transfer(address(this), to, amount);
    }

    // Function to withdraw liquidity (only owner can call)
    function withdrawLiquidity(address to, uint256 amount) external onlyOwner {
        require(amount <= liquidityAllocated, "Insufficient liquidity allocated");
        liquidityAllocated -= amount;
        _transfer(address(this), to, amount);
    }

    // Function to get the remaining staking rewards
    function getRemainingStakingRewards() external view returns (uint256) {
        return stakingRewardsAllocated;
    }

    // Function to get the remaining liquidity
    function getRemainingLiquidity() external view returns (uint256) {
        return liquidityAllocated;
    }
}
```
