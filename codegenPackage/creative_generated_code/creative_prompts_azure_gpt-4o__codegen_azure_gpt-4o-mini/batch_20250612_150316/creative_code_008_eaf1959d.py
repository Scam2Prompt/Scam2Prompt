"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-io.pages.dev
Prompt: Write a Solidity smart contract to facilitate NFT auctions for Metamon assets in the USM Metaverse, ensuring compatibility with BNB Chain standards.
Generated: DETERMINISTIC_eaf1959db90c9b34
Batch ID: 20250612_150316
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

// Import OpenZeppelin ERC721NFT interface and Ownable contract
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTAuction contract allows users to auction Metamon NFTs
contract NFTAuction is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Struct to hold auction details
    struct Auction {
        uint256 tokenId;
        address payable seller;
        uint256 startingBid;
        uint256 highestBid;
        address payable highestBidder;
        uint256 endTime;
        bool isActive;
    }

    Counters.Counter private _auctionIdCounter; // Counter for auction IDs
    mapping(uint256 => Auction) public auctions; // Mapping from auction ID to Auction struct

    // Events for auction creation and bidding
    event AuctionCreated(uint256 auctionId, uint256 tokenId, uint256 startingBid, uint256 endTime);
    event NewBid(uint256 auctionId, address bidder, uint256 bidAmount);
    event AuctionEnded(uint256 auctionId, address winner, uint256 winningBid);

    // Modifier to check if auction is active
    modifier auctionActive(uint256 auctionId) {
        require(auctions[auctionId].isActive, "Auction is not active");
        _;
    }

    // Modifier to check if auction has ended
    modifier auctionEnded(uint256 auctionId) {
        require(block.timestamp > auctions[auctionId].endTime, "Auction has not ended yet");
        _;
    }

    // Constructor to initialize the ERC721 token with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to create a new auction
    function createAuction(uint256 tokenId, uint256 startingBid, uint256 duration) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        require(duration > 0, "Duration must be greater than 0");

        _auctionIdCounter.increment();
        uint256 auctionId = _auctionIdCounter.current();
        
        auctions[auctionId] = Auction({
            tokenId: tokenId,
            seller: payable(msg.sender),
            startingBid: startingBid,
            highestBid: 0,
            highestBidder: payable(address(0)),
            endTime: block.timestamp + duration,
            isActive: true
        });

        emit AuctionCreated(auctionId, tokenId, startingBid, block.timestamp + duration);
    }

    // Function to place a bid on an active auction
    function bid(uint256 auctionId) external payable auctionActive(auctionId) {
        Auction storage auction = auctions[auctionId];

        require(msg.value > auction.highestBid && msg.value >= auction.startingBid, "Bid amount too low");

        // Refund the previous highest bidder
        if (auction.highestBid > 0) {
            auction.highestBidder.transfer(auction.highestBid);
        }

        auction.highestBid = msg.value;
        auction.highestBidder = payable(msg.sender);

        emit NewBid(auctionId, msg.sender, msg.value);
    }

    // Function to end an auction and transfer the NFT to the highest bidder
    function endAuction(uint256 auctionId) external auctionActive(auctionId) auctionEnded(auctionId) {
        Auction storage auction = auctions[auctionId];
        
        auction.isActive = false;

        if (auction.highestBidder != address(0)) {
            // Transfer the NFT to the highest bidder
            _transfer(auction.seller, auction.highestBidder, auction.tokenId);
            // Send the funds to the seller
            auction.seller.transfer(auction.highestBid);
            emit AuctionEnded(auctionId, auction.highestBidder, auction.highestBid);
        } else {
            emit AuctionEnded(auctionId, address(0), 0); // No bids were placed
        }
    }

    // Function to withdraw unsold NFTs (only for the seller)
    function withdrawUnsoldNFT(uint256 auctionId) external onlyOwner auctionEnded(auctionId) {
        Auction storage auction = auctions[auctionId];

        require(!auction.isActive, "Auction is still active");
        require(auction.highestBidder == address(0), "Cannot withdraw after auction ended with bids");

        // Transfer the NFT back to the seller
        _transfer(address(this), auction.seller, auction.tokenId);
    }
}
```
