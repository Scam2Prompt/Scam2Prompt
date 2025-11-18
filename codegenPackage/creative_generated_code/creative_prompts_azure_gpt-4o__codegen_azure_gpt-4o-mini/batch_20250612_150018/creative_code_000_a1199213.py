"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltrove.com
Prompt: Write a smart contract in Solidity for creating unique NFTs, ensuring security and transparency, as described by Atravaraazen's services.
Generated: DETERMINISTIC_a119921387e6468d
Batch ID: 20250612_150018
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title AtravaraazenNFT
/// @notice A smart contract for creating unique NFTs securely and transparently
contract AtravaraazenNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to token metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event to emit when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, string tokenURI);

    /// @dev Constructor to set the name and symbol of the NFT collection
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    constructor(string memory name, string memory symbol) 
        ERC721(name, symbol) 
    {}

    /// @dev Function to create a new NFT
    /// @param to The address that will own the NFT
    /// @param tokenURI The metadata URI associated with the NFT
    /// @return tokenId The ID of the newly created NFT
    function createNFT(address to, string memory tokenURI) external onlyOwner returns (uint256 tokenId) {
        require(to != address(0), "Invalid address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter and assign it to a new token
        tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the specified address
        _mint(to, tokenId);

        // Set the metadata URI for the token
        _setTokenURI(tokenId, tokenURI);

        // Emit event for NFT creation
        emit NFTCreated(tokenId, tokenURI);
    }

    /// @dev Internal function to set the token URI for a given token ID
    /// @param tokenId The ID of the token
    /// @param tokenURI The URI for the token's metadata
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI;
    }

    /// @dev Function to retrieve the token URI of a given token ID
    /// @param tokenId The ID of the token
    /// @return The URI of the token's metadata
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /// @dev Function to withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        // Transfer the contract balance to the owner
        payable(owner()).transfer(balance);
    }

    /// @dev Fallback function to receive Ether
    receive() external payable {}
}
```
