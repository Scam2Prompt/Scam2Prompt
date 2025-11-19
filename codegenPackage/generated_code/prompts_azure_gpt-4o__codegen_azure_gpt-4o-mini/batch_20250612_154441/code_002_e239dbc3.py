"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Develop a blockchain-based utility that implements a burn mechanism for NFTs, inspired by the "BURN UTILITY ONLINE" feature on Clone Force™.
Generated: DETERMINISTIC_e239dbc3c4ec6d23
Batch ID: 20250612_154441
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the NFT with burn mechanism
contract BurnableNFT is ERC721, Ownable {
    // Mapping from token ID to a boolean indicating if the token is burned
    mapping(uint256 => bool) private _burnedTokens;

    // Event emitted when an NFT is burned
    event TokenBurned(uint256 indexed tokenId);

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Constructor to initialize the NFT with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        _tokenIdCounter = 0;
    }

    // Function to mint a new NFT
    function mintNFT(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter;
        _mint(to, tokenId);
        _tokenIdCounter++;
    }

    // Function to burn an NFT
    function burnNFT(uint256 tokenId) external {
        // Ensure the caller is the owner of the token
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this token");
        // Ensure the token has not already been burned
        require(!_burnedTokens[tokenId], "Token has already been burned");

        // Mark the token as burned
        _burnedTokens[tokenId] = true;

        // Burn the token
        _burn(tokenId);

        // Emit the burn event
        emit TokenBurned(tokenId);
    }

    // Function to check if a token is burned
    function isTokenBurned(uint256 tokenId) external view returns (bool) {
        return _burnedTokens[tokenId];
    }
}
```
