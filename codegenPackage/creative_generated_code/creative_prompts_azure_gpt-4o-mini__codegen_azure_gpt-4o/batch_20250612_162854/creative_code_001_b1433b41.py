"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Write a smart contract using Moxie that facilitates a Batch Auction for Fan Tokens on the Farcaster network.
Generated: DETERMINISTIC_b1433b4166d77c20
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```moxie
// SPDX-License-Identifier: MIT
contract FanTokenBatchAuction {
    // State Variables
    address public owner;
    uint256 public auctionEndTime;
    uint256 public totalTokens; // Total tokens available for auction
    uint256 public minimumBid; // Minimum bid amount to participate

    mapping(address => uint256) public bids; // Track bids by participant address
    address[] public participants; // List of participants
    bool public auctionFinalized; // Tracks if auction is finalized

    // Events
    event AuctionCreated(uint256 endTime, uint256 totalTokens, uint256 minimumBid);
    event BidPlaced(address indexed bidder, uint256 amount);
    event AuctionFinalized(address[] winners, uint256[] allocations);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier auctionActive() {
        require(block.timestamp < auctionEndTime, "Auction is no longer active");
        require(!auctionFinalized, "Auction has already been finalized");
        _;
    }

    modifier auctionEnded() {
        require(block.timestamp >= auctionEndTime, "Auction is still ongoing");
        require(!auctionFinalized, "Auction has already been finalized");
        _;
    }

    // Constructor
    constructor(uint256 _durationInSeconds, uint256 _totalTokens, uint256 _minimumBid) {
        require(_durationInSeconds > 0, "Auction duration must be positive");
        require(_totalTokens > 0, "Total tokens must be greater than zero");
        require(_minimumBid > 0, "Minimum bid must be greater than zero");

        owner = msg.sender;
        auctionEndTime = block.timestamp + _durationInSeconds;
        totalTokens = _totalTokens;
        minimumBid = _minimumBid;

        emit AuctionCreated(auctionEndTime, totalTokens, minimumBid);
    }

    // Function to place a bid
    function placeBid() external payable auctionActive {
        require(msg.value >= minimumBid, "Bid must be equal to or greater than the minimum bid");

        // Record the bid and the participant
        if (bids[msg.sender] == 0) {
            participants.push(msg.sender);
        }
        bids[msg.sender] += msg.value;

        emit BidPlaced(msg.sender, msg.value);
    }

    // Function to finalize the auction
    function finalizeAuction() external auctionEnded onlyOwner {
        uint256 totalRaised = 0;
        for (uint256 i = 0; i < participants.length; i++) {
            totalRaised += bids[participants[i]];
        }

        require(totalRaised > 0, "No bids placed in the auction");

        // Calculate token allocations based on bids
        address[] memory winners = new address[](participants.length);
        uint256[] memory allocations = new uint256[](participants.length);

        for (uint256 i = 0; i < participants.length; i++) {
            uint256 allocation = (bids[participants[i]] * totalTokens) / totalRaised;
            winners[i] = participants[i];
            allocations[i] = allocation;
        }

        auctionFinalized = true;

        emit AuctionFinalized(winners, allocations);

        // Forward funds to the auction owner
        (bool sent, ) = owner.call{value: address(this).balance}("");
        require(sent, "Failed to transfer funds to owner");
    }

    // Function to get participants
    function getParticipants() external view returns (address[] memory) {
        return participants;
    }

    // Function to withdraw funds in case of emergency (only owner)
    function emergencyWithdraw() external onlyOwner {
        require(!auctionFinalized, "Cannot withdraw after auction is finalized");

        (bool sent, ) = owner.call{value: address(this).balance}("");
        require(sent, "Emergency withdrawal failed");
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
