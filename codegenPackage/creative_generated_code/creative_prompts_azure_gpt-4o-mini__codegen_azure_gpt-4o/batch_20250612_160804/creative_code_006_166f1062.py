"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-e.pages.dev
Prompt: Describe how to utilize the DOGE20 tokenomics in a smart contract to ensure fixed supply and prevent inflation.
Generated: DETERMINISTIC_166f1062631b5f80
Batch ID: 20250612_160804
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
 * @title DOGE20Token
 * @dev A simple ERC20 token implementation with fixed supply to ensure no inflation.
 */
contract DOGE20Token {
    // Token details
    string public name = "DOGE20";
    string public symbol = "DOGE20";
    uint8 public decimals = 18;

    // Total fixed token supply
    uint256 public immutable totalSupply;

    // Balance mapping to track token ownership
    mapping(address => uint256) private balances;

    // Allowance mapping for delegated transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for transfer and approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Contract deployer address
    address public immutable deployer;

    /**
     * @dev Constructor initializes the fixed supply and assigns all tokens to the deployer.
     * @param _initialSupply The fixed total supply of the token (18 decimal places).
     */
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply;
        deployer = msg.sender;
        balances[deployer] = _initialSupply;

        emit Transfer(address(0), deployer, _initialSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param to The address to transfer to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves the spender to transfer up to the specified amount on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The maximum amount to be spent.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of another address, using their allowance.
     * @param from The address from which tokens will be taken.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        allowances[from][msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that the spender can transfer on behalf of the owner.
     * @param owner The address owning the tokens.
     * @param spender The address authorized to spend.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
