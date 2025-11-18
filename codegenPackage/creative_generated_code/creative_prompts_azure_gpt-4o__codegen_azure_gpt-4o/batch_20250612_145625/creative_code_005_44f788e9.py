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

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title Cyber Lama NFT Contract
/// @dev This contract ensures limited circulation and uniqueness of NFTs
contract CyberLamaNFT is ERC721Enumerable, Ownable {
    // Maximum number of NFTs that can ever be minted
    uint256 public immutable maxSupply;

    // Mapping to ensure uniqueness of metadata (hashes of the metadata URIs)
    mapping(string => bool) private _uniqueMetadata;

    /// @notice Constructor to initialize the NFT contract
    /// @param _name Name of the NFT collection
    /// @param _symbol Symbol for the NFT
    /// @param _maxSupply Maximum supply of NFTs
    constructor(string memory _name, string memory _symbol, uint256 _maxSupply) ERC721(_name, _symbol) {
        require(_maxSupply > 0, "Max supply must be greater than 0");
        maxSupply = _maxSupply;
    }

    /// @notice Mint a new NFT
    /// @dev Ensures max supply is not exceeded and metadata uniqueness is maintained
    /// @param to Address to receive the minted NFT
    /// @param tokenId Unique ID for the NFT
    /// @param metadataURI Metadata URI for the NFT
    function mint(address to, uint256 tokenId, string memory metadataURI) external onlyOwner {
        require(totalSupply() < maxSupply, "Max supply reached"); // Ensure we don't exceed max supply
        require(!_uniqueMetadata[metadataURI], "Metadata must be unique"); // Ensure metadata is unique

        // Mark the metadata URI as used
        _uniqueMetadata[metadataURI] = true;

        // Mint the NFT
        _safeMint(to, tokenId);

        // (Optional) Set token URI if using metadata URI storage
        // This requires an implementation of _setTokenURI() in your contract or inherited class.
        // _setTokenURI(tokenId, metadataURI);
    }

    /// @notice Check if metadata URI is unique
    /// @param metadataURI Metadata URI to check
    /// @return Returns true if metadata is unique, false otherwise
    function isMetadataUnique(string memory metadataURI) external view returns (bool) {
        return !_uniqueMetadata[metadataURI];
    }
}
```

### Key Points:
1. Ensure proper imports (`ERC721Enumerable` for enumerable NFT functionality and `Ownable` for owner-only minting).
2. Tracks uniqueness of metadata via a mapping.
3. Limits the total supply of NFTs, enforced during minting.
4. Metadata uniqueness is validated using a public `isMetadataUnique` function.
