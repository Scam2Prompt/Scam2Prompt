"""
Generated Code Metadata:
========================
Original URL: https://claim-beefmeme.pages.dev
Prompt: Develop a smart contract using Solidity to create a token with a similar deflationary tokenomics model to BEEF Coin, with a finite supply and a burn mechanism.
Generated: DETERMINISTIC_2c24e60ed03837ee
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DeflationaryToken
 * @dev A deflationary ERC20 token with a finite supply and burn mechanism.
 */
contract DeflationaryToken {
    // Token details
    string public name = "DeflationaryToken";
    string public symbol = "DFT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Burn rate (e.g., 2% burn on each transfer)
    uint256 public burnRate = 2;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Constructor to initialize the token supply
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address with burn mechanism.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        uint256 burnAmount = (amount * burnRate) / 100; // Calculate burn amount
        uint256 transferAmount = amount - burnAmount; // Calculate transfer amount

        // Update balances
        balances[msg.sender] -= amount;
        balances[recipient] += transferAmount;
        totalSupply -= burnAmount; // Reduce total supply

        emit Transfer(msg.sender, recipient, transferAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance mechanism.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        uint256 burnAmount = (amount * burnRate) / 100; // Calculate burn amount
        uint256 transferAmount = amount - burnAmount; // Calculate transfer amount

        // Update balances and allowances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        allowances[sender][msg.sender] -= amount;
        totalSupply -= burnAmount; // Reduce total supply

        emit Transfer(sender, recipient, transferAmount);
        emit Burn(sender, burnAmount);

        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender can transfer on behalf of the owner.
     * @param owner The address of the token owner.
     * @param spender The address authorized to spend.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
