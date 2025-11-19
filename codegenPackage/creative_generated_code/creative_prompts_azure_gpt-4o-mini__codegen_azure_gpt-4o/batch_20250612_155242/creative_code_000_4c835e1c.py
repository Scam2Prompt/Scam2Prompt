"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe--dashboard.pages.dev
Prompt: Generate a smart contract for the $MPEPE token that includes features like transaction burning and ERC-20 compatibility.
Generated: DETERMINISTIC_4c835e1cccab55ca
Batch ID: 20250612_155242
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
 * @title MPEPE Token
 * @dev ERC-20 token implementation with transaction burn functionality.
 */
contract MPEPEToken {
    // Token metadata
    string public name = "MPEPE Token";
    string public symbol = "MPEPE";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to manage allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Burn rate (percentage of tokens burned per transaction)
    uint256 public burnRate = 2; // Example: 2%

    // Events for transparency
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 value);

    // Constructor to initialize the token with a supply
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than 0");
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the sender to the recipient, with burn applied.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one address to another, applying burn rate.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        _transfer(sender, recipient, amount);
        allowances[sender][msg.sender] -= amount;
        return true;
    }

    /**
     * @dev Internal function to perform token transfers with burn applied.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        totalSupply -= burnAmount;

        // Emit events
        emit Transfer(sender, recipient, transferAmount);
        emit Burn(sender, burnAmount);
    }
}
```
