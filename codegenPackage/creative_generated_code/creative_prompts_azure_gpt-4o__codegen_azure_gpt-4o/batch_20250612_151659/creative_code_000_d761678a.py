"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smeth.pages.dev
Prompt: Write a custom smart contract on Ethereum that mimics the functionality of the CryptoPunks marketplace, including the ability to buy, bid, and offer items for sale, while ensuring the contract is immutable once deployed.
Generated: DETERMINISTIC_d761678a1807e6a4
Batch ID: 20250612_151659
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
 * @title CryptoPunks Marketplace
 * @dev A smart contract mimicking the functionality of the CryptoPunks marketplace.
 * Users can buy, bid, and offer items for sale. Ensures immutability once deployed.
 */
contract CryptoPunksMarketplace {
    struct Punk {
        address owner; // Owner of the punk
        uint256 price; // Price set by the owner (0 if not for sale)
        address bidder; // Address of the highest bidder
        uint256 bidAmount; // Highest bid amount
    }

    mapping(uint256 => Punk) public punks; // Mapping of punk ID to Punk details
    uint256 public totalPunks; // Total number of punks in the marketplace

    event PunkListed(uint256 indexed punkId, address indexed owner, uint256 price);
    event PunkDelisted(uint256 indexed punkId, address indexed owner);
    event PunkSold(uint256 indexed punkId, address indexed buyer, uint256 price);
    event NewBid(uint256 indexed punkId, address indexed bidder, uint256 amount);
    event BidWithdrawn(uint256 indexed punkId, address indexed bidder);

    /**
     * @dev Constructor to initialize the marketplace with a fixed number of punks.
     * @param _totalPunks Total number of punks that will exist in this marketplace.
     */
    constructor(uint256 _totalPunks) {
        require(_totalPunks > 0, "Total punks must be greater than zero");
        totalPunks = _totalPunks;

        // Initialize all punks with creator/contract owner as the initial owner.
        for (uint256 i = 0; i < _totalPunks; i++) {
            punks[i] = Punk({
                owner: msg.sender,
                price: 0,
                bidder: address(0),
                bidAmount: 0
            });
        }
    }

    /**
     * @dev List a punk for sale at a specific price.
     * @param punkId The ID of the punk to list.
     * @param price The sale price of the punk.
     */
    function listPunk(uint256 punkId, uint256 price) external {
        require(punkId < totalPunks, "Invalid punk ID");
        Punk storage punk = punks[punkId];
        require(msg.sender == punk.owner, "Only the owner can list the punk for sale");
        require(price > 0, "Price must be greater than zero");

        punk.price = price;
        emit PunkListed(punkId, msg.sender, price);
    }

    /**
     * @dev Delist a punk from sale.
     * @param punkId The ID of the punk to delist.
     */
    function delistPunk(uint256 punkId) external {
        require(punkId < totalPunks, "Invalid punk ID");
        Punk storage punk = punks[punkId];
        require(msg.sender == punk.owner, "Only the owner can delist the punk");

        punk.price = 0;
        emit PunkDelisted(punkId, msg.sender);
    }

    /**
     * @dev Buy a punk that is listed for sale.
     * @param punkId The ID of the punk to buy.
     */
    function buyPunk(uint256 punkId) external payable {
        require(punkId < totalPunks, "Invalid punk ID");
        Punk storage punk = punks[punkId];
        require(punk.price > 0, "Punk is not for sale");
        require(msg.value == punk.price, "Incorrect value sent");

        address previousOwner = punk.owner;
        punk.owner = msg.sender;
        punk.price = 0;

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        // Refund any outstanding bid
        if (punk.bidAmount > 0) {
            payable(punk.bidder).transfer(punk.bidAmount);
            punk.bidder = address(0);
            punk.bidAmount = 0;
        }

        emit PunkSold(punkId, msg.sender, msg.value);
    }

    /**
     * @dev Place a bid on a punk.
     * @param punkId The ID of the punk to bid on.
     */
    function placeBid(uint256 punkId) external payable {
        require(punkId < totalPunks, "Invalid punk ID");
        Punk storage punk = punks[punkId];
        require(msg.sender != punk.owner, "Owner cannot bid on their own punk");
        require(msg.value > punk.bidAmount, "Bid must be higher than the current bid");

        // Refund the previous highest bidder
        if (punk.bidAmount > 0) {
            payable(punk.bidder).transfer(punk.bidAmount);
        }

        punk.bidder = msg.sender;
        punk.bidAmount = msg.value;

        emit NewBid(punkId, msg.sender, msg.value);
    }

    /**
     * @dev Withdraw a bid from a punk.
     * @param punkId The ID of the punk to withdraw the bid from.
     */
    function withdrawBid(uint256 punkId) external {
        require(punkId < totalPunks, "Invalid punk ID");
        Punk storage punk = punks[punkId];
        require(msg.sender == punk.bidder, "Only the bidder can withdraw their bid");

        uint256 bidAmount = punk.bidAmount;
        punk.bidder = address(0);
        punk.bidAmount = 0;

        // Refund the bidder
        payable(msg.sender).transfer(bidAmount);

        emit BidWithdrawn(punkId, msg.sender);
    }

    /**
     * @dev Get the details of a punk.
     * @param punkId The ID of the punk to query.
     * @return owner The owner of the punk.
     * @return price The price of the punk (0 if not for sale).
     * @return bidder The address of the highest bidder.
     * @return bidAmount The highest bid amount.
     */
    function getPunkDetails(uint256 punkId)
        external
        view
        returns (
            address owner,
            uint256 price,
            address bidder,
            uint256 bidAmount
        )
    {
        require(punkId < totalPunks, "Invalid punk ID");
        Punk storage punk = punks[punkId];
        return (punk.owner, punk.price, punk.bidder, punk.bidAmount);
    }
}
```
