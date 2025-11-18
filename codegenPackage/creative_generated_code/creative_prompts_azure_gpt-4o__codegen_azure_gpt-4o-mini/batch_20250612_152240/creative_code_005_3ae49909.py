"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safetontransact.pages.dev
Prompt: Create a smart contract on the TON Blockchain to facilitate NFT auctions, ensuring compatibility with the Safe Transaction feature and Tonkeeper wallet.
Generated: DETERMINISTIC_3ae4990996d1adf0
Batch ID: 20250612_152240
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

// Import the necessary libraries and interfaces for working with NFTs and auctions
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";

// Contract for NFT auctions on the TON Blockchain
contract NFTAuction is ERC721Holder {
    // Struct to represent an auction
    struct Auction {
        address seller;      // Address of the seller
        address nftAddress;  // Address of the NFT contract
        uint256 tokenId;     // ID of the NFT being auctioned
        uint256 startPrice;  // Starting price of the auction
        uint256 biddingEnd;  // End time for bidding
        address highestBidder; // Address of the current highest bidder
        uint256 highestBid;  // Amount of the highest bid
        bool ended;          // Status of the auction
    }

    // Mapping to store auctions by their ID
    mapping(uint256 => Auction) public auctions;
    uint256 public auctionCount; // Counter for auction IDs

    // Event emitted when a new auction is created
    event AuctionCreated(uint256 auctionId, address seller, address nftAddress, uint256 tokenId, uint256 startPrice, uint256 biddingEnd);
    // Event emitted when a new bid is placed
    event NewBid(uint256 auctionId, address bidder, uint256 amount);
    // Event emitted when an auction ends
    event AuctionEnded(uint256 auctionId, address winner, uint256 amount);

    // Function to create a new auction
    function createAuction(address _nftAddress, uint256 _tokenId, uint256 _startPrice, uint256 _biddingTime) external {
        // Validate input parameters
        require(_startPrice > 0, "Start price must be greater than zero");
        require(_biddingTime > 0, "Bidding time must be greater than zero");

        // Increase auction count and create a new auction
        auctionCount++;
        auctions[auctionCount] = Auction({
            seller: msg.sender,
            nftAddress: _nftAddress,
            tokenId: _tokenId,
            startPrice: _startPrice,
            biddingEnd: block.timestamp + _biddingTime,
            highestBidder: address(0),
            highestBid: 0,
            ended: false
        });

        // Transfer the NFT to this contract
        IERC721(_nftAddress).safeTransferFrom(msg.sender, address(this), _tokenId);

        // Emit the auction created event
        emit AuctionCreated(auctionCount, msg.sender, _nftAddress, _tokenId, _startPrice, auctions[auctionCount].biddingEnd);
    }

    // Function to place a bid in an auction
    function placeBid(uint256 _auctionId) external payable {
        Auction storage auction = auctions[_auctionId];

        // Validate that the auction exists and has not ended
        require(auction.seller != address(0), "Auction does not exist");
        require(block.timestamp < auction.biddingEnd, "Auction has already ended");
        require(msg.value > auction.highestBid && msg.value >= auction.startPrice, "Bid amount is not high enough");

        // Refund the previous highest bidder
        if (auction.highestBidder != address(0)) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }

        // Update the highest bid and bidder
        auction.highestBidder = msg.sender;
        auction.highestBid = msg.value;

        // Emit the new bid event
        emit NewBid(_auctionId, msg.sender, msg.value);
    }

    // Function to end the auction and transfer the NFT to the winner
    function endAuction(uint256 _auctionId) external {
        Auction storage auction = auctions[_auctionId];

        // Validate that the auction exists and can be ended
        require(auction.seller == msg.sender || auction.highestBidder == msg.sender, "Only the seller or highest bidder can end the auction");
        require(block.timestamp >= auction.biddingEnd, "Auction is still ongoing");
        require(!auction.ended, "Auction has already ended");

        // Mark the auction as ended
        auction.ended = true;

        // Transfer the NFT to the highest bidder if a valid bid was made
        if (auction.highestBidder != address(0)) {
            IERC721(auction.nftAddress).safeTransferFrom(address(this), auction.highestBidder, auction.tokenId);
            // Transfer the highest bid amount to the seller
            payable(auction.seller).transfer(auction.highestBid);
            emit AuctionEnded(_auctionId, auction.highestBidder, auction.highestBid);
        } else {
            // If no bids were placed, return the NFT to the seller
            IERC721(auction.nftAddress).safeTransferFrom(address(this), auction.seller, auction.tokenId);
        }
    }

    // Fallback function to prevent sending Ether directly to the contract
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
