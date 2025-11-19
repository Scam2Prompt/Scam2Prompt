"""
Generated Code Metadata:
========================
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Create a Solidity contract to manage the Crudo Protocol's tokenomics, including allocations for presale, rewards, marketing, development, and liquidity, as outlined in the webpage content.
Generated: DETERMINISTIC_7fc4848c725b578b
Batch ID: 20250612_151141
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
 * @title CrudoToken
 * @dev This contract manages the tokenomics for the Crudo Protocol.
 * It includes allocations for presale, rewards, marketing, development, and liquidity.
 */
contract CrudoToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant REWARDS_ALLOCATION = 30; // 30%
    uint256 public constant MARKETING_ALLOCATION = 15; // 15%
    uint256 public constant DEVELOPMENT_ALLOCATION = 10; // 10%
    uint256 public constant LIQUIDITY_ALLOCATION = 25; // 25%

    // Mappings to track allocated tokens
    mapping(address => uint256) public allocations;

    // Events
    event TokensAllocated(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor that initializes the token and allocates tokens to respective addresses.
     */
    constructor() ERC20("CrudoToken", "CRUDO") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocate tokens based on defined percentages
        allocateTokens(msg.sender, PRESALE_ALLOCATION);
        allocateTokens(msg.sender, REWARDS_ALLOCATION);
        allocateTokens(msg.sender, MARKETING_ALLOCATION);
        allocateTokens(msg.sender, DEVELOPMENT_ALLOCATION);
        allocateTokens(msg.sender, LIQUIDITY_ALLOCATION);
    }

    /**
     * @dev Allocates tokens to a specified address based on the allocation percentage.
     * @param recipient The address to receive the allocated tokens.
     * @param allocationPercentage The percentage of the total supply to allocate.
     */
    function allocateTokens(address recipient, uint256 allocationPercentage) internal {
        require(allocationPercentage > 0, "Allocation percentage must be greater than zero");
        require(allocationPercentage <= 100, "Allocation percentage must not exceed 100");

        uint256 allocationAmount = (TOTAL_SUPPLY * allocationPercentage) / 100;
        allocations[recipient] += allocationAmount;

        // Emit an event for the allocation
        emit TokensAllocated(recipient, allocationAmount);
    }

    /**
     * @dev Allows the owner to withdraw any tokens mistakenly sent to the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance in contract");
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Function to get the total allocated tokens for a specific address.
     * @param recipient The address to check allocations for.
     * @return The total allocated tokens for the specified address.
     */
    function getAllocatedTokens(address recipient) external view returns (uint256) {
        return allocations[recipient];
    }
}
```
