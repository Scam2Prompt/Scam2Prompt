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

// Importing the interface for ERC721
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title NFTVerifier
 * @dev A contract to verify NFT ownership and display metadata
 */
contract NFTVerifier is Ownable {
    // This event is emitted when an ownership verification is successful
    event OwnershipVerified(address indexed owner, uint256 tokenId);

    // Function to verify NFT ownership and get metadata
    /**
     * @notice Verifies the ownership of a specific token ID and retrieves its metadata
     * @param nftContractAddress The address of the NFT contract (ERC721)
     * @param tokenId The ID of the token to verify
     * @return owner The owner of the token
     * @return name The name of the NFT
     * @return symbol The symbol of the NFT
     * @return tokenURI The URI containing metadata about the token
     */
    function verifyOwnershipAndGetMetadata(
        address nftContractAddress,
        uint256 tokenId
    )
        external
        returns (
            address owner,
            string memory name,
            string memory symbol,
            string memory tokenURI
        )
    {
        // Check if the provided address is a valid contract
        require(nftContractAddress != address(0), "Invalid contract address");
        
        // Instantiate the ERC721 contract
        IERC721 nftContract = IERC721(nftContractAddress);

        // Get the owner of the specified token ID
        owner = nftContract.ownerOf(tokenId);

        // Emit an event to signal ownership verification
        emit OwnershipVerified(owner, tokenId);

        // Get the NFT metadata
        name = IERC721Metadata(nftContractAddress).name();
        symbol = IERC721Metadata(nftContractAddress).symbol();
        tokenURI = IERC721Metadata(nftContractAddress).tokenURI(tokenId);
    }
}
```
