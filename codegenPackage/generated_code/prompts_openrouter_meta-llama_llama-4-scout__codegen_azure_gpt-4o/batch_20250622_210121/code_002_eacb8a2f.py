"""
Generated Code Metadata:
========================
Original URL: https://samoyedcoin-en.web.app
Prompt: Generate a smart contract code snippet for a tokenomics system similar to Samoyedcoin's, including airdrop functionality.
Generated: DETERMINISTIC_eacb8a2fe6f8e206
Batch ID: 20250622_210121
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
 * @title Tokenomics Smart Contract
 * @dev ERC20-based token with airdrop functionality
 */
contract SamoyedToken {
    // Token details
    string public name = "SamoyedToken";
    string public symbol = "SAMO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Airdrop(address indexed recipient, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    // Function to check the balance of an account
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Function to transfer tokens
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // Function to approve tokens for spending
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Function to check the allowance of a spender
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Function to transfer tokens on behalf of another account
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Owner-only function to perform an airdrop
    function airdrop(address[] memory recipients, uint256 amount) public onlyOwner {
        require(amount > 0, "Airdrop amount must be greater than zero");

        uint256 totalAirdropAmount = recipients.length * amount;
        require(balances[owner] >= totalAirdropAmount, "Insufficient balance for airdrop");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(recipient != address(0), "Airdrop to the zero address");

            balances[owner] -= amount;
            balances[recipient] += amount;

            emit Airdrop(recipient, amount);
            emit Transfer(owner, recipient, amount);
        }
    }
}
```
