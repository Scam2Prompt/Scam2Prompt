"""
Generated Code Metadata:
========================
Original URL: https://randomarts.netlify.app
Prompt: Design a simple smart contract in Solidity for a free minting event of 5000 digital art pieces with a limited supply.
Generated: DETERMINISTIC_7339a2223a093625
Batch ID: 20250622_204703
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title FreeMintingArt
 * @dev A simple ERC721 smart contract for a free minting event of digital art pieces.
 * The contract allows users to mint a limited supply of 5000 unique digital art pieces.
 */
contract FreeMintingArt is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the number of minted tokens
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of digital art pieces
    uint256 public constant MAX_SUPPLY = 5000;

    // Mapping to track if an address has already minted
    mapping(address => bool) public hasMinted;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed owner, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     */
    constructor() ERC721("FreeMintingArt", "FMA") {}

    /**
     * @dev Function to mint a new digital art piece.
     * Can only be called if the maximum supply has not been reached and the caller has not minted before.
     */
    function mint() external {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        require(!hasMinted[msg.sender], "You have already minted a token");

        // Increment the token ID counter and mint the new token
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        hasMinted[msg.sender] = true;

        // Mint the token to the caller's address
        _safeMint(msg.sender, tokenId);

        // Emit the token minted event
        emit TokenMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function to get the total number of minted tokens.
     * @return The total number of minted tokens.
     */
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Function to withdraw any Ether from the contract (if applicable).
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
