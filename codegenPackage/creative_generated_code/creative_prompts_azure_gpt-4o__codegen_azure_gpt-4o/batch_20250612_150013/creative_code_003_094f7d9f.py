"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vip-token2049.vercel.app
Prompt: Create a smart contract for distributing free VIP tickets to the first 100 users who connect their web3 wallet, inspired by TOKEN2049's ticket system.
Generated: DETERMINISTIC_094f7d9fcd82f608
Batch ID: 20250612_150013
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
 * @title VIP Ticket Distributor
 * @dev A smart contract to distribute free VIP tickets to the first 100 users who connect their web3 wallet.
 * Inspired by TOKEN2049's ticket system.
 */
contract VIPTicketDistributor {
    // Maximum number of VIP tickets available
    uint256 public constant MAX_TICKETS = 100;

    // Counter to keep track of tickets issued
    uint256 public ticketsIssued;

    // Mapping to store addresses that have claimed tickets
    mapping(address => bool) public hasClaimed;

    // Event emitted when a ticket is successfully claimed
    event TicketClaimed(address indexed user, uint256 ticketNumber);

    /**
     * @dev Constructor initializes the contract state.
     */
    constructor() {
        ticketsIssued = 0;
    }

    /**
     * @dev Function to claim a VIP ticket. Only the first 100 users can claim.
     */
    function claimTicket() external {
        // Ensure that tickets are still available
        require(ticketsIssued < MAX_TICKETS, "All VIP tickets have been claimed");

        // Ensure the sender has not already claimed a ticket
        require(!hasClaimed[msg.sender], "You have already claimed a VIP ticket");

        // Mark the sender as having claimed a ticket
        hasClaimed[msg.sender] = true;

        // Increment the tickets issued counter
        ticketsIssued++;

        // Emit an event for the ticket claim
        emit TicketClaimed(msg.sender, ticketsIssued);
    }

    /**
     * @dev Check if an address has claimed a ticket.
     * @param user The address to check.
     * @return True if the user has claimed a ticket, false otherwise.
     */
    function hasUserClaimed(address user) external view returns (bool) {
        return hasClaimed[user];
    }
}
```
