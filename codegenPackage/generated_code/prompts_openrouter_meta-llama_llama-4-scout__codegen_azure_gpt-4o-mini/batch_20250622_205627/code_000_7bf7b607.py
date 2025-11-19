"""
Generated Code Metadata:
========================
Original URL: https://mint-nakamigos.vercel.app
Prompt: Write a smart contract code for a limited sale of NFTs, with a maximum of 1 set per buyer and a total cap of 0.1 ETH, using Ethereum blockchain.
Generated: DETERMINISTIC_7bf7b60715760606
Batch ID: 20250622_205627
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

contract LimitedNFTSale is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    uint256 public constant MAX_SALE_CAP = 0.1 ether; // Maximum sale cap
    uint256 public constant MAX_NFT_PER_BUYER = 1; // Maximum NFTs per buyer
    mapping(address => uint256) public buyerNFTCount; // Track NFTs bought by each address

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed buyer, uint256 tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("LimitedNFT", "LNFT") {}

    // Function to mint a new NFT
    function mintNFT() external payable {
        // Check if the sale cap is reached
        require(msg.value <= MAX_SALE_CAP, "Exceeds maximum sale cap");
        
        // Check if the buyer has already purchased an NFT
        require(buyerNFTCount[msg.sender] < MAX_NFT_PER_BUYER, "Limit of 1 NFT per buyer reached");

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        // Update the buyer's NFT count
        buyerNFTCount[msg.sender]++;

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to withdraw the contract's balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to get the current token ID counter
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
