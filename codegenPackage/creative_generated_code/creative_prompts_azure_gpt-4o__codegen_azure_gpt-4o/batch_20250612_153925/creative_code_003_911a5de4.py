"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepseachain.online
Prompt: Create a function in Solidity to track ownership and display rights of NFTs purchased on the DeepSea marketplace.
Generated: DETERMINISTIC_911a5de4276acfb0
Batch ID: 20250612_153925
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
 * @title NFTMarketplace
 * @dev Contract to track ownership and display rights of NFTs purchased on the DeepSea marketplace
 */
contract NFTMarketplace {
    // Struct to represent an NFT
    struct NFT {
        uint256 id; // Unique identifier for the NFT
        address owner; // Address of the current owner
        bool displayRights; // True if the owner has display rights, otherwise false
    }

    // Mapping to store NFTs by their ID
    mapping(uint256 => NFT) private nfts;

    // Event triggered when an NFT's ownership is transferred
    event OwnershipTransferred(uint256 indexed nftId, address indexed previousOwner, address indexed newOwner);

    // Event triggered when display rights are updated
    event DisplayRightsUpdated(uint256 indexed nftId, bool displayRights);

    /**
     * @dev Function to purchase an NFT, setting ownership and display rights
     * @param nftId The unique identifier of the NFT
     * @param displayRights True if the buyer wants display rights, false otherwise
     */
    function purchaseNFT(uint256 nftId, bool displayRights) external payable {
        require(nfts[nftId].owner == address(0), "NFT already owned"); // Ensure the NFT is not already owned
        require(msg.value > 0, "Payment must be greater than zero"); // Ensure payment is made

        // Assign ownership and set display rights
        nfts[nftId] = NFT(nftId, msg.sender, displayRights);

        // Emit events for ownership transfer and display rights update
        emit OwnershipTransferred(nftId, address(0), msg.sender);
        emit DisplayRightsUpdated(nftId, displayRights);
    }

    /**
     * @dev Function to transfer ownership of an NFT to another address
     * @param nftId The unique identifier of the NFT
     * @param newOwner Address of the new owner
     */
    function transferOwnership(uint256 nftId, address newOwner) external {
        require(nfts[nftId].owner == msg.sender, "Caller is not the owner"); // Ensure the caller is the owner
        require(newOwner != address(0), "New owner address cannot be zero"); // Ensure the new owner address is valid

        // Update ownership
        address previousOwner = nfts[nftId].owner;
        nfts[nftId].owner = newOwner;

        // Emit event for ownership transfer
        emit OwnershipTransferred(nftId, previousOwner, newOwner);
    }

    /**
     * @dev Function to update display rights of an owned NFT
     * @param nftId The unique identifier of the NFT
     * @param displayRights True to enable display rights, false to disable
     */
    function updateDisplayRights(uint256 nftId, bool displayRights) external {
        require(nfts[nftId].owner == msg.sender, "Caller is not the owner"); // Ensure the caller is the owner

        // Update display rights
        nfts[nftId].displayRights = displayRights;

        // Emit event for display rights update
        emit DisplayRightsUpdated(nftId, displayRights);
    }

    /**
     * @dev Function to get details of an NFT
     * @param nftId The unique identifier of the NFT
     * @return id The unique identifier of the NFT
     * @return owner The address of the current owner
     * @return displayRights True if the owner has display rights, false otherwise
     */
    function getNFTDetails(uint256 nftId) external view returns (uint256 id, address owner, bool displayRights) {
        require(nfts[nftId].owner != address(0), "NFT does not exist"); // Ensure the NFT exists

        NFT memory nft = nfts[nftId];
        return (nft.id, nft.owner, nft.displayRights);
    }
}
```
