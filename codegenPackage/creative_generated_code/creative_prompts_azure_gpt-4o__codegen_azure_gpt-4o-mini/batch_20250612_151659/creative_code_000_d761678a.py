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

contract CryptoPunksMarketplace {
    struct Punk {
        address owner;
        uint256 price;
        bool forSale;
    }

    mapping(uint256 => Punk) public punks;
    mapping(address => mapping(uint256 => bool)) public bids;

    event PunkListed(uint256 indexed punkId, uint256 price);
    event PunkSold(uint256 indexed punkId, address indexed buyer);
    event BidPlaced(uint256 indexed punkId, address indexed bidder, uint256 bid);
    event BidAccepted(uint256 indexed punkId, address indexed bidder);

    modifier onlyOwner(uint256 punkId) {
        require(msg.sender == punks[punkId].owner, "Not the owner");
        _;
    }

    modifier punkExists(uint256 punkId) {
        require(punks[punkId].owner != address(0), "Punk does not exist");
        _;
    }

    /// @dev List a punk for sale with a specified price
    /// @param punkId The ID of the punk to list
    /// @param price The price at which the punk is for sale
    function listPunk(uint256 punkId, uint256 price) external punkExists(punkId) onlyOwner(punkId) {
        punks[punkId].price = price;
        punks[punkId].forSale = true;
        emit PunkListed(punkId, price);
    }

    /// @dev Buy a punk directly at its listed price
    /// @param punkId The ID of the punk to buy
    function buyPunk(uint256 punkId) external payable punkExists(punkId) {
        require(punks[punkId].forSale, "Punk not for sale");
        require(msg.value == punks[punkId].price, "Incorrect price");

        address seller = punks[punkId].owner;
        punks[punkId].owner = msg.sender;
        punks[punkId].forSale = false;

        // Transfer funds to the seller
        payable(seller).transfer(msg.value);

        emit PunkSold(punkId, msg.sender);
    }

    /// @dev Place a bid on a punk
    /// @param punkId The ID of the punk to bid on
    /// @param bidAmount The amount of the bid
    function placeBid(uint256 punkId) external payable punkExists(punkId) {
        require(msg.value > 0, "Bid must be greater than zero");
        bids[msg.sender][punkId] = true;

        emit BidPlaced(punkId, msg.sender, msg.value);
    }

    /// @dev Accept a bid on a punk
    /// @param punkId The ID of the punk to accept a bid on
    /// @param bidder The address of the bidder whose bid to accept
    function acceptBid(uint256 punkId, address bidder) external punkExists(punkId) onlyOwner(punkId) {
        require(bids[bidder][punkId], "Bid does not exist");
        
        uint256 bidAmount = address(this).balance; // Assuming the bid was sent with this transaction
        punks[punkId].owner = bidder;
        punks[punkId].forSale = false;

        // Transfer funds to the seller
        payable(msg.sender).transfer(bidAmount);

        emit BidAccepted(punkId, bidder);
    }

    /// @dev Create a new punk and assign it to the caller
    /// @param punkId The ID of the punk to create
    function createPunk(uint256 punkId) external {
        require(punks[punkId].owner == address(0), "Punk already exists");
        punks[punkId] = Punk({
            owner: msg.sender,
            price: 0,
            forSale: false
        });
    }

    /// @dev Prevent accidental Ether transfers to the contract
    receive() external payable {
        revert("Direct payments not allowed");
    }
}
```
