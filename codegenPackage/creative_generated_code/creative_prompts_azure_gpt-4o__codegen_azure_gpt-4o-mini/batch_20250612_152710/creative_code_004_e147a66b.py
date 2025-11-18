"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qhozali.pages.dev
Prompt: Create a smart contract for minting NFTs that align with the Ghozali 404 hybrid concept on the Base blockchain.
Generated: DETERMINISTIC_e147a66bad056681
Batch ID: 20250612_152710
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

// Import OpenZeppelin's ERC721 and Ownable contracts to leverage existing standards and functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Ghozali404NFT is a smart contract for minting NFTs based on the Ghozali 404 hybrid concept
contract Ghozali404NFT is ERC721, Ownable {
    using Counters for Counters.Counter; // Using counters for unique token IDs
    Counters.Counter private _tokenIdCounter; // Counter for tracking the next token ID

    // Base URI for the NFT metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event Minted(uint256 tokenId, address owner);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI; // Set the base URI for metadata
    }

    // Function to mint a new NFT
    function mintNFT(address to) external onlyOwner {
        require(to != address(0), "Invalid address"); // Ensure that the target address is valid
        
        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId); // Mint the NFT safely
        emit Minted(tokenId, to); // Emit the Minted event
    }

    // Function to set a new base URI (only owner can change it)
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI; // Update the base URI
    }

    // Override the _baseURI function to return the base URI for the NFT metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI; // Return the base URI
    }

    // Function to get the total supply of minted NFTs
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current(); // Return the current token ID count
    }
}
```
