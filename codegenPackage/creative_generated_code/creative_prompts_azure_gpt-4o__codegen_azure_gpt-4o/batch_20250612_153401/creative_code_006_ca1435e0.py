"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinuairdrop.pages.dev
Prompt: Develop a smart contract for minting soulbound receipt tokens in the Diamond Hands app, ensuring compatibility with all EVM chains.
Generated: DETERMINISTIC_ca1435e06c731732
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
 * @title DiamondHandsReceiptToken
 * @dev A smart contract for minting soulbound receipt tokens in the Diamond Hands app.
 * Soulbound tokens are non-transferable and represent commitments made by users.
 * This contract is compatible with all EVM chains.
 */

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract DiamondHandsReceiptToken is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Mapping to track whether a token is soulbound
    mapping(uint256 => bool) public soulbound;

    // Event emitted when a new soulbound receipt token is minted
    event SoulboundTokenMinted(address indexed recipient, uint256 tokenId);

    /**
     * @dev Constructor initializes the ERC721 token with a name and symbol for the Diamond Hands app.
     */
    constructor() ERC721("DiamondHandsReceiptToken", "DHRT") {}

    /**
     * @dev Mint a soulbound receipt token for the specified recipient.
     * @param recipient The address of the recipient receiving the token.
     * @return tokenId The ID of the newly minted token.
     */
    function mintSoulboundToken(address recipient) external onlyOwner returns (uint256) {
        require(recipient != address(0), "Recipient address cannot be zero");

        // Increment the token ID counter
        _tokenIds.increment();
        uint256 tokenId = _tokenIds.current();

        // Mint the token to the recipient
        _mint(recipient, tokenId);

        // Mark the token as soulbound
        soulbound[tokenId] = true;

        // Emit an event for tracking
        emit SoulboundTokenMinted(recipient, tokenId);

        return tokenId;
    }

    /**
     * @dev Override the _transfer function to prevent soulbound tokens from being transferred.
     * @param from The address the token is being transferred from.
     * @param to The address the token is being transferred to.
     * @param tokenId The ID of the token being transferred.
     */
    function _transfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override {
        require(!soulbound[tokenId], "Soulbound tokens are non-transferable");
        super._transfer(from, to, tokenId);
    }

    /**
     * @dev Override the approve function to prevent soulbound tokens from being approved for transfer.
     * @param to The address to approve.
     * @param tokenId The ID of the token to approve.
     */
    function approve(address to, uint256 tokenId) public virtual override {
        require(!soulbound[tokenId], "Soulbound tokens cannot be approved for transfer");
        super.approve(to, tokenId);
    }

    /**
     * @dev Override the setApprovalForAll function to prevent soulbound tokens from being approved for all.
     * @param operator The address of the operator.
     * @param approved Boolean indicating whether the operator is approved.
     */
    function setApprovalForAll(address operator, bool approved) public virtual override {
        revert("Soulbound tokens cannot be approved for transfer");
    }

    /**
     * @dev Function to check whether a given token is soulbound.
     * @param tokenId The ID of the token to check.
     * @return isSoulbound True if the token is soulbound, false otherwise.
     */
    function isSoulbound(uint256 tokenId) external view returns (bool isSoulbound) {
        return soulbound[tokenId];
    }
}
```
