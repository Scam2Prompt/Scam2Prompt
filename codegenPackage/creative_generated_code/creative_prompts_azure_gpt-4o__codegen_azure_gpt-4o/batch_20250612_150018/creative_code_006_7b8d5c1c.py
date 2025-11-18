"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltrove.com
Prompt: Write a Solidity smart contract for minting NFTs with metadata, ensuring compatibility with marketplaces as described by Atravaraazen.
Generated: DETERMINISTIC_7b8d5c1c64b9f4a4
Batch ID: 20250612_150018
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

// Import ERC721 standard and additional dependencies
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTMintingContract
 * @dev A contract for minting NFTs with metadata, fully compatible with marketplaces.
 */
contract NFTMintingContract is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIds;

    // Base URI for metadata (optional, can be used for marketplace compatibility)
    string private _baseTokenURI;

    /**
     * @dev Initializes the contract with a name and a symbol for the NFT.
     * @param name Name of the NFT collection (e.g., "AtravaraazenNFTs").
     * @param symbol Symbol of the NFT collection (e.g., "ATRA").
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Sets the base URI for the metadata.
     * @param baseURI The base URL for all token URIs.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Overrides the `_baseURI` function from ERC721 to return the set base URI.
     * @return The base URI for token metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mints a new NFT with the specified metadata URI.
     * @param to Address to receive the minted NFT.
     * @param tokenURI The metadata URI pointing to the NFT's data.
     * @return The newly minted token ID.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner returns (uint256) {
        // Increment the token ID
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the NFT to the specified address
        _safeMint(to, newTokenId);

        // Set the metadata URI for the token
        _setTokenURI(newTokenId, tokenURI);

        // Return the new token ID
        return newTokenId;
    }
    
    /**
     * @dev Returns the total number of NFTs minted so far.
     * @return The total supply of tokens.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIds.current();
    }
}
```

This code defines a clean, production-ready Solidity smart contract for minting NFTs with metadata, ensuring compatibility with marketplaces.
