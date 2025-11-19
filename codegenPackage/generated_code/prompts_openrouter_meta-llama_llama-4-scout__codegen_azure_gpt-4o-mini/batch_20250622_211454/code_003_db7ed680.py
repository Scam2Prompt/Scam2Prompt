"""
Generated Code Metadata:
========================
Original URL: https://rewardtevara.xyz
Prompt: "Design a simple smart contract using Solidity to create and manage Soulbound NFTs on a ZK Stack powered platform like Tevara."
Generated: DETERMINISTIC_db7ed680172c44ec
Batch ID: 20250622_211454
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
 * @title SoulboundNFT
 * @dev A simple smart contract to create and manage Soulbound NFTs.
 * Soulbound NFTs are non-transferable and are bound to the owner's address.
 */
contract SoulboundNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to a boolean indicating if the NFT is soulbound
    mapping(uint256 => bool) private _soulbound;

    // Event emitted when a new Soulbound NFT is created
    event SoulboundNFTCreated(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT contract with a name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) 
        ERC721(name, symbol) 
    {}

    /**
     * @dev Function to create a new Soulbound NFT.
     * Only the contract owner can create new NFTs.
     * @param to The address that will own the newly created NFT.
     */
    function createSoulboundNFT(address to) external onlyOwner {
        require(to != address(0), "Invalid address: cannot mint to the zero address");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the specified address
        _mint(to, tokenId);
        _soulbound[tokenId] = true; // Mark the NFT as soulbound

        emit SoulboundNFTCreated(to, tokenId);
    }

    /**
     * @dev Override the transfer function to prevent transfers of soulbound NFTs.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param tokenId The ID of the token to transfer.
     */
    function transferFrom(address from, address to, uint256 tokenId) public override {
        require(!_soulbound[tokenId], "Soulbound NFT: cannot transfer soulbound NFTs");
        super.transferFrom(from, to, tokenId);
    }

    /**
     * @dev Override the safeTransferFrom function to prevent transfers of soulbound NFTs.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param tokenId The ID of the token to transfer.
     * @param data Additional data to pass with the transfer.
     */
    function safeTransferFrom(address from, address to, uint256 tokenId, bytes memory data) public override {
        require(!_soulbound[tokenId], "Soulbound NFT: cannot transfer soulbound NFTs");
        super.safeTransferFrom(from, to, tokenId, data);
    }

    /**
     * @dev Function to check if a token is soulbound.
     * @param tokenId The ID of the token to check.
     * @return bool indicating if the token is soulbound.
     */
    function isSoulbound(uint256 tokenId) external view returns (bool) {
        return _soulbound[tokenId];
    }
}
```
