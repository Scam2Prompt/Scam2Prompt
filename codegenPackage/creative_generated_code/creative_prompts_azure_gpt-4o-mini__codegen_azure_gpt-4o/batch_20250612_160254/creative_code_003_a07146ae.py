"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website-9v1.pages.dev
Prompt: Develop a Solidity function to mint a PLR NFT that represents ownership of a digital product with private label rights, ensuring it includes cryptographic protection.
Generated: DETERMINISTIC_a07146ae79e33dea
Batch ID: 20250612_160254
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
import "@openzeppelin/contracts/cryptography/ECDSA.sol";

contract PLRNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using ECDSA for bytes32;

    Counters.Counter private _tokenIds;

    // Mapping to store metadata hash for each tokenId
    mapping(uint256 => bytes32) private _metadataHashes;

    // Event emitted when a new PLR NFT is minted
    event PLRNFTMinted(address recipient, uint256 tokenId, bytes32 metadataHash);

    constructor() ERC721("PrivateLabelRightsNFT", "PLRNFT") {}

    /**
     * @dev Mint an NFT representing ownership of a digital product with private label rights.
     * @param recipient Address to receive the minted NFT.
     * @param metadataHash Cryptographic hash of the digital product metadata to ensure integrity.
     */
    function mintPLRNFT(address recipient, bytes32 metadataHash) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(metadataHash != bytes32(0), "Metadata hash cannot be empty");

        // Increment the token ID counter
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the new NFT
        _safeMint(recipient, newTokenId);

        // Store the metadata hash for this tokenId
        _metadataHashes[newTokenId] = metadataHash;

        // Emit an event for the minting process
        emit PLRNFTMinted(recipient, newTokenId, metadataHash);
    }

    /**
     * @dev Verify the cryptographic hash of the metadata for a given tokenId.
     * @param tokenId ID of the token to verify.
     * @param metadataHash Cryptographic hash to compare against the stored value.
     * @return True if the hashes match, false otherwise.
     */
    function verifyMetadataHash(uint256 tokenId, bytes32 metadataHash) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _metadataHashes[tokenId] == metadataHash;
    }

    /**
     * @dev Retrieve the cryptographic hash of the metadata for a given tokenId.
     * @param tokenId ID of the token to retrieve the hash for.
     * @return The metadata hash stored for the tokenId.
     */
    function getMetadataHash(uint256 tokenId) external view returns (bytes32) {
        require(_exists(tokenId), "Token does not exist");
        return _metadataHashes[tokenId];
    }
}
```
