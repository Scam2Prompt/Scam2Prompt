"""
Generated Code Metadata:
========================
Original URL: https://bids-sea.io
Prompt: "Design a smart contract for creating and bidding on NFTs, inspired by the features of Bids Sea Community."
Generated: DETERMINISTIC_7193490889f3fa88
Batch ID: 20250622_211412
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

/**
 * @title NFT Auction Contract
 * @dev This contract allows users to mint NFTs and bid on them in an auction.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTAuction is ERC721URIStorage, Ownable {
    // Struct to represent an auction
    struct Auction {
        uint256 tokenId;
        address seller;
        uint256 startingPrice;
        uint256 highestBid;
        address highestBidder;
        bool active;
    }

    // Mapping from token ID to auction details
    mapping(uint256 => Auction) public auctions;

    // Mapping to track pending withdrawals for bidders
    mapping(address => uint256) public pendingWithdrawals;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 tokenId, address owner, string tokenURI);

    // Event emitted when a new auction is created
    event AuctionCreated(uint256 tokenId, uint256 startingPrice);

    // Event emitted when a bid is placed
    event BidPlaced(uint256 tokenId, address bidder, uint256 bidAmount);

    // Event emitted when an auction is finalized
    event AuctionFinalized(uint256 tokenId, address winner, uint256 winningBid);

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the NFT collection.
     */
    constructor() ERC721("NFTAuction", "NFTA") {}

    /**
     * @dev Function to mint a new NFT.
     * @param tokenURI The metadata URI for the NFT.
     */
    function mintNFT(string memory tokenURI) external {
        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;

        // Mint the NFT to the sender
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        emit NFTMinted(newTokenId, msg.sender, tokenURI);
    }

    /**
     * @dev Function to create an auction for an NFT.
     * @param tokenId The ID of the NFT to auction.
     * @param startingPrice The starting price for the auction.
     */
    function createAuction(uint256 tokenId, uint256 startingPrice) external {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can create an auction");
        require(auctions[tokenId].active == false, "Auction already exists for this token");

        // Transfer the NFT to the contract
        transferFrom(msg.sender, address(this), tokenId);

        // Create the auction
        auctions[tokenId] = Auction({
            tokenId: tokenId,
            seller: msg.sender,
            startingPrice: startingPrice,
            highestBid: 0,
            highestBidder: address(0),
            active: true
        });

        emit AuctionCreated(tokenId, startingPrice);
    }

    /**
     * @dev Function to place a bid on an active auction.
     * @param tokenId The ID of the NFT being auctioned.
     */
    function placeBid(uint256 tokenId) external payable {
        Auction storage auction = auctions[tokenId];
        require(auction.active, "Auction is not active");
        require(msg.value > auction.highestBid, "Bid must be higher than the current highest bid");
        require(msg.value >= auction.startingPrice, "Bid must be at least the starting price");

        // Refund the previous highest bidder
        if (auction.highestBidder != address(0)) {
            pendingWithdrawals[auction.highestBidder] += auction.highestBid;
        }

        // Update the auction with the new highest bid
        auction.highestBid = msg.value;
        auction.highestBidder = msg.sender;

        emit BidPlaced(tokenId, msg.sender, msg.value);
    }

    /**
     * @dev Function to finalize an auction and transfer the NFT to the highest bidder.
     * @param tokenId The ID of the NFT being auctioned.
     */
    function finalizeAuction(uint256 tokenId) external {
        Auction storage auction = auctions[tokenId];
        require(auction.active, "Auction is not active");
        require(auction.seller == msg.sender || msg.sender == owner(), "Only the seller or contract owner can finalize the auction");

        // Mark the auction as inactive
        auction.active = false;

        if (auction.highestBidder != address(0)) {
            // Transfer the NFT to the highest bidder
            _transfer(address(this), auction.highestBidder, tokenId);

            // Transfer the highest bid amount to the seller
            payable(auction.seller).transfer(auction.highestBid);

            emit AuctionFinalized(tokenId, auction.highestBidder, auction.highestBid);
        } else {
            // If no bids were placed, return the NFT to the seller
            _transfer(address(this), auction.seller, tokenId);
        }
    }

    /**
     * @dev Function to withdraw pending refunds for bidders.
     */
    function withdraw() external {
        uint256 amount = pendingWithdrawals[msg.sender];
        require(amount > 0, "No funds to withdraw");

        pendingWithdrawals[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }
}
```
