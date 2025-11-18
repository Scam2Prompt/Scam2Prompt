"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fffrfh.pages.dev
Prompt: Write a Solidity function that ensures MOR tokens are non-transferable for the first 90 days after fair launch, as described in the Morpheus documentation. Include logic to enable transfers after this period.
Generated: DETERMINISTIC_efca2957c7c720c4
Batch ID: 20250612_151329
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

contract MORToken {
    // State variables
    string public name = "MOR Token";
    string public symbol = "MOR";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    uint256 public launchTimestamp;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier to ensure transfers are allowed after the 90-day lock period
    modifier transferAllowed() {
        require(block.timestamp >= launchTimestamp + 90 days, "Transfers are locked for the first 90 days after launch.");
        _;
    }

    constructor(uint256 _initialSupply) {
        // Initialize total supply and assign all tokens to the deployer
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        launchTimestamp = block.timestamp; // Record the launch timestamp
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Function to check the balance of a specific address
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    // Transfer function with 90-day lock enforcement
    function transfer(address recipient, uint256 amount) external transferAllowed returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        require(recipient != address(0), "Cannot transfer to zero address.");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Approve function to allow spending by other accounts
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Cannot approve zero address.");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // TransferFrom function with 90-day lock enforcement
    function transferFrom(address sender, address recipient, uint256 amount) external transferAllowed returns (bool) {
        require(balances[sender] >= amount, "Insufficient balance.");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded.");
        require(recipient != address(0), "Cannot transfer to zero address.");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Function to check the allowance for specific accounts
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
