"""
Generated Code Metadata:
========================
Original URL: https://globalmiracle.online
Prompt: Generate a smart contract in Solidity for managing charitable donations using the Global Miracle Coin blockchain, ensuring transparency and immutability as outlined in the GMC use cases.
Generated: DETERMINISTIC_4d70c17f17c92865
Batch ID: 20250612_152358
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

/// @title Charity Donation Smart Contract
/// @author Your Name
/// @notice This contract manages charitable donations, ensuring transparency and immutability.
/// @dev All interactions with this contract are logged on the blockchain.

contract CharityDonation {
    // Struct to represent a donation
    struct Donation {
        address donor;
        uint256 amount;
        uint256 timestamp;
        string message;
    }

    // Mapping to store donations by charity address
    mapping(address => Donation[]) private donationsByCharity;

    // Event emitted when a donation is made
    event DonationMade(address indexed charity, address indexed donor, uint256 amount, string message, uint256 timestamp);

    /// @notice Allows a donor to make a donation to a specified charity
    /// @param charity The address of the charity receiving the donation
    /// @param message An optional message from the donor
    /// @dev The donation amount must be greater than zero
    function donate(address payable charity, string memory message) public payable {
        require(msg.value > 0, "Donation amount must be greater than zero");
        require(charity != address(0), "Invalid charity address");

        // Create a new donation
        Donation memory newDonation = Donation({
            donor: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp,
            message: message
        });

        // Store the donation
        donationsByCharity[charity].push(newDonation);

        // Emit the donation event
        emit DonationMade(charity, msg.sender, msg.value, message, block.timestamp);

        // Transfer the donation to the charity
        (bool success, ) = charity.call{value: msg.value}("");
        require(success, "Transfer failed");
    }

    /// @notice Retrieve all donations made to a specific charity
    /// @param charity The address of the charity
    /// @return donations An array of donations made to the charity
    function getDonations(address charity) public view returns (Donation[] memory) {
        require(charity != address(0), "Invalid charity address");
        return donationsByCharity[charity];
    }

    /// @notice Get the total amount donated to a specific charity
    /// @param charity The address of the charity
    /// @return totalAmount The total amount of donations received by the charity
    function getTotalDonations(address charity) public view returns (uint256 totalAmount) {
        require(charity != address(0), "Invalid charity address");
        Donation[] memory donations = donationsByCharity[charity];
        
        for (uint256 i = 0; i < donations.length; i++) {
            totalAmount += donations[i].amount;
        }
    }
}
```
