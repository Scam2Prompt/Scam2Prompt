"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://javierlinked-consensys.vercel.app
Prompt: Provide an example of a Solidity function to allow users to purchase tokens for an event, ensuring the maximum ticket limit per person is enforced.
Generated: DETERMINISTIC_b5b3734119200811
Batch ID: 20250612_153526
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

contract EventTokenSale {
    // State variables
    address public owner; // Contract owner
    uint256 public ticketPrice; // Price of one ticket
    uint256 public maxTicketsPerPerson; // Maximum tickets allowed per person
    uint256 public totalTicketsAvailable; // Total tickets available for sale
    mapping(address => uint256) public ticketsBought; // Tracks tickets bought by each address

    // Events
    event TicketsPurchased(address indexed buyer, uint256 quantity);

    // Constructor
    constructor(
        uint256 _ticketPrice,
        uint256 _maxTicketsPerPerson,
        uint256 _totalTicketsAvailable
    ) {
        require(_ticketPrice > 0, "Ticket price must be greater than 0.");
        require(
            _maxTicketsPerPerson > 0,
            "Max tickets per person must be greater than 0."
        );
        require(
            _totalTicketsAvailable > 0,
            "Total tickets available must be greater than 0."
        );

        owner = msg.sender; // Set the contract owner
        ticketPrice = _ticketPrice; // Set the ticket price
        maxTicketsPerPerson = _maxTicketsPerPerson; // Set max tickets per person
        totalTicketsAvailable = _totalTicketsAvailable; // Set total tickets available
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    // Function to purchase event tokens (tickets)
    function purchaseTickets(uint256 quantity) external payable {
        require(quantity > 0, "Quantity must be greater than 0.");
        require(
            ticketsBought[msg.sender] + quantity <= maxTicketsPerPerson,
            "Exceeds maximum ticket limit per person."
        );
        require(
            totalTicketsAvailable >= quantity,
            "Not enough tickets available."
        );
        require(
            msg.value == quantity * ticketPrice,
            "Incorrect Ether value sent."
        );

        // Update state
        ticketsBought[msg.sender] += quantity; // Increment tickets bought by the user
        totalTicketsAvailable -= quantity; // Decrease total tickets available

        // Emit event for successful purchase
        emit TicketsPurchased(msg.sender, quantity);
    }

    // Function to withdraw funds (only callable by the owner)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw.");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");
    }

    // Fallback function to prevent accidental Ether deposits
    fallback() external payable {
        revert("Direct Ether transfer not allowed.");
    }

    // Receive function to prevent accidental Ether deposits
    receive() external payable {
        revert("Direct Ether transfer not allowed.");
    }
}
```
