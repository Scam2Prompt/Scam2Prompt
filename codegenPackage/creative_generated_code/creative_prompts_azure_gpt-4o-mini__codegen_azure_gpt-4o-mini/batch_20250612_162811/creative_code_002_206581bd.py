"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mega-rabbit.com
Prompt: Create a Solidity smart contract that allows users to mint NFTs from the MegaRabbit collection, ensuring it adheres to the specified limits per wallet.
Generated: DETERMINISTIC_206581bd643aec1c
Batch ID: 20250612_162811
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
import "@openzeppelin/contracts/utils/Counters.sol";

// MegaRabbit NFT contract
contract MegaRabbit is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Constants
    uint256 public constant MAX_SUPPLY = 10000; // Maximum supply of NFTs
    uint256 public constant MAX_PER_WALLET = 5; // Maximum NFTs per wallet

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    mapping(address => uint256) private _mintedCount; // Mapping of wallets to their minted NFT count

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("MegaRabbit", "MRBT") {}

    // Function to mint new NFTs
    function mint() external {
        // Check if minting exceeds max supply
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        
        // Check if wallet has exceeded mint limit
        require(_mintedCount[msg.sender] < MAX_PER_WALLET, "Mint limit reached for this wallet");

        // Increment the token ID counter and get the new token ID
        uint256 newTokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _safeMint(msg.sender, newTokenId);

        // Update the minted count for the wallet
        _mintedCount[msg.sender]++;

        // Emit event for minted NFT
        emit NFTMinted(msg.sender, newTokenId);
    }

    // Function to get the mint count for a specific wallet
    function getMintedCount(address wallet) external view returns (uint256) {
        return _mintedCount[wallet];
    }

    // Function to withdraw the contract's balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to prevent direct ETH transfers to the contract
    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }
}
```
