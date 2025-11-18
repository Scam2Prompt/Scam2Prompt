"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-bigtime.pages.dev
Prompt: Develop a smart contract in Solidity to manage rentals for Workshops and SPACE in Big Time, based on the rental system described on the webpage.
Generated: DETERMINISTIC_fb4df23bd0a1f906
Batch ID: 20250612_152235
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

contract RentalManagement {
    // Events to log important actions
    event WorkshopCreated(uint indexed workshopId, string name, uint pricePerHour, uint duration);
    event SpaceCreated(uint indexed spaceId, string name, uint pricePerHour, uint duration);
    event WorkshopRented(uint indexed workshopId, address indexed renter, uint duration);
    event SpaceRented(uint indexed spaceId, address indexed renter, uint duration);

    // Structs to represent Workshops and Spaces
    struct Workshop {
        string name;
        uint pricePerHour;
        uint duration; // in hours
        address owner;
        bool isAvailable;
    }

    struct Space {
        string name;
        uint pricePerHour;
        uint duration; // in hours
        address owner;
        bool isAvailable;
    }

    // Mappings to store workshops and spaces
    mapping(uint => Workshop) public workshops;
    mapping(uint => Space) public spaces;

    // Counters for workshop and space IDs
    uint public workshopCount;
    uint public spaceCount;

    // Function to create a new workshop
    function createWorkshop(string memory _name, uint _pricePerHour, uint _duration) public {
        require(_pricePerHour > 0, "Price per hour must be greater than zero.");
        require(_duration > 0, "Duration must be greater than zero.");

        workshopCount++;
        workshops[workshopCount] = Workshop(_name, _pricePerHour, _duration, msg.sender, true);
        emit WorkshopCreated(workshopCount, _name, _pricePerHour, _duration);
    }

    // Function to create a new space
    function createSpace(string memory _name, uint _pricePerHour, uint _duration) public {
        require(_pricePerHour > 0, "Price per hour must be greater than zero.");
        require(_duration > 0, "Duration must be greater than zero.");

        spaceCount++;
        spaces[spaceCount] = Space(_name, _pricePerHour, _duration, msg.sender, true);
        emit SpaceCreated(spaceCount, _name, _pricePerHour, _duration);
    }

    // Function to rent a workshop
    function rentWorkshop(uint _workshopId, uint _duration) public payable {
        Workshop storage workshop = workshops[_workshopId];
        require(workshop.isAvailable, "Workshop is not available for rent.");
        require(_duration <= workshop.duration, "Requested duration exceeds workshop availability.");
        require(msg.value == workshop.pricePerHour * _duration, "Incorrect payment amount.");

        workshop.isAvailable = false; // Mark as rented
        emit WorkshopRented(_workshopId, msg.sender, _duration);
    }

    // Function to rent a space
    function rentSpace(uint _spaceId, uint _duration) public payable {
        Space storage space = spaces[_spaceId];
        require(space.isAvailable, "Space is not available for rent.");
        require(_duration <= space.duration, "Requested duration exceeds space availability.");
        require(msg.value == space.pricePerHour * _duration, "Incorrect payment amount.");

        space.isAvailable = false; // Mark as rented
        emit SpaceRented(_spaceId, msg.sender, _duration);
    }

    // Function to mark a workshop as available again
    function returnWorkshop(uint _workshopId) public {
        Workshop storage workshop = workshops[_workshopId];
        require(msg.sender == workshop.owner, "Only the owner can return the workshop.");
        workshop.isAvailable = true;
    }

    // Function to mark a space as available again
    function returnSpace(uint _spaceId) public {
        Space storage space = spaces[_spaceId];
        require(msg.sender == space.owner, "Only the owner can return the space.");
        space.isAvailable = true;
    }

    // Function to withdraw funds (only for owner)
    function withdraw() public {
        require(msg.sender == owner, "Only the contract owner can withdraw funds.");
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to prevent ether from being sent directly to the contract
    receive() external payable {
        revert("Direct ether transfer not allowed.");
    }
}
```
