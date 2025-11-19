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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MK Tokenomics Contract
 * @author [Your Name]
 * @notice Implements tokenomics for $MK, including presale allocation, staking rewards, DEX liquidity, and community rewards.
 */
contract MKTokenomics is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their respective allocations
    mapping(address => uint256) public allocations;

    // Addresses for different allocations
    address public presaleAddress;
    address public stakingRewardsAddress;
    address public dexLiquidityAddress;
    address public communityRewardsAddress;

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 50;
    uint256 public constant STAKING_REWARDS_ALLOCATION = 30;
    uint256 public constant DEX_LIQUIDITY_ALLOCATION = 10;
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 10;

    // Total supply of $MK
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18;

    /**
     * @notice Initializes the contract with tokenomics allocations.
     * @param presaleAddr Presale address.
     * @param stakingRewardsAddr Staking rewards address.
     * @param dexLiquidityAddr DEX liquidity address.
     * @param communityRewardsAddr Community rewards address.
     */
    constructor(
        address presaleAddr,
        address stakingRewardsAddr,
        address dexLiquidityAddr,
        address communityRewardsAddr
    ) ERC20("MK Token", "MK") {
        require(
            presaleAddr != address(0) &&
                stakingRewardsAddr != address(0) &&
                dexLiquidityAddr != address(0) &&
                communityRewardsAddr != address(0),
            "Invalid address"
        );

        presaleAddress = presaleAddr;
        stakingRewardsAddress = stakingRewardsAddr;
        dexLiquidityAddress = dexLiquidityAddr;
        communityRewardsAddress = communityRewardsAddr;

        // Mint total supply
        _mint(address(this), TOTAL_SUPPLY);

        // Allocate tokens
        allocateTokens();
    }

    /**
     * @notice Allocates tokens according to tokenomics.
     */
    function allocateTokens() internal {
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 stakingRewardsAmount = (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 100;
        uint256 dexLiquidityAmount = (TOTAL_SUPPLY * DEX_LIQUIDITY_ALLOCATION) / 100;
        uint256 communityRewardsAmount = (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100;

        // Transfer allocations
        _transfer(address(this), presaleAddress, presaleAmount);
        _transfer(address(this), stakingRewardsAddress, stakingRewardsAmount);
        _transfer(address(this), dexLiquidityAddress, dexLiquidityAmount);
        _transfer(address(this), communityRewardsAddress, communityRewardsAmount);

        // Update allocations mapping
        allocations[presaleAddress] = presaleAmount;
        allocations[stakingRewardsAddress] = stakingRewardsAmount;
        allocations[dexLiquidityAddress] = dexLiquidityAmount;
        allocations[communityRewardsAddress] = communityRewardsAmount;
    }

    /**
     * @notice Burns tokens from the specified address.
     * @param account Address to burn tokens from.
     * @param amount Amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override {
        require(msg.sender == stakingRewardsAddress, "Only staking rewards address can burn tokens");
        super.burnFrom(account, amount);
    }

    /**
     * @notice Transfers tokens from the contract to the specified address.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool Whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(msg.sender == stakingRewardsAddress || msg.sender == communityRewardsAddress, "Only staking rewards and community rewards addresses can transfer tokens");
        return super.transfer(to, amount);
    }
}
```
