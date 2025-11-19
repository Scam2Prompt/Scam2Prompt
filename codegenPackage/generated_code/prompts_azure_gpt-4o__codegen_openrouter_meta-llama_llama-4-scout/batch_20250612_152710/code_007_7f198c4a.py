"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-icu.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics, ensuring proper allocation of the fixed supply (e.g., presale, marketing, treasury, staking rewards, and liquidity).
Generated: DETERMINISTIC_7f198c4a244b730f
Batch ID: 20250612_152710
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Token Contract
 * @author [Your Name]
 * @notice This contract represents the DOGE20 token with its tokenomics.
 */
contract DOGE20 is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of address to its allocation
    mapping(address => bool) public allocations;

    // Presale, marketing, treasury, staking rewards, and liquidity addresses
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityAddress;

    // Fixed supply of DOGE20 tokens
    uint256 public constant TOTAL_SUPPLY = 10**9 * 10**18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant TREASURY_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 35; // 35%

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
            "Invalid address"
        );

        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityAddress = _liquidityAddress;

        // Mint and allocate tokens
        _mint(msg.sender, TOTAL_SUPPLY);

        // Presale allocation
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        _transfer(msg.sender, presaleAddress, presaleAmount);
        allocations[presaleAddress] = true;

        // Marketing allocation
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        _transfer(msg.sender, marketingAddress, marketingAmount);
        allocations[marketingAddress] = true;

        // Treasury allocation
        uint256 treasuryAmount = (TOTAL_SUPPLY * TREASURY_ALLOCATION) / 100;
        _transfer(msg.sender, treasuryAddress, treasuryAmount);
        allocations[treasuryAddress] = true;

        // Staking rewards allocation
        uint256 stakingRewardsAmount = (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 100;
        _transfer(msg.sender, stakingRewardsAddress, stakingRewardsAmount);
        allocations[stakingRewardsAddress] = true;

        // Liquidity allocation
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        _transfer(msg.sender, liquidityAddress, liquidityAmount);
        allocations[liquidityAddress] = true;

        // Burn remaining tokens in contract
        uint256 remainingBalance = balanceOf(msg.sender);
        _burn(msg.sender, remainingBalance);
    }

    /**
     * @notice Function to handle ERC20 token transfers
     * @param from Sender address
     * @param to Receiver address
     * @param amount Transfer amount
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256[] memory ids,
        uint256[] memory amounts,
        bytes memory data
    ) internal virtual override {
        for (uint256 i = 0; i < ids.length; i++) {
            require(!allocations[to] || to == owner(), "Invalid recipient");
        }
        super._beforeTokenTransfer(from, to, ids, amounts, data);
    }

    /**
     * @notice Function to handle ERC20 token transfer
     * @param from Sender address
     * @param to Receiver address
     * @param amount Transfer amount
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        require(!allocations[to] || to == owner(), "Invalid recipient");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
