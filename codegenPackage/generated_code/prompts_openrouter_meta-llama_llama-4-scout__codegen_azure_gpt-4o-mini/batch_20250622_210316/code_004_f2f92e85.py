"""
Generated Code Metadata:
========================
Original URL: https://degeneratebugs.firebaseapp.com
Prompt: Create a function in Solidity to handle the reveal of Degen Fat Cats NFTs once a certain condition is met.
Generated: DETERMINISTIC_f2f92e85a71590d6
Batch ID: 20250622_210316
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
 * @title DegenFatCats
 * @dev This contract manages the minting and revealing of Degen Fat Cats NFTs.
 */
contract DegenFatCats is ERC721, Ownable {
    // State variables
    uint256 public totalSupply; // Total number of NFTs minted
    uint256 public revealCondition; // Condition to trigger the reveal
    bool public revealed; // Status of the reveal
    string private baseURI; // Base URI for the NFT metadata
    mapping(uint256 => string) private tokenURIs; // Mapping from token ID to token URI

    // Events
    event NFTRevealed(string baseURI);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param _name The name of the NFT collection.
     * @param _symbol The symbol of the NFT collection.
     */
    constructor(string memory _name, string memory _symbol) ERC721(_name, _symbol) {
        totalSupply = 0;
        revealed = false;
    }

    /**
     * @dev Mint a new NFT.
     * @param to The address to receive the minted NFT.
     * @return tokenId The ID of the minted NFT.
     */
    function mint(address to) external onlyOwner returns (uint256 tokenId) {
        require(totalSupply < 10000, "Max supply reached"); // Limit total supply
        tokenId = totalSupply + 1; // Increment token ID
        _mint(to, tokenId); // Mint the NFT
        totalSupply++; // Update total supply
    }

    /**
     * @dev Set the reveal condition.
     * @param _condition The condition to trigger the reveal.
     */
    function setRevealCondition(uint256 _condition) external onlyOwner {
        revealCondition = _condition;
    }

    /**
     * @dev Reveal the NFTs once the condition is met.
     * @param _baseURI The base URI for the NFT metadata.
     */
    function reveal(string memory _baseURI) external onlyOwner {
        require(!revealed, "Already revealed"); // Ensure not already revealed
        require(totalSupply >= revealCondition, "Reveal condition not met"); // Check condition

        baseURI = _baseURI; // Set the base URI
        revealed = true; // Update reveal status
        emit NFTRevealed(baseURI); // Emit reveal event
    }

    /**
     * @dev Override the baseURI function to return the correct URI.
     * @return The base URI for the NFT metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return revealed ? baseURI : ""; // Return base URI if revealed
    }

    /**
     * @dev Set a specific token URI for a given token ID.
     * @param tokenId The ID of the token.
     * @param _tokenURI The URI to set for the token.
     */
    function setTokenURI(uint256 tokenId, string memory _tokenURI) external onlyOwner {
        require(_exists(tokenId), "Token does not exist"); // Ensure token exists
        tokenURIs[tokenId] = _tokenURI; // Set the token URI
    }

    /**
     * @dev Get the token URI for a given token ID.
     * @param tokenId The ID of the token.
     * @return The token URI for the specified token ID.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist"); // Ensure token exists
        return revealed ? tokenURIs[tokenId] : ""; // Return token URI if revealed
    }
}
```
