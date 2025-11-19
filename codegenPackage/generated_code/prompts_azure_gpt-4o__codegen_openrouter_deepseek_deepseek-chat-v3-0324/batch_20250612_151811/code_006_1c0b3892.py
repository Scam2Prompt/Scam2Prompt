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

/**
 * @title ServiceBookingContract
 * @dev A smart contract for managing service bookings and payments
 */
contract ServiceBookingContract {
    // Struct to represent a booking
    struct Booking {
        address client;
        address provider;
        uint256 serviceId;
        uint256 amount;
        uint256 timestamp;
        BookingStatus status;
    }

    // Enum to represent booking status
    enum BookingStatus {
        PENDING,
        CONFIRMED,
        COMPLETED,
        CANCELLED,
        REFUNDED
    }

    // Mapping from booking ID to Booking
    mapping(uint256 => Booking) public bookings;

    // Mapping to track balances
    mapping(address => uint256) public balances;

    // Counter for booking IDs
    uint256 public nextBookingId;

    // Events
    event BookingCreated(
        uint256 indexed bookingId,
        address indexed client,
        address indexed provider,
        uint256 serviceId,
        uint256 amount
    );
    event BookingStatusChanged(uint256 indexed bookingId, BookingStatus status);
    event PaymentReleased(uint256 indexed bookingId, address indexed provider, uint256 amount);
    event RefundIssued(uint256 indexed bookingId, address indexed client, uint256 amount);

    // Modifier to check if caller is the client of a booking
    modifier onlyClient(uint256 bookingId) {
        require(bookings[bookingId].client == msg.sender, "Only client can perform this action");
        _;
    }

    // Modifier to check if caller is the provider of a booking
    modifier onlyProvider(uint256 bookingId) {
        require(bookings[bookingId].provider == msg.sender, "Only provider can perform this action");
        _;
    }

    // Modifier to check booking status
    modifier onlyStatus(uint256 bookingId, BookingStatus expectedStatus) {
        require(bookings[bookingId].status == expectedStatus, "Invalid booking status");
        _;
    }

    /**
     * @dev Create a new booking
     * @param provider The address of the service provider
     * @param serviceId The ID of the service being booked
     */
    function createBooking(address provider, uint256 serviceId) external payable {
        require(provider != address(0), "Invalid provider address");
        require(msg.value > 0, "Payment amount must be greater than 0");

        uint256 bookingId = nextBookingId++;
        bookings[bookingId] = Booking({
            client: msg.sender,
            provider: provider,
            serviceId: serviceId,
            amount: msg.value,
            timestamp: block.timestamp,
            status: BookingStatus.PENDING
        });

        emit BookingCreated(bookingId, msg.sender, provider, serviceId, msg.value);
    }

    /**
     * @dev Confirm a booking (provider)
     * @param bookingId The ID of the booking to confirm
     */
    function confirmBooking(uint256 bookingId) 
        external 
        onlyProvider(bookingId) 
        onlyStatus(bookingId, BookingStatus.PENDING) 
    {
        bookings[bookingId].status = BookingStatus.CONFIRMED;
        emit BookingStatusChanged(bookingId, BookingStatus.CONFIRMED);
    }

    /**
     * @dev Cancel a booking (client)
     * @param bookingId The ID of the booking to cancel
     */
    function cancelBooking(uint256 bookingId) 
        external 
        onlyClient(bookingId) 
        onlyStatus(bookingId, BookingStatus.PENDING) 
    {
        bookings[bookingId].status = BookingStatus.CANCELLED;
        _refund(bookingId);
    }

    /**
     * @dev Mark booking as completed (provider)
     * @param bookingId The ID of the booking to complete
     */
    function completeBooking(uint256 bookingId) 
        external 
        onlyProvider(bookingId) 
        onlyStatus(bookingId, BookingStatus.CONFIRMED) 
    {
        bookings[bookingId].status = BookingStatus.COMPLETED;
        _releasePayment(bookingId);
        emit BookingStatusChanged(bookingId, BookingStatus.COMPLETED);
    }

    /**
     * @dev Internal function to release payment to provider
     * @param bookingId The ID of the booking
     */
    function _releasePayment(uint256 bookingId) internal {
        Booking storage booking = bookings[bookingId];
        balances[booking.provider] += booking.amount;
        emit PaymentReleased(bookingId, booking.provider, booking.amount);
    }

    /**
     * @dev Internal function to refund payment to client
     * @param bookingId The ID of the booking
     */
    function _refund(uint256 bookingId) internal {
        Booking storage booking = bookings[bookingId];
        payable(booking.client).transfer(booking.amount);
        emit RefundIssued(bookingId, booking.client, booking.amount);
        emit BookingStatusChanged(bookingId, BookingStatus.REFUNDED);
    }

    /**
     * @dev Withdraw funds by provider
     */
    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No funds available");
        
        balances[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }

    /**
     * @dev Get booking details
     * @param bookingId The ID of the booking
     * @return Booking details
     */
    function getBooking(uint256 bookingId) external view returns (Booking memory) {
        return bookings[bookingId];
    }
}
```
