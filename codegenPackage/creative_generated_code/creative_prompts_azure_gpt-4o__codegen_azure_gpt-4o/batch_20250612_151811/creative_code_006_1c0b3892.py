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

/**
 * @title ServiceBookingContract
 * @dev A smart contract for managing service bookings and payments on the blockchain.
 * Inspired by the SEAL blockchain platform.
 */
contract ServiceBookingContract {
    // Struct representing a service booking
    struct Booking {
        uint256 id;
        address customer;
        address provider;
        string serviceDetails; // Description of the service
        uint256 amount; // Payment amount in Wei
        bool isPaid;
        bool isCompleted;
    }

    // State variables
    uint256 private nextBookingId;
    mapping(uint256 => Booking) public bookings;
    address public owner;

    // Events
    event BookingCreated(uint256 bookingId, address indexed customer, address indexed provider, uint256 amount);
    event PaymentReceived(uint256 bookingId, uint256 amount);
    event ServiceCompleted(uint256 bookingId);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    modifier onlyCustomer(uint256 bookingId) {
        require(msg.sender == bookings[bookingId].customer, "Only the customer can perform this action");
        _;
    }

    modifier onlyProvider(uint256 bookingId) {
        require(msg.sender == bookings[bookingId].provider, "Only the provider can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new booking for a service.
     * @param provider Address of the service provider.
     * @param serviceDetails Description of the service being booked.
     * @param amount Payment amount for the service (in Wei).
     */
    function createBooking(address provider, string memory serviceDetails, uint256 amount) external {
        require(provider != address(0), "Invalid provider address");
        require(amount > 0, "Amount must be greater than zero");

        uint256 bookingId = nextBookingId;
        bookings[bookingId] = Booking({
            id: bookingId,
            customer: msg.sender,
            provider: provider,
            serviceDetails: serviceDetails,
            amount: amount,
            isPaid: false,
            isCompleted: false
        });

        nextBookingId++;
        emit BookingCreated(bookingId, msg.sender, provider, amount);
    }

    /**
     * @dev Pay for a booking.
     * The customer sends the payment amount to the contract.
     * @param bookingId ID of the booking to be paid.
     */
    function payForBooking(uint256 bookingId) external payable onlyCustomer(bookingId) {
        Booking storage booking = bookings[bookingId];
        require(!booking.isPaid, "Booking has already been paid for");
        require(msg.value == booking.amount, "Incorrect payment amount");

        booking.isPaid = true;
        emit PaymentReceived(bookingId, msg.value);
    }

    /**
     * @dev Mark a service booking as completed by the provider.
     * Funds are then released to the provider.
     * @param bookingId ID of the booking to be marked as completed.
     */
    function completeBooking(uint256 bookingId) external onlyProvider(bookingId) {
        Booking storage booking = bookings[bookingId];
        require(booking.isPaid, "Booking must be paid before completion");
        require(!booking.isCompleted, "Booking has already been completed");

        booking.isCompleted = true;
        payable(booking.provider).transfer(booking.amount);
        emit ServiceCompleted(bookingId);
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits.
     */
    fallback() external payable {
        revert("Direct deposits are not allowed");
    }

    receive() external payable {
        revert("Direct deposits are not allowed");
    }
}
```
