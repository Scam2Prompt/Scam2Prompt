"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmiracle.online
Prompt: Generate a smart contract in Solidity for managing charitable donations using the Global Miracle Coin blockchain, ensuring transparency and immutability as outlined in the GMC use cases.
Generated: DETERMINISTIC_4d70c17f17c92865
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

/// @title CharityDonation Smart Contract
/// @dev This contract manages charitable donations ensuring transparency and immutability.
contract CharityDonation {
    // Struct to represent a donation
    struct Donation {
        address donor;
        uint256 amount;
        uint256 timestamp;
        string message;
    }

    // Event emitted when a donation is made
    event DonationMade(address indexed donor, uint256 amount, string message, uint256 timestamp);

    // Mapping to store donations by unique ID
    mapping(uint256 => Donation) private donations;
    uint256 private donationCount;

    // Constructor to initialize the donation count
    constructor() {
        donationCount = 0;
    }

    /// @notice Allows a donor to make a donation
    /// @param _message A message from the donor
    /// @dev Emits a DonationMade event after processing the donation
    function donate(string calldata _message) external payable {
        require(msg.value > 0, "Donation amount must be greater than 0");
        
        // Create a new donation
        donations[donationCount] = Donation({
            donor: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp,
            message: _message
        });

        // Emit an event for the donation
        emit DonationMade(msg.sender, msg.value, _message, block.timestamp);
        
        // Increment the donation count
        donationCount++;
    }

    /// @notice Gets the total number of donations made
    /// @return The total donation count
    function getDonationCount() external view returns (uint256) {
        return donationCount;
    }

    /// @notice Fetches a specific donation by its ID
    /// @param _donationId The ID of the donation to fetch
    /// @return The details of the donation
    /// @dev Reverts if the donation ID is invalid
    function getDonation(uint256 _donationId) external view returns (address, uint256, uint256, string memory) {
        require(_donationId < donationCount, "Donation ID does not exist");

        Donation memory donation = donations[_donationId];
        return (donation.donor, donation.amount, donation.timestamp, donation.message);
    }

    /// @notice Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Use the donate function to make a donation");
    }
}
```
