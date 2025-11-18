"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-live.web.app
Prompt: Generate code to create an NFT minting contract inspired by `$MPEPE`'s Player Card NFTs, ensuring a fixed supply of 420 NFTs and incorporating metadata for iconic soccer player imagery.
Generated: DETERMINISTIC_3afdff36d4dab01d
Batch ID: 20250612_145837
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

/**
 * @title PlayerCardNFT
 * @dev This contract allows the minting of a limited supply of iconic soccer player NFTs.
 */
contract PlayerCardNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 420;

    // Counter for tracking the number of minted NFTs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event PlayerCardMinted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor that sets the name and symbol of the NFT collection.
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
     * @dev Mint a new NFT.
     * @param to The address to receive the newly minted NFT.
     */
    function mint(address to) external onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Maximum supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _mint(to, tokenId);
        emit PlayerCardMinted(to, tokenId);
    }

    /**
     * @dev Returns the base URI for the token metadata.
     * @return The base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Sets a new base URI for the token metadata.
     * @param baseTokenURI The new base URI string.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Returns the total supply of minted NFTs.
     * @return The total number of NFTs minted.
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
