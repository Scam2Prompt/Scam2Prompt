"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotitties.fun
Prompt: Write a function in Solidity to verify NFT ownership and display metadata, inspired by CryptoTitties' verification on OpenSea.
Generated: DETERMINISTIC_16e22ebb20e8e5f2
Batch ID: 20250612_150323
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
 * @title NFTVerification
 * @dev A contract to verify NFT ownership and display metadata.
 */
contract NFTVerification {
    // Interface for the ERC721 contract to interact with NFTs
    interface IERC721 {
        function ownerOf(uint256 tokenId) external view returns (address);
        function tokenURI(uint256 tokenId) external view returns (string memory);
    }

    /**
     * @dev Verifies NFT ownership and retrieves metadata.
     * @param nftContract The address of the ERC721 contract.
     * @param tokenId The ID of the NFT to verify.
     * @return owner The address of the NFT owner.
     * @return metadataURI The metadata URI of the NFT.
     */
    function verifyOwnershipAndMetadata(address nftContract, uint256 tokenId)
        external
        view
        returns (address owner, string memory metadataURI)
    {
        // Ensure the address is not a zero address
        require(nftContract != address(0), "Invalid NFT contract address");

        // Cast the provided contract address to the ERC721 interface
        IERC721 nft = IERC721(nftContract);

        // Use a try-catch block to catch any errors from the ERC721 contract
        try nft.ownerOf(tokenId) returns (address currentOwner) {
            owner = currentOwner;
        } catch {
            revert("Failed to verify ownership: Token may not exist or invalid contract");
        }

        try nft.tokenURI(tokenId) returns (string memory uri) {
            metadataURI = uri;
        } catch {
            revert("Failed to retrieve metadata URI: Token may not exist or invalid contract");
        }

        return (owner, metadataURI);
    }
}
```
