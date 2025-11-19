"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyber-networkrw.web.app
Prompt: How can I create an ERC-20 compatible smart contract to manage rewards like $CYBER for users?
Generated: DETERMINISTIC_b9923412fc2fe8dd
Batch ID: 20250612_161427
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
 * @title CYBER Rewards Token (ERC-20 Token Implementation)
 * @dev This smart contract is an implementation of the ERC-20 standard
 *      and includes functionality for managing rewards like $CYBER for users.
 */
contract CYBERToken {
    // Token details
    string public name = "CYBER Rewards Token";
    string public symbol = "CYBER";
    uint8 public decimals = 18; // Standard for ERC-20 tokens
    uint256 public totalSupply;

    // Balances mapping for each account
    mapping(address => uint256) private balances;

    // Allowances mapping for delegated transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Events as per ERC-20 standard
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /// @notice Constructor initializes the token and assigns total supply to the owner
    /// @param initialSupply Total initial supply of the token
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply * (10 ** uint256(decimals)); // Adjust for decimals
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /// @notice Get the balance of a specific account
    /// @param account Address of the account to query the balance of
    /// @return Balance of the account
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /// @notice Transfer tokens from the sender to a recipient
    /// @param recipient Address to transfer tokens to
    /// @param amount Amount of tokens to transfer
    /// @return Success status
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /// @notice Approve a spender to transfer tokens on behalf of the sender
    /// @param spender Address authorized to spend tokens
    /// @param amount Amount of tokens they are authorized to spend
    /// @return Success status
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Invalid spender address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /// @notice Check the allowance of a spender for a specific owner
    /// @param owner Address of the token owner
    /// @param spender Address of the spender
    /// @return Remaining allowance for the spender
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /// @notice Transfer tokens on behalf of the owner (requires approval)
    /// @param sender Address of the token owner
    /// @param recipient Address to transfer tokens to
    /// @param amount Amount of tokens to transfer
    /// @return Success status
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Invalid sender address");
        require(recipient != address(0), "Invalid recipient address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /// @notice Mint new tokens to a specific address (owner-only)
    /// @param recipient Address to mint tokens to
    /// @param amount Amount of tokens to mint
    function mint(address recipient, uint256 amount) public onlyOwner {
        require(recipient != address(0), "Invalid recipient address");

        uint256 mintAmount = amount * (10 ** uint256(decimals)); // Adjust for decimals
        totalSupply += mintAmount;
        balances[recipient] += mintAmount;

        emit Transfer(address(0), recipient, mintAmount);
    }

    /// @notice Burn tokens from a specific address (owner-only)
    /// @param account Address to burn tokens from
    /// @param amount Amount of tokens to burn
    function burn(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Invalid account address");
        require(balances[account] >= amount, "Insufficient balance to burn");

        uint256 burnAmount = amount * (10 ** uint256(decimals)); // Adjust for decimals
        balances[account] -= burnAmount;
        totalSupply -= burnAmount;

        emit Transfer(account, address(0), burnAmount);
    }
}
```
