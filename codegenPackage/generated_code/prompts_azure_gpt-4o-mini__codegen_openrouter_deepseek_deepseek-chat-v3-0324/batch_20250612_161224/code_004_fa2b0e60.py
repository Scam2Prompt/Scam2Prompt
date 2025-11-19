"""
Generated Code Metadata:
========================
Original URL: https://topgtest.vercel.app
Prompt: Outline a smart contract in Solidity for managing the distribution of 50 ETH NFTs in a fair manner.
Generated: DETERMINISTIC_fa2b0e603910e874
Batch ID: 20250612_161224
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FairNFTAuction is ERC721, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 50;
    uint256 public constant AUCTION_DURATION = 7 days;
    uint256 public constant MIN_BID_INCREMENT = 0.01 ether;

    uint256 public auctionEndTime;
    bool public auctionEnded;
    address public highestBidder;
    uint256 public highestBid;

    mapping(address => uint256) public pendingReturns;
    mapping(uint256 => string) private _tokenURIs;

    event NewHighestBid(address bidder, uint256 amount);
    event AuctionEnded(address winner, uint256 amount);
    event NFTClaimed(address owner, uint256 tokenId);

    constructor() ERC721("FairNFT", "FNFT") {
        auctionEndTime = block.timestamp + AUCTION_DURATION;
    }

    function bid() external payable {
        require(block.timestamp < auctionEndTime, "Auction has ended");
        require(msg.value > highestBid.add(MIN_BID_INCREMENT), "Bid too low");

        if (highestBid != 0) {
            pendingReturns[highestBidder] += highestBid;
        }

        highestBidder = msg.sender;
        highestBid = msg.value;

        emit NewHighestBid(msg.sender, msg.value);
    }

    function withdraw() external {
        uint256 amount = pendingReturns[msg.sender];
        require(amount > 0, "No funds to withdraw");

        pendingReturns[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    function endAuction() external onlyOwner {
        require(block.timestamp >= auctionEndTime, "Auction not ended");
        require(!auctionEnded, "Auction already ended");

        auctionEnded = true;
        emit AuctionEnded(highestBidder, highestBid);
    }

    function claimNFT(string memory tokenURI) external {
        require(auctionEnded, "Auction not ended");
        require(highestBidder == msg.sender, "Not the winner");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        _tokenURIs[tokenId] = tokenURI;

        emit NFTClaimed(msg.sender, tokenId);
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    function withdrawFunds() external onlyOwner {
        require(auctionEnded, "Auction not ended");
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }
}
```
