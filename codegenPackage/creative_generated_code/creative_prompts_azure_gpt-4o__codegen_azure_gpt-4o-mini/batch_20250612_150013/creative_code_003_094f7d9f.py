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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title VIPTicketDistributor
 * @dev Smart contract to distribute VIP tickets to the first 100 users who connect their web3 wallet.
 */
contract VIPTicketDistributor is Ownable {
    // The maximum number of VIP tickets available.
    uint256 public constant MAX_TICKETS = 100;

    // Mapping to track users who have claimed their tickets
    mapping(address => bool) public hasClaimed;

    // Counter for the number of tickets distributed
    uint256 public ticketCount;

    // Event emitted when a ticket is claimed
    event TicketClaimed(address indexed user);

    /**
     * @dev Allows a user to claim a VIP ticket if they are among the first 100 users.
     */
    function claimTicket() external {
        // Check if the user has already claimed a ticket
        require(!hasClaimed[msg.sender], "Ticket already claimed.");
        
        // Check if the maximum number of tickets has been reached
        require(ticketCount < MAX_TICKETS, "All tickets have been claimed.");

        // Mark the user as having claimed a ticket
        hasClaimed[msg.sender] = true;

        // Increment the total ticket count
        ticketCount++;

        // Emit an event for the ticket claim
        emit TicketClaimed(msg.sender);
    }

    /**
     * @dev Function to retrieve the number of tickets already claimed.
     * @return The number of tickets that have been claimed.
     */
    function getClaimedTicketsCount() external view returns (uint256) {
        return ticketCount;
    }

    /**
     * @dev Function to check if a user has claimed a ticket.
     * @param user The address of the user to check.
     * @return True if the user has claimed a ticket, false otherwise.
     */
    function hasUserClaimed(address user) external view returns (bool) {
        return hasClaimed[user];
    }
}
```
