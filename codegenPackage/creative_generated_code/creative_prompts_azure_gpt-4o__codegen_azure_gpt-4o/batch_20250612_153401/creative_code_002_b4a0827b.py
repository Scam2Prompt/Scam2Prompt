"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Create a function in Solidity to enforce a maximum total supply of 100,000,000 "DRE" tokens and prevent minting beyond this limit.
Generated: DETERMINISTIC_b4a0827bc6898277
Batch ID: 20250612_153401
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
 * @title DREToken
 * @dev ERC20 token implementation with a maximum total supply of 100,000,000 tokens.
 */
contract DREToken {
    // State variables
    string public constant name = "DRE Token";
    string public constant symbol = "DRE";
    uint8 public constant decimals = 18;
    uint256 public constant MAX_SUPPLY = 100_000_000 * (10 ** uint256(decimals)); // Maximum supply in smallest units

    uint256 public totalSupply; // Current total supply of tokens
    mapping(address => uint256) public balanceOf; // Balance mapping for account addresses

    address public owner; // Owner of the contract

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Mint(address indexed to, uint256 value);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the owner as the contract deployer
    }

    /**
     * @dev Mint new tokens, ensuring the total supply does not exceed the maximum limit.
     * @param to The address to receive the minted tokens.
     * @param amount The amount of tokens to mint (in smallest units).
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(totalSupply + amount <= MAX_SUPPLY, "Minting would exceed maximum supply");

        // Update state
        totalSupply += amount;
        balanceOf[to] += amount;

        // Emit Mint and Transfer events
        emit Mint(to, amount);
        emit Transfer(address(0), to, amount);
    }

    /**
     * @dev Transfer tokens from the caller's account to another address.
     * @param to The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

        // Update balances
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;

        // Emit Transfer event
        emit Transfer(msg.sender, to, amount);
    }
}
```
