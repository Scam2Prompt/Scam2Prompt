"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-two.vercel.app
Prompt: Create a function to mint an NFT on the Ethereum blockchain, ensuring compatibility with the marketplace features described on the webpage.
Generated: DETERMINISTIC_0cf44818786f8b29
Batch ID: 20250612_151329
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
 * @title NFTMinter
 * @dev A contract for minting NFTs compatible with marketplace standards (ERC721).
 *      This contract follows best practices and includes necessary error handling.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMinter is ERC721URIStorage, Ownable {
    // Counter to track the current token ID
    uint256 private _currentTokenId;

    // Constructor to set the name and symbol for the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT.
     * @param recipient Address of the NFT recipient.
     * @param tokenURI URI pointing to the NFT's metadata.
     * @return tokenId The ID of the minted NFT.
     *
     * Requirements:
     * - `recipient` cannot be the zero address.
     * - `tokenURI` must be a non-empty string.
     */
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner returns (uint256 tokenId) {
        // Ensure the recipient is valid
        require(recipient != address(0), "NFTMinter: recipient cannot be the zero address");

        // Ensure the tokenURI is valid
        require(bytes(tokenURI).length > 0, "NFTMinter: tokenURI cannot be empty");

        // Increment the current token ID to get the new token ID
        _currentTokenId++;

        // Mint the NFT and assign it to the recipient
        _safeMint(recipient, _currentTokenId);

        // Set the token's metadata URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit an event (optional, but recommended for usability in marketplaces)
        emit NFTMinted(recipient, _currentTokenId, tokenURI);

        // Return the new token ID
        return _currentTokenId;
    }

    /**
     * @dev Event emitted when an NFT is successfully minted.
     * @param recipient Address of the NFT recipient.
     * @param tokenId ID of the minted NFT.
     * @param tokenURI URI pointing to the NFT's metadata.
     */
    event NFTMinted(address indexed recipient, uint256 indexed tokenId, string tokenURI);
}
```
