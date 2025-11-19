"""
Generated Code Metadata:
========================
Original URL: https://memekombat-in.pages.dev
Prompt: Create a Solidity contract that implements the tokenomics for $MK, including presale allocation (50%), staking rewards (30%), DEX liquidity (10%), and community rewards (10%).
Generated: DETERMINISTIC_6103dd5ffe4f7f43
Batch ID: 20250612_152924
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MKToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant PRESALE_PERCENT = 50;
    uint256 public constant STAKING_REWARDS_PERCENT = 30;
    uint256 public constant DEX_LIQUIDITY_PERCENT = 10;
    uint256 public constant COMMUNITY_REWARDS_PERCENT = 10;

    // Addresses for allocations
    address public presaleAddress;
    address public stakingRewardsAddress;
    address public dexLiquidityAddress;
    address public communityRewardsAddress;

    // Total supply
    uint256 private constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens

    // Flags for allocation completion
    bool private presaleAllocated = false;
    bool private stakingRewardsAllocated = false;
    bool private dexLiquidityAllocated = false;
    bool private communityRewardsAllocated = false;

    constructor() ERC20("MK Token", "MK") {
        _mint(address(this), TOTAL_SUPPLY);
    }

    function setAllocationAddresses(
        address _presaleAddress,
        address _stakingRewardsAddress,
        address _dexLiquidityAddress,
        address _communityRewardsAddress
    ) external onlyOwner {
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_stakingRewardsAddress != address(0), "Invalid staking rewards address");
        require(_dexLiquidityAddress != address(0), "Invalid DEX liquidity address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");

        presaleAddress = _presaleAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        dexLiquidityAddress = _dexLiquidityAddress;
        communityRewardsAddress = _communityRewardsAddress;
    }

    function allocatePresaleTokens() external onlyOwner {
        require(!presaleAllocated, "Presale tokens already allocated");
        require(presaleAddress != address(0), "Presale address not set");

        uint256 amount = TOTAL_SUPPLY.mul(PRESALE_PERCENT).div(100);
        _transfer(address(this), presaleAddress, amount);
        presaleAllocated = true;
    }

    function allocateStakingRewards() external onlyOwner {
        require(!stakingRewardsAllocated, "Staking rewards already allocated");
        require(stakingRewardsAddress != address(0), "Staking rewards address not set");

        uint256 amount = TOTAL_SUPPLY.mul(STAKING_REWARDS_PERCENT).div(100);
        _transfer(address(this), stakingRewardsAddress, amount);
        stakingRewardsAllocated = true;
    }

    function allocateDexLiquidity() external onlyOwner {
        require(!dexLiquidityAllocated, "DEX liquidity already allocated");
        require(dexLiquidityAddress != address(0), "DEX liquidity address not set");

        uint256 amount = TOTAL_SUPPLY.mul(DEX_LIQUIDITY_PERCENT).div(100);
        _transfer(address(this), dexLiquidityAddress, amount);
        dexLiquidityAllocated = true;
    }

    function allocateCommunityRewards() external onlyOwner {
        require(!communityRewardsAllocated, "Community rewards already allocated");
        require(communityRewardsAddress != address(0), "Community rewards address not set");

        uint256 amount = TOTAL_SUPPLY.mul(COMMUNITY_REWARDS_PERCENT).div(100);
        _transfer(address(this), communityRewardsAddress, amount);
        communityRewardsAllocated = true;
    }

    function reclaimUnallocatedTokens() external onlyOwner {
        uint256 remainingBalance = balanceOf(address(this));
        require(remainingBalance > 0, "No unallocated tokens remaining");

        _transfer(address(this), owner(), remainingBalance);
    }
}
```
