"""
Generated Code Metadata:
========================
Original URL: https://embersft.costhentic.com
Prompt: Develop a Dutch Auction smart contract in Solidity that decreases the price of an Ember NFT from 0.3 ETH to 0.15 ETH during the Public Sale.
Generated: DETERMINISTIC_91a315cf588c75c1
Batch ID: 20250622_205348
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

contract EmberNFTDutchAuction is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant START_PRICE = 0.3 ether;
    uint256 public constant END_PRICE = 0.15 ether;
    uint256 public constant DURATION = 1 days;
    uint256 public constant PRICE_DECREMENT = (START_PRICE - END_PRICE) / (DURATION / 1 hours);
    
    uint256 public auctionStartTime;
    bool public publicSaleActive;

    constructor() ERC721("EmberNFT", "EMBER") {}

    function startPublicSale() external onlyOwner {
        require(!publicSaleActive, "Public sale already active");
        auctionStartTime = block.timestamp;
        publicSaleActive = true;
    }

    function stopPublicSale() external onlyOwner {
        require(publicSaleActive, "Public sale not active");
        publicSaleActive = false;
    }

    function getCurrentPrice() public view returns (uint256) {
        require(publicSaleActive, "Public sale not active");
        uint256 elapsedTime = block.timestamp - auctionStartTime;
        
        if (elapsedTime >= DURATION) {
            return END_PRICE;
        }
        
        uint256 hoursElapsed = elapsedTime / 1 hours;
        uint256 priceDecrement = PRICE_DECREMENT * hoursElapsed;
        
        if (START_PRICE - priceDecrement < END_PRICE) {
            return END_PRICE;
        }
        
        return START_PRICE - priceDecrement;
    }

    function mintNFT() external payable {
        require(publicSaleActive, "Public sale not active");
        uint256 currentPrice = getCurrentPrice();
        require(msg.value >= currentPrice, "Insufficient ETH sent");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
        
        if (msg.value > currentPrice) {
            payable(msg.sender).transfer(msg.value - currentPrice);
        }
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
