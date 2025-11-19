"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-ca.web.app
Prompt: Write a smart contract in Solidity to create and manage Player Card NFTs on the Mpeppe platform, ensuring a maximum supply of 420 NFTs.
Generated: DETERMINISTIC_f8ee55b35f5ffdbd
Batch ID: 20250622_205006
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

/// @title Player Card NFT Smart Contract for Mpeppe Platform
/// @dev This contract allows minting and managing Player Card NFTs with a maximum supply of 420.
contract PlayerCardNFT is ERC721Enumerable, Ownable {
    // Maximum supply of Player Card NFTs
    uint256 public constant MAX_SUPPLY = 420;

    // Base URI for metadata
    string private _baseTokenURI;

    /// @notice Constructor to initialize the contract
    /// @param name Name of the NFT collection
    /// @param symbol Symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /// @notice Mint a new Player Card NFT
    /// @dev Only the owner can mint NFTs. Ensures the total supply does not exceed MAX_SUPPLY.
    /// @param to Address to receive the minted NFT
    function mint(address to) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        uint256 tokenId = totalSupply() + 1; // Token IDs start from 1
        _safeMint(to, tokenId);
    }

    /// @notice Set the base URI for metadata
    /// @dev Only the owner can set the base URI.
    /// @param baseURI The new base URI
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /// @notice Override the base URI function from ERC721
    /// @return The base URI for metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Withdraw contract balance to the owner's address
    /// @dev Only the owner can withdraw funds.
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /// @notice Fallback function to accept Ether
    /// @dev Allows the contract to receive Ether.
    receive() external payable {}

    fallback() external payable {}
}
```

### Notes:
- This contract uses OpenZeppelin's `ERC721Enumerable` for NFT functionality and `Ownable` for access control.
- The `mint` function ensures the total supply does not exceed the maximum limit of 420.
- The `setBaseURI` function allows the owner to set the base URI for metadata.
- Proper error handling is included for minting and withdrawing funds.
- The contract includes fallback and receive functions to accept Ether.
