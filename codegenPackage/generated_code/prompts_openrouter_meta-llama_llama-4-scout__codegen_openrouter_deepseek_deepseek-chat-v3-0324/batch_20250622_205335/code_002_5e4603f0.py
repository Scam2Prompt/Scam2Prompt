"""
Generated Code Metadata:
========================
Original URL: https://cknft.pages.dev
Prompt: Generate a smart contract in Solidity for an NFT project that grants exclusive access to events and merchandise for holders, similar to the Blvck Alpha Membership benefits.
Generated: DETERMINISTIC_5e4603f0db48436e
Batch ID: 20250622_205335
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

/**
 * @title ExclusiveAccessNFT
 * @dev ERC721 token that grants exclusive access to events and merchandise for holders
 */
contract ExclusiveAccessNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Mapping from token ID to whether it's been used for event access
    mapping(uint256 => bool) private _usedForEventAccess;

    // Mapping from token ID to whether it's been used for merchandise access
    mapping(uint256 => bool) private _usedForMerchandiseAccess;

    // Event emitted when NFT is used for event access
    event EventAccessUsed(uint256 indexed tokenId, address indexed owner);

    // Event emitted when NFT is used for merchandise access
    event MerchandiseAccessUsed(uint256 indexed tokenId, address indexed owner);

    /**
     * @dev Constructor that sets the name and symbol of the token
     * @param name Name of the NFT
     * @param symbol Symbol of the NFT
     * @param baseTokenURI Base URI for token metadata
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mints a new NFT to the specified address (only callable by owner)
     * @param to Address to mint the NFT to
     */
    function safeMint(address to) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Updates the base URI for token metadata (only callable by owner)
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) public onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Marks an NFT as used for event access (only callable by owner)
     * @param tokenId ID of the NFT to mark as used
     */
    function useForEventAccess(uint256 tokenId) public onlyOwner {
        require(_exists(tokenId), "ExclusiveAccessNFT: Token does not exist");
        require(!_usedForEventAccess[tokenId], "ExclusiveAccessNFT: Token already used for event access");

        _usedForEventAccess[tokenId] = true;
        emit EventAccessUsed(tokenId, ownerOf(tokenId));
    }

    /**
     * @dev Marks an NFT as used for merchandise access (only callable by owner)
     * @param tokenId ID of the NFT to mark as used
     */
    function useForMerchandiseAccess(uint256 tokenId) public onlyOwner {
        require(_exists(tokenId), "ExclusiveAccessNFT: Token does not exist");
        require(!_usedForMerchandiseAccess[tokenId], "ExclusiveAccessNFT: Token already used for merchandise access");

        _usedForMerchandiseAccess[tokenId] = true;
        emit MerchandiseAccessUsed(tokenId, ownerOf(tokenId));
    }

    /**
     * @dev Checks if an NFT has been used for event access
     * @param tokenId ID of the NFT to check
     * @return bool Whether the NFT has been used for event access
     */
    function isUsedForEventAccess(uint256 tokenId) public view returns (bool) {
        require(_exists(tokenId), "ExclusiveAccessNFT: Token does not exist");
        return _usedForEventAccess[tokenId];
    }

    /**
     * @dev Checks if an NFT has been used for merchandise access
     * @param tokenId ID of the NFT to check
     * @return bool Whether the NFT has been used for merchandise access
     */
    function isUsedForMerchandiseAccess(uint256 tokenId) public view returns (bool) {
        require(_exists(tokenId), "ExclusiveAccessNFT: Token does not exist");
        return _usedForMerchandiseAccess[tokenId];
    }

    /**
     * @dev Overrides transfer functions to prevent transfers if needed (optional)
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, tokenId);
        // Add any transfer restrictions here if needed
    }
}
```
