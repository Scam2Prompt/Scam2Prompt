"""
Generated Code Metadata:
========================
Original URL: https://bzreards.top
Prompt: Write a code snippet using ERC721A to create a decentralized anime NFT collection inspired by Azuki's interactive lore.
Generated: DETERMINISTIC_81b3506ad8298794
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

// Import ERC721A from Chiru Labs
import "erc721a/contracts/ERC721A.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title AnimeNFTCollection
/// @dev A decentralized anime NFT collection inspired by Azuki's interactive lore.
contract AnimeNFTCollection is ERC721A, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Base URI for metadata
    string private baseTokenURI;

    // Mint price per NFT
    uint256 public mintPrice = 0.05 ether;

    // Maximum number of NFTs per transaction
    uint256 public maxPerTx = 5;

    // Tracks whether minting is active
    bool public mintingActive = false;

    /// @notice Constructor to initialize the NFT collection
    /// @param _name Name of the NFT collection
    /// @param _symbol Symbol of the NFT collection
    constructor(string memory _name, string memory _symbol) ERC721A(_name, _symbol) {}

    /// @notice Mint NFTs
    /// @param quantity Number of NFTs to mint
    function mint(uint256 quantity) external payable {
        require(mintingActive, "Minting is not active");
        require(quantity > 0 && quantity <= maxPerTx, "Invalid mint quantity");
        require(totalSupply() + quantity <= MAX_SUPPLY, "Exceeds maximum supply");
        require(msg.value >= mintPrice * quantity, "Insufficient payment");

        _safeMint(msg.sender, quantity);
    }

    /// @notice Set the base URI for metadata
    /// @param _baseTokenURI The new base URI
    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /// @notice Toggle minting state
    function toggleMinting() external onlyOwner {
        mintingActive = !mintingActive;
    }

    /// @notice Set the mint price
    /// @param _mintPrice The new mint price
    function setMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }

    /// @notice Set the maximum number of NFTs per transaction
    /// @param _maxPerTx The new maximum per transaction
    function setMaxPerTx(uint256 _maxPerTx) external onlyOwner {
        maxPerTx = _maxPerTx;
    }

    /// @notice Withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /// @dev Override _baseURI to return the baseTokenURI
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }
}
```

This code snippet creates a decentralized anime NFT collection using the ERC721A standard. It includes features such as minting, metadata management, and owner controls, following best practices for Solidity development.
