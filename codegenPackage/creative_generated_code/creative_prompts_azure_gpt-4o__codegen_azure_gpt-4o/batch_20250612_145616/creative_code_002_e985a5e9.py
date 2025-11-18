"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flipperzerobase-presales.pages.dev
Prompt: Generate a smart contract for an NFT-based game coin with utilities that align with Flipper Zero's community-driven ecosystem.
Generated: DETERMINISTIC_e985a5e9cbb83f4c
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
pragma solidity ^0.8.17;

/**
 * @title FlipperGameCoin
 * @dev ERC-721 based NFT smart contract for a community-driven ecosystem inspired by Flipper Zero.
 *      The coin can be minted, transferred, and includes utility functions for in-game interactions.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FlipperGameCoin is ERC721Enumerable, Ownable {
    // Track the base URI for metadata
    string private baseURI;

    // Event for utility-related actions
    event UtilityUsed(uint256 tokenId, address user, string action);

    // Mapping to track utility points for each NFT
    mapping(uint256 => uint256) private utilityPoints;

    // Constructor: Initializes the ERC-721 token with a name and symbol
    constructor(string memory name, string memory symbol, string memory initialBaseURI) ERC721(name, symbol) {
        baseURI = initialBaseURI;
    }

    /**
     * @dev Set a new base URI for token metadata.
     * @param newBaseURI The new base URI.
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        baseURI = newBaseURI;
    }

    /**
     * @dev Override _baseURI to return the contract's base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Mint a new token.
     * @param to Address to mint the token to.
     * @param tokenId Unique ID of the token to be minted.
     */
    function mint(address to, uint256 tokenId) external onlyOwner {
        require(!_exists(tokenId), "Token already exists");
        _safeMint(to, tokenId);
    }

    /**
     * @dev Burn an existing token.
     * @param tokenId Unique ID of the token to be burned.
     */
    function burn(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner of this token");
        _burn(tokenId);
    }

    /**
     * @dev Grant utility points to a token.
     * @param tokenId Unique ID of the token to receive points.
     * @param points Number of points to grant.
     */
    function grantUtilityPoints(uint256 tokenId, uint256 points) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        utilityPoints[tokenId] += points;
    }

    /**
     * @dev Consume utility points for a specific action.
     * @param tokenId Unique ID of the token.
     * @param points Number of points to consume.
     * @param action Description of the action performed.
     */
    function useUtilityPoints(uint256 tokenId, uint256 points, string memory action) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner of this token");
        require(utilityPoints[tokenId] >= points, "Insufficient utility points");

        utilityPoints[tokenId] -= points;
        emit UtilityUsed(tokenId, msg.sender, action);
    }

    /**
     * @dev Get the utility points of a token.
     * @param tokenId Unique ID of the token.
     * @return The utility points associated with the token.
     */
    function getUtilityPoints(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return utilityPoints[tokenId];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Ether not accepted");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Ether not accepted");
    }
}
```
