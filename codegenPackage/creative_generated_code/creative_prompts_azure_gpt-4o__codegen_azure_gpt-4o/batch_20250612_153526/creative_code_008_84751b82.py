"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://javierlinked-consensys.vercel.app
Prompt: Write a function in Solidity to calculate the remaining ticket supply for an event after tokens are purchased, ensuring compliance with the maximum sell limit per person.
Generated: DETERMINISTIC_84751b82126f1de6
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

/**
 * @title EventTicketManager
 * @dev Manages ticket supply and ensures compliance with individual purchase limits.
 */
contract EventTicketManager {
    // State variables
    uint256 public totalTickets; // Total tickets available for the event
    uint256 public maxTicketsPerPerson; // Maximum number of tickets one person can purchase
    mapping(address => uint256) public ticketsPurchased; // Tracks tickets purchased by each address

    /**
     * @dev Constructor to initialize ticket supply and purchase limit.
     * @param _totalTickets The total number of tickets for the event.
     * @param _maxTicketsPerPerson The maximum tickets each person can purchase.
     */
    constructor(uint256 _totalTickets, uint256 _maxTicketsPerPerson) {
        require(_totalTickets > 0, "Total tickets must be greater than zero");
        require(_maxTicketsPerPerson > 0, "Maximum tickets per person must be greater than zero");
        totalTickets = _totalTickets;
        maxTicketsPerPerson = _maxTicketsPerPerson;
    }

    /**
     * @dev Calculates the remaining ticket supply after a purchase.
     * @param buyer The address of the buyer.
     * @param quantity The number of tickets the buyer wants to purchase.
     * @return remainingTickets The remaining tickets after the purchase.
     */
    function purchaseTickets(address buyer, uint256 quantity) external returns (uint256 remainingTickets) {
        require(buyer != address(0), "Invalid buyer address");
        require(quantity > 0, "Quantity must be greater than zero");
        require(quantity <= maxTicketsPerPerson, "Exceeded maximum tickets per person");
        require(ticketsPurchased[buyer] + quantity <= maxTicketsPerPerson, "Buyer exceeds purchase limit");
        require(quantity <= totalTickets, "Not enough tickets available");

        // Update state
        ticketsPurchased[buyer] += quantity;
        totalTickets -= quantity;

        // Return remaining ticket supply
        return totalTickets;
    }
}
```
