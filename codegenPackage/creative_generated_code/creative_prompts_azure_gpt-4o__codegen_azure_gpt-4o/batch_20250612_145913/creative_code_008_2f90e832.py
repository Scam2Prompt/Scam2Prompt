"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testme-p7m.pages.dev
Prompt: Write a script in Solidity to verify ownership of Pepe 2.0 NFTs using the contract address `0xfb66321d7c674995dfcc2cb67a30bc978dc862ad`.
Generated: DETERMINISTIC_2f90e832add824cd
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title Pepe2NFTVerifier
 * @dev Contract to verify ownership of Pepe 2.0 NFTs.
 */
contract Pepe2NFTVerifier {
    // Address of the Pepe 2.0 NFT contract
    address private constant PEPE_2_0_NFT_CONTRACT = 0xfb66321d7c674995dFCC2cb67A30bc978DC862AD;

    /**
     * @dev Interface for the ERC721 token standard, which defines the `ownerOf` function.
     */
    interface IERC721 {
        function ownerOf(uint256 tokenId) external view returns (address);
    }

    /**
     * @dev Verify ownership of a specific Pepe 2.0 NFT.
     * @param tokenId The ID of the NFT to verify ownership of.
     * @return owner The address of the owner of the specified NFT.
     */
    function verifyOwnership(uint256 tokenId) external view returns (address owner) {
        // Ensure the NFT contract address is valid
        require(PEPE_2_0_NFT_CONTRACT != address(0), "Invalid NFT contract address");

        // Create an interface instance for the Pepe 2.0 NFT contract
        IERC721 nftContract = IERC721(PEPE_2_0_NFT_CONTRACT);

        // Query the owner of the tokenId from the NFT contract
        owner = nftContract.ownerOf(tokenId);

        // Return the owner address
        return owner;
    }
}
```
