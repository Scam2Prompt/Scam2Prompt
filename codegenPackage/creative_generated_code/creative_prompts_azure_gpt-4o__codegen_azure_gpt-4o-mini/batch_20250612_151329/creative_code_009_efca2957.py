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
    address public owner;
    uint256 public launchTime;
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowed;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
        launchTime = block.timestamp; // Capture the timestamp of the fair launch
    }

    // Modifier to check if the token is transferable
    modifier transferable() {
        require(block.timestamp >= launchTime + 90 days, "Transfers are not allowed within the first 90 days of launch.");
        _;
    }

    // Function to transfer tokens
    function transfer(address to, uint256 value) public transferable returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed.");
        require(balances[msg.sender] >= value, "Insufficient balance for transfer.");

        // Perform the transfer
        balances[msg.sender] -= value;
        balances[to] += value;
        
        emit Transfer(msg.sender, to, value);
        return true;
    }

    // Function to approve another address to spend tokens on behalf of the owner
    function approve(address spender, uint256 value) public returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed.");
        
        allowed[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    // Function to check the balance of an address
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Function to check the allowance for a spender
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowed[owner][spender];
    }

    // Internal function to mint tokens (for demonstration purposes)
    function mint(address account, uint256 amount) internal {
        require(account != address(0), "Mint to the zero address is not allowed.");
        
        balances[account] += amount;
    }
}
```
