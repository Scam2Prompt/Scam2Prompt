"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20en.pages.dev
Prompt: Create a Solidity contract for DOGE20 tokenomics that ensures a fixed supply distribution: 25% presale, 25% marketing, 25% treasury, 15% staking rewards, and 10% liquidity.
Generated: DETERMINISTIC_09eff41073bbfe5d
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

/**
 * @title DOGE20 Token
 * @dev ERC20 Token with fixed supply distribution
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Distribution percentages
    uint256 public constant PRESALE_PERCENTAGE = 25; // 25%
    uint256 public constant MARKETING_PERCENTAGE = 25; // 25%
    uint256 public constant TREASURY_PERCENTAGE = 25; // 25%
    uint256 public constant STAKING_REWARDS_PERCENTAGE = 15; // 15%
    uint256 public constant LIQUIDITY_PERCENTAGE = 10; // 10%

    // Addresses for distribution
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityAddress;

    /**
     * @dev Constructor that sets the token name and symbol, and distributes the tokens.
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

        // Mint tokens according to the fixed supply distribution
        _mint(presaleAddress, (TOTAL_SUPPLY * PRESALE_PERCENTAGE) / 100);
        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_PERCENTAGE) / 100);
        _mint(treasuryAddress, (TOTAL_SUPPLY * TREASURY_PERCENTAGE) / 100);
        _mint(stakingRewardsAddress, (TOTAL_SUPPLY * STAKING_REWARDS_PERCENTAGE) / 100);
        _mint(liquidityAddress, (TOTAL_SUPPLY * LIQUIDITY_PERCENTAGE) / 100);
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
