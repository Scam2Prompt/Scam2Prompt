"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Write a smart contract in Solidity that integrates a minting platform for NFTs, similar to the MintStone and Relic minting system described on Clone Force™.
Generated: DETERMINISTIC_28bba52bdab6d5b6
Batch ID: 20250612_154441
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/metadata/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing required OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMintingContract is an ERC721 token contract that allows minting of NFTs
contract NFTMintingContract is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new token is minted
    event TokenMinted(uint256 indexed tokenId, address indexed owner);

    // Counter to keep track of the number of minted tokens
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Constructor that initializes the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        _baseTokenURI = "https://api.example.com/metadata/"; // Base URI for metadata
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get current token ID
        _tokenIdCounter.increment(); // Increment the counter for the next token

        // Mint the token to the caller
        _mint(msg.sender, tokenId);
        
        emit TokenMinted(tokenId, msg.sender); // Emit event for the new token
    }

    // Function to set the base URI for metadata
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    // Override the _baseURI function to return the base token URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to retrieve the current token ID (for testing purposes)
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to withdraw any Ether held by the contract (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to receive Ether 
    receive() external payable {}
}
```
