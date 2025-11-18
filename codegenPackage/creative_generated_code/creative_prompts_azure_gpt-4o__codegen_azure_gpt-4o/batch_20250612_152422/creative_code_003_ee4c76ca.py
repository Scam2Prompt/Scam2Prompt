"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://funkybunnies.pages.dev
Prompt: Write a smart contract in Solidity for a token called "Funky Bunnies" that supports minting and burning functionalities.
Generated: DETERMINISTIC_ee4c76caa175a5a1
Batch ID: 20250612_152422
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
 * @title FunkyBunniesToken
 * @dev A simple ERC20-like token with minting and burning functionalities
 */
contract FunkyBunniesToken {
    // Token details
    string public name = "Funky Bunnies";
    string public symbol = "FBUN";
    uint8 public decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track balances of addresses
    mapping(address => uint256) private balances;

    // Owner of the contract
    address public owner;

    // Events for minting and burning tokens
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Mint(address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that sets the deployer as the owner of the contract
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to check the balance of a given address
     * @param account The address to query the balance of
     * @return The balance of the specified address
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to mint new tokens
     * @param to The address to receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        balances[to] += amount;
        totalSupply += amount;

        emit Mint(to, amount);
        emit Transfer(address(0), to, amount);
    }

    /**
     * @dev Function to burn tokens
     * @param from The address to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function burn(address from, uint256 amount) public onlyOwner {
        require(from != address(0), "Cannot burn from the zero address");
        require(amount > 0, "Burn amount must be greater than zero");
        require(balances[from] >= amount, "Insufficient balance to burn");

        balances[from] -= amount;
        totalSupply -= amount;

        emit Burn(from, amount);
        emit Transfer(from, address(0), amount);
    }

    /**
     * @dev Function to transfer tokens between addresses
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance for transfer");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);

        return true;
    }
}
```
