"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safedao.pages.dev
Prompt: Explain how to use Safe{Core} to build a secure NFT collective platform with multi-sig functionality, and provide example code.
Generated: DETERMINISTIC_251ef4aea24cd468
Batch ID: 20250612_151947
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

import "@gnosis.pm/safe-contracts/contracts/GnosisSafe.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

// NFTCollective is a smart contract that represents a collective of NFTs
// It supports multi-signature functionality using Gnosis Safe
contract NFTCollective is ERC721 {
    // State variable to store the Gnosis Safe contract address
    GnosisSafe public gnosisSafe;

    // Mapping to store the NFT metadata
    mapping(uint256 => string) private _tokenMetadata;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 tokenId, string metadata);

    // Modifier to ensure only the Gnosis Safe can call certain functions
    modifier onlySafe() {
        require(msg.sender == address(gnosisSafe), "Caller is not the Gnosis Safe");
        _;
    }

    // Constructor to initialize the contract
    constructor(string memory name, string memory symbol, address _gnosisSafe) 
        ERC721(name, symbol) 
    {
        require(_gnosisSafe != address(0), "Invalid Gnosis Safe address");
        gnosisSafe = GnosisSafe(_gnosisSafe);
    }

    // Function to mint a new NFT
    function mintNFT(string memory metadata) external onlySafe {
        uint256 tokenId = totalSupply(); // Unique token ID
        _mint(address(this), tokenId); // Mint NFT to the contract itself
        _tokenMetadata[tokenId] = metadata; // Store metadata
        emit NFTCreated(tokenId, metadata); // Emit event
    }

    // Function to retrieve NFT metadata
    function getNFTMetadata(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "NFT does not exist");
        return _tokenMetadata[tokenId];
    }

    // Function to transfer an NFT from this contract to a different address
    function transferNFT(address to, uint256 tokenId) external onlySafe {
        require(_exists(tokenId), "NFT does not exist");
        require(to != address(0), "Invalid address");
        safeTransferFrom(address(this), to, tokenId); // Transfer the NFT
    }

    // Internal function to get the total supply of NFTs
    function totalSupply() internal view returns (uint256) {
        return _tokenIds.current(); // Use OpenZeppelin's Counters for tracking
    }
}
```

**Note:**
- Ensure you have the appropriate libraries installed (Gnosis Safe and OpenZeppelin).
- This code assumes you have already set up the Gnosis Safe and its address is passed during the contract initialization. 
- The contract provides basic functionality for creating and transferring NFTs while ensuring that operations are controlled via the Gnosis Safe.
