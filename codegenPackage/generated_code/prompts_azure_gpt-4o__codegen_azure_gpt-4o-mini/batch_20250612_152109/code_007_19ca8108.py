"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-a.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics, ensuring fixed supply allocation: 25% presale, 25% marketing, 25% treasury, 15% staking rewards, and 10% liquidity.
Generated: DETERMINISTIC_19ca8108ad663341
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Token
 * @dev Implementation of the DOGE20 token with fixed supply allocation.
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25%
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25%
    uint256 public constant TREASURY_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25%
    uint256 public constant STAKING_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10%

    // Addresses for allocations
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityAddress;

    // Event for allocation distribution
    event TokensAllocated(string allocationType, address indexed to, uint256 amount);

    /**
     * @dev Constructor that sets the token name and symbol, and allocates tokens.
     * @param _presaleAddress Address for presale allocation
     * @param _marketingAddress Address for marketing allocation
     * @param _treasuryAddress Address for treasury allocation
     * @param _stakingRewardsAddress Address for staking rewards allocation
     * @param _liquidityAddress Address for liquidity allocation
     */
    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _treasuryAddress,
        address _stakingRewardsAddress,
        address _liquidityAddress
    ) ERC20("DOGE20", "DOGE20") {
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_treasuryAddress != address(0), "Invalid treasury address");
        require(_stakingRewardsAddress != address(0), "Invalid staking rewards address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");

        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityAddress = _liquidityAddress;

        // Allocate tokens to respective addresses
        _mint(presaleAddress, PRESALE_ALLOCATION);
        emit TokensAllocated("Presale", presaleAddress, PRESALE_ALLOCATION);

        _mint(marketingAddress, MARKETING_ALLOCATION);
        emit TokensAllocated("Marketing", marketingAddress, MARKETING_ALLOCATION);

        _mint(treasuryAddress, TREASURY_ALLOCATION);
        emit TokensAllocated("Treasury", treasuryAddress, TREASURY_ALLOCATION);

        _mint(stakingRewardsAddress, STAKING_REWARDS_ALLOCATION);
        emit TokensAllocated("Staking Rewards", stakingRewardsAddress, STAKING_REWARDS_ALLOCATION);

        _mint(liquidityAddress, LIQUIDITY_ALLOCATION);
        emit TokensAllocated("Liquidity", liquidityAddress, LIQUIDITY_ALLOCATION);
    }

    /**
     * @dev Function to retrieve the total supply of the token.
     * @return The total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    /**
     * @dev Function to retrieve the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return super.balanceOf(account);
    }

    /**
     * @dev Function to transfer tokens from the caller to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Function to approve a spender to spend a specified amount of tokens on behalf of the caller.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        return super.approve(spender, amount);
    }

    /**
     * @dev Function to transfer tokens from one address to another on behalf of a third party.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        return super.transferFrom(sender, recipient, amount);
    }
}
```
