"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://docs-beefmeme.pages.dev
Prompt: Create a Solidity contract that implements a token burning mechanism for BEEF Coin, similar to the deflationary model described on the website.
Generated: DETERMINISTIC_146ad3e8d740510d
Batch ID: 20250612_155137
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
 * @title BEEF Coin with Burn Mechanism
 * @dev ERC20 token with a deflationary model where tokens can be burned.
 */
contract BeefCoin {
    // State variables
    string public constant name = "BeefCoin";
    string public constant symbol = "BEEF";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Constructor to initialize the total supply
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = initialSupply * (10**uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Public function to get the balance of an address
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Public function to transfer tokens
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Public function to approve tokens for spending by another address
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address is not allowed");
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Public function to transfer tokens from one address to another
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        _transfer(sender, recipient, amount);
        allowances[sender][msg.sender] -= amount;
        return true;
    }

    // Public function to get the allowance of an address
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Public function to burn tokens
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    // Internal function to handle transfers
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }

    // Internal function to handle burning
    function _burn(address burner, uint256 amount) internal {
        require(burner != address(0), "Burn from the zero address is not allowed");
        require(balances[burner] >= amount, "Burn amount exceeds balance");

        balances[burner] -= amount;
        totalSupply -= amount;
        emit Burn(burner, amount);
    }
}
```
