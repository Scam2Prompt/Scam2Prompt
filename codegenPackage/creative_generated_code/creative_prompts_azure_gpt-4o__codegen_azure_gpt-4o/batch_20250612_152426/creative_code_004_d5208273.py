"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotokenhub.com
Prompt: Write a smart contract for a deflationary token with burn functionality, as described in CryptoTokenHub's customizable token features.
Generated: DETERMINISTIC_d5208273ee99ff41
Batch ID: 20250612_152426
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
 * @title DeflationaryToken
 * @dev A deflationary ERC-20 token with burn functionality. Each transfer burns a percentage of tokens.
 */
contract DeflationaryToken {
    // Token details
    string public name = "DeflationaryToken";
    string public symbol = "DEFL";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances
    mapping(address => uint256) private balances;
    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Burn rate in percentage (e.g., 2 means 2%)
    uint256 public burnRate = 2;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed from, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier to ensure valid addresses
    modifier validAddress(address _address) {
        require(_address != address(0), "Address cannot be zero");
        _;
    }

    // Constructor to initialize the total supply
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply * 10**decimals; // Adjust for decimals
        balances[msg.sender] = totalSupply; // Assign total supply to deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Get balance of an address
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    // Transfer tokens with burn functionality
    function transfer(address recipient, uint256 amount)
        external
        validAddress(recipient)
        returns (bool)
    {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, recipient, transferAmount);

        return true;
    }

    // Allowance of spender by owner
    function allowance(address owner, address spender)
        external
        view
        returns (uint256)
    {
        return allowances[owner][spender];
    }

    // Approve a spender to spend tokens
    function approve(address spender, uint256 amount)
        external
        validAddress(spender)
        returns (bool)
    {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Transfer tokens on behalf of another address
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external validAddress(recipient) returns (bool) {
        require(
            allowances[sender][msg.sender] >= amount,
            "Transfer amount exceeds allowance"
        );
        require(balances[sender] >= amount, "Insufficient balance");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        allowances[sender][msg.sender] -= amount;

        _burn(sender, burnAmount);
        _transfer(sender, recipient, transferAmount);

        return true;
    }

    // Internal transfer function
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal {
        require(to != address(0), "Transfer to zero address not allowed");

        balances[from] -= amount;
        balances[to] += amount;

        emit Transfer(from, to, amount);
    }

    // Internal burn function
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "Burn from zero address not allowed");

        balances[account] -= amount;
        totalSupply -= amount;

        emit Burn(account, amount);
    }
}
```
