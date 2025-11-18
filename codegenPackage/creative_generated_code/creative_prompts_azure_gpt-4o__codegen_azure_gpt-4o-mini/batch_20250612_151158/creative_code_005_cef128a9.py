"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-tensorians.pages.dev
Prompt: Create a smart contract example for managing digital assets or collectibles, inspired by the Tensorians platform.
Generated: DETERMINISTIC_cef128a98bbbb56a
Batch ID: 20250612_151158
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

/// @title Digital Asset Management Smart Contract
/// @author Your Name
/// @notice This contract allows the management of digital assets or collectibles
/// @dev This contract is inspired by the Tensorians platform

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Define the main contract
contract DigitalAsset is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to asset URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 indexed tokenId, string tokenURI);

    // Constructor to set the name and symbol of the token
    constructor() ERC721("DigitalAsset", "DASSET") {}

    /// @notice Create a new digital asset
    /// @param tokenURI The URI pointing to the asset's metadata
    /// @dev Only the contract owner can create new assets
    function createAsset(string memory tokenURI) external onlyOwner {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new token to the owner's address
        _mint(msg.sender, tokenId);

        // Set the token URI for the newly created token
        _setTokenURI(tokenId, tokenURI);

        // Emit the asset creation event
        emit AssetCreated(tokenId, tokenURI);
    }

    /// @notice Set the token URI for a given token ID
    /// @param tokenId The ID of the token
    /// @param tokenURI The URI of the token metadata
    /// @dev Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /// @notice Retrieve the token URI for a given token ID
    /// @param tokenId The ID of the token
    /// @return The URI of the token metadata
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /// @notice Retrieve the total number of assets created
    /// @return The total asset count
    function totalAssets() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
