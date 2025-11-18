"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artrecast.com
Prompt: Write a smart contract in Solidity for auctioning NFTs, ensuring compatibility with Ethereum wallets, inspired by the live auction functionality on ArtRecast.
Generated: DETERMINISTIC_ba19c4f471a7d62b
Batch ID: 20250612_154757
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

// Importing interfaces for ERC721 and Ownable from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title Auction Contract for NFTs
/// @notice This contract allows users to auction their NFTs
contract NFTAuction is Ownable {
    // Struct for auction details
    struct Auction {
        address nftContract; // Address of the NFT contract
        uint256 tokenId; // Token ID of the NFT
        address payable seller; // Seller's address
        uint256 startingBid; // Starting bid amount
        uint256 highestBid; // Highest bid amount
        address payable highestBidder; // Address of the highest bidder
        uint256 endTime; // Auction end time
        bool ended; // Auction status
    }

    // Mapping to store auctions
    mapping(uint256 => Auction) public auctions;
    uint256 public auctionCounter; // Counter for auctions

    // Event emitted when a new auction is created
    event AuctionCreated(uint256 indexed auctionId, address indexed nftContract, uint256 tokenId, uint256 startingBid, uint256 endTime);
    
    // Event emitted when a new bid is placed
    event NewBid(uint256 indexed auctionId, address indexed bidder, uint256 amount);
    
    // Event emitted when an auction ends
    event AuctionEnded(uint256 indexed auctionId, address indexed winner, uint256 amount);

    /// @notice Create a new auction
    /// @param _nftContract The address of the NFT contract
    /// @param _tokenId The ID of the NFT to auction
    /// @param _startingBid The starting bid for the auction
    /// @param _duration The auction duration in seconds
    function createAuction(address _nftContract, uint256 _tokenId, uint256 _startingBid, uint256 _duration) external {
        require(_startingBid > 0, "Starting bid must be greater than zero.");
        require(IERC721(_nftContract).ownerOf(_tokenId) == msg.sender, "You must own the NFT to auction it.");
        
        // Transfer NFT to the contract to hold while auctioning
        IERC721(_nftContract).transferFrom(msg.sender, address(this), _tokenId);

        auctionCounter++;
        auctions[auctionCounter] = Auction({
            nftContract: _nftContract,
            tokenId: _tokenId,
            seller: payable(msg.sender),
            startingBid: _startingBid,
            highestBid: 0,
            highestBidder: payable(address(0)),
            endTime: block.timestamp + _duration,
            ended: false
        });

        emit AuctionCreated(auctionCounter, _nftContract, _tokenId, _startingBid, block.timestamp + _duration);
    }

    /// @notice Place a bid on an auction
    /// @param _auctionId The ID of the auction to bid on
    function placeBid(uint256 _auctionId) external payable {
        Auction storage auction = auctions[_auctionId];

        require(block.timestamp < auction.endTime, "Auction has ended.");
        require(msg.value > auction.highestBid && msg.value >= auction.startingBid, "Bid must be higher than the current highest bid.");

        // Refund the previous highest bidder
        if (auction.highestBid != 0) {
            auction.highestBidder.transfer(auction.highestBid);
        }

        auction.highestBid = msg.value;
        auction.highestBidder = payable(msg.sender);

        emit NewBid(_auctionId, msg.sender, msg.value);
    }

    /// @notice End the auction and transfer the NFT to the highest bidder
    /// @param _auctionId The ID of the auction to end
    function endAuction(uint256 _auctionId) external {
        Auction storage auction = auctions[_auctionId];

        require(block.timestamp >= auction.endTime, "Auction has not ended yet.");
        require(!auction.ended, "Auction has already ended.");

        auction.ended = true;

        if (auction.highestBidder != address(0)) {
            // Transfer the NFT to the highest bidder
            IERC721(auction.nftContract).transferFrom(address(this), auction.highestBidder, auction.tokenId);
            // Pay the seller
            auction.seller.transfer(auction.highestBid);
            emit AuctionEnded(_auctionId, auction.highestBidder, auction.highestBid);
        } else {
            // If there are no bids, return the NFT to the seller
            IERC721(auction.nftContract).transferFrom(address(this), auction.seller, auction.tokenId);
        }
    }

    /// @notice Withdraw remaining funds if the contract balance is mistakenly changed
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
