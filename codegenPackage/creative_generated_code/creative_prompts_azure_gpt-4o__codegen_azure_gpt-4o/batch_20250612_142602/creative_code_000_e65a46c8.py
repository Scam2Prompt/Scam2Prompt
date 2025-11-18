"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suipad.web3-mint.pro
Prompt: Write a smart contract in Solidity for minting NFTs, referencing Web3 minting processes similar to those described on web3-mint.pro.
Generated: DETERMINISTIC_e65a46c869dc2f63
Batch ID: 20250612_142602
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

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title NFTMintingContract
/// @dev This contract allows the owner to mint NFTs and assign metadata URIs.
contract NFTMintingContract is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    /// @notice Constructor initializes the ERC721 token name and symbol.
    /// @param name The name of the NFT collection.
    /// @param symbol The symbol of the NFT collection.
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Mint a new NFT to the specified address.
    /// @param recipient The address that will receive the minted NFT.
    /// @param tokenURI The metadata URI for the NFT.
    /// @return The token ID of the newly minted NFT.
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner returns (uint256) {
        // Increment the current token ID
        _currentTokenId++;

        // Mint the NFT to the recipient
        _mint(recipient, _currentTokenId);

        // Set the metadata URI for the token
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit an event for the minting process (optional, can be added later)

        // Return the token ID
        return _currentTokenId;
    }

    /// @notice Retrieve the current token ID counter.
    /// @return The current token ID.
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
