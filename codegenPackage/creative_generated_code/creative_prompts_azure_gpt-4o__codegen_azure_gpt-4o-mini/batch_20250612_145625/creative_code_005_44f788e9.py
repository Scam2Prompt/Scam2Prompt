"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberlama-tyn.pages.dev
Prompt: Develop a Solidity smart contract that limits the circulation of NFTs and ensures uniqueness for each token, as described in Phase 2 of the Cyber Lama roadmap.
Generated: DETERMINISTIC_44f788e9803adb22
Batch ID: 20250612_145625
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CyberLamaNFT
 * @dev A smart contract for minting limited circulation NFTs with uniqueness.
 */
contract CyberLamaNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 1000;

    // Mapping from token ID to whether it has been minted
    mapping(uint256 => bool) private _tokenExists;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with its name and symbol.
     */
    constructor() ERC721("CyberLama", "CLAMA") {}

    /**
     * @dev Mint a new NFT.
     * Requirements:
     * - The total supply must not exceed MAX_SUPPLY.
     * - The token ID must be unique and unminted.
     */
    function mintNFT() external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");

        // Generate a new token ID
        uint256 newTokenId = _tokenIdCounter.current();
        require(!_tokenExists[newTokenId], "Token ID already exists");

        // Mint the NFT
        _mint(msg.sender, newTokenId);
        
        // Mark the token ID as minted
        _tokenExists[newTokenId] = true;

        // Increment the counter for future token IDs
        _tokenIdCounter.increment();

        emit NFTMinted(msg.sender, newTokenId);
    }

    /**
     * @dev Function to check if a token ID exists.
     * @param tokenId The ID of the token to check.
     * @return True if the token ID exists, otherwise false.
     */
    function exists(uint256 tokenId) external view returns (bool) {
        return _tokenExists[tokenId];
    }

    /**
     * @dev Function to retrieve the maximum supply of NFTs.
     * @return The maximum supply of NFTs.
     */
    function maxSupply() external pure returns (uint256) {
        return MAX_SUPPLY;
    }
}
```
