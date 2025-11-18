"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pik-dapp.hk.bigfly.xyz
Prompt: Create a smart contract for NFT令牌 (NFT tokens) that aligns with the 元宇宙 (metaverse) use cases described on the 极峯(PIK) platform.
Generated: DETERMINISTIC_f92c666f48f52711
Batch ID: 20250612_145510
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

// @title: PIKMetaverseNFT
// @description: Smart contract for NFT tokens compatible with the PIK platform for metaverse use cases.

contract PIKMetaverseNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Track the current token ID
    Counters.Counter private _tokenIdCounter;
    
    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to a description of the NFT
    mapping(uint256 => string) private _tokenDescriptions;

    event TokenMinted(address indexed owner, uint256 tokenId, string description);

    // Constructor to set the name and symbol of the NFT
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    // @notice Mint a new NFT token
    // @param description A description of the NFT being minted
    // @return uint256 The new token ID
    function mint(string memory description) external onlyOwner returns (uint256) {
        require(bytes(description).length > 0, "Description cannot be empty");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _safeMint(msg.sender, tokenId);
        _tokenDescriptions[tokenId] = description;

        emit TokenMinted(msg.sender, tokenId, description);

        return tokenId;
    }

    // @notice Get metadata URI for a token
    // @param tokenId The ID of the token to query
    // @return string The token's metadata URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString()));
    }

    // @notice Get the description of a token
    // @param tokenId The ID of the token to query
    // @return string The description of the token
    function getTokenDescription(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenDescriptions[tokenId];
    }

    // @notice Update the base URI for metadata
    // @param baseURI The new base URI
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    // @notice Override supportsInterface to include ERC721 interface
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, IERC165) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
