"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simpsontrump.pages.dev
Prompt: Write a Solidity contract that allows users to mint AI-generated NFTs related to the Simpson Trump theme.
Generated: DETERMINISTIC_4a76c534de1724d2
Batch ID: 20250612_164304
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

/// @title SimpsonTrumpAI NFT Contract
/// @dev This contract allows users to mint AI-generated NFTs related to the Simpson Trump theme.
/// @author [Your Name]

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract SimpsonTrumpAINFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_SUPPLY = 10000;

    // Minting fee in wei
    uint256 public mintingFee = 0.05 ether;

    // Mapping to store metadata of each token
    mapping(uint256 => string) private _tokenMetadata;

    /// @dev Constructor for the contract.
    /// @param name The name of the NFT collection.
    /// @param symbol The symbol of the NFT collection.
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Allows users to mint a new NFT.
    /// @param metadataURI The URI pointing to the metadata of the NFT.
    function mintNFT(string memory metadataURI) external payable {
        // Check if minting fee is provided
        require(msg.value >= mintingFee, "Insufficient minting fee");

        // Check if maximum supply has been reached
        require(totalSupply() < MAX_SUPPLY, "Maximum supply reached");

        // Increment token ID counter
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the new token
        _safeMint(msg.sender, newTokenId);

        // Store metadata for the newly minted token
        _tokenMetadata[newTokenId] = metadataURI;
    }

    /// @notice Retrieves the metadata URI of a given token ID.
    /// @param tokenId The ID of the token whose metadata URI is to be retrieved.
    /// @return The metadata URI of the token.
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");

        // Return the metadata URI
        return _tokenMetadata[tokenId];
    }

    /// @notice Sets a new minting fee.
    /// @param newFee The new minting fee in wei.
    function setMintingFee(uint256 newFee) external onlyOwner {
        mintingFee = newFee;
    }

    /// @notice Withdraws the contract balance to the owner's address.
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer balance to the owner
        payable(owner()).transfer(balance);
    }
}
```
