"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morsenft.org
Prompt: Generate a code snippet for minting and revealing NFTs on the Mitosis platform.
Generated: DETERMINISTIC_527ab665aec64324
Batch ID: 20250612_163646
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for minting and revealing NFTs on the Mitosis platform
contract MitosisNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter; // Using Counters for tokenId management
    Counters.Counter private _tokenIdCounter;

    // Mapping to store the revealed status of tokens
    mapping(uint256 => string) private _tokenURIs;
    mapping(uint256 => bool) private _revealed;

    // Base URI for the token metadata
    string private _baseTokenURI;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);
    // Event emitted when an NFT is revealed
    event NFTRevealed(uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT() public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get current tokenId
        _safeMint(msg.sender, tokenId); // Mint the NFT
        _tokenIdCounter.increment(); // Increment the tokenId counter
        emit NFTMinted(msg.sender, tokenId); // Emit mint event
    }

    // Function to reveal a minted NFT
    function revealNFT(uint256 tokenId, string memory tokenURI) public onlyOwner {
        require(_exists(tokenId), "MitosisNFT: Token does not exist"); // Check if token exists
        require(!_revealed[tokenId], "MitosisNFT: Token already revealed"); // Check if already revealed

        _tokenURIs[tokenId] = tokenURI; // Set the token URI
        _revealed[tokenId] = true; // Mark the token as revealed
        emit NFTRevealed(tokenId, tokenURI); // Emit reveal event
    }

    // Override baseURI function to return the base URI for the NFT metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to retrieve the token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "MitosisNFT: Token does not exist"); // Check if token exists
        if (_revealed[tokenId]) {
            return _tokenURIs[tokenId]; // Return the revealed token URI
        } else {
            return ""; // Return an empty string if not revealed
        }
    }
}
```
