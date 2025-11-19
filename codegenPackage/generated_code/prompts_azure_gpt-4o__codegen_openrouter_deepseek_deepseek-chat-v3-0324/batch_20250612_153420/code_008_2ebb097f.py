"""
Generated Code Metadata:
========================
Original URL: https://nfa-ai.pages.dev
Prompt: Create a smart contract function that logs the migration of $NFAI V1 to $NFAI V2 tokens and emits an event with the sender's address and token amount.
Generated: DETERMINISTIC_2ebb097f68e56a00
Batch ID: 20250612_153420
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

contract NFAITokenMigration {
    // Event to log token migration
    event TokensMigrated(
        address indexed sender,
        uint256 amountV1,
        uint256 amountV2
    );

    // Mapping to track migrated amounts per address
    mapping(address => uint256) public migratedAmounts;

    // Address of the V1 token contract (set in constructor)
    address public v1TokenAddress;

    // Address of the V2 token contract (set in constructor)
    address public v2TokenAddress;

    // Conversion rate from V1 to V2 (e.g., 1:100 would mean 100 V2 per 1 V1)
    uint256 public conversionRate;

    // Contract owner
    address public owner;

    // Modifier to restrict function access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _v1TokenAddress Address of the V1 token contract
     * @param _v2TokenAddress Address of the V2 token contract
     * @param _conversionRate Conversion rate from V1 to V2 tokens
     */
    constructor(
        address _v1TokenAddress,
        address _v2TokenAddress,
        uint256 _conversionRate
    ) {
        require(_v1TokenAddress != address(0), "Invalid V1 token address");
        require(_v2TokenAddress != address(0), "Invalid V2 token address");
        require(_conversionRate > 0, "Conversion rate must be greater than 0");

        v1TokenAddress = _v1TokenAddress;
        v2TokenAddress = _v2TokenAddress;
        conversionRate = _conversionRate;
        owner = msg.sender;
    }

    /**
     * @dev Function to migrate V1 tokens to V2 tokens
     * @param amountV1 Amount of V1 tokens to migrate
     */
    function migrateTokens(uint256 amountV1) external {
        require(amountV1 > 0, "Amount must be greater than 0");

        // In a real implementation, you would:
        // 1. Transfer V1 tokens from sender to this contract
        // 2. Mint/burn tokens as needed for V2
        // For this example, we just log the migration

        uint256 amountV2 = amountV1 * conversionRate;
        migratedAmounts[msg.sender] += amountV2;

        emit TokensMigrated(msg.sender, amountV1, amountV2);
    }

    /**
     * @dev Function to update conversion rate (owner only)
     * @param newRate New conversion rate from V1 to V2 tokens
     */
    function setConversionRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Conversion rate must be greater than 0");
        conversionRate = newRate;
    }

    /**
     * @dev Function to transfer ownership (owner only)
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid owner address");
        owner = newOwner;
    }
}
```
