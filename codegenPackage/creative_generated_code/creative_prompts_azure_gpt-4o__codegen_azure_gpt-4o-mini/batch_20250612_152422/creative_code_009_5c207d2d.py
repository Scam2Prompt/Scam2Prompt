"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piiiix.pages.dev
Prompt: Write a smart contract that interacts with the Pixels API to manage NFT rewards in a blockchain-connected game.
Generated: DETERMINISTIC_5c207d2dd1f57708
Batch ID: 20250612_152422
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title GameNFT
 * @dev Smart contract for managing NFT rewards in a blockchain-connected game.
 */
contract GameNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter; // Counter for NFT IDs

    // Mapping from token ID to user address
    mapping(uint256 => address) private _owners;

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor for the GameNFT contract.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT.
     * @param to The address to receive the new NFT.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(address to) external onlyOwner returns (uint256) {
        require(to != address(0), "Invalid address.");

        // Increment the token ID counter to get a new ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT and assign it to the recipient
        _mint(to, tokenId);
        _owners[tokenId] = to;

        emit Minted(to, tokenId); // Emit the minting event
        return tokenId; // Return the new token ID
    }

    /**
     * @dev Function to get the owner of a specific token.
     * @param tokenId The ID of the token.
     * @return The address of the token owner.
     */
    function ownerOfToken(uint256 tokenId) external view returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "Token does not exist.");
        return owner;
    }
}
```
