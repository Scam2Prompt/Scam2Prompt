"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runemilio.pages.dev
Prompt: Create a smart contract that supports minting and inscription processes inspired by Runemilio's methodology.
Generated: DETERMINISTIC_439088902e729643
Batch ID: 20250612_153526
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

/// @title RunemilioMinting
/// @author Your Name
/// @notice This contract enables minting and inscription processes for NFTs
/// @dev The contract allows users to mint NFTs and inscribe data to their tokens

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Custom error declaration for better error handling
error MintingFailed();
error InscriptionFailed();
error TokenDoesNotExist();

contract RunemilioMinting is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to inscription data
    mapping(uint256 => string) private _inscriptions;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner);

    // Event emitted when an inscription is added
    event Inscribed(uint256 indexed tokenId, string data);

    /// @notice Constructor to initialize the contract with a name and symbol
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Function to mint a new NFT
    /// @return tokenId The ID of the newly minted NFT
    function mint() external onlyOwner returns (uint256 tokenId) {
        tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();

        emit Minted(tokenId, msg.sender);
    }

    /// @notice Function to inscribe data to an existing NFT
    /// @param tokenId The ID of the token to inscribe data to
    /// @param data The data to inscribe
    function inscribe(uint256 tokenId, string calldata data) external {
        // Check that the token exists and caller owns the token
        if (!_exists(tokenId) || ownerOf(tokenId) != msg.sender) {
            revert TokenDoesNotExist();
        }

        _inscriptions[tokenId] = data;

        emit Inscribed(tokenId, data);
    }

    /// @notice Function to retrieve the inscription of a token
    /// @param tokenId The ID of the token to retrieve the inscription from
    /// @return The inscription data associated with the token
    function getInscription(uint256 tokenId) external view returns (string memory) {
        if (!_exists(tokenId)) {
            revert TokenDoesNotExist();
        }
        return _inscriptions[tokenId];
    }

    /// @notice Function to check if an inscription exists for a specific token
    /// @param tokenId The ID of the token to check
    /// @return bool indicating whether the inscription exists
    function inscriptionExists(uint256 tokenId) external view returns (bool) {
        return bytes(_inscriptions[tokenId]).length > 0;
    }
}
```
