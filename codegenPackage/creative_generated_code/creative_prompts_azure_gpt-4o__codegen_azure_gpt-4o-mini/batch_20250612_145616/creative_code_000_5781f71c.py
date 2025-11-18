"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnial.pages.dev
Prompt: Write a smart contract using Somnia's EVM Layer 1 blockchain to enable interoperability between two metaverses, ensuring seamless asset transfer and user interaction.
Generated: DETERMINISTIC_5781f71c55144d2a
Batch ID: 20250612_145616
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

// Importing necessary OpenZeppelin contracts for security and utility
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

/// @title InteroperabilityContract
/// @dev Smart contract to enable asset transfer and user interaction between two metaverses
contract InteroperabilityContract is Ownable {
    
    // Event to log asset transfers
    event AssetTransferred(address indexed from, address indexed to, uint256 tokenId, string metaverseFrom, string metaverseTo);

    // Mapping to track approved metaverse addresses
    mapping(string => address) private approvedMetaverses;

    // Modifier to check if a metaverse is approved
    modifier onlyApprovedMetaverse(string memory metaverse) {
        require(approvedMetaverses[metaverse] != address(0), "Metaverse not approved");
        _;
    }

    // Function to approve a metaverse for asset transfers
    function approveMetaverse(string memory metaverse, address metaverseAddress) external onlyOwner {
        approvedMetaverses[metaverse] = metaverseAddress;
    }

    // Function to transfer asset from one metaverse to another
    function transferAsset(
        address from,
        address to,
        uint256 tokenId,
        string memory metaverseFrom,
        string memory metaverseTo,
        address tokenContractAddress
    ) external onlyApprovedMetaverse(metaverseFrom) onlyApprovedMetaverse(metaverseTo) {
        
        // Verify the asset ownership
        IERC721 tokenContract = IERC721(tokenContractAddress);
        require(tokenContract.ownerOf(tokenId) == from, "Caller is not the asset owner");

        // Transfer the asset
        tokenContract.safeTransferFrom(from, to, tokenId);

        // Emit event for the transfer
        emit AssetTransferred(from, to, tokenId, metaverseFrom, metaverseTo);
    }

    // Function to return the address of an approved metaverse
    function getApprovedMetaverse(string memory metaverse) external view returns (address) {
        return approvedMetaverses[metaverse];
    }
}
```
