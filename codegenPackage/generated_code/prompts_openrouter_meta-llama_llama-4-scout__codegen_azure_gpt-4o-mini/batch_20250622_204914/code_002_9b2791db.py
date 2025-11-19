"""
Generated Code Metadata:
========================
Original URL: https://poly-market.now.sh
Prompt: Generate a simple smart contract using Solidity to create and manage NFTs on the Polygon network, similar to PolyMarket 1.0.
Generated: DETERMINISTIC_9b2791dbf6bfc40a
Batch ID: 20250622_204914
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

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for managing NFTs
contract SimpleNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

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
        
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to set the base URI for the NFT metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override the _baseURI function to return the base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to retrieve the current token ID counter
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to withdraw any Ether from the contract (if applicable)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
