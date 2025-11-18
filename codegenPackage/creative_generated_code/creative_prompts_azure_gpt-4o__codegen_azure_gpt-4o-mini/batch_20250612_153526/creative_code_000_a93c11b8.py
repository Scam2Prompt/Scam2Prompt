"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://javierlinked-consensys.vercel.app
Prompt: Write a smart contract in Solidity to implement a ticketing system similar to TicketChain, including features like setting ticket prices, managing token supply, and limiting the number of tickets sold per person.
Generated: DETERMINISTIC_a93c11b8d2ba1422
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title TicketingSystem
/// @notice A smart contract to manage ticket sales with price setting and limits.
contract TicketingSystem is Ownable {
    // Event emitted when a ticket is purchased
    event TicketPurchased(address indexed buyer, uint256 quantity);

    // Variables to store ticket information
    uint256 public ticketPrice; // Price of each ticket in wei
    uint256 public maxTicketsPerPerson; // Maximum tickets a single address can purchase
    uint256 public totalSupply; // Total number of tickets available
    uint256 public ticketsSold; // Total tickets sold

    // Mapping to track tickets purchased by each address
    mapping(address => uint256) public ticketsBought;

    /// @notice Constructor to initialize the contract with ticket details
    /// @param _ticketPrice Initial price of each ticket in wei
    /// @param _totalSupply Total number of tickets available for sale
    /// @param _maxTicketsPerPerson Maximum tickets a single address can purchase
    constructor(uint256 _ticketPrice, uint256 _totalSupply, uint256 _maxTicketsPerPerson) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        require(_maxTicketsPerPerson > 0, "Max tickets per person must be greater than zero");

        ticketPrice = _ticketPrice;
        totalSupply = _totalSupply;
        maxTicketsPerPerson = _maxTicketsPerPerson;
    }

    /// @notice Function to purchase tickets
    /// @param quantity Number of tickets to purchase
    function purchaseTickets(uint256 quantity) external payable {
        require(quantity > 0, "Quantity must be greater than zero");
        require(msg.value == quantity * ticketPrice, "Incorrect ETH amount sent");
        require(ticketsSold + quantity <= totalSupply, "Not enough tickets available");
        require(ticketsBought[msg.sender] + quantity <= maxTicketsPerPerson, "Exceeds max tickets per person");

        // Update state variables
        ticketsSold += quantity;
        ticketsBought[msg.sender] += quantity;

        // Emit event for ticket purchase
        emit TicketPurchased(msg.sender, quantity);
    }

    /// @notice Function to withdraw contract's balance (owner only)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw");
        payable(owner()).transfer(balance);
    }

    /// @notice Function to set a new ticket price
    /// @param newPrice New price for each ticket in wei
    function setTicketPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "New price must be greater than zero");
        ticketPrice = newPrice;
    }

    /// @notice Function to set a new maximum number of tickets purchasable per person
    /// @param newMaxTickets New maximum tickets per person
    function setMaxTicketsPerPerson(uint256 newMaxTickets) external onlyOwner {
        require(newMaxTickets > 0, "New max tickets must be greater than zero");
        maxTicketsPerPerson = newMaxTickets;
    }

    /// @notice Function to get the total tickets sold
    /// @return The number of tickets sold
    function getTotalTicketsSold() external view returns (uint256) {
        return ticketsSold;
    }

    /// @notice Function to get the ticket price
    /// @return Current ticket price in wei
    function getTicketPrice() external view returns (uint256) {
        return ticketPrice;
    }
}
```
