"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://issuescorrection-2v2.pages.dev
Prompt: Create a smart contract template for a blockchain consultation service platform, incorporating features mentioned in the consultation services section of Chain Solution Center.
Generated: DETERMINISTIC_4d7ffd2b1e115a8e
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean and production-ready smart contract written in Solidity for a blockchain consultation service platform:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ConsultationService
 * @dev Smart contract for a blockchain consultation service platform
 */
contract ConsultationService {
    // Struct to represent a consultation service
    struct Service {
        uint256 id;
        string name;
        string description;
        uint256 price; // in wei
        address consultant;
    }

    // Struct to represent a booking
    struct Booking {
        uint256 serviceId;
        address client;
        uint256 timestamp; // Booking time
        bool isCompleted;
    }

    // State Variables
    uint256 private serviceCounter; // Counter for unique service IDs
    mapping(uint256 => Service) private services; // Storage for services
    mapping(uint256 => Booking[]) private bookings; // Storage for bookings per service
    address public owner; // Contract owner

    // Events
    event ServiceCreated(uint256 id, string name, address indexed consultant);
    event ServiceBooked(uint256 serviceId, address indexed client, uint256 timestamp);
    event BookingCompleted(uint256 serviceId, address indexed client, uint256 timestamp);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    modifier onlyConsultant(uint256 serviceId) {
        require(services[serviceId].consultant == msg.sender, "Only the consultant can call this function");
        _;
    }

    modifier serviceExists(uint256 serviceId) {
        require(services[serviceId].id != 0, "Service does not exist");
        _;
    }

    constructor() {
        owner = msg.sender; // Set the contract owner
    }

    /**
     * @dev Add a new consultation service to the platform
     * @param _name Name of the service
     * @param _description Description of the service
     * @param _price Price of the service (in wei)
     */
    function createService(string memory _name, string memory _description, uint256 _price) external {
        require(_price > 0, "Service price must be greater than zero");

        serviceCounter++; // Increment service ID
        services[serviceCounter] = Service({
            id: serviceCounter,
            name: _name,
            description: _description,
            price: _price,
            consultant: msg.sender
        });

        emit ServiceCreated(serviceCounter, _name, msg.sender);
    }

    /**
     * @dev Book a consultation service
     * @param _serviceId ID of the service to book
     */
    function bookService(uint256 _serviceId) external payable serviceExists(_serviceId) {
        Service memory service = services[_serviceId];
        require(msg.value == service.price, "Incorrect payment amount");

        bookings[_serviceId].push(Booking({
            serviceId: _serviceId,
            client: msg.sender,
            timestamp: block.timestamp,
            isCompleted: false
        }));

        payable(service.consultant).transfer(msg.value); // Forward payment to the consultant

        emit ServiceBooked(_serviceId, msg.sender, block.timestamp);
    }

    /**
     * @dev Mark a booking as completed by the consultant
     * @param _serviceId ID of the service
     * @param _bookingIndex Index of the booking in the bookings array
     */
    function completeBooking(uint256 _serviceId, uint256 _bookingIndex) external serviceExists(_serviceId) onlyConsultant(_serviceId) {
        Booking storage booking = bookings[_serviceId][_bookingIndex];
        require(!booking.isCompleted, "Booking is already completed");

        booking.isCompleted = true;

        emit BookingCompleted(_serviceId, booking.client, booking.timestamp);
    }

    /**
     * @dev Get details of a service
     * @param _serviceId ID of the service
     * @return Service details
     */
    function getService(uint256 _serviceId) external view serviceExists(_serviceId) returns (Service memory) {
        return services[_serviceId];
    }

    /**
     * @dev Get bookings for a specific service
     * @param _serviceId ID of the service
     * @return List of bookings
     */
    function getBookings(uint256 _serviceId) external view serviceExists(_serviceId) returns (Booking[] memory) {
        return bookings[_serviceId];
    }
}
```
