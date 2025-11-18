"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledqinlv.com
Prompt: Create a Solidity smart contract template for minting NFTs that can be listed and sold on OpenSea, including metadata customization.
Generated: DETERMINISTIC_ec4767f215630b3f
Batch ID: 20250612_150440
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

// Import OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Define the NFT contract
contract MyNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    // Constructor to set the name and symbol of the NFT
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to set the base URI for metadata
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    // Function to retrieve the base URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(msg.sender, tokenId);
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to mint a new NFT to a specific address
    function mintNFTTo(address to) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(to, tokenId);
        emit NFTMinted(to, tokenId);
    }
    
    // Override the tokenURI function to return the token's metadata URI
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        
        return string(abi.encodePacked(_baseURI(), Strings.toString(tokenId), ".json"));
    }
}
```
