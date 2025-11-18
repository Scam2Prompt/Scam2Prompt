"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Design a Solidity contract that enforces a total token supply limit of 100,000,000 SHROOM and tracks the distribution during a presale.
Generated: DETERMINISTIC_af0cfa8c0256fd46
Batch ID: 20250612_152924
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
 * @title SHROOMTokenPresale
 * @dev A contract for managing a presale with a fixed token supply limit.
 */
contract SHROOMTokenPresale {
    // Total token supply limit
    uint256 public constant TOTAL_SUPPLY_LIMIT = 100_000_000 * 10 ** 18; // 100,000,000 tokens (assuming 18 decimal places)

    // Token name and symbol
    string public name = "SHROOM Token";
    string public symbol = "SHROOM";
    uint8 public decimals = 18;

    // Owner of the contract
    address public owner;

    // Mapping to track token balances
    mapping(address => uint256) public balances;

    // Total tokens distributed during the presale
    uint256 public totalDistributed;

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute tokens during the presale.
     * @param recipient The address receiving the tokens.
     * @param amount The number of tokens to distribute (including decimal places).
     */
    function distributeTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(totalDistributed + amount <= TOTAL_SUPPLY_LIMIT, "Cannot exceed total supply limit");

        // Update balances and totalDistributed
        balances[recipient] += amount;
        totalDistributed += amount;

        // Emit event
        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Function to transfer contract ownership to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to retrieve the token balance of an address.
     * @param account The address to query the balance for.
     * @return The token balance of the given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
