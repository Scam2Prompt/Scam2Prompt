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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DOGE20 Token Contract
 * @author [Your Name]
 * @notice This contract represents the DOGE20 token with fixed supply allocation.
 */
contract DOGE20 is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of address to its allocation status
    mapping(address => bool) public allocatedAddresses;

    // Presale, marketing, treasury, staking rewards, and liquidity percentages
    uint256 public constant PRESALE_PERCENTAGE = 25;
    uint256 public constant MARKETING_PERCENTAGE = 25;
    uint256 public constant TREASURY_PERCENTAGE = 25;
    uint256 public constant STAKING_REWARDS_PERCENTAGE = 15;
    uint256 public constant LIQUIDITY_PERCENTAGE = 10;

    // Total supply
    uint256 public constant TOTAL_SUPPLY = 1 * 10**12 * 10**18; // 1 trillion tokens with 18 decimals

    // Allocation addresses
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityAddress;

    /**
     * @notice Constructor for DOGE20 token contract
     * @param _presaleAddress Presale address
     * @param _marketingAddress Marketing address
     * @param _treasuryAddress Treasury address
     * @param _stakingRewardsAddress Staking rewards address
     * @param _liquidityAddress Liquidity address
     */
    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _treasuryAddress,
        address _stakingRewardsAddress,
        address _liquidityAddress
    ) ERC20("DOGE20", "DOGE20") {
        require(
            _presaleAddress != address(0) &&
                _marketingAddress != address(0) &&
                _treasuryAddress != address(0) &&
                _stakingRewardsAddress != address(0) &&
                _liquidityAddress != address(0),
            "Allocation addresses cannot be zero"
        );

        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityAddress = _liquidityAddress;

        // Mint total supply
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocate tokens
        _allocateTokens();
    }

    /**
     * @notice Allocate tokens to presale, marketing, treasury, staking rewards, and liquidity addresses
     */
    function _allocateTokens() internal {
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_PERCENTAGE) / 100;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_PERCENTAGE) / 100;
        uint256 treasuryAmount = (TOTAL_SUPPLY * TREASURY_PERCENTAGE) / 100;
        uint256 stakingRewardsAmount = (TOTAL_SUPPLY * STAKING_REWARDS_PERCENTAGE) / 100;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_PERCENTAGE) / 100;

        // Transfer tokens to allocation addresses
        _transfer(msg.sender, presaleAddress, presaleAmount);
        _transfer(msg.sender, marketingAddress, marketingAmount);
        _transfer(msg.sender, treasuryAddress, treasuryAmount);
        _transfer(msg.sender, stakingRewardsAddress, stakingRewardsAmount);
        _transfer(msg.sender, liquidityAddress, liquidityAmount);

        // Mark allocation addresses
        allocatedAddresses[presaleAddress] = true;
        allocatedAddresses[marketingAddress] = true;
        allocatedAddresses[treasuryAddress] = true;
        allocatedAddresses[stakingRewardsAddress] = true;
        allocatedAddresses[liquidityAddress] = true;
    }

    /**
     * @notice Burn tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        super.burn(amount);
    }

    /**
     * @notice Transfer tokens
     * @param to Recipient address
     * @param amount Amount of tokens to transfer
     * @return bool Whether transfer was successful
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        // Only allow transfers from allocated addresses or the contract owner
        require(
            allocatedAddresses[msg.sender] || msg.sender == owner(),
            "Only allocated addresses or the contract owner can transfer tokens"
        );

        return super.transfer(to, amount);
    }
}
```
