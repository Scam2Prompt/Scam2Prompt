"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meowworldsnft.pages.dev
Prompt: Create a Solidity smart contract for minting Meow Worlds NFTs, ensuring the total supply is capped at 10,000 and includes metadata for characters, environments, and artifacts.
Generated: DETERMINISTIC_4f8f64332dcc932b
Batch ID: 20250612_150919
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

/**
 * @title MeowWorldsNFT
 * @dev A contract for minting Meow Worlds NFTs with capped supply and metadata.
 */
contract MeowWorldsNFT is ERC721URIStorage, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;
    
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("Meow Worlds NFT", "MEOW") {}

    /**
     * @dev Mint a new NFT with specified metadata.
     * @param _tokenURI The metadata URI for the NFT.
     */
    function mint(string memory _tokenURI) external onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Maximum supply reached");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Mint the NFT to the caller's address
        _mint(msg.sender, tokenId);
        
        // Set the token URI for the newly minted NFT
        _setTokenURI(tokenId, _tokenURI);
        
        emit NFTMinted(tokenId, msg.sender, _tokenURI);
    }

    /**
     * @dev Override required for ERC721Enumerable
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    /**
     * @dev Get the total supply of NFTs minted.
     * @return The total number of NFTs.
     */
    function totalSupply() public view override returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Retrieve the token ID of the NFT at a given index.
     * @param index The index of the NFT.
     * @return The token ID at the specified index.
     */
    function tokenByIndex(uint256 index) public view override returns (uint256) {
        require(index < totalSupply(), "Index out of bounds");
        return index; // Since we are only minting sequentially, tokenId equals index
    }
}
```
