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

/**
 * @title TicketingSystem
 * @dev A smart contract for managing a ticketing system with features like ticket pricing,
 * token supply, and limiting the number of tickets sold per person.
 */
contract TicketingSystem {
    // Owner of the contract
    address public owner;

    // Ticket price in wei
    uint256 public ticketPrice;

    // Maximum number of tickets available
    uint256 public maxSupply;

    // Maximum number of tickets per person
    uint256 public maxTicketsPerPerson;

    // Number of tickets sold
    uint256 public ticketsSold;

    // Mapping to track tickets owned by each address
    mapping(address => uint256) public ticketsOwned;

    // Event emitted when a ticket is purchased
    event TicketPurchased(address indexed buyer, uint256 quantity);

    // Event emitted when the ticket price is updated
    event TicketPriceUpdated(uint256 newPrice);

    // Event emitted when the max supply is updated
    event MaxSupplyUpdated(uint256 newMaxSupply);

    // Event emitted when the max tickets per person is updated
    event MaxTicketsPerPersonUpdated(uint256 newMaxTicketsPerPerson);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with ticket parameters.
     * @param _ticketPrice Initial price of a ticket in wei.
     * @param _maxSupply Maximum number of tickets available.
     * @param _maxTicketsPerPerson Maximum number of tickets that can be purchased by a single person.
     */
    constructor(
        uint256 _ticketPrice,
        uint256 _maxSupply,
        uint256 _maxTicketsPerPerson
    ) {
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        require(_maxSupply > 0, "Max supply must be greater than zero");
        require(
            _maxTicketsPerPerson > 0,
            "Max tickets per person must be greater than zero"
        );

        owner = msg.sender;
        ticketPrice = _ticketPrice;
        maxSupply = _maxSupply;
        maxTicketsPerPerson = _maxTicketsPerPerson;
    }

    /**
     * @dev Function to purchase tickets.
     * @param quantity Number of tickets to purchase.
     */
    function purchaseTickets(uint256 quantity) external payable {
        require(quantity > 0, "Quantity must be greater than zero");
        require(
            ticketsOwned[msg.sender] + quantity <= maxTicketsPerPerson,
            "Exceeds max tickets per person"
        );
        require(ticketsSold + quantity <= maxSupply, "Exceeds max supply");
        require(
            msg.value == ticketPrice * quantity,
            "Incorrect payment amount"
        );

        ticketsOwned[msg.sender] += quantity;
        ticketsSold += quantity;

        emit TicketPurchased(msg.sender, quantity);
    }

    /**
     * @dev Function to update ticket price.
     * @param _ticketPrice New ticket price in wei.
     */
    function updateTicketPrice(uint256 _ticketPrice) external onlyOwner {
        require(_ticketPrice > 0, "Ticket price must be greater than zero");
        ticketPrice = _ticketPrice;

        emit TicketPriceUpdated(_ticketPrice);
    }

    /**
     * @dev Function to update the maximum supply of tickets.
     * @param _maxSupply New maximum supply.
     */
    function updateMaxSupply(uint256 _maxSupply) external onlyOwner {
        require(
            _maxSupply >= ticketsSold,
            "New max supply must be at least equal to tickets sold"
        );
        maxSupply = _maxSupply;

        emit MaxSupplyUpdated(_maxSupply);
    }

    /**
     * @dev Function to update the max tickets per person.
     * @param _maxTicketsPerPerson New max tickets per person.
     */
    function updateMaxTicketsPerPerson(uint256 _maxTicketsPerPerson)
        external
        onlyOwner
    {
        require(
            _maxTicketsPerPerson > 0,
            "Max tickets per person must be greater than zero"
        );
        maxTicketsPerPerson = _maxTicketsPerPerson;

        emit MaxTicketsPerPersonUpdated(_maxTicketsPerPerson);
    }

    /**
     * @dev Function to withdraw funds collected from ticket sales.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
