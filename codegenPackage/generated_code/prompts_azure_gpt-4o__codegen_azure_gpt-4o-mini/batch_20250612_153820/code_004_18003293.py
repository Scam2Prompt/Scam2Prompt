"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Create a Solidity smart contract for implementing the HighTable Secret Deal Program, using the key features described in the Good Games Guild documentation.
Generated: DETERMINISTIC_18003293dc81789d
Batch ID: 20250612_153820
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// HighTableSecretDealProgram contract
contract HighTableSecretDealProgram is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a secret deal
    struct SecretDeal {
        uint256 id;
        address creator;
        string dealDetails;
        uint256 rewardAmount;
        bool isActive;
    }

    // Mapping to store secret deals by their ID
    mapping(uint256 => SecretDeal) private deals;
    Counters.Counter private dealIdCounter;

    // Event emitted when a new deal is created
    event DealCreated(uint256 indexed dealId, address indexed creator, string dealDetails, uint256 rewardAmount);

    // Event emitted when a deal is activated or deactivated
    event DealStatusChanged(uint256 indexed dealId, bool isActive);

    // Modifier to check if the deal exists
    modifier dealExists(uint256 dealId) {
        require(deals[dealId].creator != address(0), "Deal does not exist");
        _;
    }

    // Function to create a new secret deal
    function createDeal(string memory dealDetails, uint256 rewardAmount) external onlyOwner {
        require(bytes(dealDetails).length > 0, "Deal details cannot be empty");
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        dealIdCounter.increment();
        uint256 newDealId = dealIdCounter.current();

        deals[newDealId] = SecretDeal({
            id: newDealId,
            creator: msg.sender,
            dealDetails: dealDetails,
            rewardAmount: rewardAmount,
            isActive: true
        });

        emit DealCreated(newDealId, msg.sender, dealDetails, rewardAmount);
    }

    // Function to activate or deactivate a deal
    function changeDealStatus(uint256 dealId, bool isActive) external onlyOwner dealExists(dealId) {
        deals[dealId].isActive = isActive;
        emit DealStatusChanged(dealId, isActive);
    }

    // Function to retrieve deal information
    function getDeal(uint256 dealId) external view dealExists(dealId) returns (SecretDeal memory) {
        return deals[dealId];
    }

    // Function to retrieve the total number of deals created
    function totalDeals() external view returns (uint256) {
        return dealIdCounter.current();
    }
}
```
