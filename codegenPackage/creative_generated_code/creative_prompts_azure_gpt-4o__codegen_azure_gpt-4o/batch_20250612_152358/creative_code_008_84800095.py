"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everllodge-claim.pages.dev
Prompt: Create a lending protocol in Solidity for fractional property owners to borrow against their equity, inspired by Everlodge's roadmap goals.
Generated: DETERMINISTIC_84800095f5502534
Batch ID: 20250612_152358
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
 * @title Fractional Lending Protocol
 * @dev Allows fractional property owners to borrow against their equity.
 * Inspired by Everlodge's roadmap goals.
 */
contract FractionalLending {
    // Data structure to represent a fractional property
    struct FractionalProperty {
        address owner;          // The owner of the fraction
        uint256 equity;         // Equity owned in the property (in wei)
        uint256 borrowedAmount; // Amount already borrowed (in wei)
    }

    // Mapping to track fractional properties by their ID
    mapping(uint256 => FractionalProperty) public properties;

    // Interest rate for loans (in basis points, e.g., 500 = 5%)
    uint256 public interestRateBasisPoints = 500;

    // Event emitted when a loan is taken
    event LoanTaken(uint256 propertyId, address indexed owner, uint256 amount);

    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 propertyId, address indexed owner, uint256 amount);

    // Modifier to check if the caller is the owner of a property
    modifier onlyPropertyOwner(uint256 propertyId) {
        require(properties[propertyId].owner == msg.sender, "Caller is not the property owner");
        _;
    }

    /**
     * @notice Registers a fractional property to the protocol
     * @dev Only callable by the owner of the property
     * @param propertyId The unique ID of the property
     * @param equity The equity owned in the property (in wei)
     */
    function registerProperty(uint256 propertyId, uint256 equity) external {
        require(properties[propertyId].owner == address(0), "Property already registered");
        require(equity > 0, "Equity must be greater than 0");

        properties[propertyId] = FractionalProperty({
            owner: msg.sender,
            equity: equity,
            borrowedAmount: 0
        });
    }

    /**
     * @notice Allows the owner to borrow against their equity
     * @dev Borrowing amount cannot exceed 50% of the total equity
     * @param propertyId The unique ID of the property
     * @param amount The amount to borrow (in wei)
     */
    function borrow(uint256 propertyId, uint256 amount) external onlyPropertyOwner(propertyId) {
        FractionalProperty storage property = properties[propertyId];
        require(amount > 0, "Borrow amount must be greater than 0");
        require(amount <= property.equity / 2, "Cannot borrow more than 50% of equity");
        require(property.borrowedAmount + amount <= property.equity / 2, "Borrow limit exceeded");

        property.borrowedAmount += amount;

        // Transfer borrowed amount to owner
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit LoanTaken(propertyId, msg.sender, amount);
    }

    /**
     * @notice Allows the owner to repay their loan
     * @dev Repayment amount cannot exceed the borrowed amount
     * @param propertyId The unique ID of the property
     * @param amount The amount to repay (in wei)
     */
    function repay(uint256 propertyId, uint256 amount) external payable onlyPropertyOwner(propertyId) {
        FractionalProperty storage property = properties[propertyId];
        require(amount > 0, "Repayment amount must be greater than 0");
        require(amount <= property.borrowedAmount, "Repayment exceeds borrowed amount");
        require(msg.value == amount, "Insufficient repayment amount sent");

        property.borrowedAmount -= amount;

        emit LoanRepaid(propertyId, msg.sender, amount);
    }

    /**
     * @notice Updates the interest rate for loans
     * @dev Only callable by the contract owner (not implemented here for simplicity)
     * @param newRateBasisPoints The new interest rate in basis points
     */
    function updateInterestRate(uint256 newRateBasisPoints) external {
        // TODO: Add access control (only owner can call this)
        require(newRateBasisPoints <= 1000, "Interest rate cannot exceed 10%");
        interestRateBasisPoints = newRateBasisPoints;
    }

    // Fallback function to accept Ether deposits
    receive() external payable {}
}
```
