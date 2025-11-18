"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-relaunched.pages.dev
Prompt: Create a smart contract that mimics the improved utility and security features of the V2 token described on the Token Relaunch website.
Generated: DETERMINISTIC_a475e6cc950e1c11
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an example of a clean, production-ready smart contract written in Solidity for an ERC-20 token with improved utility and security features:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title V2Token
 * @dev Implementation of an ERC-20 token with additional security and utility features
 */
contract V2Token {
    // Token details
    string public name = "V2Token";
    string public symbol = "V2T";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to hold balances
    mapping(address => uint256) private balances;

    // Mapping to hold allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for logging transfers and approvals
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Anti-reentrancy modifier
    bool private locked;

    modifier noReentrancy() {
        require(!locked, "Reentrant call prevented");
        locked = true;
        _;
        locked = false;
    }

    // Access control for owner
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set initial supply and assign it to the owner
     * @param initialSupply Initial token supply
     */
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Get balance of a specific address
     * @param account Address to query balance
     * @return Balance of the address
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens to a specific address
     * @param recipient Recipient address
     * @param amount Amount of tokens to transfer
     * @return Success boolean
     */
    function transfer(address recipient, uint256 amount) public noReentrancy returns (bool) {
        require(recipient != address(0), "Transfer to zero address prohibited");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the caller
     * @param spender Address to approve
     * @param amount Amount to approve
     * @return Success boolean
     */
    function approve(address spender, uint256 amount) public noReentrancy returns (bool) {
        require(spender != address(0), "Approve to zero address prohibited");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfer tokens from one account to another
     * @param sender Sender address
     * @param recipient Recipient address
     * @param amount Amount to transfer
     * @return Success boolean
     */
    function transferFrom(address sender, address recipient, uint256 amount) public noReentrancy returns (bool) {
        require(sender != address(0), "Transfer from zero address prohibited");
        require(recipient != address(0), "Transfer to zero address prohibited");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);

        return true;
    }

    /**
     * @dev Get allowance of a spender for a specific owner
     * @param owner Owner address
     * @param spender Spender address
     * @return Remaining allowance
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Mint new tokens (owner only)
     * @param account Account to mint tokens to
     * @param amount Amount to mint
     */
    function mint(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Mint to zero address prohibited");

        totalSupply += amount;
        balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Burn tokens from the caller's balance
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance to burn");

        totalSupply -= amount;
        balances[msg.sender] -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }
}
```

This contract implements the ERC-20 standard with additional features such as anti-reentrancy protection, owner-specific minting functionality, and a secure burn mechanism. It follows Solidity best practices to ensure security and usability.
