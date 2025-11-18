"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Write Solidity code for setting up Moxie Batch Auctions to enable fair price discovery for Fan Tokens on Farcaster.
Generated: DETERMINISTIC_67f20de656bd9eab
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title MoxieBatchAuction
 * @dev Smart contract for conducting batch auctions for fair price discovery of Fan Tokens.
 */
contract MoxieBatchAuction {
    // State variables
    address public auctionOwner; // Owner of the auction
    uint256 public auctionEndTime; // End time of the auction
    uint256 public tokenSupply; // Total supply of tokens being auctioned
    uint256 public minimumBid; // Minimum bid required to participate
    mapping(address => uint256) public bids; // Mapping of bidder addresses to their bid amounts
    address[] public participants; // Array of participants in the auction
    bool public auctionFinalized; // Tracks whether the auction has been finalized
    uint256 public clearingPrice; // Final price per token after auction ends

    // Events
    event BidPlaced(address indexed bidder, uint256 amount);
    event AuctionFinalized(uint256 clearingPrice);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == auctionOwner, "Only the auction owner can call this function");
        _;
    }

    modifier auctionActive() {
        require(block.timestamp < auctionEndTime, "Auction has ended");
        _;
    }

    modifier auctionEnded() {
        require(block.timestamp >= auctionEndTime, "Auction is still active");
        _;
    }

    constructor(uint256 _auctionDuration, uint256 _tokenSupply, uint256 _minimumBid) {
        require(_auctionDuration > 0, "Auction duration must be greater than zero");
        require(_tokenSupply > 0, "Token supply must be greater than zero");
        require(_minimumBid > 0, "Minimum bid must be greater than zero");

        auctionOwner = msg.sender;
        auctionEndTime = block.timestamp + _auctionDuration; // Auction end time
        tokenSupply = _tokenSupply; // Total token supply
        minimumBid = _minimumBid; // Minimum bid required
    }

    /**
     * @dev Allow participants to place a bid.
     * @param _amount The amount of the bid.
     */
    function placeBid(uint256 _amount) external auctionActive {
        require(_amount >= minimumBid, "Bid amount is below the minimum required");
        require(_amount > bids[msg.sender], "New bid must be higher than previous bid");

        // Track the bid
        bids[msg.sender] = _amount;

        // Add the participant if they are placing a bid for the first time
        if (_amount == minimumBid || bids[msg.sender] == 0) {
            participants.push(msg.sender);
        }

        emit BidPlaced(msg.sender, _amount);
    }

    /**
     * @dev Finalize the auction and calculate the clearing price.
     * This function can only be called by the auction owner after the auction has ended.
     */
    function finalizeAuction() external auctionEnded onlyOwner {
        require(!auctionFinalized, "Auction has already been finalized");

        // Sort participants by bid amount (descending order)
        sortParticipantsByBidDescending();

        // Calculate clearing price
        uint256 accumulatedBids = 0;
        uint256 tokensDistributed = 0;

        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            uint256 participantBid = bids[participant];

            // If accumulated bids exceed token supply, stop
            if (tokensDistributed + participantBid > tokenSupply) {
                clearingPrice = participantBid;
                break;
            }

            accumulatedBids += participantBid;
            tokensDistributed += 1;
        }

        auctionFinalized = true;
        emit AuctionFinalized(clearingPrice);
    }

    /**
     * @dev Helper function to sort participants by their bid amounts in descending order.
     * Uses bubble sort for simplicity (not optimized for large datasets).
     */
    function sortParticipantsByBidDescending() internal {
        for (uint256 i = 0; i < participants.length; i++) {
            for (uint256 j = i + 1; j < participants.length; j++) {
                if (bids[participants[j]] > bids[participants[i]]) {
                    // Swap
                    address temp = participants[i];
                    participants[i] = participants[j];
                    participants[j] = temp;
                }
            }
        }
    }

    /**
     * @dev Retrieve the number of participants in the auction.
     */
    function getParticipantCount() external view returns (uint256) {
        return participants.length;
    }

    /**
     * @dev Get the bid amount for a specific participant.
     * @param _participant The address of the participant.
     */
    function getBidAmount(address _participant) external view returns (uint256) {
        return bids[_participant];
    }
}
```
