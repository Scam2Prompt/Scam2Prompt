"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://primeart.org
Prompt: Recommend a method to programmatically mint NFTs on Prime Art using blockchain integration, and provide an example implementation in Solidity.
Generated: DETERMINISTIC_55424f1f4911b865
Batch ID: 20250612_153821
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
 * @title NFTMintingContract
 * @dev A smart contract for minting NFTs on Prime Art using ERC-721 standards.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintingContract is ERC721, Ownable {
    // Maintain a counter for token IDs
    uint256 private _currentTokenId;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    // Mapping to store token URIs
    mapping(uint256 => string) private _tokenURIs;

    /**
     * @dev Constructor to initialize the NFT contract with a name and symbol.
     * @param name Name of the NFT collection (e.g., "PrimeArtNFT").
     * @param symbol Symbol of the NFT collection (e.g., "ART").
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT.
     * @param to Address of the recipient.
     * @param tokenURI Metadata URI for the NFT.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner returns (uint256 tokenId) {
        // Increment the token ID counter
        _currentTokenId++;

        // Assign the new token ID
        tokenId = _currentTokenId;

        // Mint the NFT and assign it to the recipient
        _mint(to, tokenId);

        // Store the token URI
        _setTokenURI(tokenId, tokenURI);

        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId, tokenURI);
    }

    /**
     * @dev Internal function to set the token URI for a specific token ID.
     * @param tokenId The ID of the token.
     * @param tokenURI Metadata URI for the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Error: URI set for nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Public function to retrieve the token URI for a specific token ID.
     * @param tokenId The ID of the token.
     * @return The token URI.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Error: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Function to retrieve the current token ID counter.
     * @return The current token ID counter.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
