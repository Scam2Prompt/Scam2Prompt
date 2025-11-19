"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Create an Ethereum smart contract that enforces CC0 licensing for an NFT collection, as described on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_31eb85cd2c79b806
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CC0NFTCollection
 * @dev This contract implements an NFT collection that enforces CC0 licensing.
 * The CC0 license allows creators to waive all their copyright and related rights,
 * enabling the public to use the work without restrictions.
 */
contract CC0NFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseTokenURI The base URI for the token metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new NFT to the caller's address.
     * Only the owner of the contract can mint new tokens.
     */
    function mint() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
        
        emit TokenMinted(msg.sender, tokenId);
    }

    /**
     * @dev Override the baseURI function to return the base URI for token metadata.
     * @return The base URI for the token metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Set a new base URI for the token metadata.
     * Only the owner of the contract can set a new base URI.
     * @param newBaseURI The new base URI for the token metadata.
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    /**
     * @dev Get the current token ID counter.
     * @return The current token ID counter.
     */
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
