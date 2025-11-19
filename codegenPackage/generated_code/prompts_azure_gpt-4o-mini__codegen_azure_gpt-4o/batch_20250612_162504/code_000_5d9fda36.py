"""
Generated Code Metadata:
========================
Original URL: https://sportnode.nl
Prompt: Generate a smart contract for a sports organization using web3 principles as described by Sportnode.
Generated: DETERMINISTIC_5d9fda36e59e8f32
Batch ID: 20250612_162504
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

/**
 * @title SportsOrganizationContract
 * @dev A smart contract for managing sports organizations using Web3 principles.
 *      This contract allows for membership management, event creation, and fund handling.
 */
contract SportsOrganizationContract {
    // Owner of the contract
    address public owner;

    // Struct to represent a member
    struct Member {
        address walletAddress;
        string name;
        bool isActive;
    }

    // Struct to represent an event
    struct Event {
        uint256 id;
        string name;
        uint256 date; // Timestamp of the event
        uint256 ticketPrice; // Price of a ticket in wei
        uint256 ticketsSold;
        bool isActive;
    }

    // Mapping to store members
    mapping(address => Member) public members;

    // Mapping to store events
    mapping(uint256 => Event) public events;

    // Counter for event IDs
    uint256 private eventCounter;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to check if a member is active
    modifier onlyActiveMember() {
        require(members[msg.sender].isActive, "You must be an active member to perform this action");
        _;
    }

    // Event declarations
    event MemberAdded(address indexed walletAddress, string name);
    event MemberRemoved(address indexed walletAddress);
    event EventCreated(uint256 indexed eventId, string name, uint256 date, uint256 ticketPrice);
    event TicketPurchased(uint256 indexed eventId, address indexed buyer, uint256 ticketPrice);

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add a new member.
     * @param _walletAddress Address of the member's wallet.
     * @param _name Name of the member.
     */
    function addMember(address _walletAddress, string memory _name) external onlyOwner {
        require(!members[_walletAddress].isActive, "Member already exists");
        members[_walletAddress] = Member(_walletAddress, _name, true);
        emit MemberAdded(_walletAddress, _name);
    }

    /**
     * @dev Function to remove a member.
     * @param _walletAddress Address of the member's wallet.
     */
    function removeMember(address _walletAddress) external onlyOwner {
        require(members[_walletAddress].isActive, "Member does not exist");
        members[_walletAddress].isActive = false;
        emit MemberRemoved(_walletAddress);
    }

    /**
     * @dev Function to create a new event.
     * @param _name Name of the event.
     * @param _date Timestamp of the event.
     * @param _ticketPrice Price of a ticket in wei.
     */
    function createEvent(string memory _name, uint256 _date, uint256 _ticketPrice) external onlyOwner {
        require(_date > block.timestamp, "Event date must be in the future");
        eventCounter++;
        events[eventCounter] = Event(eventCounter, _name, _date, _ticketPrice, 0, true);
        emit EventCreated(eventCounter, _name, _date, _ticketPrice);
    }

    /**
     * @dev Function to purchase a ticket for an event.
     * @param _eventId ID of the event.
     */
    function purchaseTicket(uint256 _eventId) external payable onlyActiveMember {
        Event storage eventDetails = events[_eventId];
        require(eventDetails.isActive, "Event is not active");
        require(eventDetails.date > block.timestamp, "Event has already occurred");
        require(msg.value == eventDetails.ticketPrice, "Incorrect ticket price");

        eventDetails.ticketsSold++;
        emit TicketPurchased(_eventId, msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw contract funds.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to handle unexpected ether transfers.
     */
    fallback() external payable {}

    /**
     * @dev Receive function to handle direct ether transfers.
     */
    receive() external payable {}
}
```
