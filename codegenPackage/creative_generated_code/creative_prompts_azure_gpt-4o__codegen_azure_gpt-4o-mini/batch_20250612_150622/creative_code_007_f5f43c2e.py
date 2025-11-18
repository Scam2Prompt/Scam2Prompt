"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://normilio.pages.dev
Prompt: Create a smart contract snippet for managing $NORMILIO token claims, emphasizing the "no funny business" principle.
Generated: DETERMINISTIC_f5f43c2e570e5a65
Batch ID: 20250612_150622
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

contract NormilioTokenClaim {
    // Define state variables
    string public constant name = "Normilio Token";
    string public constant symbol = "NORMILIO";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => uint256) private claims;
    address public owner;

    // Events for logging
    event Claimed(address indexed claimant, uint256 amount);
    event TokensIssued(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to check ownership
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 initialSupply) {
        owner = msg.sender; // Set the contract creator as the owner
        totalSupply = initialSupply * (10 ** uint256(decimals)); // Initialize total supply
        balances[owner] = totalSupply; // Assign total supply to the owner
    }

    // Function to issue tokens to a specific address
    function issueTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        
        balances[recipient] += amount;
        totalSupply += amount;
        
        emit TokensIssued(recipient, amount);
    }

    // Function to claim tokens
    function claimTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(claims[msg.sender] + amount <= balances[msg.sender], "Insufficient balance to claim");

        claims[msg.sender] += amount; // Track claims for the user
        balances[msg.sender] -= amount; // Deduct from user balance
        
        emit Claimed(msg.sender, amount);
    }

    // Function to get balance of an address
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    // Function to get claims of an address
    function claimsOf(address account) external view returns (uint256) {
        return claims[account];
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
