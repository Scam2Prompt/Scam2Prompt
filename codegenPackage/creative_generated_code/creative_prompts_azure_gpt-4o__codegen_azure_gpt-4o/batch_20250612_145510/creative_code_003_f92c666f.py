"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pik-dapp.hk.bigfly.xyz
Prompt: Create a smart contract for NFT令牌 (NFT tokens) that aligns with the 元宇宙 (metaverse) use cases described on the 极峯(PIK) platform.
Generated: DETERMINISTIC_f92c666f48f52711
Batch ID: 20250612_145510
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
 * @title MetaverseNFT
 * @dev A smart contract for creating and managing NFTs for metaverse use cases on the 极峯 (PIK) platform.
 *      This contract follows the ERC721 standard and includes metadata and minting functionality.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MetaverseNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track if a token URI has been used (to prevent duplicate tokens)
    mapping(string => bool) private _tokenURIExists;

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with a unique token URI.
     * @param recipient The address that will receive the NFT.
     * @param tokenURI The metadata URI associated with the NFT.
     */
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero.");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty.");
        require(!_tokenURIExists[tokenURI], "Token URI already exists.");

        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the new NFT
        _safeMint(recipient, newTokenId);

        // Set the token URI
        _setTokenURI(newTokenId, tokenURI);

        // Mark the token URI as used
        _tokenURIExists[tokenURI] = true;
    }

    /**
     * @dev Get the total number of NFTs minted by the contract.
     * @return The total number of minted NFTs.
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Override _burn function to clear URI tracking on token burn.
     * @param tokenId The ID of the token to burn.
     */
    function _burn(uint256 tokenId) internal override {
        string memory tokenURI = tokenURI(tokenId);
        super._burn(tokenId);

        // Mark the token URI as no longer used
        if (bytes(tokenURI).length > 0) {
            _tokenURIExists[tokenURI] = false;
        }
    }
}
```
