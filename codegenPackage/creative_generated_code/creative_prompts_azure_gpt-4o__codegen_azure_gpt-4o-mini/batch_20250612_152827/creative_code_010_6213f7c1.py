"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Write a Solidity contract that prevents token inflation by implementing a fixed supply mechanism, inspired by DOGE20's solution to Dogecoin's infinite supply issue.
Generated: DETERMINISTIC_6213f7c11e95d506
Batch ID: 20250612_152827
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
 * @title FixedSupplyToken
 * @dev A simple ERC20 token with a fixed supply to prevent inflation.
 */
contract FixedSupplyToken {
    // Declare state variables
    string public name; // Token name
    string public symbol; // Token symbol
    uint8 public decimals; // Number of decimal places
    uint256 public totalSupply; // Total supply of the token

    // Mappings for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for logging transfers and approvals
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token's properties and assign total supply.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _decimals Number of decimal places.
     * @param _initialSupply Initial total supply of the token.
     */
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * (10 ** uint256(decimals)); // Adjust total supply based on decimals
        balances[msg.sender] = totalSupply; // Assign total supply to the contract deployer
    }

    /**
     * @dev Returns the balance of the specified address.
     * @param account The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount; // Deduct the amount from sender's balance
        balances[to] += amount; // Add the amount to the recipient's balance
        emit Transfer(msg.sender, to, amount); // Emit the transfer event
        return true;
    }

    /**
     * @dev Approves an address to spend a specified amount of tokens on behalf of the caller.
     * @param spender The address authorized to spend tokens.
     * @param amount The amount of tokens to allow spending.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");
        
        allowances[msg.sender][spender] = amount; // Set the allowance
        emit Approval(msg.sender, spender, amount); // Emit the approval event
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        require(from != address(0), "Transfer from the zero address is not allowed");
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount; // Deduct the amount from sender's balance
        balances[to] += amount; // Add the amount to the recipient's balance
        allowances[from][msg.sender] -= amount; // Decrease the allowance
        emit Transfer(from, to, amount); // Emit the transfer event
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that an owner allowed to a spender.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
