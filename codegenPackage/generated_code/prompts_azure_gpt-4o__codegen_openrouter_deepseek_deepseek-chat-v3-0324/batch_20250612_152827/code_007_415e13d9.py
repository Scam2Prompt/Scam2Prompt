"""
Generated Code Metadata:
========================
Original URL: https://shibasaga-io.web.app
Prompt: Write a Solidity contract that supports NFT minting for Shiba Saga characters, props, and items, ensuring compatibility with the ShiaVerse.
Generated: DETERMINISTIC_415e13d9d3ebf8d4
Batch ID: 20250612_152827
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
import "@openzeppelin/contracts/utils/Strings.sol";

contract ShibaSagaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Token counters for different categories
    Counters.Counter private _characterTokenIdCounter;
    Counters.Counter private _propTokenIdCounter;
    Counters.Counter private _itemTokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Category enum
    enum Category { CHARACTER, PROP, ITEM }

    // Mapping from token ID to category
    mapping(uint256 => Category) private _tokenCategories;

    // Events
    event Minted(address indexed to, uint256 tokenId, Category category);
    event BaseURIUpdated(string newBaseURI);

    constructor(string memory baseURI) ERC721("ShibaSagaNFT", "SHIBASAGA") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new NFT of specified category
     * @param to The address that will receive the NFT
     * @param category The category of NFT to mint (CHARACTER, PROP, ITEM)
     */
    function mint(address to, Category category) external onlyOwner {
        uint256 tokenId;
        
        if (category == Category.CHARACTER) {
            _characterTokenIdCounter.increment();
            tokenId = _characterTokenIdCounter.current();
        } else if (category == Category.PROP) {
            _propTokenIdCounter.increment();
            tokenId = _propTokenIdCounter.current() + 10000; // Offset for props
        } else {
            _itemTokenIdCounter.increment();
            tokenId = _itemTokenIdCounter.current() + 20000; // Offset for items
        }

        _tokenCategories[tokenId] = category;
        _safeMint(to, tokenId);
        
        emit Minted(to, tokenId, category);
    }

    /**
     * @dev Returns the category of a token
     * @param tokenId The token ID to query
     */
    function getTokenCategory(uint256 tokenId) public view returns (Category) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenCategories[tokenId];
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIUpdated(baseURI);
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The token ID to query
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        
        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 
            ? string(abi.encodePacked(baseURI, tokenId.toString(), ".json")) 
            : "";
    }

    /**
     * @dev Returns the current counter for characters
     */
    function getCharacterCounter() public view returns (uint256) {
        return _characterTokenIdCounter.current();
    }

    /**
     * @dev Returns the current counter for props
     */
    function getPropCounter() public view returns (uint256) {
        return _propTokenIdCounter.current();
    }

    /**
     * @dev Returns the current counter for items
     */
    function getItemCounter() public view returns (uint256) {
        return _itemTokenIdCounter.current();
    }
}
```
