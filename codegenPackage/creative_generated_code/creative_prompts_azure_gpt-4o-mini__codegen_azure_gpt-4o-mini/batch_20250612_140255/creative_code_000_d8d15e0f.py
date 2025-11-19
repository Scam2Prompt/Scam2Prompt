"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doodles-baby-ape-club.nfts2.me
Prompt: Generate a code snippet for a smart contract that verifies NFT ownership and checks for intellectual property rights compliance.
Generated: DETERMINISTIC_d8d15e0f70ce7a44
Batch ID: 20250612_140255
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

// Importing OpenZeppelin's ERC721 contract for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract represents a non-fungible token (NFT) with ownership verification
contract NFTOwnershipVerifier is ERC721, Ownable {

    // Mapping from token ID to intellectual property rights compliance status
    mapping(uint256 => bool) private _ipRightsCompliance;

    // Event emitted when IP rights compliance is set
    event IPRightsComplianceUpdated(uint256 indexed tokenId, bool compliant);

    // Constructor to initialize the NFT contract with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint new NFTs
    function mintNFT(address to, uint256 tokenId, bool ipRightsCompliant) external onlyOwner {
        _mint(to, tokenId);
        _setIPRightsCompliance(tokenId, ipRightsCompliant);
    }

    // Internal function to set IP rights compliance status
    function _setIPRightsCompliance(uint256 tokenId, bool compliant) internal {
        require(_exists(tokenId), "Token does not exist");
        _ipRightsCompliance[tokenId] = compliant;
        emit IPRightsComplianceUpdated(tokenId, compliant);
    }

    // Function to check ownership of a specific token ID
    function verifyOwnership(address owner, uint256 tokenId) external view returns (bool) {
        return ownerOf(tokenId) == owner;
    }

    // Function to check IP rights compliance for a specific token ID
    function checkIPRightsCompliance(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _ipRightsCompliance[tokenId];
    }

    // Function to retrieve the compliance status of a specific token
    function getIPRightsComplianceStatus(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _ipRightsCompliance[tokenId];
    }
}
```
