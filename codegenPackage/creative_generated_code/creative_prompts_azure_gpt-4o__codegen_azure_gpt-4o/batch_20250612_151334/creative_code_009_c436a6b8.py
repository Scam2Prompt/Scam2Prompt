"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magic-eden.io
Prompt: Write a smart contract example for minting NFTs that can be directly listed on Magic Eden's marketplace.
Generated: DETERMINISTIC_c436a6b85b6fd667
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title NFTCollection
 * @dev An ERC721-based NFT smart contract that allows minting of unique tokens
 * and integrates with Magic Eden's marketplace.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTCollection is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the next token ID
    Counters.Counter private _tokenIds;

    // Base URI for metadata (Magic Eden requires proper metadata standards)
    string private _baseTokenURI;

    // Event emitted when a token is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    /**
     * @dev Contract constructor sets the name and symbol of the NFT collection
     * and initializes the base URI for metadata.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseURI Initial base URI for metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Internal override to return the base URI for metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Allows the contract owner to update the base URI for metadata.
     * @param baseURI New base URI string.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Allows the contract owner to mint a new NFT.
     * @param recipient Address of the recipient.
     * @return The newly minted token ID.
     */
    function mintNFT(address recipient) external onlyOwner returns (uint256) {
        require(recipient != address(0), "Recipient address cannot be zero.");

        // Increment token ID counter and mint the token
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        _mint(recipient, newTokenId);

        emit NFTMinted(recipient, newTokenId); // Emit event for tracking

        return newTokenId;
    }

    /**
     * @dev Returns the total number of tokens minted so far.
     * @return Total count of minted tokens.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIds.current();
    }
}
```
