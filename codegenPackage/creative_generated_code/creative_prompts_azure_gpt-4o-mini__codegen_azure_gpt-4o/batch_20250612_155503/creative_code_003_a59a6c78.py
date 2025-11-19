"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vantard-presale.pages.dev
Prompt: Create a Solidity smart contract that handles the burning of tokens upon redemption, as described in the Vantard fund's mechanics.
Generated: DETERMINISTIC_a59a6c781c606d98
Batch ID: 20250612_155503
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
 * @title VantardFundToken
 * @dev A smart contract for managing token burning upon redemption for the Vantard fund mechanics.
 */
contract VantardFundToken {

    // State variables
    string public name = "VantardFundToken";
    string public symbol = "VFT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balances;

    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    modifier hasSufficientBalance(address account, uint256 amount) {
        require(balances[account] >= amount, "Insufficient balance for this operation.");
        _;
    }

    /**
     * @dev Constructor to set the initial supply of tokens and assign them to the contract owner.
     * @param initialSupply The initial token supply.
     */
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfers tokens from the sender's account to a recipient.
     * @param recipient The address of the receiving party.
     * @param amount The number of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external hasSufficientBalance(msg.sender, amount) returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address.");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Burns tokens from the sender's account upon redemption.
     * This decreases the total supply of tokens.
     * @param amount The number of tokens to burn.
     */
    function burn(uint256 amount) external hasSufficientBalance(msg.sender, amount) returns (bool) {
        balances[msg.sender] -= amount;
        totalSupply -= amount;

        emit Burn(msg.sender, amount);
        return true;
    }

    /**
     * @dev Allows the owner to mint new tokens to a specific address.
     * @param recipient The address to receive the new tokens.
     * @param amount The number of tokens to mint.
     */
    function mint(address recipient, uint256 amount) external onlyOwner returns (bool) {
        require(recipient != address(0), "Cannot mint to the zero address.");

        uint256 mintAmount = amount * (10 ** uint256(decimals));
        totalSupply += mintAmount;
        balances[recipient] += mintAmount;

        emit Transfer(address(0), recipient, mintAmount);
        return true;
    }
}
```
