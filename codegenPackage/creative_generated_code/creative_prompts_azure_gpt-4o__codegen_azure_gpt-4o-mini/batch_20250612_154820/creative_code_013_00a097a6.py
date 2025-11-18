"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimalvara.pages.dev
Prompt: Write a Solidity function to verify ownership of ERC-7621 Basket Tokens using the ERC-721 standard, ensuring secure management rights and transferability.
Generated: DETERMINISTIC_00a097a69c74576e
Batch ID: 20250612_154820
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

// Importing the ERC721 interface
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Metadata.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BasketTokenVerifier
 * @dev This contract allows verification of the ownership of ERC-7621 Basket Tokens
 * using the ERC-721 standard. It ensures secure management rights and transferability.
 */
contract BasketTokenVerifier is Ownable {
    // Mapping to store the ERC-721 token contract addresses associated with each Basket Token
    mapping(uint256 => address) private basketTokenContracts;

    /**
     * @dev Sets the ERC-721 token contract address for the given Basket Token ID.
     * @param basketTokenId The ID of the Basket Token.
     * @param tokenContract The address of the ERC-721 token contract.
     */
    function setBasketTokenContract(uint256 basketTokenId, address tokenContract) external onlyOwner {
        require(tokenContract != address(0), "BasketTokenVerifier: Invalid token contract address");
        basketTokenContracts[basketTokenId] = tokenContract;
    }

    /**
     * @dev Verifies ownership of a specific ERC-7621 Basket Token by checking the ownership
     * of the associated ERC-721 Token.
     * @param basketTokenId The ID of the Basket Token.
     * @param owner The address of the expected owner of the ERC-721 token.
     * @return bool Indicates whether the owner is indeed the owner of the corresponding ERC-721 token.
     */
    function verifyOwnership(uint256 basketTokenId, address owner) external view returns (bool) {
        address tokenContract = basketTokenContracts[basketTokenId];
        require(tokenContract != address(0), "BasketTokenVerifier: Token contract not set for this Basket Token");

        // Create an instance of the ERC-721 token contract
        IERC721 erc721Token = IERC721(tokenContract);

        // Check if the owner is the actual owner of the ERC-721 token
        return erc721Token.ownerOf(basketTokenId) == owner;
    }
}
```
