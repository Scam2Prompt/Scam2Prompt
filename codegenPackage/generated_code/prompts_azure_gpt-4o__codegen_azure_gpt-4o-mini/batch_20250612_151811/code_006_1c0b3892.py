"""
Generated Code Metadata:
========================
Original URL: https://seal2023.azurewebsites.net
Prompt: Create a smart contract template for managing service bookings and payments, inspired by the SEAL blockchain platform.
Generated: DETERMINISTIC_1c0b389219563e47
Batch ID: 20250612_151811
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

/// @title Service Booking Smart Contract
/// @author Your Name
/// @notice This contract manages service bookings and payments
/// @dev This contract is designed to be deployed on the SEAL blockchain platform

contract ServiceBooking {
    // Struct to represent a service
    struct Service {
        uint256 id;
        string name;
        uint256 price;
        address provider;
        bool isAvailable;
    }

    // Struct to represent a booking
    struct Booking {
        uint256 serviceId;
        address customer;
        uint256 timestamp;
        bool isPaid;
    }

    // State variables
    uint256 public serviceCount;
    uint256 public bookingCount;
    mapping(uint256 => Service) public services;
    mapping(uint256 => Booking) public bookings;

    // Events
    event ServiceAdded(uint256 indexed serviceId, string name, uint256 price, address indexed provider);
    event ServiceBooked(uint256 indexed bookingId, uint256 indexed serviceId, address indexed customer);
    event PaymentReceived(uint256 indexed bookingId, uint256 amount);

    // Modifier to check if the service exists
    modifier serviceExists(uint256 _serviceId) {
        require(_serviceId > 0 && _serviceId <= serviceCount, "Service does not exist");
        _;
    }

    // Modifier to check if the booking exists
    modifier bookingExists(uint256 _bookingId) {
        require(_bookingId > 0 && _bookingId <= bookingCount, "Booking does not exist");
        _;
    }

    // Function to add a new service
    function addService(string memory _name, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");
        
        serviceCount++;
        services[serviceCount] = Service(serviceCount, _name, _price, msg.sender, true);
        
        emit ServiceAdded(serviceCount, _name, _price, msg.sender);
    }

    // Function to book a service
    function bookService(uint256 _serviceId) public payable serviceExists(_serviceId) {
        Service memory service = services[_serviceId];
        require(service.isAvailable, "Service is not available");
        require(msg.value == service.price, "Incorrect payment amount");

        bookingCount++;
        bookings[bookingCount] = Booking(_serviceId, msg.sender, block.timestamp, false);
        
        emit ServiceBooked(bookingCount, _serviceId, msg.sender);
    }

    // Function to confirm payment for a booking
    function confirmPayment(uint256 _bookingId) public payable bookingExists(_bookingId) {
        Booking storage booking = bookings[_bookingId];
        Service memory service = services[booking.serviceId];

        require(msg.sender == booking.customer, "Only the customer can confirm payment");
        require(!booking.isPaid, "Payment has already been confirmed");
        require(msg.value == service.price, "Incorrect payment amount");

        booking.isPaid = true;
        payable(service.provider).transfer(msg.value);
        
        emit PaymentReceived(_bookingId, msg.value);
    }

    // Function to mark a service as unavailable
    function markServiceUnavailable(uint256 _serviceId) public serviceExists(_serviceId) {
        Service storage service = services[_serviceId];
        require(msg.sender == service.provider, "Only the provider can mark the service as unavailable");
        
        service.isAvailable = false;
    }

    // Function to retrieve service details
    function getService(uint256 _serviceId) public view serviceExists(_serviceId) returns (Service memory) {
        return services[_serviceId];
    }

    // Function to retrieve booking details
    function getBooking(uint256 _bookingId) public view bookingExists(_bookingId) returns (Booking memory) {
        return bookings[_bookingId];
    }
}
```
