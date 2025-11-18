"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-token.pages.dev
Prompt: Write a smart contract in Solidity for a deflationary token similar to $GFOX, incorporating a burn mechanism that reduces the circulating supply with each transaction.
Generated: DETERMINISTIC_09d526b60ca4e148
Batch ID: 20250612_151024
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
 * @dev Implements a deflationary ERC20 token with a burn mechanism on each transaction.
 */
contract DeflationaryToken {
    string public name = "DeflationaryToken";
    string public symbol = "DFT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Burn rate in percentage (e.g., 1 for 1%)
    uint256 public burnRate = 1;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Contract constructor that initializes the total supply and assigns it to the owner.
     * @param initialSupply Initial token supply
     */
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        totalSupply = initialSupply * (10 ** decimals);
        _balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query the balance of
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient, applying the burn mechanism.
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender Address of the spender
     * @param amount Amount of tokens to approve
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from a sender to a recipient, applying the burn mechanism.
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        _allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the allowance of a spender for a given owner.
     * @param owner Address of the token owner
     * @param spender Address of the spender
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle transfers and burn tokens.
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        // Calculate burn amount
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        _balances[sender] -= amount;
        _balances[recipient] += transferAmount;
        totalSupply -= burnAmount;

        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, address(0), burnAmount); // Emitting burn event as transfer to zero address
    }
}
```
