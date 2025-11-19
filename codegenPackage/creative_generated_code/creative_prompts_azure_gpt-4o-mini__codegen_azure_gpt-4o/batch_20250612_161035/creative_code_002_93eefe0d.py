"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokcoin.pages.dev
Prompt: Create a code snippet in Solidity to implement a smart contract for the GROK token, including features like token burning and tax-free transactions.
Generated: DETERMINISTIC_93eefe0db4981c32
Batch ID: 20250612_161035
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
 * @title GROK Token Smart Contract
 * @dev Implements a burnable ERC20 token with tax-free transaction functionality
 */
contract GROKToken {
    // ERC20 token details
    string public name = "GROK Token";
    string public symbol = "GROK";
    uint8 public decimals = 18; 
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the token contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Contract constructor
    constructor(uint256 _initialSupply) {
        owner = msg.sender; // Assign the deployer as the owner
        totalSupply = _initialSupply * (10 ** uint256(decimals)); // Set the total supply with decimals
        balances[owner] = totalSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, totalSupply); // Emit the initial transfer event
    }

    /**
     * @dev Returns the balance of a specific address
     * @param account The address to query the balance of
     * @return The balance of the address
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address
     * @param to The recipient's address
     * @param amount The amount of tokens to transfer
     * @return success True if the transfer was successful
     */
    function transfer(address to, uint256 amount) public returns (bool success) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);

        return true;
    }

    /**
     * @dev Approves a spender to spend a specific amount of tokens on behalf of the owner
     * @param spender The spender's address
     * @param amount The amount to approve
     * @return success True if the approval was successful
     */
    function approve(address spender, uint256 amount) public returns (bool success) {
        require(spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Returns the allowance of a spender for a specific account
     * @param account The account that owns the tokens
     * @param spender The spender's address
     * @return The allowance of the spender
     */
    function allowance(address account, address spender) public view returns (uint256) {
        return allowances[account][spender];
    }

    /**
     * @dev Transfers tokens from one account to another using allowance
     * @param from The sender's address
     * @param to The recipient's address
     * @param amount The amount to transfer
     * @return success True if the transfer was successful
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool success) {
        require(from != address(0) && to != address(0), "Cannot use the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;
        emit Transfer(from, to, amount);

        return true;
    }

    /**
     * @dev Burns a specific amount of tokens, reducing the total supply
     * @param amount The amount of tokens to burn
     * @return success True if the burn was successful
     */
    function burn(uint256 amount) public returns (bool success) {
        require(balances[msg.sender] >= amount, "Insufficient balance to burn");

        balances[msg.sender] -= amount;
        totalSupply -= amount;
        emit Burn(msg.sender, amount);

        return true;
    }

    /**
     * @dev Allows the owner to perform tax-free transfers
     * @param from The sender's address
     * @param to The recipient's address
     * @param amount The amount to transfer
     * @return success True if the transfer was successful
     */
    function taxFreeTransfer(address from, address to, uint256 amount) public onlyOwner returns (bool success) {
        require(from != address(0) && to != address(0), "Cannot use the zero address");
        require(balances[from] >= amount, "Insufficient balance");

        balances[from] -= amount;
        balances[to] += amount;
        emit Transfer(from, to, amount);

        return true;
    }
}
```
