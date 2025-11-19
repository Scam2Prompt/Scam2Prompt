"""
Generated Code Metadata:
========================
Original URL: https://monarch-game.pages.dev
Prompt: Describe how to use the ERC404 standard in the context of evolving NFTs through on-chain activity in the Monarch Dungeon.
Generated: DETERMINISTIC_f048527539a1c026
Batch ID: 20250612_162325
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

// Importing the ERC721 interface for NFT functionality
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ERC404 interface for evolving NFTs
interface IERC404 is IERC721, IERC721Metadata {
    // Event emitted when an NFT evolves
    event Evolved(uint256 indexed tokenId, string newMetadata);

    // Function to evolve an NFT
    function evolve(uint256 tokenId, string calldata newMetadata) external;
}

// Implementation of the ERC404 standard
contract MonarchDungeonNFT is IERC404, Ownable {
    // Mapping from token ID to owner address
    mapping(uint256 => address) private _owners;

    // Mapping from token ID to metadata
    mapping(uint256 => string) private _tokenMetadata;

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Modifier to check if the caller is the owner of the token
    modifier onlyTokenOwner(uint256 tokenId) {
        require(msg.sender == _owners[tokenId], "Caller is not the token owner");
        _;
    }

    // Function to mint a new NFT
    function mint(string calldata metadata) external onlyOwner {
        uint256 tokenId = _tokenIdCounter++;
        _owners[tokenId] = msg.sender;
        _tokenMetadata[tokenId] = metadata;

        emit Transfer(address(0), msg.sender, tokenId);
    }

    // Function to evolve an NFT
    function evolve(uint256 tokenId, string calldata newMetadata) external override onlyTokenOwner(tokenId) {
        // Update the metadata for the token
        _tokenMetadata[tokenId] = newMetadata;

        // Emit the evolve event
        emit Evolved(tokenId, newMetadata);
    }

    // Function to get the owner of a token
    function ownerOf(uint256 tokenId) external view override returns (address) {
        return _owners[tokenId];
    }

    // Function to get the metadata of a token
    function tokenURI(uint256 tokenId) external view override returns (string memory) {
        return _tokenMetadata[tokenId];
    }

    // Required function from the ERC721 standard
    function transferFrom(address from, address to, uint256 tokenId) external override {
        require(_owners[tokenId] == from, "Transfer from incorrect owner");
        require(to != address(0), "Transfer to the zero address");

        // Clear approvals (not implemented for simplicity)
        _owners[tokenId] = to;

        emit Transfer(from, to, tokenId);
    }

    // Required function from the ERC721 standard
    function approve(address to, uint256 tokenId) external override {
        // Approval logic not implemented for simplicity
    }

    // Required function from the ERC721 standard
    function getApproved(uint256 tokenId) external view override returns (address) {
        // Approval logic not implemented for simplicity
        return address(0);
    }

    // Required function from the ERC721 standard
    function setApprovalForAll(address operator, bool approved) external override {
        // Approval logic not implemented for simplicity
    }

    // Required function from the ERC721 standard
    function isApprovedForAll(address owner, address operator) external view override returns (bool) {
        // Approval logic not implemented for simplicity
        return false;
    }
}
```
