"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openswe.io
Prompt: Develop a smart contract for creating and managing non-fungible tokens (NFTs) tailored for software engineers, inspired by the auction model described on OpenSwe.io.
Generated: DETERMINISTIC_7550e7c4064e5992
Batch ID: 20250612_153745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, well-documented implementation of an NFT smart contract with an auction model, written in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DevNFTAuction
 * @dev Smart contract to create and manage NFTs tailored for software engineers with an auction system.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DevNFTAuction is ERC721URIStorage, Ownable {
    struct Auction {
        uint256 tokenId;
        address seller;
        uint256 startingPrice;
        uint256 highestBid;
        address highestBidder;
        bool active;
    }

    uint256 private _tokenIds;
    mapping(uint256 => Auction) public auctions;

    event NFTMinted(uint256 tokenId, address owner, string tokenURI);
    event AuctionCreated(uint256 tokenId, uint256 startingPrice);
    event NewBid(uint256 tokenId, address bidder, uint256 bidAmount);
    event AuctionEnded(uint256 tokenId, address winner, uint256 winningBid);

    constructor() ERC721("DevNFT", "DEVNFT") {}

    /**
     * @dev Mint a new NFT and create an auction for it.
     * @param tokenURI The metadata URI of the NFT.
     * @param startingPrice The starting price for the auction.
     */
    function mintNFTWithAuction(string memory tokenURI, uint256 startingPrice) external onlyOwner {
        require(startingPrice > 0, "Starting price must be greater than 0");

        // Mint the NFT
        _tokenIds++;
        uint256 newTokenId = _tokenIds;
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        // Create a new auction
        auctions[newTokenId] = Auction({
            tokenId: newTokenId,
            seller: msg.sender,
            startingPrice: startingPrice,
            highestBid: 0,
            highestBidder: address(0),
            active: true
        });

        emit NFTMinted(newTokenId, msg.sender, tokenURI);
        emit AuctionCreated(newTokenId, startingPrice);
    }

    /**
     * @dev Bid on an active auction.
     * @param tokenId The ID of the NFT being auctioned.
     */
    function bid(uint256 tokenId) external payable {
        Auction storage auction = auctions[tokenId];
        require(auction.active, "Auction is not active");
        require(msg.value > auction.highestBid, "Bid must be higher than the current highest bid");
        require(msg.value >= auction.startingPrice, "Bid must be at least the starting price");

        // Refund the previous highest bidder
        if (auction.highestBidder != address(0)) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }

        // Update the auction with the new highest bid
        auction.highestBid = msg.value;
        auction.highestBidder = msg.sender;

        emit NewBid(tokenId, msg.sender, msg.value);
    }

    /**
     * @dev End an auction and transfer the NFT to the highest bidder.
     * @param tokenId The ID of the NFT being auctioned.
     */
    function endAuction(uint256 tokenId) external {
        Auction storage auction = auctions[tokenId];
        require(auction.active, "Auction is not active");
        require(msg.sender == auction.seller, "Only the seller can end the auction");

        // Mark the auction as ended
        auction.active = false;

        if (auction.highestBidder != address(0)) {
            // Transfer the NFT to the highest bidder
            _transfer(auction.seller, auction.highestBidder, tokenId);

            // Transfer the highest bid amount to the seller
            payable(auction.seller).transfer(auction.highestBid);

            emit AuctionEnded(tokenId, auction.highestBidder, auction.highestBid);
        } else {
            // No bids were placed; auction ends without transfer
            emit AuctionEnded(tokenId, address(0), 0);
        }
    }

    /**
     * @dev Get details of an auction.
     * @param tokenId The ID of the NFT being auctioned.
     * @return Auction details.
     */
    function getAuctionDetails(uint256 tokenId) external view returns (Auction memory) {
        return auctions[tokenId];
    }
}
```
