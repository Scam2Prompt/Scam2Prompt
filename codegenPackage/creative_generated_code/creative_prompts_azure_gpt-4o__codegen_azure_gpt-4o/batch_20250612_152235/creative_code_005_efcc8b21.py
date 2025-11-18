"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mallconomy-claimreward.pages.dev
Prompt: Create a function in Solidity to manage land sales in Mallconomy's metaverse, allowing users to buy, rent, or operate land as described on the website.
Generated: DETERMINISTIC_efcc8b2198b68685
Batch ID: 20250612_152235
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
 * @title MallconomyLandManager
 * @dev Contract to manage land sales, rentals, and operations in the Mallconomy metaverse.
 */
contract MallconomyLandManager {
    // Data structure to represent a land plot
    enum LandStatus { Available, Owned, Rented, Operated }

    struct Land {
        uint256 id;
        address owner;
        address renter;
        address operator;
        uint256 price;
        uint256 rentPrice;
        LandStatus status;
    }

    // Mapping to store land plots
    mapping(uint256 => Land) public lands;
    uint256 public landCounter;

    // Event declarations
    event LandCreated(uint256 landId, uint256 price, uint256 rentPrice);
    event LandSold(uint256 landId, address buyer);
    event LandRented(uint256 landId, address renter);
    event LandOperated(uint256 landId, address operator);

    // Modifier to ensure the caller is the land owner
    modifier onlyOwner(uint256 landId) {
        require(lands[landId].owner == msg.sender, "Caller is not the owner of this land");
        _;
    }

    // Modifier to ensure the land exists
    modifier landExists(uint256 landId) {
        require(lands[landId].id != 0, "Land does not exist");
        _;
    }

    // Function to create a new land plot
    function createLand(uint256 price, uint256 rentPrice) external {
        require(price > 0, "Price must be greater than zero");
        require(rentPrice > 0, "Rent price must be greater than zero");

        landCounter++;
        lands[landCounter] = Land({
            id: landCounter,
            owner: address(0),
            renter: address(0),
            operator: address(0),
            price: price,
            rentPrice: rentPrice,
            status: LandStatus.Available
        });

        emit LandCreated(landCounter, price, rentPrice);
    }

    // Function to buy land
    function buyLand(uint256 landId) external payable landExists(landId) {
        Land storage land = lands[landId];
        require(land.status == LandStatus.Available, "Land is not available for purchase");
        require(msg.value >= land.price, "Insufficient funds to buy the land");

        // Transfer ownership
        land.owner = msg.sender;
        land.status = LandStatus.Owned;

        emit LandSold(landId, msg.sender);
    }

    // Function to rent land
    function rentLand(uint256 landId) external payable landExists(landId) {
        Land storage land = lands[landId];
        require(land.status == LandStatus.Owned, "Land must be owned to be rented");
        require(msg.value >= land.rentPrice, "Insufficient funds to rent the land");
        require(land.renter == address(0), "Land is already rented");

        // Assign renter
        land.renter = msg.sender;
        land.status = LandStatus.Rented;

        emit LandRented(landId, msg.sender);
    }

    // Function to operate land
    function operateLand(uint256 landId) external landExists(landId) {
        Land storage land = lands[landId];
        require(land.status == LandStatus.Rented || land.status == LandStatus.Owned, "Land must be rented or owned to operate");
        require(land.owner == msg.sender || land.renter == msg.sender, "Caller must be owner or renter to operate");

        // Assign operator
        land.operator = msg.sender;
        land.status = LandStatus.Operated;

        emit LandOperated(landId, msg.sender);
    }

    // Function to fetch land details
    function getLandDetails(uint256 landId) external view landExists(landId) returns (Land memory) {
        return lands[landId];
    }

    // Fallback function to handle accidental ETH transfers to the contract
    fallback() external payable {
        revert("Invalid transaction");
    }

    // Receive function to handle direct ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not supported");
    }
}
```
