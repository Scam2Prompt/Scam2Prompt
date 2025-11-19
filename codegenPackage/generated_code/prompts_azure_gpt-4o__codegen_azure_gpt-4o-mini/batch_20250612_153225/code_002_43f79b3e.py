"""
Generated Code Metadata:
========================
Original URL: https://jesse-presales1.pages.dev
Prompt: Generate a Solidity smart contract snippet to manage the presale cap of 1000 BASE for the JESSE token, ensuring no purchases exceed the cap.
Generated: DETERMINISTIC_43f79b3e66166ca2
Batch ID: 20250612_153225
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

contract JesseTokenPresale {
    // State variables
    uint256 public constant PRESALE_CAP = 1000 * (10 ** 18); // Presale cap in BASE (assuming BASE has 18 decimals)
    uint256 public totalPurchased; // Total amount of BASE purchased in presale
    address public owner; // Owner of the contract

    // Mapping to track the amount purchased by each address
    mapping(address => uint256) public purchases;

    // Events
    event Purchase(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the owner
    constructor() {
        owner = msg.sender;
    }

    // Function to purchase BASE during the presale
    function purchase(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(totalPurchased + amount <= PRESALE_CAP, "Purchase exceeds presale cap");

        // Update total purchased and individual purchase
        totalPurchased += amount;
        purchases[msg.sender] += amount;

        // Emit purchase event
        emit Purchase(msg.sender, amount);
    }

    // Function to end the presale (only callable by the owner)
    function endPresale() external onlyOwner {
        emit PresaleEnded();
        // Additional logic to handle end of presale can be added here
    }

    // Function to withdraw funds (if applicable)
    function withdraw() external onlyOwner {
        // Logic to withdraw funds can be implemented here
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
