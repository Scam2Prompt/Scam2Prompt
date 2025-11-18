"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meowworldsnft.pages.dev
Prompt: Create a Solidity smart contract for minting Meow Worlds NFTs, ensuring the total supply is capped at 10,000 and includes metadata for characters, environments, and artifacts.
Generated: DETERMINISTIC_4f8f64332dcc932b
Batch ID: 20250612_150919
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MeowWorldsNFT is ERC721URIStorage, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Counter for token IDs
    uint256 private _currentTokenId;

    // Metadata structure for Meow Worlds NFTs
    struct Metadata {
        string character; // Character info
        string environment; // Environment description
        string artifact; // Artifact details
    }

    // Mapping from token ID to metadata
    mapping(uint256 => Metadata) private _tokenMetadata;

    // Event emitted after a new NFT is minted
    event MeowWorldMinted(
        address indexed owner,
        uint256 indexed tokenId,
        string character,
        string environment,
        string artifact
    );

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("MeowWorldsNFT", "MEOW") {}

    /**
     * @dev Mint a new NFT with metadata.
     * @param to Address to mint the NFT to.
     * @param character Character metadata.
     * @param environment Environment metadata.
     * @param artifact Artifact metadata.
     * @param tokenURI URI pointing to the NFT's metadata (IPFS, etc.).
     */
    function mintNFT(
        address to,
        string memory character,
        string memory environment,
        string memory artifact,
        string memory tokenURI
    ) external onlyOwner {
        // Ensure the total supply cap is not breached
        require(_currentTokenId < MAX_SUPPLY, "Max supply reached");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the new token
        _safeMint(to, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Save the metadata
        _tokenMetadata[_currentTokenId] = Metadata(character, environment, artifact);

        // Emit the minting event
        emit MeowWorldMinted(to, _currentTokenId, character, environment, artifact);
    }

    /**
     * @dev Get metadata for a specific token ID.
     * @param tokenId The ID of the token to query.
     * @return Metadata structure containing character, environment, and artifact details.
     */
    function getMetadata(uint256 tokenId) external view returns (Metadata memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Query for nonexistent token");

        // Return the metadata
        return _tokenMetadata[tokenId];
    }

    /**
     * @dev Get the current total supply of minted tokens.
     * @return The current total supply.
     */
    function totalSupply() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Override the supportsInterface function to support ERC721.
     * @param interfaceId The identifier of the interface.
     * @return Boolean indicating whether the interface is supported.
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        virtual
        override(ERC721)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
