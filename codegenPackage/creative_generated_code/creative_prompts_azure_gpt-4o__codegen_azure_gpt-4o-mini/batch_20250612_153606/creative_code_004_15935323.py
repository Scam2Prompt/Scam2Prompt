"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gofurs-cash.pages.dev
Prompt: Write a Solidity function that checks whether a wallet address holds a GOFURS NFT and returns the NFT metadata. Use the ERC404 token standard as the basis for the implementation.
Generated: DETERMINISTIC_15935323c0eb743f
Batch ID: 20250612_153606
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

// Interface for the ERC404 token standard
interface IERC404 {
    function ownerOf(uint256 tokenId) external view returns (address owner);
    function getMetadata(uint256 tokenId) external view returns (string memory);
}

contract GOFURSNFTChecker {
    // Address of the GOFURS NFT contract
    address public gofursNFTAddress;

    // Event emitted when a wallet address checks for an NFT
    event NFTChecked(address indexed wallet, uint256 tokenId, string metadata);

    // Constructor to set the GOFURS NFT contract address
    constructor(address _gofursNFTAddress) {
        require(_gofursNFTAddress != address(0), "Invalid contract address");
        gofursNFTAddress = _gofursNFTAddress;
    }

    /**
     * @dev Checks if a wallet address holds a GOFURS NFT and returns its metadata.
     * @param wallet The address of the wallet to check.
     * @param tokenId The ID of the NFT to check.
     * @return metadata The metadata of the NFT if the wallet holds it, otherwise an empty string.
     */
    function checkNFT(address wallet, uint256 tokenId) external returns (string memory metadata) {
        require(wallet != address(0), "Invalid wallet address");

        // Retrieve the owner of the token
        address owner = IERC404(gofursNFTAddress).ownerOf(tokenId);

        // Check if the wallet is the owner of the NFT
        if (owner == wallet) {
            // Retrieve the metadata for the NFT
            metadata = IERC404(gofursNFTAddress).getMetadata(tokenId);
            emit NFTChecked(wallet, tokenId, metadata);
        } else {
            // Return empty string if the wallet does not own the NFT
            metadata = "";
        }
    }
}
```
