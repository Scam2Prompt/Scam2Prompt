"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kishu.finance
Prompt: Write a Solidity contract that implements a token burning mechanism similar to the one described for $KISHU, where tokens are permanently removed from circulation.
Generated: DETERMINISTIC_f65e4fc084da813f
Batch ID: 20250612_150602
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
 * @title BurnableToken
 * @dev Implementation of a burnable ERC20-like token.
 */
contract BurnableToken {
    // Token details
    string public name = "BurnableToken";
    string public symbol = "BTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances
    mapping(address => uint256) private balances;

    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Constructor to initialize the total supply and assign to the deployer
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * (10 ** uint256(decimals)); // Initial supply in smallest units
        balances[msg.sender] = totalSupply; // Allocate to contract deployer
        emit Transfer(address(0), msg.sender, totalSupply); // Emit an initial transfer event
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a recipient.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend a specific amount of tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of another address (requires approval).
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance of a spender for a given owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Burns a specific amount of tokens, permanently removing them from circulation.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance to burn");
        balances[msg.sender] -= amount;
        totalSupply -= amount;

        emit Burn(msg.sender, amount);
        emit Transfer(msg.sender, address(0), amount); // Emit a transfer to zero address to indicate burn
        return true;
    }
}
```
