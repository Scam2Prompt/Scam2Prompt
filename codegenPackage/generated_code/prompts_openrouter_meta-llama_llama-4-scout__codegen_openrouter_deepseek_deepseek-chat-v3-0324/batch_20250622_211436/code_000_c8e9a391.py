"""
Generated Code Metadata:
========================
Original URL: https://moxie.credit
Prompt: Write a smart contract in Solidity that implements a fan token auction using Moxie Batch Auctions on Farcaster.
Generated: DETERMINISTIC_c8e9a391233082d5
Batch ID: 20250622_211436
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title FanTokenAuction
 * @dev Implements a fan token auction using Moxie Batch Auction mechanism on Farcaster
 */
contract FanTokenAuction is Ownable, ReentrancyGuard {
    // Token being auctioned
    IERC20 public fanToken;
    
    // Auction parameters
    uint256 public auctionStartTime;
    uint256 public auctionEndTime;
    uint256 public minPrice;
    uint256 public totalTokensForSale;
    uint256 public totalBids;
    
    // Auction state
    bool public auctionFinalized;
    mapping(address => uint256) public bids;
    address[] public bidders;
    
    event BidPlaced(address indexed bidder, uint256 amount);
    event AuctionFinalized(uint256 clearingPrice, uint256 totalSold);
    event TokensClaimed(address indexed bidder, uint256 amount);
    
    /**
     * @dev Constructor to initialize the auction
     * @param _fanToken Address of the ERC20 fan token
     * @param _totalTokensForSale Total tokens available for sale
     * @param _minPrice Minimum price per token (in wei)
     * @param _duration Auction duration in seconds
     */
    constructor(
        address _fanToken,
        uint256 _totalTokensForSale,
        uint256 _minPrice,
        uint256 _duration
    ) {
        require(_fanToken != address(0), "Invalid token address");
        require(_totalTokensForSale > 0, "Invalid token amount");
        require(_minPrice > 0, "Invalid min price");
        require(_duration > 0, "Invalid duration");
        
        fanToken = IERC20(_fanToken);
        totalTokensForSale = _totalTokensForSale;
        minPrice = _minPrice;
        auctionStartTime = block.timestamp;
        auctionEndTime = auctionStartTime + _duration;
    }
    
    /**
     * @dev Place a bid in the auction
     */
    function placeBid() external payable nonReentrant {
        require(block.timestamp >= auctionStartTime, "Auction not started");
        require(block.timestamp <= auctionEndTime, "Auction ended");
        require(msg.value >= minPrice, "Bid below minimum price");
        require(!auctionFinalized, "Auction already finalized");
        
        if (bids[msg.sender] == 0) {
            bidders.push(msg.sender);
        }
        
        bids[msg.sender] += msg.value;
        totalBids += msg.value;
        
        emit BidPlaced(msg.sender, msg.value);
    }
    
    /**
     * @dev Finalize the auction and calculate clearing price
     */
    function finalizeAuction() external onlyOwner nonReentrant {
        require(block.timestamp > auctionEndTime, "Auction not ended");
        require(!auctionFinalized, "Already finalized");
        
        auctionFinalized = true;
        
        if (totalBids == 0) {
            emit AuctionFinalized(0, 0);
            return;
        }
        
        // Calculate clearing price (simplified Moxie batch auction)
        uint256 clearingPrice = totalBids / totalTokensForSale;
        emit AuctionFinalized(clearingPrice, totalTokensForSale);
    }
    
    /**
     * @dev Allow bidders to claim their tokens after auction
     */
    function claimTokens() external nonReentrant {
        require(auctionFinalized, "Auction not finalized");
        require(bids[msg.sender] > 0, "No bid to claim");
        
        uint256 clearingPrice = totalBids / totalTokensForSale;
        uint256 tokensToClaim = bids[msg.sender] / clearingPrice;
        
        // Transfer tokens to bidder
        fanToken.transfer(msg.sender, tokensToClaim);
        
        // Reset bid amount
        bids[msg.sender] = 0;
        
        emit TokensClaimed(msg.sender, tokensToClaim);
    }
    
    /**
     * @dev Withdraw funds after auction ends
     */
    function withdrawFunds() external onlyOwner nonReentrant {
        require(auctionFinalized, "Auction not finalized");
        payable(owner()).transfer(address(this).balance);
    }
    
    /**
     * @dev Emergency withdraw tokens if needed
     */
    function emergencyWithdrawTokens() external onlyOwner {
        require(!auctionFinalized, "Auction already finalized");
        fanToken.transfer(owner(), fanToken.balanceOf(address(this)));
    }
}
```
