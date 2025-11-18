"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://veipeicoin.pages.dev
Prompt: Develop a solution for minting and transferring NFTs while addressing migration issues, as outlined on the Decentralized Dapps webpage.
Generated: DETERMINISTIC_997fa048cd3629c9
Batch ID: 20250612_145923
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTCollection is ERC721, ERC721Burnable, ERC721Pausable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;
    
    // Mapping from token ID to a boolean indicating whether it has been migrated
    mapping(uint256 => bool) private _migratedTokens;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed to, uint256 tokenId);

    // Event emitted when an NFT is transferred
    event NFTTransferred(address indexed from, address indexed to, uint256 tokenId);

    // Constructor to initialize the NFT collection with a name and symbol
    constructor() ERC721("MyNFTCollection", "MNFT") {}

    // Function to mint an NFT
    function mintNFT(address to) external onlyOwner {
        require(to != address(0), "Invalid address");
        
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _tokenIdCounter.increment();

        emit NFTMinted(to, tokenId);
    }

    // Function to transfer an NFT with checks for migration issues
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(ownerOf(tokenId) == from, "Not the owner of the token");
        require(!_migratedTokens[tokenId], "Token has been migrated");

        _transfer(from, to, tokenId);
        emit NFTTransferred(from, to, tokenId);
    }

    // Function to migrate an NFT, marking it as migrated
    function migrateNFT(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner of the token");
        require(!_migratedTokens[tokenId], "Token is already migrated");

        _migratedTokens[tokenId] = true;
    }

    // Function to check if a token is migrated
    function isTokenMigrated(uint256 tokenId) external view returns (bool) {
        return _migratedTokens[tokenId];
    }

    // Function to pause all token transfers
    function pause() external onlyOwner {
        _pause();
    }

    // Function to unpause all token transfers
    function unpause() external onlyOwner {
        _unpause();
    }

    // Override the _beforeTokenTransfer function to enforce pause functionality
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721, ERC721Pausable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```

This code provides a simple NFT minting and transferring solution while addressing migration issues. It utilizes the OpenZeppelin library for safe and efficient contract development.
