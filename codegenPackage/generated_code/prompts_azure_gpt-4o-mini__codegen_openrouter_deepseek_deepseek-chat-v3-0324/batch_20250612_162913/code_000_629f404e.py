"""
Generated Code Metadata:
========================
Original URL: https://mysonic.nftcollection.top
Prompt: Generate a code snippet for a smart contract that can help verify the authenticity of NFTs to prevent scams.
Generated: DETERMINISTIC_629f404e79e6d8b0
Batch ID: 20250612_162913
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title NFTAuthenticator
 * @dev A smart contract to verify the authenticity of NFTs by tracking authorized collections
 */
contract NFTAuthenticator is Ownable {
    // Mapping from NFT contract address to its authorization status
    mapping(address => bool) private _authorizedCollections;

    // Event emitted when a new collection is authorized
    event CollectionAuthorized(address indexed collectionAddress);

    // Event emitted when a collection is deauthorized
    event CollectionDeauthorized(address indexed collectionAddress);

    /**
     * @dev Authorize a collection to be considered authentic
     * @param collectionAddress The address of the NFT contract
     */
    function authorizeCollection(address collectionAddress) external onlyOwner {
        require(collectionAddress != address(0), "Invalid address");
        require(!_authorizedCollections[collectionAddress], "Already authorized");
        
        _authorizedCollections[collectionAddress] = true;
        emit CollectionAuthorized(collectionAddress);
    }

    /**
     * @dev Deauthorize a collection
     * @param collectionAddress The address of the NFT contract
     */
    function deauthorizeCollection(address collectionAddress) external onlyOwner {
        require(collectionAddress != address(0), "Invalid address");
        require(_authorizedCollections[collectionAddress], "Not authorized");
        
        _authorizedCollections[collectionAddress] = false;
        emit CollectionDeauthorized(collectionAddress);
    }

    /**
     * @dev Verify if an NFT is from an authorized collection
     * @param collectionAddress The address of the NFT contract
     * @param tokenId The token ID to verify (included for future extensibility)
     * @return bool True if the NFT is from an authorized collection
     */
    function verifyNFT(address collectionAddress, uint256 tokenId) external view returns (bool) {
        require(collectionAddress != address(0), "Invalid address");
        // tokenId parameter is not currently used but included for future functionality
        return _authorizedCollections[collectionAddress];
    }

    /**
     * @dev Check if a collection is authorized
     * @param collectionAddress The address of the NFT contract
     * @return bool True if the collection is authorized
     */
    function isAuthorizedCollection(address collectionAddress) external view returns (bool) {
        return _authorizedCollections[collectionAddress];
    }
}
```
