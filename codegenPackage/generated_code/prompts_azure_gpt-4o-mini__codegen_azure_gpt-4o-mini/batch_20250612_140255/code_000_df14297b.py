"""
Generated Code Metadata:
========================
Original URL: https://unicats-on-unichain.nfts2.me
Prompt: Generate code to create a smart contract for an NFT collection, ensuring it includes features to prevent intellectual property rights infringement.
Generated: DETERMINISTIC_df14297b22666c66
Batch ID: 20250612_140255
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
 * @title NFTCollection
 * @dev A smart contract for creating a non-fungible token (NFT) collection
 * with features to prevent intellectual property rights infringement.
 */
contract NFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to the creator's address
    mapping(uint256 => address) private _creators;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed creator, string tokenURI);

    // Modifier to check if the caller is the creator of the token
    modifier onlyCreator(uint256 tokenId) {
        require(_creators[tokenId] == msg.sender, "Caller is not the creator");
        _;
    }

    /**
     * @dev Constructor to initialize the NFT collection with a name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to create a new NFT.
     * @param to The address to mint the NFT to.
     * @param tokenURI The metadata URI for the NFT.
     */
    function createNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(bytes(tokenURI).length > 0, "Invalid token URI");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _creators[tokenId] = msg.sender;

        emit NFTCreated(tokenId, msg.sender, tokenURI);
        _tokenIdCounter.increment();
    }

    /**
     * @dev Function to transfer ownership of an NFT.
     * @param from The current owner of the NFT.
     * @param to The new owner of the NFT.
     * @param tokenId The ID of the NFT to transfer.
     */
    function transferNFT(address from, address to, uint256 tokenId) external onlyCreator(tokenId) {
        require(from == ownerOf(tokenId), "From address is not the owner");
        require(to != address(0), "Invalid address");

        _transfer(from, to, tokenId);
    }

    /**
     * @dev Function to get the creator of a specific token.
     * @param tokenId The ID of the NFT.
     * @return The address of the creator.
     */
    function getCreator(uint256 tokenId) external view returns (address) {
        return _creators[tokenId];
    }

    /**
     * @dev Internal function to set the token URI.
     * @param tokenId The ID of the NFT.
     * @param tokenURI The metadata URI for the NFT.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal virtual {
        // This function can be overridden to implement a token URI storage mechanism
        // For example, using a mapping or an external storage solution
    }
}
```
