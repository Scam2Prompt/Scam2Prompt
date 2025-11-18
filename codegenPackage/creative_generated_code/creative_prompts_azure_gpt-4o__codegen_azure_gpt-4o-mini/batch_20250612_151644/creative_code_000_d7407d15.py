"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerobeings.app
Prompt: Write a smart contract in Solidity that mimics the functionality of the "Zero Beings" verified contract, ensuring compatibility with OpenSea.
Generated: DETERMINISTIC_d7407d153a605cb4
Batch ID: 20250612_151644
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

// Import OpenZeppelin's ERC721 implementation for safe and secure minting
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title ZeroBeingsNFT
/// @author Your Name
/// @notice This contract allows for minting and managing Zero Beings NFTs
contract ZeroBeingsNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event TokenMinted(uint256 indexed tokenId, address owner);

    /// @param name Name of the NFT collection
    /// @param symbol Symbol of the NFT collection
    /// @param baseTokenURI Initial base URI for token metadata
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /// @notice Mint a new NFT
    /// @param to The address to receive the minted NFT
    /// @return tokenId The ID of the minted token
    function mint(address to) external onlyOwner returns (uint256 tokenId) {
        require(to != address(0), "Cannot mint to the zero address");

        // Increment the counter and get the new token ID
        tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the token to the recipient
        _mint(to, tokenId);
        
        // Emit the minting event
        emit TokenMinted(tokenId, to);
    }

    /// @notice Set the base URI for the token metadata
    /// @param baseTokenURI New base URI for metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /// @notice Override the base URI function for OpenSea compatibility
    /// @return string The base URI for token metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Retrieve the total number of minted tokens
    /// @return uint256 The total number of minted tokens
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /// @notice Ensure that NFTs are transferred safely
    /// @dev Override to prevent accidental transfers to the zero address
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        require(to != address(0), "Transfer to the zero address is not allowed");
    }
}
```
