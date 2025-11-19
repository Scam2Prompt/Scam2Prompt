"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity for an ERC20 token named ALIEN with a total supply of 100,000,000 tokens.
Generated: DETERMINISTIC_2515aebfab6ba9b9
Batch ID: 20250612_160940
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
 * @title ALIEN Token
 * @dev Implementation of the ERC20 standard token with fixed supply
 */
contract AlienToken {
    // ERC20 Standard Variables
    string public name = "ALIEN";
    string public symbol = "ALIEN";
    uint8 public decimals = 18; // Standard decimal places for ERC20 tokens

    uint256 public totalSupply; // Total supply of tokens
    mapping(address => uint256) private balances; // Balances of accounts
    mapping(address => mapping(address => uint256)) private allowances; // Allowances for spending on behalf of others

    // Events for ERC20 standard
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Address of the contract deployer
    address public owner;

    /**
     * @dev Constructor to initialize the token and mint the total supply to the deployer
     */
    constructor() {
        owner = msg.sender; // Set the deployer as the contract owner
        totalSupply = 100_000_000 * (10 ** uint256(decimals)); // Mint 100,000,000 tokens with 18 decimals
        balances[owner] = totalSupply; // Assign total supply to the deployer's address

        emit Transfer(address(0), owner, totalSupply); // Emit Transfer event for initial minting
    }

    /**
     * @dev Returns the balance of an account
     * @param account Address of the account
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a recipient
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return success True if the transfer is successful
     */
    function transfer(address recipient, uint256 amount) public returns (bool success) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[msg.sender] >= amount, "ERC20: transfer amount exceeds balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the msg.sender
     * @param spender Address of the spender
     * @param amount Amount of tokens to approve
     * @return success True if the approval is successful
     */
    function approve(address spender, uint256 amount) public returns (bool success) {
        require(spender != address(0), "ERC20: approve to the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the allowance of a spender for a specific owner
     * @param owner Address of the token holder
     * @param spender Address of the spender
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one account to another using an allowance
     * @param sender Address of the account sending the tokens
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return success True if the transfer is successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool success) {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[sender] >= amount, "ERC20: transfer amount exceeds balance");
        require(allowances[sender][msg.sender] >= amount, "ERC20: transfer amount exceeds allowance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }
}
```
