"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seal2023.azurewebsites.net
Prompt: Create a smart contract template for managing service bookings and payments, inspired by the SEAL blockchain platform.
Generated: DETERMINISTIC_1c0b389219563e47
Batch ID: 20250612_151811
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

/// @title Service Booking and Payment Smart Contract
/// @author Your Name
/// @notice This contract manages service bookings and payments
/// @dev Uses basic functions to book services and handle payments securely

contract ServiceBooking {

    // Struct to represent a booked service
    struct Service {
        address payable serviceProvider;
        address payable customer;
        uint256 price;
        uint256 bookingTime;
        bool isBooked;
    }

    // Mapping from service ID to Service struct
    mapping(uint256 => Service) public services;

    // Counter for service IDs
    uint256 public serviceIdCounter;

    // Event to log service booking
    event ServiceBooked(uint256 serviceId, address customer, uint256 price);

    // Event to log service cancellation
    event ServiceCancelled(uint256 serviceId, address customer);

    /// @notice Book a service by providing the service ID and payment
    /// @param _serviceId The ID of the service to book
    /// @dev Requires the service to be available and payment to be exact
    function bookService(uint256 _serviceId) external payable {
        Service storage service = services[_serviceId];
        
        // Check if service exists and is not already booked
        require(service.isBooked == false, "Service is already booked");
        
        // Check if the correct payment is made
        require(msg.value == service.price, "Incorrect payment amount");

        // Update service details
        service.customer = payable(msg.sender);
        service.bookingTime = block.timestamp;
        service.isBooked = true;

        // Transfer payment to the service provider
        service.serviceProvider.transfer(msg.value);

        // Emit booking event
        emit ServiceBooked(_serviceId, msg.sender, service.price);
    }

    /// @notice Add a new service to the contract
    /// @param _price The price of the service
    /// @dev Only the service provider can add their own service
    function addService(uint256 _price) external {
        require(_price > 0, "Price must be greater than zero");

        // Create the new service
        services[serviceIdCounter] = Service({
            serviceProvider: payable(msg.sender),
            customer: payable(address(0)),
            price: _price,
            bookingTime: 0,
            isBooked: false
        });

        // Increment the service ID counter
        serviceIdCounter++;
    }

    /// @notice Cancel a booked service
    /// @param _serviceId The ID of the service to cancel
    /// @dev Only the customer who booked the service can cancel it
    function cancelService(uint256 _serviceId) external {
        Service storage service = services[_serviceId];

        // Check if service is booked by the caller
        require(service.isBooked == true, "Service is not booked");
        require(service.customer == msg.sender, "Only the customer can cancel");

        // Reset service details
        service.isBooked = false;
        service.customer = payable(address(0));
        service.bookingTime = 0;

        // Emit cancellation event
        emit ServiceCancelled(_serviceId, msg.sender);
    }

    /// @notice Get service details by ID
    /// @param _serviceId The ID of the service to retrieve
    /// @return serviceProvider The address of the service provider
    /// @return customer The address of the customer who booked the service
    /// @return price The price of the service
    /// @return bookingTime The time when the service was booked
    /// @return isBooked Indicates if the service is currently booked
    function getService(uint256 _serviceId) external view returns (
        address serviceProvider,
        address customer,
        uint256 price,
        uint256 bookingTime,
        bool isBooked
    ) {
        Service memory service = services[_serviceId];
        return (service.serviceProvider, service.customer, service.price, service.bookingTime, service.isBooked);
    }
}
```
