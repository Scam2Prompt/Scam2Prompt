"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abstractdog.testnet.nfts2.me
Prompt: Write a smart contract for minting abstract art-inspired dog meme NFTs on the Abstract Testnet, compatible with NFTs2Me.com.
Generated: DETERMINISTIC_656ea9c671dd39c6
Batch ID: 20250612_155102
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

// AbstractArtDogMemeNFT is a contract for minting dog meme NFTs inspired by abstract art
contract AbstractArtDogMemeNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter; // Using Counters for unique token IDs
    Counters.Counter private _tokenIdCounter; // Counter for tracking the token IDs

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI; // Set the base URI for the NFTs
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        _tokenIdCounter.increment(); // Increment the token ID counter
        _safeMint(msg.sender, tokenId); // Mint the NFT to the owner's address
        emit Minted(msg.sender, tokenId); // Emit the minted event
    }

    // Function to set a new base URI for the NFTs
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    // Override the base URI function to return the base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to retrieve the total supply of minted NFTs
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current(); // Return the total minted NFTs
    }

    // Override the transfer function to include checks (if needed) for NFT transfers
    function transferFrom(address from, address to, uint256 tokenId) 
        public 
        virtual 
        override 
        onlyOwner 
    {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Not owner nor approved");
        _transfer(from, to, tokenId);
    }

    // Function to withdraw any funds from the contract (if applicable)
    function withdraw() external onlyOwner {
        // Add functionality to withdraw funds if the contract accepts payments
        payable(owner()).transfer(address(this).balance);
    }
}
```
