"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neftyartstudio.com
Prompt: Provide an example of a smart contract in Solidity for minting NFTs, ensuring compatibility with the Neftyartstudio marketplace's auction system.
Generated: DETERMINISTIC_51b4a2dba6df3240
Batch ID: 20250612_151610
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Example of a smart contract for minting NFTs compatible with NeftyArtStudio auction system
contract NeftyArtNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for unique token IDs
    Counters.Counter private _tokenIdCounter;
    
    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to set the name and symbol of the NFT
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT(string memory tokenURI) external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Mint the NFT
        _mint(msg.sender, tokenId);
        
        // Set the token URI
        _setTokenURI(tokenId, tokenURI);
        
        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId, tokenURI);
    }

    // Function to set the base URI for the NFTs
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to get the base URI
    function baseURI() external view returns (string memory) {
        return _baseTokenURI;
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        // Logic to set the token URI (could use a mapping)
        // For demonstration purposes, this is left as an example
    }

    // Override function to return the base URI for token metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to withdraw any ETH from the contract (for owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
