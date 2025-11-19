"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unicats-on-unichain.nfts2.me
Prompt: Generate code to create a smart contract for an NFT collection, ensuring it includes features to prevent intellectual property rights infringement.
Generated: DETERMINISTIC_df14297b22666c66
Batch ID: 20250612_140255
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

/**
 * @title NFTCollection
 * @dev Smart contract for creating an NFT collection with added features to prevent intellectual property rights infringement.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTCollection is ERC721URIStorage, Ownable {
    uint256 private _currentTokenId; // Tracks the current token ID
    mapping(string => bool) private _registeredHashes; // Stores hashes of metadata/URIs to prevent duplication

    /**
     * @dev Constructor sets the name and symbol of the NFT collection.
     * @param name - Name of the NFT collection.
     * @param symbol - Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT.
     * @param recipient - Address of the NFT recipient.
     * @param tokenURI - Metadata URI for the NFT.
     * @param metadataHash - Hash of the metadata content to ensure uniqueness and prevent infringement.
     */
    function mintNFT(address recipient, string memory tokenURI, string memory metadataHash) external onlyOwner {
        require(!_registeredHashes[metadataHash], "NFTCollection: Duplicate metadata detected.");
        
        // Register the metadata hash to prevent duplication
        _registeredHashes[metadataHash] = true;

        // Increment the current token ID
        _currentTokenId++;

        // Mint the new NFT
        _mint(recipient, _currentTokenId);

        // Set the token URI for the minted NFT
        _setTokenURI(_currentTokenId, tokenURI);
    }

    /**
     * @dev Burn an existing NFT.
     * @param tokenId - ID of the NFT to be burned.
     */
    function burnNFT(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "NFTCollection: Token does not exist.");
        
        // Clear the metadata hash registration (optional, if applicable)
        string memory tokenURI = tokenURI(tokenId);
        bytes32 metadataHash = keccak256(abi.encodePacked(tokenURI));
        if (_registeredHashes[string(metadataHash)]) {
            _registeredHashes[string(metadataHash)] = false;
        }

        // Burn the NFT
        _burn(tokenId);
    }

    /**
     * @dev Check if a metadata hash is already registered.
     * @param metadataHash - Hash of the metadata content.
     * @return bool - Returns true if the metadata hash is registered, false otherwise.
     */
    function isMetadataHashRegistered(string memory metadataHash) external view returns (bool) {
        return _registeredHashes[metadataHash];
    }

    /**
     * @dev Override supportsInterface to include interface checking.
     * @param interfaceId - ID of the interface to check.
     * @return bool - Returns true if the interface is supported, false otherwise.
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```

**Dependencies:**
Ensure the following dependencies are installed in your project:
1. OpenZeppelin Contracts (ERC721, Ownable): Install via `npm install @openzeppelin/contracts`.
