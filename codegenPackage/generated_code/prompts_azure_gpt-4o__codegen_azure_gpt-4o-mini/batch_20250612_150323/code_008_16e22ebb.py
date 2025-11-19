"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Write a function in Solidity to verify NFT ownership and display metadata, inspired by CryptoTitties' verification on OpenSea.
Generated: DETERMINISTIC_16e22ebb20e8e5f2
Batch ID: 20250612_150323
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

// Importing the ERC721 interface for NFT standard
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract NFTVerifier {
    // Using the Strings library for string manipulation
    using Strings for uint256;

    // Event to emit when NFT ownership is verified
    event OwnershipVerified(address indexed owner, uint256 tokenId, string metadata);

    // Function to verify NFT ownership and retrieve metadata
    function verifyOwnershipAndGetMetadata(
        address nftContractAddress,
        uint256 tokenId,
        address owner
    ) external view returns (string memory) {
        // Check if the provided NFT contract address is a valid contract
        require(nftContractAddress != address(0), "Invalid NFT contract address");

        // Create an instance of the ERC721 contract
        IERC721 nftContract = IERC721(nftContractAddress);

        // Verify ownership of the NFT
        address tokenOwner = nftContract.ownerOf(tokenId);
        require(tokenOwner == owner, "You do not own this NFT");

        // Retrieve metadata URI from the NFT contract
        string memory metadataURI = nftContract.tokenURI(tokenId);
        require(bytes(metadataURI).length > 0, "Metadata not found");

        // Emit event for successful verification
        emit OwnershipVerified(owner, tokenId, metadataURI);

        // Return the metadata URI
        return metadataURI;
    }
}
```
