"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakamigos.art
Prompt: Develop a Solidity contract that allows Nakamigos holders to transfer their commercial rights to another wallet.
Generated: DETERMINISTIC_c7f15b1aebff7d35
Batch ID: 20250612_135717
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title NakamigosRightsTransfer
 * @dev A contract that allows Nakamigos NFT holders to transfer their commercial rights to another wallet.
 */
contract NakamigosRightsTransfer is Ownable {
    // Mapping from NFT token ID to the address that holds the commercial rights
    mapping(uint256 => address) private commercialRightsHolders;

    // The address of the Nakamigos NFT contract
    IERC721 public nakamigosNFT;

    /**
     * @dev Set the Nakamigos NFT contract address.
     * @param _nakamigosNFT The address of the Nakamigos NFT contract.
     */
    constructor(IERC721 _nakamigosNFT) {
        nakamigosNFT = _nakamigosNFT;
    }

    /**
     * @dev Transfer commercial rights of a Nakamigos NFT to another wallet.
     * @param tokenId The ID of the Nakamigos NFT.
     * @param newRightsHolder The address that will receive the commercial rights.
     */
    function transferCommercialRights(uint256 tokenId, address newRightsHolder) external {
        // Ensure the sender is the current rights holder
        require(nakamigosNFT.ownerOf(tokenId) == msg.sender, "Caller is not the NFT owner");

        // Validate the new rights holder address
        require(newRightsHolder != address(0), "New rights holder cannot be the zero address");

        // Transfer commercial rights
        commercialRightsHolders[tokenId] = newRightsHolder;
        
        // Emit an event for tracking
        emit CommercialRightsTransferred(tokenId, msg.sender, newRightsHolder);
    }

    /**
     * @dev Get the current commercial rights holder for a given NFT.
     * @param tokenId The ID of the Nakamigos NFT.
     * @return The address of the current commercial rights holder.
     */
    function getCommercialRightsHolder(uint256 tokenId) external view returns (address) {
        return commercialRightsHolders[tokenId];
    }

    // Event emitted when commercial rights are transferred
    event CommercialRightsTransferred(uint256 indexed tokenId, address indexed previousHolder, address indexed newHolder);
}
```
