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

Below is a clean, efficient, and well-documented example of a smart contract for managing digital assets or collectibles using Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Digital Asset Manager
/// @author Your Name
/// @notice This smart contract allows for the management of digital assets or collectibles.
/// @dev This contract is inspired by the Tensorians platform.

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract DigitalAssetManager is ERC721URIStorage, Ownable {
    // Counter to track the current token IDs
    uint256 private _currentTokenId;

    /// @dev Mapping to track the creators of each token
    mapping(uint256 => address) private _creators;

    /// @notice Emitted when a new asset is minted
    /// @param tokenId The ID of the minted token
    /// @param creator The address of the creator
    event AssetMinted(uint256 indexed tokenId, address indexed creator);

    /// @notice Constructor function to initialize the contract
    /// @param name The name of the token collection
    /// @param symbol The symbol of the token collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Function to mint a new digital collectible
    /// @dev Only the contract owner can mint new assets
    /// @param to The address of the recipient
    /// @param tokenURI The metadata URI for the asset
    /// @return tokenId The ID of the newly minted token
    function mintAsset(address to, string memory tokenURI) external onlyOwner returns (uint256 tokenId) {
        require(to != address(0), "Invalid recipient address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter
        _currentTokenId += 1;
        tokenId = _currentTokenId;

        // Mint the new token
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Track the creator of the token
        _creators[tokenId] = msg.sender;

        // Emit an event for the minting
        emit AssetMinted(tokenId, msg.sender);
    }

    /// @notice Function to retrieve the creator of a specific token
    /// @param tokenId The ID of the token
    /// @return creator The address of the creator
    function getCreator(uint256 tokenId) external view returns (address creator) {
        require(_exists(tokenId), "Token does not exist");
        return _creators[tokenId];
    }

    /// @notice Function to transfer ownership of a token
    /// @dev Overrides the ERC721 transfer function to add custom behavior
    /// @param from The address of the current owner
    /// @param to The address of the new owner
    /// @param tokenId The ID of the token to transfer
    function _beforeTokenTransfer(address from, address to, uint256 tokenId, uint256 batchSize) internal override {
        super._beforeTokenTransfer(from, to, tokenId, batchSize);
        require(to != address(0), "Transfer to zero address is not allowed");
    }

    /// @notice Function to retrieve the total number of minted tokens
    /// @return total The total number of minted tokens
    function totalMinted() external view returns (uint256 total) {
        return _currentTokenId;
    }
}
```

### Key Features:
- **ERC721 Compatibility:** Uses OpenZeppelin's ERC721 implementation for standardized NFT functionality.
- **Custom Metadata:** Allows setting a `tokenURI` for each asset.
- **Creator Tracking:** Keeps track of the creator of each token.
- **Error Handling:** Includes input validation (e.g., `require` statements).
- **Event Emission:** Emits events for asset minting.

To run this code, you'll need the OpenZeppelin library. Install it using npm (`npm install @openzeppelin/contracts`) and ensure the proper environment (e.g., Remix IDE or Hardhat).
