"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Write a smart contract in Solidity for minting NFTs similar to the "Cats World" collection, ensuring features like tier-based pricing and free initial mints are included.
Generated: DETERMINISTIC_d10ac8b32eea1090
Batch ID: 20250612_150040
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CatsWorld is ERC721Enumerable, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter for minting NFTs
    Counters.Counter private _tokenIdCounter;
    
    // Mapping to store tier prices
    mapping(uint256 => uint256) public tierPrices;
    
    // Variable to control free minting
    uint256 public freeMintsAvailable;

    // Event to log minting of new NFTs
    event Minted(address indexed owner, uint256 tokenId, string tokenURI);
    
    // Constructor to initialize the contract
    constructor(uint256 _freeMintsAvailable) ERC721("Cats World", "CAT") {
        freeMintsAvailable = _freeMintsAvailable;

        // Setting tier prices (1: Basic, 2: Premium, 3: Exclusive)
        tierPrices[1] = 0.01 ether; // Basic tier
        tierPrices[2] = 0.05 ether; // Premium tier
        tierPrices[3] = 0.1 ether;  // Exclusive tier
    }

    // Mint function to create a new NFT
    function mintNFT(string memory tokenURI, uint256 tier) external payable {
        require(tier >= 1 && tier <= 3, "Invalid tier");
        uint256 price = tierPrices[tier];

        if (freeMintsAvailable > 0) {
            // Allow free minting for the initial mints
            freeMintsAvailable--;
        } else {
            require(msg.value >= price, "Insufficient funds");
        }

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit Minted(msg.sender, tokenId, tokenURI);
    }

    // Function to withdraw ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        payable(owner()).transfer(balance);
    }

    // Function to set tier prices (onlyOwner)
    function setTierPrice(uint256 tier, uint256 price) external onlyOwner {
        require(tier >= 1 && tier <= 3, "Invalid tier");
        tierPrices[tier] = price;
    }

    // Function to get the current price for a specific tier
    function getTierPrice(uint256 tier) external view returns (uint256) {
        require(tier >= 1 && tier <= 3, "Invalid tier");
        return tierPrices[tier];
    }
}
```
