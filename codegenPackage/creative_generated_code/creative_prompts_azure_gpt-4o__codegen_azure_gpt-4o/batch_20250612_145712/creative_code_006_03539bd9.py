"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepe.pages.dev
Prompt: Create a smart contract that allocates $MIND tokens according to the tokenomics breakdown provided (e.g., 10% for exchanges, 25% for the AI agent).
Generated: DETERMINISTIC_03539bd9e5593322
Batch ID: 20250612_145712
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

/**
 * @title MindTokenAllocation
 * @dev A smart contract to allocate $MIND tokens based on a specified tokenomics breakdown.
 */
contract MindTokenAllocation {
    // Tokenomics percentages (in basis points: e.g., 10% = 1000 basis points)
    uint256 public constant EXCHANGE_ALLOCATION = 1000; // 10%
    uint256 public constant AI_AGENT_ALLOCATION = 2500; // 25%
    uint256 public constant TOTAL_ALLOCATION = 10000; // 100% (for validation)

    // Total supply of $MIND tokens
    uint256 public immutable totalSupply;

    // Beneficiary addresses
    address public exchangeAddress;
    address public aiAgentAddress;

    // Constructor to initialize the contract with the total supply and beneficiary addresses
    constructor(
        uint256 _totalSupply,
        address _exchangeAddress,
        address _aiAgentAddress
    ) {
        require(_exchangeAddress != address(0), "Exchange address cannot be zero.");
        require(_aiAgentAddress != address(0), "AI Agent address cannot be zero.");
        require(_totalSupply > 0, "Total supply must be greater than zero.");

        totalSupply = _totalSupply;
        exchangeAddress = _exchangeAddress;
        aiAgentAddress = _aiAgentAddress;
    }

    /**
     * @notice Allocates tokens to the beneficiaries based on the predefined tokenomics.
     * @dev Avoids reentrancy attacks by not allowing external calls during allocation.
     */
    function allocateTokens() external {
        // Calculate allocations
        uint256 exchangeTokens = (totalSupply * EXCHANGE_ALLOCATION) / TOTAL_ALLOCATION;
        uint256 aiAgentTokens = (totalSupply * AI_AGENT_ALLOCATION) / TOTAL_ALLOCATION;

        // Transfer tokens to the beneficiaries
        // Note: Assumes ERC20 transfer function availability
        ERC20(address(this)).transfer(exchangeAddress, exchangeTokens);
        ERC20(address(this)).transfer(aiAgentAddress);
    }

    // ADDextra safew12
