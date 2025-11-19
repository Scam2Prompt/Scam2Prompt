"""
Generated Code Metadata:
========================
Original URL: https://taxfarmxyz.pages.dev
Prompt: Generate a smart contract in Solidity for a token on the Ethereum blockchain that implements a tax farming mechanism, where a percentage of each transaction is automatically collected as revenue.
Generated: DETERMINISTIC_ba46938e47efcb56
Batch ID: 20250622_204919
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
 * @title TaxableToken
 * @dev ERC20 token with a tax farming mechanism where a percentage of each transaction is collected as revenue.
 */
contract TaxableToken {
    // Token details
    string public name = "TaxableToken";
    string public symbol = "TAX";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Address where tax revenue is collected
    address public taxCollector;

    // Tax rate (percentage of transaction amount, e.g., 2 for 2%)
    uint256 public taxRate;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token and set the tax collector and tax rate.
     * @param _initialSupply Initial supply of tokens.
     * @param _taxCollector Address where tax revenue will be collected.
     * @param _taxRate Tax rate as a percentage (e.g., 2 for 2%).
     */
    constructor(uint256 _initialSupply, address _taxCollector, uint256 _taxRate) {
        require(_taxCollector != address(0), "Tax collector address cannot be zero");
        require(_taxRate <= 100, "Tax rate must be between 0 and 100");

        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        taxCollector = _taxCollector;
        taxRate = _taxRate;

        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient, applying the tax rate.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender Address to approve.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another, applying the tax rate.
     * @param sender Address to transfer tokens from.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender can transfer on behalf of an owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle token transfers, applying the tax rate.
     * @param sender Address to transfer tokens from.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Sender address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        // Calculate tax amount
        uint256 taxAmount = (amount * taxRate) / 100;
        uint256 transferAmount = amount - taxAmount;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        balances[taxCollector] += taxAmount;

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, taxCollector, taxAmount);
    }
}
```
