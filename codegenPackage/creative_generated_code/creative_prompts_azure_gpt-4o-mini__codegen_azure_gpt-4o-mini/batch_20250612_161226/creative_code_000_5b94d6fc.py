"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://timcheese.pages.dev
Prompt: How can I create a smart contract to mint NFTs for a collection like Tim Cheese's 10,000 diverse tim?
Generated: DETERMINISTIC_5b94d6fc863f57ee
Batch ID: 20250612_161226
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

// Import the OpenZeppelin ERC721 library for secure and well-tested NFT implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title TimCheeseCollection
 * @dev Smart contract for minting a collection of 10,000 unique NFTs
 */
contract TimCheeseCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the total number of minted NFTs
    Counters.Counter private _tokenIdCounter;

    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_SUPPLY = 10000;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT collection with a name and symbol.
     * @param name string - The name of the NFT collection.
     * @param symbol string - The symbol of the NFT collection.
     * @param baseTokenURI string - The base URI for NFT metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new NFT to the specified address.
     * @param to address - The address to which the NFT will be minted.
     * @return uint256 - The token ID of the newly minted NFT.
     */
    function mint(address to) public onlyOwner returns (uint256) {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _safeMint(to, tokenId);

        // Emit an event for the minted NFT
        emit Minted(to, tokenId);

        return tokenId;
    }

    /**
     * @dev Override the baseURI function to return the base URI for the metadata.
     * @return string - The base URI for the NFT metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to update the base URI for the NFT metadata.
     * @param baseTokenURI string - The new base URI for the NFT metadata.
     */
    function setBaseURI(string memory baseTokenURI) public onlyOwner {
        _baseTokenURI = baseTokenURI;
    }
}
```
