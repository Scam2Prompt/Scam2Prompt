"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-3bb.pages.dev
Prompt: Write a Solidity smart contract to manage the tokenomics distribution of $POODL, ensuring compliance with the outlined allocations (50% presale, 30% staking, etc.).
Generated: DETERMINISTIC_4d03ee8b2783ec91
Batch ID: 20250612_153400
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

/**
 * @title POODL Token Contract
 * @dev A simple ERC20 token contract for managing tokenomics distribution
 */
contract POODLToken is ERC20, Ownable {
    // Constants for allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 50; // 50% for presale
    uint256 public constant STAKING_ALLOCATION = 30; // 30% for staking
    uint256 public constant TEAM_ALLOCATION = 10;     // 10% for the team
    uint256 public constant MARKETING_ALLOCATION = 5; // 5% for marketing
    uint256 public constant RESERVE_ALLOCATION = 5;   // 5% for reserves

    // Total supply of $POODL tokens
    uint256 private constant TOTAL_SUPPLY = 1e6 * 10**18; // 1 million tokens with 18 decimals

    // Track the amount allocated to each category
    uint256 public presaleTokens;
    uint256 public stakingTokens;
    uint256 public teamTokens;
    uint256 public marketingTokens;
    uint256 public reserveTokens;

    // Event to log token distribution
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     * Distributes tokens according to the defined allocations.
     */
    constructor() ERC20("POODL", "POODL") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Calculate allocated tokens
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        stakingTokens = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        teamTokens = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;
        marketingTokens = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        reserveTokens = (TOTAL_SUPPLY * RESERVE_ALLOCATION) / 100;
    }

    /**
     * @dev Distribution function to allocate tokens to a specified recipient.
     * @param recipient The address of the recipient
     * @param amount The amount of tokens to distribute
     */
    function distributeTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the recipient
        _transfer(msg.sender, recipient, amount);
        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Function to retrieve the remaining tokens allocated for a category.
     * @param category The category for which to check the remaining tokens
     * @return remainingTokens The number of remaining tokens for the specified category
     */
    function remainingTokens(string memory category) public view returns (uint256) {
        if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("presale"))) {
            return presaleTokens;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("staking"))) {
            return stakingTokens;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("team"))) {
            return teamTokens;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("marketing"))) {
            return marketingTokens;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("reserve"))) {
            return reserveTokens;
        } else {
            revert("Invalid category");
        }
    }

    /**
     * @dev Function to withdraw any accidentally sent tokens to the contract.
     * @param tokenAddress The address of the token contract to withdraw from
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");

        ERC20 token = ERC20(tokenAddress);
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient token balance in contract");

        token.transfer(msg.sender, amount);
    }
}
```
