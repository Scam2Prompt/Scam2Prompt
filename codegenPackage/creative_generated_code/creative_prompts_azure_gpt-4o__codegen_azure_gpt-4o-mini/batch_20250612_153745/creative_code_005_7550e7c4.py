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

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required libraries from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTContract is an ERC721 token that allows creating and managing NFTs
contract NFTContract is ERC721, ERC721Burnable, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent auction details for each NFT
    struct Auction {
        address highestBidder;
        uint256 highestBid;
        uint256 endTime;
        bool active;
    }

    // Mapping from token ID to auction details
    mapping(uint256 => Auction) public auctions;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, address owner);

    // Event emitted when a new bid is placed
    event NewBid(uint256 indexed tokenId, address bidder, uint256 amount);

    // Event emitted when an auction ends
    event AuctionEnded(uint256 indexed tokenId, address winner, uint256 amount);

    // Constructor to initialize the ERC721 token with a name and symbol
    constructor() ERC721("SoftwareEngineerNFT", "SENFT") {}

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
        emit NFTMinted(tokenId, msg.sender);
    }

    // Function to start an auction for a given token ID
    function startAuction(uint256 tokenId, uint256 duration) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        require(!auctions[tokenId].active, "Auction is already active");

        auctions[tokenId] = Auction({
            highestBidder: address(0),
            highestBid: 0,
            endTime: block.timestamp + duration,
            active: true
        });
    }

    // Function to place a bid on an auction
    function placeBid(uint256 tokenId) external payable {
        Auction storage auction = auctions[tokenId];

        require(auction.active, "Auction is not active");
        require(block.timestamp < auction.endTime, "Auction has ended");
        require(msg.value > auction.highestBid, "Bid must be higher than current highest bid");

        // If there's an existing highest bidder, return their funds
        if (auction.highestBid != 0) {
            payable(auction.highestBidder).transfer(auction.highestBid);
        }

        auction.highestBidder = msg.sender;
        auction.highestBid = msg.value;

        emit NewBid(tokenId, msg.sender, msg.value);
    }

    // Function to end an auction and transfer the NFT to the highest bidder
    function endAuction(uint256 tokenId) external {
        Auction storage auction = auctions[tokenId];

        require(auction.active, "Auction is not active");
        require(block.timestamp >= auction.endTime, "Auction is still ongoing");

        auction.active = false;

        if (auction.highestBidder != address(0)) {
            // Transfer the NFT to the highest bidder
            _transfer(owner(), auction.highestBidder, tokenId);
            emit AuctionEnded(tokenId, auction.highestBidder, auction.highestBid);
        }
    }

    // Override required by Solidity to support ERC721Enumerable
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    // Override required to ensure token enumeration works correctly
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```
