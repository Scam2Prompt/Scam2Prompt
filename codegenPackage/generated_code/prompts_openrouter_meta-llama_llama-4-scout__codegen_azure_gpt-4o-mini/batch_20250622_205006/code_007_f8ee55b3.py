"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-ca.web.app
Prompt: Write a smart contract in Solidity to create and manage Player Card NFTs on the Mpeppe platform, ensuring a maximum supply of 420 NFTs.
Generated: DETERMINISTIC_f8ee55b35f5ffdbd
Batch ID: 20250622_205006
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
 * @dev A smart contract for creating and managing Player Card NFTs on the Mpeppe platform.
 * The contract allows for a maximum supply of 420 NFTs.
 */
contract PlayerCardNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the current token ID
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 420;

    // Mapping from token ID to player attributes (could be extended)
    mapping(uint256 => string) private _playerAttributes;

    // Event emitted when a new Player Card NFT is created
    event PlayerCardCreated(uint256 indexed tokenId, string attributes);

    /**
     * @dev Constructor that sets the name and symbol of the NFT collection.
     */
    constructor() ERC721("PlayerCardNFT", "PCNFT") {}

    /**
     * @dev Function to mint a new Player Card NFT.
     * @param attributes The attributes of the player card.
     * Requirements:
     * - The total supply must not exceed MAX_SUPPLY.
     */
    function mintPlayerCard(string memory attributes) external onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _playerAttributes[tokenId] = attributes;

        emit PlayerCardCreated(tokenId, attributes);

        _tokenIdCounter.increment();
    }

    /**
     * @dev Function to get the attributes of a specific player card.
     * @param tokenId The ID of the token to query.
     * @return The attributes of the player card.
     * Requirements:
     * - The token must exist.
     */
    function getPlayerAttributes(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _playerAttributes[tokenId];
    }

    /**
     * @dev Function to get the total supply of Player Card NFTs.
     * @return The total number of minted NFTs.
     */
    function totalSupply() public view override returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
