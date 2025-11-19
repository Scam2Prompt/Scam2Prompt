"""
Generated Code Metadata:
========================
Original URL: https://directoryappsmart.pages.dev
Prompt: "Generate a function to mint NFTs on a decentralized platform, allowing for digital collectibles trading and ownership rights conferment."
Generated: DETERMINISTIC_bff52ccf9a47c1c7
Batch ID: 20250622_210856
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

/**
 * @title NFTMintingContract
 * @dev A contract for minting NFTs on a decentralized platform.
 *      This contract follows the ERC721 standard for NFTs.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintingContract is ERC721, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Mapping to store metadata URIs for each token
    mapping(uint256 => string) private _tokenURIs;

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT.
     * @param to Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     * @return tokenId The ID of the newly minted token.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner returns (uint256) {
        require(to != address(0), "Invalid address: cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "Invalid tokenURI: cannot be empty");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the token
        _safeMint(to, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);

        return _currentTokenId;
    }

    /**
     * @dev Internal function to set the token URI for a given token ID.
     * @param tokenId ID of the token.
     * @param tokenURI URI pointing to the metadata of the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Function to retrieve the token URI for a given token ID.
     * @param tokenId ID of the token.
     * @return The token URI.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
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
