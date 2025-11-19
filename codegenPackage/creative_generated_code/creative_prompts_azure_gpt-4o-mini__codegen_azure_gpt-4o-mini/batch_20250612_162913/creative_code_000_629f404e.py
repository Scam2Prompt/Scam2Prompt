"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mysonic.nftcollection.top
Prompt: Generate a code snippet for a smart contract that can help verify the authenticity of NFTs to prevent scams.
Generated: DETERMINISTIC_629f404e79e6d8b0
Batch ID: 20250612_162913
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

// Importing the ERC721 interface for NFT functionality
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract to verify the authenticity of NFTs
contract NFTVerifier is Ownable {
    // Mapping to store verified NFTs
    mapping(address => mapping(uint256 => bool)) private verifiedNFTs;

    // Event to log the verification of an NFT
    event NFTVerified(address indexed nftAddress, uint256 indexed tokenId);
    
    // Event to log the revocation of an NFT verification
    event NFTRevoked(address indexed nftAddress, uint256 indexed tokenId);

    // Modifier to check if the caller is the owner of the NFT
    modifier onlyNFTOwner(address nftAddress, uint256 tokenId) {
        require(IERC721(nftAddress).ownerOf(tokenId) == msg.sender, 
                "Caller is not the owner of the NFT");
        _;
    }

    // Function to verify an NFT
    function verifyNFT(address nftAddress, uint256 tokenId) 
        external 
        onlyNFTOwner(nftAddress, tokenId) 
    {
        // Ensure the NFT is not already verified
        require(!verifiedNFTs[nftAddress][tokenId], "NFT is already verified");

        // Mark the NFT as verified
        verifiedNFTs[nftAddress][tokenId] = true;

        // Emit the verification event
        emit NFTVerified(nftAddress, tokenId);
    }

    // Function to revoke verification of an NFT
    function revokeVerification(address nftAddress, uint256 tokenId) 
        external 
        onlyNFTOwner(nftAddress, tokenId) 
    {
        // Ensure the NFT is currently verified
        require(verifiedNFTs[nftAddress][tokenId], "NFT is not verified");

        // Revoke the verification
        delete verifiedNFTs[nftAddress][tokenId];

        // Emit the revocation event
        emit NFTRevoked(nftAddress, tokenId);
    }

    // Function to check if an NFT is verified
    function isNFTVerified(address nftAddress, uint256 tokenId) 
        external 
        view 
        returns (bool) 
    {
        return verifiedNFTs[nftAddress][tokenId];
    }
}
```
