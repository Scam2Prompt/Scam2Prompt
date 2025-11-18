"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topgtest.vercel.app
Prompt: Provide code examples for implementing a fair distribution mechanism for an NFT drop using Solidity, referencing the Masked Soldiers ETH NFT February supply of 50.
Generated: DETERMINISTIC_703ed3d532243dd1
Batch ID: 20250612_152511
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
import "@openzeppelin/contracts/utils/Strings.sol";

contract FairNFTDrop is ERC721Enumerable, Ownable {
    using Strings for uint256;

    // Total supply of NFTs
    uint256 public constant MAX_SUPPLY = 50;
    
    // Mapping to track if an address has claimed their NFT
    mapping(address => bool) public hasClaimed;

    // Event for NFT minting
    event NFTMinted(address indexed recipient, uint256 tokenId);

    // Constructor to set the NFT collection name and symbol
    constructor() ERC721("Masked Soldiers ETH", "MSET") {}

    // Function to mint NFTs to the sender. Only callable by users.
    function claimNFT() external {
        // Ensure the sender has not claimed an NFT before
        require(!hasClaimed[msg.sender], "You have already claimed your NFT");

        // Ensure the total supply has not been reached
        require(totalSupply() < MAX_SUPPLY, "All NFTs have been claimed");

        // Mint the NFT
        uint256 tokenId = totalSupply(); // New tokenId is the current total supply
        _safeMint(msg.sender, tokenId);

        // Mark the sender as having claimed their NFT
        hasClaimed[msg.sender] = true;

        // Emit an event for the minting
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to check if an address has claimed their NFT
    function hasAddressClaimed(address _address) external view returns (bool) {
        return hasClaimed[_address];
    }

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    // Function to receive Ether. Allows the contract to accept Ether.
    receive() external payable {}
}
```
