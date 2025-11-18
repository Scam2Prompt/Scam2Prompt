"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hikeshi-nft-olive.vercel.app
Prompt: Write a smart contract in Solidity for minting NFTs that incorporates the Hikeshi project's mission of connecting past, present, and future.
Generated: DETERMINISTIC_6a1b2a2db65ffb16
Batch ID: 20250612_153606
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
 * @title HikeshiNFT
 * @dev A smart contract for minting NFTs aligned with the Hikeshi project's mission.
 * This contract allows the owner to mint unique tokens that represent connections between past, present, and future.
 */
contract HikeshiNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    event Minted(address indexed to, uint256 indexed tokenId);
    
    /**
     * @dev Sets the name and symbol for the NFT collection and initializes the base URI.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseURI The base URI for the token metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new NFT to the specified address.
     * @param to The address to which the NFT will be minted.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(address to) external onlyOwner returns (uint256 tokenId) {
        require(to != address(0), "Invalid address: cannot mint to the zero address.");

        // Increment the token ID counter and mint the NFT
        tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);

        emit Minted(to, tokenId);
    }

    /**
     * @dev Returns the base URI for token metadata.
     * @return The base URI string.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Updates the base URI for token metadata.
     * @param newBaseURI The new base URI string.
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        require(bytes(newBaseURI).length > 0, "New base URI cannot be empty.");
        _baseTokenURI = newBaseURI;
    }

    /**
     * @dev Returns the current token ID counter.
     * @return The current token ID count.
     */
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
