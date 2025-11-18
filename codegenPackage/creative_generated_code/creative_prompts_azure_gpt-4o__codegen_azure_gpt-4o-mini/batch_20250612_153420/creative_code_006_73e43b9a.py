"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1edsdoggggggggggggg.pages.dev
Prompt: Provide code for tracking ETH deposits in a smart contract and updating the presale progress, ensuring the cap of 1000 ETH is enforced.
Generated: DETERMINISTIC_73e43b9ae31e1a65
Batch ID: 20250612_153420
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

contract Presale {
    // Address of the owner who can manage the presale
    address public owner;
    
    // Maximum cap for the presale in wei (1 ETH = 1e18 wei)
    uint256 public constant MAX_CAP = 1000 ether; 
    
    // Total amount of ETH deposited in the presale
    uint256 public totalDeposited;

    // Event to log deposits
    event Deposit(address indexed investor, uint256 amount);
    
    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to deposit ETH into the presale
    function deposit() external payable {
        // Check that the deposit amount is greater than 0
        require(msg.value > 0, "Deposit must be greater than 0");

        // Check that the new total does not exceed the max cap
        require(totalDeposited + msg.value <= MAX_CAP, "Cap exceeded");

        // Update the total deposited amount
        totalDeposited += msg.value;

        // Emit a deposit event
        emit Deposit(msg.sender, msg.value);
    }

    // Function to withdraw remaining ETH from the presale, callable by the owner
    function withdraw() external onlyOwner {
        // Calculate the total balance of the contract
        uint256 balance = address(this).balance;
        
        // Ensure that the balance is greater than 0
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        
        // Ensure the transfer was successful
        require(success, "Transfer failed");
    }

    // Function to check the current balance of the contract
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to check the total amount deposited
    function getTotalDeposited() external view returns (uint256) {
        return totalDeposited;
    }
    
    // Fallback function to prevent accidental ETH transfers to the contract
    receive() external payable {
        revert("Direct transfers not allowed; use deposit() function.");
    }
}
```
