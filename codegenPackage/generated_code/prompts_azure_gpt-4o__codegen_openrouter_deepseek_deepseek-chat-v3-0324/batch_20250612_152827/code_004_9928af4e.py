"""
Generated Code Metadata:
========================
Original URL: https://doge-coin20.pages.dev
Prompt: Provide an example of tokenomics implementation in an ERC-20 smart contract, including fixed supply allocation for presale, marketing, staking rewards, and liquidity pools, as outlined for DOGE20.
Generated: DETERMINISTIC_9928af4eb3a60144
Batch ID: 20250612_152827
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

contract DOGE20 is ERC20, Ownable {
    // Token allocation percentages (basis points)
    uint256 public constant PRESALE_ALLOCATION = 3000; // 30%
    uint256 public constant MARKETING_ALLOCATION = 1000; // 10%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 2000; // 20%
    uint256 public constant LIQUIDITY_POOL_ALLOCATION = 4000; // 40%
    
    // Addresses for allocations
    address public presaleAddress;
    address public marketingAddress;
    address public stakingRewardsAddress;
    address public liquidityPoolAddress;
    
    // Total fixed supply
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    
    // Track if allocations have been distributed
    bool private _allocationsDistributed = false;

    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _stakingRewardsAddress,
        address _liquidityPoolAddress
    ) ERC20("DOGE20", "DOGE20") {
        require(
            _presaleAddress != address(0) &&
            _marketingAddress != address(0) &&
            _stakingRewardsAddress != address(0) &&
            _liquidityPoolAddress != address(0),
            "Invalid address"
        );
        
        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityPoolAddress = _liquidityPoolAddress;
        
        _mint(address(this), TOTAL_SUPPLY);
    }

    function distributeAllocations() external onlyOwner {
        require(!_allocationsDistributed, "Allocations already distributed");
        
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000;
        uint256 stakingRewardsAmount = (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 10000;
        uint256 liquidityPoolAmount = (TOTAL_SUPPLY * LIQUIDITY_POOL_ALLOCATION) / 10000;
        
        _transfer(address(this), presaleAddress, presaleAmount);
        _transfer(address(this), marketingAddress, marketingAmount);
        _transfer(address(this), stakingRewardsAddress, stakingRewardsAmount);
        _transfer(address(this), liquidityPoolAddress, liquidityPoolAmount);
        
        _allocationsDistributed = true;
    }

    function updatePresaleAddress(address _newPresaleAddress) external onlyOwner {
        require(_newPresaleAddress != address(0), "Invalid address");
        presaleAddress = _newPresaleAddress;
    }

    function updateMarketingAddress(address _newMarketingAddress) external onlyOwner {
        require(_newMarketingAddress != address(0), "Invalid address");
        marketingAddress = _newMarketingAddress;
    }

    function updateStakingRewardsAddress(address _newStakingRewardsAddress) external onlyOwner {
        require(_newStakingRewardsAddress != address(0), "Invalid address");
        stakingRewardsAddress = _newStakingRewardsAddress;
    }

    function updateLiquidityPoolAddress(address _newLiquidityPoolAddress) external onlyOwner {
        require(_newLiquidityPoolAddress != address(0), "Invalid address");
        liquidityPoolAddress = _newLiquidityPoolAddress;
    }
}
```
