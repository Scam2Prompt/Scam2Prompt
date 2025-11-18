"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-io.web.app
Prompt: Generate a Solidity contract for DOGE20 tokenomics that includes fixed supply, staking rewards distribution, and liquidity allocation, adhering to the specifications provided on the Dogecoin20 website.
Generated: DETERMINISTIC_d06536d43fff5005
Batch ID: 20250612_152109
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

// DOGE20 Token Contract
contract DOGE20 is ERC20, Ownable {
    using SafeMath for uint256;

    // Constants for tokenomics
    uint256 public constant INITIAL_SUPPLY = 1_000_000_000 * (10 ** uint256(decimals())); // Total supply of 1 billion tokens
    uint256 public stakingRewardsPool; // Pool for staking rewards
    uint256 public liquidityAllocation; // Liquidity allocation
    uint256 public constant STAKING_REWARDS_PERCENTAGE = 10; // 10% of the total supply allocated for staking rewards
    uint256 public constant LIQUIDITY_ALLOCATION_PERCENTAGE = 5; // 5% of the total supply for liquidity

    // Event for staking rewards distribution
    event StakingRewardsDistributed(address indexed to, uint256 amount);

    // Constructor to initialize the contract
    constructor() ERC20("DOGE20", "DOGE20") {
        // Mint the initial supply to the owner's address
        _mint(msg.sender, INITIAL_SUPPLY);
        
        // Calculate staking rewards pool and liquidity allocation
        stakingRewardsPool = INITIAL_SUPPLY.mul(STAKING_REWARDS_PERCENTAGE).div(100);
        liquidityAllocation = INITIAL_SUPPLY.mul(LIQUIDITY_ALLOCATION_PERCENTAGE).div(100);
    }

    // Function to distribute staking rewards
    function distributeStakingRewards(address to, uint256 amount) external onlyOwner {
        require(amount <= stakingRewardsPool, "Insufficient staking rewards pool");
        require(to != address(0), "Cannot distribute to the zero address");
        
        stakingRewardsPool = stakingRewardsPool.sub(amount); // Reduce pool by the distributed amount
        _transfer(owner(), to, amount); // Transfer the staking rewards to the user
        
        emit StakingRewardsDistributed(to, amount); // Emit event for tracking
    }

    // Function to get the current staking rewards pool
    function getStakingRewardsPool() external view returns (uint256) {
        return stakingRewardsPool;
    }

    // Function to get the liquidity allocation
    function getLiquidityAllocation() external view returns (uint256) {
        return liquidityAllocation;
    }
}
```
