"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marvinonbase.pages.dev
Prompt: Write a smart contract in Solidity for a token with similar tokenomics to Marvin, including features like a 1% tax for burns, a 5% tax for marketing and app development, and a reserved supply for exchange listings and burns.
Generated: DETERMINISTIC_25d3df7651012b2f
Batch ID: 20250612_152358
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
 * @title MarvinToken
 * @dev ERC20 Token implementation with tokenomics similar to Marvin.
 * Includes burn tax, marketing/app development tax, and reserved supply for exchange listings and burns.
 */
contract MarvinToken {
    // Token details
    string public name = "MarvinToken";
    string public symbol = "MARVIN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Tax rates
    uint256 public burnTaxRate = 1; // 1%
    uint256 public marketingTaxRate = 5; // 5%

    // Address to receive marketing/app development tax
    address public marketingWallet;

    // Reserved supply for exchange listings and burns
    uint256 public reservedSupply;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token with total supply and reserved supply.
     * @param _totalSupply The total supply of tokens.
     * @param _reservedSupply The reserved supply for exchange listings and burns.
     * @param _marketingWallet The address to receive marketing/app development tax.
     */
    constructor(uint256 _totalSupply, uint256 _reservedSupply, address _marketingWallet) {
        require(_reservedSupply <= _totalSupply, "Reserved supply cannot exceed total supply");
        require(_marketingWallet != address(0), "Invalid marketing wallet address");

        totalSupply = _totalSupply;
        reservedSupply = _reservedSupply;
        marketingWallet = _marketingWallet;

        // Mint the total supply to the deployer
        balances[msg.sender] = totalSupply - reservedSupply;
        balances[address(this)] = reservedSupply;

        emit Transfer(address(0), msg.sender, totalSupply - reservedSupply);
        emit Transfer(address(0), address(this), reservedSupply);
    }

    /**
     * @dev Returns the balance of a given account.
     * @param account The address of the account.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient, applying taxes.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return success Whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool success) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the caller.
     * @param spender The address of the spender.
     * @param amount The amount of tokens to approve.
     * @return success Whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool success) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one account to another, applying taxes.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return success Whether the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool success) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Internal function to handle token transfers, applying taxes.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(balances[sender] >= amount, "Insufficient balance");

        uint256 burnTax = (amount * burnTaxRate) / 100;
        uint256 marketingTax = (amount * marketingTaxRate) / 100;
        uint256 transferAmount = amount - burnTax - marketingTax;

        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        balances[marketingWallet] += marketingTax;
        totalSupply -= burnTax;

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, marketingWallet, marketingTax);
        emit Transfer(sender, address(0), burnTax); // Burn address
    }

    /**
     * @dev Returns the allowance of a spender for a given account.
     * @param owner The address of the owner.
     * @param spender The address of the spender.
     * @return The allowance of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
