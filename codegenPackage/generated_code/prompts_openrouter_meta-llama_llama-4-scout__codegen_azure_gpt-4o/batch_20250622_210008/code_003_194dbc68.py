"""
Generated Code Metadata:
========================
Original URL: https://molly-a5h.pages.dev
Prompt: Design a simple smart contract using Solidity to create and manage NFTs on the Molly platform, including functions for minting and transferring NFTs.
Generated: DETERMINISTIC_194dbc68f16be6c1
Batch ID: 20250622_210008
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
 * @title MollyNFT
 * @dev A simple smart contract for creating and managing NFTs on the Molly platform.
 * Implements ERC721 standard for NFTs.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MollyNFT is ERC721, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Mapping to store metadata URIs for each token
    mapping(uint256 => string) private _tokenURIs;

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT.
     * @param to Address to receive the minted NFT.
     * @param tokenURI URI pointing to the metadata of the NFT.
     * Requirements:
     * - Only the owner of the contract can call this function.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);
    }

    /**
     * @dev Function to transfer an NFT from one address to another.
     * @param from Address sending the NFT.
     * @param to Address receiving the NFT.
     * @param tokenId ID of the NFT to transfer.
     * Requirements:
     * - The caller must be approved or the owner of the NFT.
     */
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(to != address(0), "Invalid address");
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Transfer the NFT
        _transfer(from, to, tokenId);
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
     * @dev Function to get the token URI for a given token ID.
     * @param tokenId ID of the token.
     * @return Token URI as a string.
     * Requirements:
     * - The token must exist.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }
}
```
