"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openswe.io
Prompt: Write a smart contract in Solidity that facilitates the auctioning of software engineers as NFTs, inspired by the blockchain marketplace concept described on OpenSwe.io.
Generated: DETERMINISTIC_fda252f6649123fb
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title EngineerAuction
 * @dev A smart contract for auctioning software engineers as NFTs
 * Inspired by the blockchain marketplace concept.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract EngineerAuction is ERC721Enumerable, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Tracks the token IDs of the NFTs
    Counters.Counter private _tokenIdCounter;
    
    // Struct for auction details
    struct Auction {
        address seller;
        uint256 tokenId;
        uint256 startPrice;
        uint256 highestBid;
        address highestBidder;
        bool active;
    }

    // Mapping of token ID to corresponding auction
    mapping(uint256 => Auction) public auctions;
    
    // Events for logging
    event NFTMinted(address indexed owner, uint256 tokenId);
    event AuctionCreated(uint256 indexed tokenId, uint256 startPrice);
    event BidPlaced(uint256 indexed tokenId, address indexed bidder, uint256 bidAmount);
    event AuctionEnded(uint256 indexed tokenId, address indexed winner, uint256 winningBid);

    // Constructor: Initialize NFT collection
    constructor() ERC721("SoftwareEngineerNFT", "SENFT") {}

    /**
     * @dev Mint a new NFT for a software engineer.
     * @param to Address of the recipient of the NFT.
     * @return tokenId The ID of the minted NFT.
     */
    function mintNFT(address to) external onlyOwner returns (uint256 tokenId) {
        _tokenIdCounter.increment();
        tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        
        emit NFTMinted(to, tokenId);
    }

    /**
     * @dev Create an auction for an NFT owned by the caller.
     * @param tokenId The ID of the NFT to auction.
     * @param startPrice The starting price of the auction.
     */
    function createAuction(uint256 tokenId, uint256 startPrice) external {
        require(ownerOf(tokenId) == msg.sender, "You must own the NFT to create an auction.");
        require(startPrice > 0, "Start price must be greater than zero.");
        require(!auctions[tokenId].active, "Auction already exists for this NFT.");

        // Approve the contract to handle the NFT
        approve(address(this), tokenId);

        // Create auction
        auctions[tokenId] = Auction({
            seller: msg.sender,
            tokenId: tokenId,
            startPrice: startPrice,
            highestBid: 0,
            highestBidder: address(0),
            active: true
        });

        emit AuctionCreated(tokenId, startPrice);
    }

    /**
     * @dev Place a bid on an active auction.
     * @param tokenId The ID of the NFT being auctioned.
     */
    function placeBid(uint256 tokenId) external payable nonReentrant {
        Auction storage auction = auctions[tokenId];
        require(auction.active, "Auction is not active.");
        require(msg.value > auction.highestBid, "Bid must be higher than the current highest bid.");
        require(msg.sender != auction.seller, "Seller cannot place a bid on their own auction.");

        // Refund the previous highest bidder, if applicable
        if (auction.highestBidder != address(0)) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }

        // Update auction with new highest bid
        auction.highestBid = msg.value;
        auction.highestBidder = msg.sender;

        emit BidPlaced(tokenId, msg.sender, msg.value);
    }

    /**
     * @dev End the auction and transfer the NFT to the highest bidder.
     * @param tokenId The ID of the NFT being auctioned.
     */
    function endAuction(uint256 tokenId) external nonReentrant {
        Auction storage auction = auctions[tokenId];
        require(auction.active, "Auction is not active.");
        require(msg.sender == auction.seller, "Only the seller can end the auction.");

        // Mark auction as inactive
        auction.active = false;

        if (auction.highestBidder != address(0)) {
            // Transfer payment to seller
            payable(auction.seller).transfer(auction.highestBid);

            // Transfer NFT to highest bidder
            _transfer(auction.seller, auction.highestBidder, tokenId);

            emit AuctionEnded(tokenId, auction.highestBidder, auction.highestBid);
        } else {
            // No bids were placed, NFT remains with the seller
            emit AuctionEnded(tokenId, address(0), 0);
        }
    }

    /**
     * @dev Retrieve details of an auction.
     * @param tokenId The ID of the NFT being auctioned.
     * @return Auction details.
     */
    function getAuctionDetails(uint256 tokenId) external view returns (Auction memory) {
        return auctions[tokenId];
    }
}
```
