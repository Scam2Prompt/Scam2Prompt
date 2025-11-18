"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftnovamarket.com
Prompt: Create a smart contract in Solidity for minting NFTs that aligns with Nftnovamarket's roadmap phase 04, ensuring blockchain verification and secure ownership.
Generated: DETERMINISTIC_39541482c18115b0
Batch ID: 20250612_151626
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
 * @title NFTNovaMarketPhase04
 * @dev A smart contract for minting NFTs, ensuring secure ownership and blockchain verification.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTNovaMarketPhase04 is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _currentTokenId;

    // Mapping to track already minted URIs to prevent duplicates
    mapping(string => bool) private _mintedURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId, string tokenURI);

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name Name of the NFT collection
     * @param symbol Symbol of the NFT collection
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT.
     * @param to Address to receive the NFT
     * @param tokenURI URI pointing to the metadata of the NFT
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        // Validate input parameters
        require(to != address(0), "Invalid address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");
        require(!_mintedURIs[tokenURI], "Duplicate token URI is not allowed");

        // Increment the token ID for the next NFT
        _currentTokenId++;

        // Mint the NFT and set its metadata URI
        _safeMint(to, _currentTokenId);
        _setTokenURI(_currentTokenId, tokenURI);

        // Mark the URI as minted to prevent duplicates
        _mintedURIs[tokenURI] = true;

        // Emit the NFTMinted event
        emit NFTMinted(to, _currentTokenId, tokenURI);
    }

    /**
     * @dev Function to get the current token ID.
     * @return The current token ID
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    /**
     * @dev Function to check if a token URI has already been minted.
     * @param tokenURI The token URI to check
     * @return True if the URI has been minted, false otherwise
     */
    function isURIMinted(string memory tokenURI) external view returns (bool) {
        return _mintedURIs[tokenURI];
    }
}
```
