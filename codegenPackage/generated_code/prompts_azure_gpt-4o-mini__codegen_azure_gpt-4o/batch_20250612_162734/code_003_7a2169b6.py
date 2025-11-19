"""
Generated Code Metadata:
========================
Original URL: https://unisocks.fi
Prompt: Generate a code snippet for a smart contract that allows users to buy and sell Unisocks on the blockchain.
Generated: DETERMINISTIC_7a2169b62f636205
Batch ID: 20250612_162734
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
 * @title UnisocksMarketplace
 * @dev A smart contract for buying and selling Unisocks tokens on the blockchain.
 */
contract UnisocksMarketplace {
    // Address of the contract owner
    address public owner;

    // Struct to represent a Unisocks listing
    struct Unisocks {
        uint256 id;
        address seller;
        uint256 price; // Price in wei
        bool isAvailable;
    }

    // Mapping to store Unisocks listings
    mapping(uint256 => Unisocks) public unisocksListings;

    // Counter for Unisocks IDs
    uint256 public unisocksCounter;

    // Event emitted when a new Unisocks is listed
    event UnisocksListed(uint256 indexed id, address indexed seller, uint256 price);

    // Event emitted when a Unisocks is purchased
    event UnisocksPurchased(uint256 indexed id, address indexed buyer, uint256 price);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to ensure the Unisocks exists and is available
    modifier isAvailable(uint256 id) {
        require(unisocksListings[id].isAvailable, "Unisocks is not available for purchase");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to list a new Unisocks for sale.
     * @param price The price of the Unisocks in wei.
     */
    function listUnisocks(uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        unisocksCounter++;
        unisocksListings[unisocksCounter] = Unisocks({
            id: unisocksCounter,
            seller: msg.sender,
            price: price,
            isAvailable: true
        });

        emit UnisocksListed(unisocksCounter, msg.sender, price);
    }

    /**
     * @dev Function to purchase a listed Unisocks.
     * @param id The ID of the Unisocks to purchase.
     */
    function purchaseUnisocks(uint256 id) external payable isAvailable(id) {
        Unisocks storage unisocks = unisocksListings[id];

        require(msg.value == unisocks.price, "Incorrect payment amount");

        // Transfer funds to the seller
        (bool success, ) = unisocks.seller.call{value: msg.value}("");
        require(success, "Payment transfer failed");

        // Mark the Unisocks as sold
        unisocks.isAvailable = false;

        emit UnisocksPurchased(id, msg.sender, unisocks.price);
    }

    /**
     * @dev Function to withdraw contract balance (only owner).
     */
    function withdrawBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
