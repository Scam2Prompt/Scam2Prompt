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

/**
 * @title NFTAuction
 * @dev Implements a simple auction for NFTs compatible with Ethereum wallets.
 */
contract NFTAuction {
    // State variables
    address public nftOwner; // Address of the NFT owner who initiated the auction
    address public highestBidder; // Address of the current highest bidder
    uint256 public highestBid; // The current highest bid amount (in wei)
    uint256 public auctionEndTime; // Timestamp for when the auction ends
    bool public auctionEnded; // Flag to indicate whether the auction has ended

    mapping(address => uint256) public pendingReturns; // Tracks pending returns for outbid users

    address public nftContract; // The address of the NFT contract
    uint256 public tokenId; // The token ID of the NFT being auctioned

    // Events
    event AuctionStarted(address indexed nftOwner, address nftContract, uint256 tokenId, uint256 endTime);
    event HighestBidIncreased(address indexed bidder, uint256 amount);
    event AuctionEnded(address winner, uint256 amount);
    event FundsWithdrawn(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == nftOwner, "Only the owner can call this function");
        _;
    }

    modifier auctionActive() {
        require(block.timestamp <= auctionEndTime, "Auction has already ended");
        _;
    }

    modifier auctionEndedCheck() {
        require(block.timestamp > auctionEndTime, "Auction is still in progress");
        require(!auctionEnded, "Auction has already been finalized");
        _;
    }

    /**
     * @dev Initializes the auction with NFT details and an end time.
     * @param _nftContract The address of the NFT contract.
     * @param _tokenId The token ID of the NFT being auctioned.
     * @param _duration Duration of the auction in seconds.
     */
    constructor(address _nftContract, uint256 _tokenId, uint256 _duration) {
        nftOwner = msg.sender;
        nftContract = _nftContract;
        tokenId = _tokenId;
        auctionEndTime = block.timestamp + _duration;
        emit AuctionStarted(nftOwner, nftContract, tokenId, auctionEndTime);
    }

    /**
     * @dev Places a bid for the NFT during the auction.
     * Bidders must send Ether greater than the current highest bid.
     */
    function placeBid() external payable auctionActive {
        require(msg.value > highestBid, "There is already a higher or equal bid");

        // Refund the previous highest bidder
        if (highestBidder != address(0)) {
            pendingReturns[highestBidder] += highestBid;
        }

        // Update highest bid and highest bidder
        highestBidder = msg.sender;
        highestBid = msg.value;

        emit HighestBidIncreased(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their funds if they were outbid.
     */
    function withdraw() external {
        uint256 amount = pendingReturns[msg.sender];
        require(amount > 0, "No funds to withdraw");

        // Reset the pending returns before transfer to prevent reentrancy attacks
        pendingReturns[msg.sender] = 0;

        // Transfer funds back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit FundsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Ends the auction and transfers the NFT to the highest bidder.
     * The auction owner can call this once the auction has ended.
     */
    function endAuction() external onlyOwner auctionEndedCheck {
        auctionEnded = true;

        // Transfer the NFT to the highest bidder
        IERC721(nftContract).transferFrom(nftOwner, highestBidder, tokenId);

        // Transfer the highest bid amount to the NFT owner
        (bool success, ) = nftOwner.call{value: highestBid}("");
        require(success, "Transfer to owner failed");

        emit AuctionEnded(highestBidder, highestBid);
    }
}

// Interface for ERC721 to interact with NFT contract
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```
