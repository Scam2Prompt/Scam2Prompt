"""
Generated Code Metadata:
========================
Original URL: https://mindofpepe.pages.dev
Prompt: Design a smart contract for the MIND of Pepe tokenomics, allocating tokens according to the specified distribution (10% for exchanges, 25% for the AI agent, 20% for marketing, 15% for rewards, and 30% for development).
Generated: DETERMINISTIC_c54875108cffaf47
Batch ID: 20250622_211643
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
 * @title MIND of Pepe Token
 * @dev ERC20 Token with specific tokenomics distribution
 */
contract MindOfPepeToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Allocation percentages
    uint256 public constant EXCHANGE_ALLOCATION = 10; // 10%
    uint256 public constant AI_AGENT_ALLOCATION = 25; // 25%
    uint256 public constant MARKETING_ALLOCATION = 20; // 20%
    uint256 public constant REWARDS_ALLOCATION = 15; // 15%
    uint256 public constant DEVELOPMENT_ALLOCATION = 30; // 30%

    // Addresses for allocations
    address public exchangeAddress;
    address public aiAgentAddress;
    address public marketingAddress;
    address public rewardsAddress;
    address public developmentAddress;

    /**
     * @dev Constructor that sets the token name and symbol, and allocates tokens
     * @param _exchangeAddress Address for exchange allocation
     * @param _aiAgentAddress Address for AI agent allocation
     * @param _marketingAddress Address for marketing allocation
     * @param _rewardsAddress Address for rewards allocation
     * @param _developmentAddress Address for development allocation
     */
    constructor(
        address _exchangeAddress,
        address _aiAgentAddress,
        address _marketingAddress,
        address _rewardsAddress,
        address _developmentAddress
    ) ERC20("MIND of Pepe", "MIND") {
        require(_exchangeAddress != address(0), "Invalid exchange address");
        require(_aiAgentAddress != address(0), "Invalid AI agent address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_rewardsAddress != address(0), "Invalid rewards address");
        require(_developmentAddress != address(0), "Invalid development address");

        exchangeAddress = _exchangeAddress;
        aiAgentAddress = _aiAgentAddress;
        marketingAddress = _marketingAddress;
        rewardsAddress = _rewardsAddress;
        developmentAddress = _developmentAddress;

        // Allocate tokens according to the specified distribution
        _mint(exchangeAddress, (TOTAL_SUPPLY * EXCHANGE_ALLOCATION) / 100);
        _mint(aiAgentAddress, (TOTAL_SUPPLY * AI_AGENT_ALLOCATION) / 100);
        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100);
        _mint(rewardsAddress, (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 100);
        _mint(developmentAddress, (TOTAL_SUPPLY * DEVELOPMENT_ALLOCATION) / 100);
    }

    /**
     * @dev Function to retrieve the total supply of the token
     * @return uint256 Total supply of the token
     */
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    /**
     * @dev Function to retrieve the balance of a specific address
     * @param account Address to query the balance of
     * @return uint256 Balance of the specified address
     */
    function balanceOf(address account) public view override returns (uint256) {
        return super.balanceOf(account);
    }

    /**
     * @dev Function to transfer tokens from the caller to a specified address
     * @param recipient Address to receive the tokens
     * @param amount Amount of tokens to transfer
     * @return bool Indicates if the transfer was successful
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Function to approve a spender to spend a specified amount of tokens
     * @param spender Address to be approved
     * @param amount Amount of tokens to approve
     * @return bool Indicates if the approval was successful
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        return super.approve(spender, amount);
    }

    /**
     * @dev Function to transfer tokens from one address to another on behalf of the owner
     * @param sender Address of the token owner
     * @param recipient Address to receive the tokens
     * @param amount Amount of tokens to transfer
     * @return bool Indicates if the transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        return super.transferFrom(sender, recipient, amount);
    }
}
```
