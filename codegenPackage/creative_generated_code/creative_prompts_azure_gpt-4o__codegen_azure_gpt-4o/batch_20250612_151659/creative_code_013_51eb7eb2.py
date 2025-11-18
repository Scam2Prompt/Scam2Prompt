"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Generate a smart contract that supports the creation of legendary 1/1 NFTs within a collection, as described in Prime Ape Planet's roadmap.
Generated: DETERMINISTIC_51eb7eb2c44c8c12
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready smart contract written in Solidity for an NFT collection with 1/1 legendary NFTs. This contract adheres to the ERC-721 standard and implements best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import the ERC-721 implementation from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title LegendaryNFTCollection
/// @dev Supports the creation of legendary 1/1 NFTs within a collection
contract LegendaryNFTCollection is ERC721, Ownable {
    // Counter for token IDs
    uint256 private _nextTokenId;

    // Mapping to track if a token ID is legendary
    mapping(uint256 => bool) private _isLegendary;

    /// @dev Emitted when a legendary NFT is minted
    event LegendaryNFTMinted(address indexed to, uint256 tokenId);

    /// @notice Constructor function to initialize the NFT collection
    /// @param name The name of the NFT collection
    /// @param symbol The symbol for the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        _nextTokenId = 1; // Initialize token ID counter
    }

    /// @notice Mint a 1/1 legendary NFT
    /// @dev Only the owner of the contract can mint legendary NFTs
    /// @param recipient The address receiving the legendary NFT
    /// @param tokenId The unique token ID for this legendary NFT
    function mintLegendaryNFT(address recipient, uint256 tokenId) external onlyOwner {
        require(tokenId == _nextTokenId, "Token ID must match the next sequential ID.");
        require(!_isLegendary[tokenId], "This token ID has already been minted as legendary.");
        
        // Mark the token as legendary before minting
        _isLegendary[tokenId] = true;

        // Mint the NFT
        _mint(recipient, tokenId);

        // Emit event for tracking
        emit LegendaryNFTMinted(recipient, tokenId);

        // Increment the token ID counter
        _nextTokenId++;
    }

    /// @notice Check if a given token ID is legendary
    /// @param tokenId The token ID to query
    /// @return True if the token ID is legendary, otherwise false
    function isLegendary(uint256 tokenId) external view returns (bool) {
        return _isLegendary[tokenId];
    }

    /// @dev Override required by Solidity for ERC721 and Ownable.
    function supportsInterface(bytes4 interfaceId) public view override(ERC721) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```

### Notes:
- Dependencies:
  - OpenZeppelin's contracts (ERC721 and Ownable) are required. Install them using `npm install @openzeppelin/contracts`.
- Security:
  - The contract ensures that only the owner can mint legendary NFTs using `Ownable`.
  - Proper checks are in place to prevent minting duplicate legendary NFTs.
