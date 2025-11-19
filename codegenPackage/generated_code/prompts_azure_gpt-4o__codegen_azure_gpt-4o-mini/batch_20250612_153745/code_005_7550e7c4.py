"""
Generated Code Metadata:
========================
Original URL: https://openswe.io
Prompt: Develop a smart contract for creating and managing non-fungible tokens (NFTs) tailored for software engineers, inspired by the auction model described on OpenSwe.io.
Generated: DETERMINISTIC_7550e7c4064e5992
Batch ID: 20250612_153745
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTAuction
 * @dev A smart contract for creating and managing non-fungible tokens (NFTs) with an auction model.
 */
contract NFTAuction is ERC721, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to hold auction details
    struct Auction {
        address payable seller;
        uint256 startingPrice;
        uint256 highestBid;
        address highestBidder;
        uint256 endTime;
        bool active;
    }

    // Mapping from token ID to auction details
    mapping(uint256 => Auction) public auctions;

    // Event emitted when a new auction is created
    event AuctionCreated(uint256 indexed tokenId, uint256 startingPrice, uint256 endTime);

    // Event emitted when a new bid is placed
    event NewBid(uint256 indexed tokenId, address indexed bidder, uint256 amount);

    // Event emitted when an auction ends
    event AuctionEnded(uint256 indexed tokenId, address indexed winner, uint256 amount);

    /**
     * @dev Constructor to initialize the NFT contract with a name and symbol.
     */
    constructor() ERC721("NFTAuction", "NFTA") {}

    /**
     * @dev Function to mint a new NFT and create an auction for it.
     * @param startingPrice The starting price for the auction.
     * @param duration The duration of the auction in seconds.
     */
    function mintAndCreateAuction(uint256 startingPrice, uint256 duration) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();

        uint256 endTime = block.timestamp + duration;

        auctions[tokenId] = Auction({
            seller: payable(msg.sender),
            startingPrice: startingPrice,
            highestBid: 0,
            highestBidder: address(0),
            endTime: endTime,
            active: true
        });

        emit AuctionCreated(tokenId, startingPrice, endTime);
    }

    /**
     * @dev Function to place a bid on an active auction.
     * @param tokenId The ID of the NFT being bid on.
     */
    function bid(uint256 tokenId) external payable {
        Auction storage auction = auctions[tokenId];

        require(auction.active, "Auction is not active");
        require(block.timestamp < auction.endTime, "Auction has ended");
        require(msg.value > auction.startingPrice, "Bid must be higher than starting price");
        require(msg.value > auction.highestBid, "Bid must be higher than current highest bid");

        // Refund the previous highest bidder
        if (auction.highestBidder != address(0)) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }

        auction.highestBidder = msg.sender;
        auction.highestBid = msg.value;

        emit NewBid(tokenId, msg.sender, msg.value);
    }

    /**
     * @dev Function to end the auction and transfer the NFT to the highest bidder.
     * @param tokenId The ID of the NFT being auctioned.
     */
    function endAuction(uint256 tokenId) external {
        Auction storage auction = auctions[tokenId];

        require(auction.active, "Auction is not active");
        require(block.timestamp >= auction.endTime, "Auction has not ended yet");
        
        auction.active = false;

        if (auction.highestBidder != address(0)) {
            // Transfer the NFT to the highest bidder
            _transfer(auction.seller, auction.highestBidder, tokenId);
            // Transfer the highest bid amount to the seller
            auction.seller.transfer(auction.highestBid);
            emit AuctionEnded(tokenId, auction.highestBidder, auction.highestBid);
        } else {
            // If no bids were placed, the seller can reclaim the NFT
            _transfer(auction.seller, auction.seller, tokenId);
        }
    }

    /**
     * @dev Function to get auction details for a specific token ID.
     * @param tokenId The ID of the NFT.
     * @return The auction details.
     */
    function getAuctionDetails(uint256 tokenId) external view returns (Auction memory) {
        return auctions[tokenId];
    }
}
```
