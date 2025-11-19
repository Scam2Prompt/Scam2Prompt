"""
Generated Code Metadata:
========================
Original URL: https://trumpmeme.net
Prompt: Provide a code example in Solidity for creating an NFT contract that could be used for the exclusive TRUMP MEME NFTs mentioned in the roadmap.
Generated: DETERMINISTIC_7f8c040bcd84a4fa
Batch ID: 20250612_153710
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

// Importing the ERC721 interface and the Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for the TRUMP MEME NFT
contract TrumpMemeNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
        
        emit Minted(tokenId, msg.sender);
    }

    // Function to set a new base URI for the metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override the _baseURI function to return the base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to get the current token ID counter (for testing purposes)
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
