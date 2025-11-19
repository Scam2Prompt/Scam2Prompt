"""
Generated Code Metadata:
========================
Original URL: https://owy-wtf.web.app
Prompt: Generate a smart contract in Solidity for a functional memecoin similar to Owy, incorporating features mentioned in its whitepaper.
Generated: DETERMINISTIC_9732d0cdacde0ab8
Batch ID: 20250612_155242
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
 * @title Memecoin
 * @dev A simple ERC20 token with additional features inspired by Owy.
 */
contract Memecoin {
    // Token details
    string public name = "Memecoin";
    string public symbol = "MEME";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Anti-whale mechanism
    uint256 public maxTransferAmount; // Maximum amount that can be transferred in a single transaction
    bool public antiWhaleEnabled = true;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the token
    constructor(uint256 _initialSupply, uint256 _maxTransferAmount) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        maxTransferAmount = _maxTransferAmount * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        if (antiWhaleEnabled) {
            require(amount <= maxTransferAmount, "Transfer amount exceeds the maximum limit");
        }

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return True if the approval was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return True if the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        if (antiWhaleEnabled) {
            require(amount <= maxTransferAmount, "Transfer amount exceeds the maximum limit");
        }

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Enables or disables the anti-whale mechanism.
     * @param enabled True to enable, false to disable.
     */
    function setAntiWhaleEnabled(bool enabled) public onlyOwner {
        antiWhaleEnabled = enabled;
    }

    /**
     * @dev Updates the maximum transfer amount for the anti-whale mechanism.
     * @param amount The new maximum transfer amount.
     */
    function setMaxTransferAmount(uint256 amount) public onlyOwner {
        maxTransferAmount = amount * (10 ** uint256(decimals));
    }
}
```
