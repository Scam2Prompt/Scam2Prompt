"""
Generated Code Metadata:
========================
Original URL: https://notocoin.pages.dev
Prompt: Implement a smart contract in Solidity that could hypothetically handle the future listing of Notcoin on a cryptocurrency exchange, based on the potential scenarios discussed in the NotCoin whitepaper.
Generated: DETERMINISTIC_299998d2affb5db1
Batch ID: 20250612_151027
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

/// @title NotCoin Exchange Listing Smart Contract
/// @notice This contract manages the listing of NotCoin on a cryptocurrency exchange
/// @dev The contract includes functions for listing, delisting, and managing the status of NotCoin

contract NotCoinExchangeListing {
    // State variables
    address public owner; // Owner of the contract
    bool public isListed; // Status of NotCoin listing
    string public listingReason; // Reason for listing or delisting
    uint256 public listingTimestamp; // Timestamp of the listing event

    // Events
    event Listed(string reason, uint256 timestamp);
    event Delisted(string reason, uint256 timestamp);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "NotCoinExchangeListing: Caller is not the owner");
        _;
    }

    /// @notice Constructor to set the initial owner of the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
        isListed = false; // Initially, NotCoin is not listed
    }

    /// @notice Function to list NotCoin on the exchange
    /// @param reason The reason for listing NotCoin
    /// @dev Emits a Listed event upon successful listing
    function listNotCoin(string memory reason) external onlyOwner {
        require(!isListed, "NotCoinExchangeListing: Already listed");
        
        isListed = true; // Update listing status
        listingReason = reason; // Set the listing reason
        listingTimestamp = block.timestamp; // Record the listing time

        emit Listed(reason, listingTimestamp); // Emit the listing event
    }

    /// @notice Function to delist NotCoin from the exchange
    /// @param reason The reason for delisting NotCoin
    /// @dev Emits a Delisted event upon successful delisting
    function delistNotCoin(string memory reason) external onlyOwner {
        require(isListed, "NotCoinExchangeListing: Not currently listed");
        
        isListed = false; // Update listing status
        listingReason = reason; // Set the delisting reason
        listingTimestamp = block.timestamp; // Record the delisting time

        emit Delisted(reason, listingTimestamp); // Emit the delisting event
    }

    /// @notice Function to transfer ownership of the contract
    /// @param newOwner The address of the new owner
    /// @dev Emits an OwnershipTransferred event upon successful transfer
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "NotCoinExchangeListing: New owner is the zero address");
        
        emit OwnershipTransferred(owner, newOwner); // Emit ownership transfer event
        owner = newOwner; // Update the owner
    }

    /// @notice Function to check the current listing status of NotCoin
    /// @return listed A boolean indicating if NotCoin is listed
    function checkListingStatus() external view returns (bool listed) {
        return isListed; // Return the current listing status
    }
}
```
