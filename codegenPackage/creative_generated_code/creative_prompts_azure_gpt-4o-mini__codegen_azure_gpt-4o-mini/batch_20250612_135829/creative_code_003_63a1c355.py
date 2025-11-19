"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Create a guide for integrating a Dutch Auction smart contract for the Ember NFT public sale, starting at 0.3 ETH.
Generated: DETERMINISTIC_63a1c355188163aa
Batch ID: 20250612_135829
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract EmberNFT is ERC721Enumerable, Ownable {
    using SafeMath for uint256;

    // Auction parameters
    uint256 public constant START_PRICE = 0.3 ether; // Starting price of the auction
    uint256 public constant DECREMENT_SIZE = 0.01 ether; // Amount to decrease each interval
    uint256 public constant DECREMENT_INTERVAL = 5 minutes; // Time interval for price decrement
    uint256 public endTime; // End time of the auction
    uint256 public totalSupply; // Total NFTs to be sold

    // Mapping to track if an NFT has been sold
    mapping(uint256 => bool) public soldNFTs;
    
    // Event emitted when an NFT is sold
    event NFTSold(address indexed buyer, uint256 indexed tokenId, uint256 price);

    // Constructor to initialize the contract
    constructor(uint256 _totalSupply) ERC721("EmberNFT", "EMB") {
        totalSupply = _totalSupply;
        endTime = block.timestamp + (DECREMENT_INTERVAL * (START_PRICE / DECREMENT_SIZE));
    }

    // Function to calculate current auction price
    function currentPrice() public view returns (uint256) {
        if (block.timestamp >= endTime) {
            return 0; // If auction ended, price is 0
        }
        uint256 elapsedIntervals = (block.timestamp - (endTime - (DECREMENT_INTERVAL * (START_PRICE / DECREMENT_SIZE)))).div(DECREMENT_INTERVAL);
        uint256 price = START_PRICE.sub(elapsedIntervals.mul(DECREMENT_SIZE));
        return price > 0 ? price : 0; // Ensure price doesn't go negative
    }

    // Function to buy an NFT during the auction
    function buyNFT(uint256 tokenId) external payable {
        require(tokenId < totalSupply, "Invalid token ID");
        require(!soldNFTs[tokenId], "NFT already sold");
        uint256 price = currentPrice();
        require(msg.value >= price, "Insufficient funds sent");

        // Mark the NFT as sold
        soldNFTs[tokenId] = true;

        // Mint the NFT to the buyer
        _mint(msg.sender, tokenId);

        // Emit sold event
        emit NFTSold(msg.sender, tokenId, price);

        // Refund any excess amount sent
        if (msg.value > price) {
            payable(msg.sender).transfer(msg.value.sub(price));
        }
    }

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
