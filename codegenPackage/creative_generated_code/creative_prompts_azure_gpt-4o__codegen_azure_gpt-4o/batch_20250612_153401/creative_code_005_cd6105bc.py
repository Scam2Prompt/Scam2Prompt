"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Develop a smart contract for issuing soulbound tokens (SBTs) that align with Masa's rewards program.
Generated: DETERMINISTIC_cd6105bcee489517
Batch ID: 20250612_153401
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
 * @title Soulbound Token (SBT) Contract for Masa Rewards Program
 * @dev This contract implements a non-transferable ERC721 token for Masa's rewards program.
 * Soulbound tokens represent unique rewards and cannot be sold or transferred.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MasaSoulboundToken is ERC721Enumerable, Ownable {
    // Mapping to track token metadata (e.g., rewards details)
    mapping(uint256 => string) private _tokenMetadata;

    // Event emitted when a new SBT is issued
    event SoulboundTokenIssued(address indexed recipient, uint256 tokenId, string metadata);

    /**
     * @dev Constructor that initializes the ERC721 token.
     * @param name Token name.
     * @param symbol Token symbol.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Issue a new soulbound token to a recipient.
     * @param recipient Address of the token recipient.
     * @param metadata Metadata associated with the token (e.g., reward details).
     */
    function issueToken(address recipient, string memory metadata) external onlyOwner {
        require(recipient != address(0), "Recipient cannot be the zero address");
        
        // Mint the token
        uint256 tokenId = totalSupply() + 1;
        _safeMint(recipient, tokenId);
        
        // Store the token metadata
        _tokenMetadata[tokenId] = metadata;

        // Emit the event
        emit SoulboundTokenIssued(recipient, tokenId, metadata);
    }

    /**
     * @dev Override the transfer functions from ERC721 to prevent transferability.
     * Soulbound tokens cannot be transferred, making them permanently bound to the recipient.
     */
    function _transfer(address from, address to, uint256 tokenId) internal pure override {
        revert("Soulbound tokens cannot be transferred");
    }

    function approve(address to, uint256 tokenId) public pure override {
        revert("Soulbound tokens cannot be approved for transfer");
    }

    function setApprovalForAll(address operator, bool approved) public pure override {
        revert("Soulbound tokens cannot be approved for transfer");
    }

    /**
     * @dev Retrieve metadata of a specific token.
     * @param tokenId ID of the token to query.
     * @return Metadata string associated with the token.
     */
    function tokenMetadata(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenMetadata[tokenId];
    }

    /**
     * @dev Burn a soulbound token.
     * Only the contract owner can burn tokens (e.g., to revoke a reward).
     * @param tokenId ID of the token to burn.
     */
    function burnToken(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _burn(tokenId);
        delete _tokenMetadata[tokenId];
    }
}
```
