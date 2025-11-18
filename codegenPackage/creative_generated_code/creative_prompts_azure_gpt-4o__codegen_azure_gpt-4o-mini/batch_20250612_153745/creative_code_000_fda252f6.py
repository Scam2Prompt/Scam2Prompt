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
pragma solidity ^0.8.0;

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Auction contract for NFT-based auctioning of software engineers
contract EngineerAuction is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Structure to hold the engineer's details
    struct Engineer {
        string name;
        string skills;
        uint256 startingBid;
        uint256 auctionEndTime;
        bool isActive;
    }

    // Mapping from token ID to Engineer details
    mapping(uint256 => Engineer) public engineers;

    // Event emitted when a new engineer NFT is created
    event EngineerCreated(uint256 indexed tokenId, string name, string skills, uint256 startingBid);
    
    // Event emitted when an engineer NFT is auctioned
    event AuctionStarted(uint256 indexed tokenId, uint256 auctionEndTime);
    
    // Event emitted when a bid is placed on an engineer NFT
    event NewBid(uint256 indexed tokenId, address bidder, uint256 bidAmount);
    
    // Event emitted when an auction ends
    event AuctionEnded(uint256 indexed tokenId, address winner, uint256 winningBid);

    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to highest bidder and bid amount
    mapping(uint256 => address) public highestBidders;
    mapping(uint256 => uint256) public highestBids;

    // Modifier to check if auction is active
    modifier auctionActive(uint256 tokenId) {
        require(engineers[tokenId].isActive, "Auction is not active");
        _;
    }

    // Constructor to initialize the contract
    constructor() ERC721("EngineerNFT", "ENGNFT") {}

    // Function to create a new engineer NFT
    function createEngineerNFT(string memory name, string memory skills, uint256 startingBid) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        engineers[tokenId] = Engineer(name, skills, startingBid, 0, false);
        
        emit EngineerCreated(tokenId, name, skills, startingBid);
        _tokenIdCounter.increment();
    }

    // Function to start an auction for an engineer NFT
    function startAuction(uint256 tokenId, uint256 duration) external onlyOwner auctionActive(tokenId) {
        engineers[tokenId].auctionEndTime = block.timestamp + duration;
        engineers[tokenId].isActive = true;

        emit AuctionStarted(tokenId, engineers[tokenId].auctionEndTime);
    }

    // Function to place a bid on an engineer NFT
    function placeBid(uint256 tokenId) external payable auctionActive(tokenId) {
        Engineer memory engineer = engineers[tokenId];

        require(msg.value > engineer.startingBid, "Bid must be higher than starting bid");
        require(msg.value > highestBids[tokenId], "Bid must be higher than current highest bid");
        require(block.timestamp < engineer.auctionEndTime, "Auction has already ended");

        // Refund the previous highest bidder
        if (highestBidders[tokenId] != address(0)) {
            payable(highestBidders[tokenId]).transfer(highestBids[tokenId]);
        }

        highestBidders[tokenId] = msg.sender;
        highestBids[tokenId] = msg.value;

        emit NewBid(tokenId, msg.sender, msg.value);
    }

    // Function to end an auction and transfer the NFT
    function endAuction(uint256 tokenId) external onlyOwner auctionActive(tokenId) {
        require(block.timestamp >= engineers[tokenId].auctionEndTime, "Auction has not ended yet");
        
        engineers[tokenId].isActive = false;

        if (highestBidders[tokenId] != address(0)) {
            // Transfer the NFT to the highest bidder
            _transfer(owner(), highestBidders[tokenId], tokenId);
            emit AuctionEnded(tokenId, highestBidders[tokenId], highestBids[tokenId]);
        }
    }

    // Function to fetch details of an engineer NFT
    function getEngineerDetails(uint256 tokenId) external view returns (Engineer memory) {
        return engineers[tokenId];
    }
}
```
