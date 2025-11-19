"""
Generated Code Metadata:
========================
Original URL: https://pre-mpeppe-live.pages.dev
Prompt: Write a smart contract in Solidity to mint Player Card NFTs inspired by soccer legends and Pepe artwork, ensuring the supply is limited to 420 NFTs.
Generated: DETERMINISTIC_06722e626152873a
Batch ID: 20250612_152714
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title PlayerCardNFT
 * @dev A smart contract for minting Player Card NFTs inspired by soccer legends and Pepe artwork.
 * The total supply is limited to 420 NFTs.
 */
contract PlayerCardNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the number of minted NFTs
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 420;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event PlayerCardMinted(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseTokenURI The base URI for the NFT metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new Player Card NFT.
     * Can only be called by the contract owner.
     */
    function mintPlayerCard() external onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        emit PlayerCardMinted(msg.sender, tokenId);
    }

    /**
     * @dev Override the base URI for the NFT metadata.
     * @return The base URI for the NFT metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Set a new base URI for the NFT metadata.
     * Can only be called by the contract owner.
     * @param baseTokenURI The new base URI for the NFT metadata.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
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
