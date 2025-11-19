"""
Generated Code Metadata:
========================
Original URL: https://pepearab.pages.dev
Prompt: Generate a Solidity code for creating an NFT contract similar to PepeArab's Arab NFTs, with a supply limit and specific unlock conditions.
Generated: DETERMINISTIC_b8481eb2b356515b
Batch ID: 20250622_211656
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
 * @title ArabNFT
 * @dev This contract implements an NFT collection with a supply limit and unlock conditions.
 */
contract ArabNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 1000;

    // Mapping to track unlock conditions for each token
    mapping(uint256 => bool) private _unlockConditions;

    // Event emitted when an NFT is unlocked
    event NFTUnlocked(uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT collection.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT.
     * @param to The address to receive the minted NFT.
     * Requirements:
     * - The total supply must be less than MAX_SUPPLY.
     */
    function mint(address to) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId);
    }

    /**
     * @dev Set unlock condition for a specific token.
     * @param tokenId The ID of the token to set the unlock condition for.
     * @param condition The unlock condition to set.
     * Requirements:
     * - The caller must be the owner of the token.
     */
    function setUnlockCondition(uint256 tokenId, bool condition) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Caller is not the token owner");

        _unlockConditions[tokenId] = condition;
    }

    /**
     * @dev Unlock the NFT if the condition is met.
     * @param tokenId The ID of the token to unlock.
     * Requirements:
     * - The caller must be the owner of the token.
     * - The unlock condition must be true.
     */
    function unlockNFT(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Caller is not the token owner");
        require(_unlockConditions[tokenId], "Unlock condition not met");

        emit NFTUnlocked(tokenId);
        // Additional logic for unlocking can be added here
    }

    /**
     * @dev Check if the unlock condition is met for a specific token.
     * @param tokenId The ID of the token to check.
     * @return bool indicating if the unlock condition is met.
     */
    function isUnlockConditionMet(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _unlockConditions[tokenId];
    }
}
```
