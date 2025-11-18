"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superrare.fr
Prompt: Generate a Solidity smart contract for minting NFTs that include custom metadata, such as artist signatures, as described on SuperRare.fr.
Generated: DETERMINISTIC_a3ae07eed1fa961e
Batch ID: 20250612_155037
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

// Import OpenZeppelin Contracts for ERC721 (NFT Standard) and Ownable (Access Control)
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CustomMetadataNFT is ERC721URIStorage, Ownable {
    // Counter to track token IDs
    uint256 private _currentTokenId;

    // Event to notify successful minting of a new NFT
    event NFTMinted(uint256 tokenId, address owner, string tokenURI, string artistSignature);

    // Mapping to associate token IDs with artist signatures
    mapping(uint256 => string) private _artistSignatures;

    // Constructor sets the name and symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @notice Mint a new NFT with custom metadata.
     * @param to The address that will own the minted NFT.
     * @param tokenURI The metadata URI for the NFT (points to IPFS or other storage).
     * @param artistSignature A custom signature from the artist.
     */
    function mintNFT(
        address to,
        string memory tokenURI,
        string memory artistSignature
    ) external onlyOwner {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");
        require(bytes(artistSignature).length > 0, "Artist signature cannot be empty");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT to the specified address
        _mint(to, _currentTokenId);

        // Set the metadata URI for the NFT
        _setTokenURI(_currentTokenId, tokenURI);

        // Store artist signature
        _artistSignatures[_currentTokenId] = artistSignature;

        // Emit event for minting
        emit NFTMinted(_currentTokenId, to, tokenURI, artistSignature);
    }

    /**
     * @notice Retrieve the artist signature associated with a specific token ID.
     * @param tokenId The ID of the token to query.
     * @return The artist signature for the token.
     */
    function getArtistSignature(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _artistSignatures[tokenId];
    }

    /**
     * @notice Retrieve the current token ID counter (useful for external tracking).
     * @return The current token ID counter.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```

This Solidity smart contract uses the OpenZeppelin ERC721 standard for NFTs, adds custom metadata (artist signatures), and includes robust error handling and best practices. Make sure that the `@openzeppelin/contracts` library is installed in your environment before deploying or testing this code.
