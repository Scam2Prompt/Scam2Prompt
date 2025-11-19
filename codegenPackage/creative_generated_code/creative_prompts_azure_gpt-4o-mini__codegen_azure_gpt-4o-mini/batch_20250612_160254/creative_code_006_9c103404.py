"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teacoindappclaim.pages.dev
Prompt: Develop a code example for a DApp that addresses issues related to NFTs minting and transfer, as specified on the Teacoind DApp Claim website.
Generated: DETERMINISTIC_9c103404e1d7cb95
Batch ID: 20250612_160254
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

// Importing the ERC721 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTContract is a smart contract that implements an ERC721 Non-Fungible Token (NFT)
contract NFTContract is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter; // Using Counters for unique token IDs
    Counters.Counter private _tokenIdCounter; // Counter for tracking token IDs

    // Mapping from token ID to a boolean indicating if the token is minted
    mapping(uint256 => bool) private _mintedTokens;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("TeacoindNFT", "TCNFT") {}

    // Function to mint a new NFT
    // Requires the caller to be the owner of the contract
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get the current token ID
        require(!_mintedTokens[tokenId], "Token already minted"); // Ensure the token has not been minted

        // Mint the NFT to the caller
        _mint(msg.sender, tokenId);
        _mintedTokens[tokenId] = true; // Mark the token as minted
        _tokenIdCounter.increment(); // Increment the token ID counter

        emit NFTMinted(msg.sender, tokenId); // Emit the NFTMinted event
    }

    // Function to transfer ownership of an NFT
    // Requires that the caller is the owner of the token
    function transferNFT(address to, uint256 tokenId) external {
        // Ensure the sender is the owner of the token
        require(ownerOf(tokenId) == msg.sender, "Caller is not the token owner");
        // Transfer the token to the new owner
        _transfer(msg.sender, to, tokenId);
    }

    // Function to retrieve the total number of minted NFTs
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current(); // Return the current value of the token ID counter
    }

    // Function to check if a token ID has been minted
    function isMinted(uint256 tokenId) external view returns (bool) {
        return _mintedTokens[tokenId]; // Return the minted status of the token
    }
}
```

This smart contract allows minting and transferring of NFTs on the Ethereum network. It includes proper error handling, emits events, and follows best practices for development.
