"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artorvias.com
Prompt: Create a smart contract in Solidity for listing digital artworks on Artorvia, allowing users to set secondary sales fees and choose between auction or fixed-price sales.
Generated: DETERMINISTIC_9a62eace4939b1e9
Batch ID: 20250612_150446
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
 * @title Artorvia Marketplace Contract
 * @dev This contract allows users to list digital artworks for sale, 
 *      choose between auction or fixed-price sales, and set secondary sales fees.
 */
contract ArtorviaMarketplace {
    struct Artwork {
        uint256 id;
        address payable artist;
        string uri; // URI for the artwork metadata
        uint256 price; // Fixed price for the artwork
        uint256 auctionEndTime; // End time for the auction
        address highestBidder; // Current highest bidder
        uint256 highestBid; // Current highest bid
        bool isAuction; // Flag for auction or fixed price
        bool isListed; // Flag indicating if the artwork is listed
        uint256 secondaryFee; // Percentage fee for secondary sales
    }

    uint256 public artworkCount; // Total number of artworks listed
    mapping(uint256 => Artwork) public artworks; // Mapping of artwork ID to Artwork struct
    event ArtworkListed(uint256 indexed artworkId, address indexed artist, bool isAuction, uint256 price, uint256 secondaryFee);
    event ArtworkSold(uint256 indexed artworkId, address indexed buyer, uint256 price);
    event BidPlaced(uint256 indexed artworkId, address indexed bidder, uint256 bidAmount);
    event AuctionEnded(uint256 indexed artworkId, address indexed winner, uint256 winningBid);

    /**
     * @dev List a new artwork on the marketplace.
     * @param _uri URI of the artwork metadata.
     * @param _price Fixed price for the artwork (if not in auction).
     * @param _isAuction Boolean indicating if the sale is an auction.
     * @param _auctionDuration Duration for the auction in seconds (ignored if not auction).
     * @param _secondaryFee Percentage fee for secondary sales (0-100).
     */
    function listArtwork(
        string memory _uri,
        uint256 _price,
        bool _isAuction,
        uint256 _auctionDuration,
        uint256 _secondaryFee
    ) external {
        require(_secondaryFee <= 100, "Secondary fee must be between 0 and 100");

        artworkCount++;
        Artwork memory newArtwork = Artwork({
            id: artworkCount,
            artist: payable(msg.sender),
            uri: _uri,
            price: _price,
            auctionEndTime: _isAuction ? block.timestamp + _auctionDuration : 0,
            highestBidder: address(0),
            highestBid: 0,
            isAuction: _isAuction,
            isListed: true,
            secondaryFee: _secondaryFee
        });

        artworks[artworkCount] = newArtwork;
        emit ArtworkListed(artworkCount, msg.sender, _isAuction, _price, _secondaryFee);
    }

    /**
     * @dev Buy an artwork listed for a fixed price.
     * @param _artworkId ID of the artwork to buy.
     */
    function buyArtwork(uint256 _artworkId) external payable {
        Artwork storage artwork = artworks[_artworkId];
        require(artwork.isListed, "Artwork not listed");
        require(!artwork.isAuction, "Artwork is in auction, use bid function");
        require(msg.value == artwork.price, "Incorrect price sent");

        artwork.artist.transfer(msg.value);
        artwork.isListed = false; // Mark artwork as sold
        emit ArtworkSold(_artworkId, msg.sender, artwork.price);
    }

    /**
     * @dev Place a bid on an artwork listed for auction.
     * @param _artworkId ID of the artwork to bid on.
     */
    function bidOnArtwork(uint256 _artworkId) external payable {
        Artwork storage artwork = artworks[_artworkId];
        require(artwork.isListed, "Artwork not listed");
        require(artwork.isAuction, "Artwork is not an auction");
        require(block.timestamp < artwork.auctionEndTime, "Auction has ended");
        require(msg.value > artwork.highestBid, "Bid must be higher than current highest bid");

        // Refund the previous highest bidder
        if (artwork.highestBidder != address(0)) {
            payable(artwork.highestBidder).transfer(artwork.highestBid);
        }

        artwork.highestBidder = msg.sender;
        artwork.highestBid = msg.value;
        emit BidPlaced(_artworkId, msg.sender, msg.value);
    }

    /**
     * @dev End the auction for an artwork and transfer ownership.
     * @param _artworkId ID of the artwork to end auction for.
     */
    function endAuction(uint256 _artworkId) external {
        Artwork storage artwork = artworks[_artworkId];
        require(artwork.isListed, "Artwork not listed");
        require(artwork.isAuction, "Not an auction");
        require(block.timestamp >= artwork.auctionEndTime, "Auction not yet ended");

        artwork.isListed = false; // Mark artwork as sold
        if (artwork.highestBidder != address(0)) {
            artwork.artist.transfer(artwork.highestBid);
            emit AuctionEnded(_artworkId, artwork.highestBidder, artwork.highestBid);
        }
    }

    /**
     * @dev Withdraw the secondary sales fee for the artist.
     * @param _artworkId ID of the artwork for which to withdraw fees.
     */
    function withdrawSecondaryFees(uint256 _artworkId) external {
        Artwork storage artwork = artworks[_artworkId];
        require(msg.sender == artwork.artist, "Only the artist can withdraw fees");
        // Logic for calculating and transferring secondary fees (if applicable)
        // This could be implemented further based on how secondary sales are tracked.
    }
}
```
