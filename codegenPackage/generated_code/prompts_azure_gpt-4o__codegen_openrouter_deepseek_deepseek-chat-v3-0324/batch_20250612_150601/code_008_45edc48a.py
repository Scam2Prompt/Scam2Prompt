"""
Generated Code Metadata:
========================
Original URL: https://nft-good.web.app
Prompt: Write code to implement stealth minting functionality for NFTs, as referenced in the Magic Box minting process on the NFT-Good webpage.
Generated: DETERMINISTIC_45edc48ab75b9f6d
Batch ID: 20250612_150601
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract StealthNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping to track stealth minted tokens
    mapping(uint256 => bool) private _stealthMinted;
    
    // Base URI for metadata
    string private _baseTokenURI;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Sets the base URI for metadata
     * @param baseURI The base URI to set
     */
    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Stealth mints a token to a specific address without revealing it immediately
     * @param to The address to mint the token to
     */
    function stealthMint(address to) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId);
        _stealthMinted[tokenId] = true;
    }

    /**
     * @dev Reveals a stealth minted token by updating its metadata
     * @param tokenId The token ID to reveal
     */
    function revealToken(uint256 tokenId) public onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        require(_stealthMinted[tokenId], "Token was not stealth minted");
        
        _stealthMinted[tokenId] = false;
    }

    /**
     * @dev Checks if a token is still in stealth mode
     * @param tokenId The token ID to check
     * @return bool Whether the token is in stealth mode
     */
    function isStealthMinted(uint256 tokenId) public view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _stealthMinted[tokenId];
    }

    /**
     * @dev Overrides tokenURI to return different metadata for stealth tokens
     * @param tokenId The token ID to query
     * @return string The token URI
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");

        if (_stealthMinted[tokenId]) {
            return string(abi.encodePacked(_baseURI(), "stealth.json"));
        }
        
        return string(abi.encodePacked(_baseURI(), Strings.toString(tokenId), ".json"));
    }
}
```
