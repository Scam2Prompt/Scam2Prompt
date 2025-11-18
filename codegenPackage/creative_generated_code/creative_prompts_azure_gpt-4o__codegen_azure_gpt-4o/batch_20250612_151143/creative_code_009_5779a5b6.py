"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clonesx.pages.dev
Prompt: Develop a blockchain-based system for tracking and verifying ownership of RTFKT x Nike Dunk Genesis NFTs.
Generated: DETERMINISTIC_5779a5b637666dc1
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a simplified blockchain-based system to track and verify ownership of RTFKT x Nike Dunk Genesis NFTs using the Ethereum blockchain (via Solidity). 

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title NFT Ownership Tracking & Verification Contract
/// @author [Your Name]
/// @notice This contract allows tracking and verifying ownership of RTFKT x Nike Dunk Genesis NFTs.
/// @dev ERC721 standard is used for NFT implementation.

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RTFKTNikeDunkGenesisNFT is ERC721Enumerable, Ownable {
    // State variable to hold the base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event Minted(uint256 tokenId, address owner);

    /// @notice Constructor to set up the NFT collection
    /// @param name Name of the NFT collection
    /// @param symbol Symbol of the NFT collection
    /// @param baseURI Base URI for metadata
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /// @notice Function to mint a new NFT
    /// @dev Only the owner of the contract can call this function
    /// @param to Address to receive the minted NFT
    /// @param tokenId Unique ID of the NFT to be minted
    function mint(address to, uint256 tokenId) external onlyOwner {
        require(!_exists(tokenId), "Token already exists"); // Ensure token doesn't already exist
        _safeMint(to, tokenId); // Mint the NFT safely
        emit Minted(tokenId, to); // Emit the Minted event
    }

    /// @notice Override to set the base URI for metadata
    /// @return Base URI of the NFT metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Function to update the base URI for the metadata
    /// @dev Only the owner of the contract can call this function
    /// @param baseURI New base URI for the metadata
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @notice Verify ownership of a given token ID
    /// @param tokenId ID of the token to verify ownership
    /// @return Owner address of the given token ID
    function verifyOwnership(uint256 tokenId) external view returns (address) {
        require(_exists(tokenId), "Token does not exist"); // Ensure the token exists
        return ownerOf(tokenId); // Return the owner of the token
    }

    /// @notice Function to withdraw Ether from the contract
    /// @dev Only the owner of the contract can call this function
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get the contract's Ether balance
        require(balance > 0, "No Ether to withdraw"); // Ensure there's Ether to withdraw
        payable(owner()).transfer(balance); // Transfer the balance to the owner
    }

    /// @notice Fallback function to receive Ether
    receive() external payable {}

    /// @notice Fallback function for non-standard calls
    fallback() external payable {}
}
```

### Key Features:
- Uses the OpenZeppelin library for ERC721 implementation, Enumerable extension, and access control (`Ownable`).
- Allows the contract owner to mint NFTs, set metadata base URI, and verify ownership.
- Includes proper error handling (`require` statements) and uses events for transparency.
- Implements a `withdraw` function for managing Ether sent to the contract.

Before deploying to a live environment, ensure to replace `[Your Name]` with your name or organization and set appropriate initial values for `name`, `symbol`, and `baseURI`.
