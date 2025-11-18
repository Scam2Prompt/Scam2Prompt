"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://angelwings.pages.dev
Prompt: Write a smart contract in Solidity that mimics the functionality of the "Pepe 2.0" token, using the contract address format shown on the website.
Generated: DETERMINISTIC_51031e9988156815
Batch ID: 20250612_151329
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
 * @title Pepe2Token
 * @dev ERC20 Token that mimics the functionality of "Pepe 2.0" token.
 */
contract Pepe2Token {
    // Token metadata
    string public name = "Pepe 2.0";
    string public symbol = "PEPE2";
    uint8 public decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track token balances
    mapping(address => uint256) private balances;

    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events declaration
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner address
    address public owner;

    // Modifier to restrict access to owner-only functionality
    modifier onlyOwner() {
        require(msg.sender == owner, "Pepe2Token: Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with total supply and assign all tokens to the owner.
     * @param _initialSupply Initial supply of tokens (in wei).
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account The address whose balance is to be queried.
     * @return The balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens to a specific address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return Whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Pepe2Token: Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Pepe2Token: Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve another address to spend tokens on your behalf.
     * @param spender The address authorized to spend tokens.
     * @param amount The maximum amount of tokens authorized for spending.
     * @return Whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Pepe2Token: Approval to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowances.
     * @param sender The address from which tokens are transferred.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return Whether the transfer was successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(sender != address(0), "Pepe2Token: Transfer from the zero address is not allowed");
        require(recipient != address(0), "Pepe2Token: Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Pepe2Token: Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Pepe2Token: Transfer amount exceeds allowance");

        balances[sender] -= amount;
        balances[recipient] += amount;

        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Get the allowance for a spender given by the owner.
     * @param owner The address that owns the tokens.
     * @param spender The address that is authorized to spend tokens.
     * @return The remaining allowance of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Mint new tokens and add them to the total supply. Only the owner can call this function.
     * @param amount The amount of tokens to mint.
     */
    function mint(uint256 amount) public onlyOwner {
        totalSupply += amount;
        balances[owner] += amount;

        emit Transfer(address(0), owner, amount);
    }

    /**
     * @dev Burn tokens and reduce the total supply. Only the owner can call this function.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public onlyOwner {
        require(balances[owner] >= amount, "Pepe2Token: Insufficient balance to burn");

        totalSupply -= amount;
        balances[owner] -= amount;

        emit Transfer(owner, address(0), amount);
    }
}
```
