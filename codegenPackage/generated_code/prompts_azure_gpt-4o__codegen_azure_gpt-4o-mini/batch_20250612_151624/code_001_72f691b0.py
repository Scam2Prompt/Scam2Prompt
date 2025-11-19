"""
Generated Code Metadata:
========================
Original URL: https://test.fulviomenegozzo.com
Prompt: Create a smart contract in Solidity that limits NFT purchases to a maximum of 5 per wallet and includes functionality for setting a total price in ETH, based on the features of the Memeland pre-sale.
Generated: DETERMINISTIC_72f691b0efb09ad1
Batch ID: 20250612_151624
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MemelandNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    uint256 public maxPurchaseLimit = 5; // Maximum NFTs per wallet
    uint256 public totalPrice; // Total price for each NFT in wei
    mapping(address => uint256) public walletPurchases; // Track purchases per wallet

    // Events
    event NFTMinted(address indexed buyer, uint256 tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor(string memory name, string memory symbol, uint256 price) 
        ERC721(name, symbol) 
    {
        totalPrice = price; // Set the total price for each NFT
    }

    // Function to mint NFTs
    function mintNFT(uint256 quantity) external payable {
        require(quantity > 0, "Must mint at least one NFT");
        require(quantity <= maxPurchaseLimit, "Exceeds maximum purchase limit");
        require(walletPurchases[msg.sender] + quantity <= maxPurchaseLimit, "Exceeds maximum NFTs per wallet");
        require(msg.value == totalPrice * quantity, "Incorrect ETH amount sent");

        // Update the number of NFTs purchased by the wallet
        walletPurchases[msg.sender] += quantity;

        // Mint the NFTs
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(msg.sender, tokenId);
            emit NFTMinted(msg.sender, tokenId);
        }
    }

    // Function to withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to set a new price for the NFTs
    function setPrice(uint256 newPrice) external onlyOwner {
        totalPrice = newPrice;
    }

    // Function to get the current price of the NFTs
    function getPrice() external view returns (uint256) {
        return totalPrice;
    }

    // Function to get the number of NFTs purchased by a wallet
    function getPurchases(address wallet) external view returns (uint256) {
        return walletPurchases[wallet];
    }
}
```
