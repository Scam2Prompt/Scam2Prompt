"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://primeart.org
Prompt: Recommend a method to programmatically mint NFTs on Prime Art using blockchain integration, and provide an example implementation in Solidity.
Generated: DETERMINISTIC_55424f1f4911b865
Batch ID: 20250612_153821
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title PrimeArtNFT
 * @dev This contract allows for minting of NFTs for Prime Art.
 */
contract PrimeArtNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor setting the name and symbol for the NFT collection.
     */
    constructor() ERC721("PrimeArtNFT", "PANFT") {}

    /**
     * @dev Function to mint a new NFT.
     * @param to Address that will own the minted NFT.
     * @param tokenURI Metadata URI for the minted NFT.
     */
    function mintNFT(address to, string memory tokenURI) public onlyOwner {
        require(to != address(0), "Invalid address: zero address");
        require(bytes(tokenURI).length > 0, "Invalid token URI: empty URI");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _tokenIdCounter.increment();

        emit NFTMinted(to, tokenId, tokenURI);
    }

    /**
     * @dev Internal function to set the token URI.
     * @param tokenId The ID of the NFT.
     * @param tokenURI The metadata URI to assign to the NFT.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Function to retrieve the token URI for a given token ID.
     * @param tokenId The ID of the NFT.
     * @return string The metadata URI of the NFT.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }
}
```
