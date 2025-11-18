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

/**
 * @title MetamonNFTAuction
 * @dev This contract facilitates NFT auctions for Metamon assets in the USM Metaverse.
 *      It is designed to be compatible with BNB Chain standards.
 */
contract MetamonNFTAuction {
    // Represents a single auction
    struct Auction {
        address seller; // Address of the seller
        address highestBidder; // Address of the highest bidder
        uint256 highestBid; // Value of the highest bid
        uint256 startingPrice; // Minimum bid price for the auction
        uint256 endTime; // Auction expiration time (in seconds since epoch)
        bool isActive; // Whether the auction is active
    }

    // Mapping from NFT token ID to its corresponding auction
    mapping(uint256 => Auction) public auctions;

    // Events for logging important actions
    event AuctionCreated(uint256 indexed tokenId, address indexed seller, uint256 startingPrice, uint256 endTime);
    event BidPlaced(uint256 indexed tokenId, address indexed bidder, uint256 bidAmount);
    event AuctionEnded(uint256 indexed tokenId, address indexed winner, uint256 winningBid);

    // Reference to the NFT contract
    IERC721 public nftContract;

    // Ensures bid amount is greater than zero
    modifier nonZeroValue() {
        require(msg.value > 0, "Bid amount must be greater than zero");
        _;
    }

    // Ensures auction exists and is active
    modifier validAuction(uint256 tokenId) {
        require(auctions[tokenId].isActive, "No active auction found for this NFT token ID");
        require(block.timestamp < auctions[tokenId].endTime, "Auction has already ended");
        _;
    }

    /**
     * @dev Constructor function to initialize the contract with the NFT contract address.
     * @param _nftContract The address of the ERC721-compliant NFT contract.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Creates an auction for a given NFT token ID.
     * @param tokenId The ID of the NFT token to be auctioned.
     * @param startingPrice The minimum bid price for the auction.
     * @param duration The duration of the auction in seconds.
     */
    function createAuction(uint256 tokenId, uint256 startingPrice, uint256 duration) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT token");
        require(duration > 0, "Auction duration must be greater than zero");

        // Transfer NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Initialize auction details
        auctions[tokenId] = Auction({
            seller: msg.sender,
            highestBidder: address(0),
            highestBid: 0,
            startingPrice: startingPrice,
            endTime: block.timestamp + duration,
            isActive: true
        });

        emit AuctionCreated(tokenId, msg.sender, startingPrice, block.timestamp + duration);
    }

    /**
     * @dev Places a bid on an active auction for a given NFT token ID.
     * @param tokenId The ID of the NFT token being auctioned.
     */
    function placeBid(uint256 tokenId) external payable nonZeroValue validAuction(tokenId) {
        Auction storage auction = auctions[tokenId];

        require(msg.value > auction.highestBid && msg.value >= auction.startingPrice, "Bid amount must be higher than the current highest bid and starting price");

        // Refund the previous highest bidder if applicable
        if (auction.highestBidder != address(0)) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }

        // Update auction details
        auction.highestBidder = msg.sender;
        auction.highestBid = msg.value;

        emit BidPlaced(tokenId, msg.sender, msg.value);
    }

    /**
     * @dev Ends an auction for a given NFT token ID and transfers the asset to the highest bidder.
     * @param tokenId The ID of the NFT token being auctioned.
     */
    function endAuction(uint256 tokenId) external {
        Auction storage auction = auctions[tokenId];

        require(auction.isActive, "Auction is already ended or does not exist");
        require(block.timestamp >= auction.endTime, "Auction is still active");
        require(msg.sender == auction.seller, "Only the seller can end the auction");

        auction.isActive = false;

        if (auction.highestBidder != address(0)) {
            // Transfer NFT to the highest bidder
            nftContract.transferFrom(address(this), auction.highestBidder, tokenId);
            payable(auction.seller).transfer(auction.highestBid);
        } else {
            // No bids were placed, return the NFT to the seller
            nftContract.transferFrom(address(this), auction.seller, tokenId);
        }

        emit AuctionEnded(tokenId, auction.highestBidder, auction.highestBid);
    }

    /**
     * @dev Cancels an active auction for a given NFT token ID and returns the asset to the seller.
     * @param tokenId The ID of the NFT token being auctioned.
     */
    function cancelAuction(uint256 tokenId) external {
        Auction storage auction = auctions[tokenId];

        require(auction.isActive, "Auction is already ended or does not exist");
        require(msg.sender == auction.seller, "Only the seller can cancel the auction");
        
        auction.isActive = false;

        // Return the NFT to the seller
        nftContract.transferFrom(address(this), auction.seller, tokenId);

        // Refund the highest bidder if applicable
        if (auction.highestBidder != address(0)) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }
    }
}

// Minimalistic ERC721 interface for interacting with the NFT contract
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}
```
