"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsmix.biz
Prompt: Write a Solidity contract for managing fractional ownership of NFTs, inspired by the acquisition model of "NiftyKit" by カイカイキキ.
Generated: DETERMINISTIC_41809dfc2e67a2e2
Batch ID: 20250612_151414
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

/**
 * @title FractionalNFTOwnership
 * @dev A contract for managing fractional ownership of NFTs.
 * Inspired by fractional acquisition models such as NiftyKit by カイカイキキ.
 */
contract FractionalNFTOwnership {
    // Structure to represent an NFT share
    struct NFTShare {
        uint256 tokenId;         // Token ID of the NFT
        address owner;           // Owner of the fractional share
        uint256 sharePercentage; // Percentage of ownership (in basis points, e.g., 10000 = 100%)
    }

    // Mapping from NFT token ID to its fractional shares
    mapping(uint256 => NFTShare[]) public nftShares;

    // Mapping to track the total share percentages per token ID
    mapping(uint256 => uint256) public totalShares;

    // Events
    event ShareCreated(uint256 indexed tokenId, address indexed owner, uint256 sharePercentage);
    event ShareTransferred(uint256 indexed tokenId, address indexed from, address indexed to, uint256 sharePercentage);

    /**
     * @dev Create fractional shares for an NFT. Total shares must equal 10000 basis points (100%).
     * @param tokenId The NFT token ID.
     * @param owners An array of addresses representing fractional owners.
     * @param shares An array of share percentages corresponding to the owners.
     */
    function createShares(uint256 tokenId, address[] calldata owners, uint256[] calldata shares) external {
        require(owners.length == shares.length, "Mismatched owners and shares length");
        require(totalShares[tokenId] == 0, "Shares already exist for this token");

        uint256 totalShare = 0;

        for (uint256 i = 0; i < owners.length; i++) {
            require(shares[i] > 0, "Share percentage must be greater than 0");
            nftShares[tokenId].push(NFTShare({
                tokenId: tokenId,
                owner: owners[i],
                sharePercentage: shares[i]
            }));
            totalShare += shares[i];
            emit ShareCreated(tokenId, owners[i], shares[i]);
        }

        require(totalShare == 10000, "Total share percentage must equal 100%");
        totalShares[tokenId] = totalShare;
    }

    /**
     * @dev Transfer fractional ownership of an NFT from one owner to another.
     * @param tokenId The NFT token ID.
     * @param from The current owner of the fractional share.
     * @param to The new owner of the fractional share.
     * @param sharePercentage The percentage of ownership being transferred.
     */
    function transferShare(uint256 tokenId, address from, address to, uint256 sharePercentage) external {
        require(sharePercentage > 0, "Share percentage must be greater than 0");
        require(to != address(0), "Invalid recipient address");

        bool shareFound = false;

        for (uint256 i = 0; i < nftShares[tokenId].length; i++) {
            NFTShare storage share = nftShares[tokenId][i];

            if (share.owner == from && share.sharePercentage >= sharePercentage) {
                shareFound = true;

                // Reduce share of the current owner
                share.sharePercentage -= sharePercentage;

                // Add share for the new owner
                nftShares[tokenId].push(NFTShare({
                    tokenId: tokenId,
                    owner: to,
                    sharePercentage: sharePercentage
                }));

                emit ShareTransferred(tokenId, from, to, sharePercentage);

                // Break the loop once the share is handled
                break;
            }
        }

        require(shareFound, "Share not found or insufficient share percentage");
    }

    /**
     * @dev Get all fractional shares for a specific NFT token ID.
     * @param tokenId The NFT token ID.
     * @return An array of NFTShare structs representing the fractional ownership details.
     */
    function getShares(uint256 tokenId) external view returns (NFTShare[] memory) {
        return nftShares[tokenId];
    }
}
```
