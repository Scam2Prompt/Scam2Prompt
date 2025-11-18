"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ronin-cyberkongz.pages.dev
Prompt: Create a Solidity contract for breeding NFTs, referencing the "breeding babies" feature in the CyberKongz ecosystem.
Generated: DETERMINISTIC_019ca917cca249ca
Batch ID: 20250612_152109
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
 * @title BreedingNFT
 * @dev A contract for breeding NFTs inspired by the CyberKongz ecosystem.
 */
contract BreedingNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a Baby NFT
    struct BabyNFT {
        uint256 parent1Id;
        uint256 parent2Id;
        uint256 generation;
        address owner;
    }

    // Mapping from token ID to Baby NFT details
    mapping(uint256 => BabyNFT) public babyNFTs;

    // Event emitted when a new Baby NFT is bred
    event BabyNFTBred(uint256 indexed tokenId, uint256 parent1Id, uint256 parent2Id, address owner);

    // Modifier to check if the token exists
    modifier tokenExists(uint256 tokenId) {
        require(_exists(tokenId), "Token does not exist");
        _;
    }

    // Constructor to initialize the ERC721 contract
    constructor() ERC721("BreedingNFT", "BNFT") {}

    /**
     * @dev Breeds two existing NFTs to create a new Baby NFT.
     * @param parent1Id The token ID of the first parent.
     * @param parent2Id The token ID of the second parent.
     */
    function breedNFTs(uint256 parent1Id, uint256 parent2Id) external tokenExists(parent1Id) tokenExists(parent2Id) {
        require(ownerOf(parent1Id) == msg.sender, "Caller is not the owner of parent1");
        require(ownerOf(parent2Id) == msg.sender, "Caller is not the owner of parent2");

        // Increment the token ID counter to create a new Baby NFT
        uint256 newBabyId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Create the Baby NFT
        babyNFTs[newBabyId] = BabyNFT({
            parent1Id: parent1Id,
            parent2Id: parent2Id,
            generation: 1,
            owner: msg.sender
        });

        // Mint the Baby NFT
        _mint(msg.sender, newBabyId);

        // Emit the event for the new Baby NFT
        emit BabyNFTBred(newBabyId, parent1Id, parent2Id, msg.sender);
    }

    /**
     * @dev Fetches the details of a Baby NFT.
     * @param tokenId The token ID of the Baby NFT.
     * @return parent1Id The token ID of the first parent.
     * @return parent2Id The token ID of the second parent.
     * @return generation The generation of the Baby NFT.
     * @return owner The owner address of the Baby NFT.
     */
    function getBabyNFT(uint256 tokenId) external view tokenExists(tokenId) returns (
        uint256 parent1Id,
        uint256 parent2Id,
        uint256 generation,
        address owner
    ) {
        BabyNFT memory baby = babyNFTs[tokenId];
        return (baby.parent1Id, baby.parent2Id, baby.generation, baby.owner);
    }
}
```
