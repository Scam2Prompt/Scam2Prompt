"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://911d9012.metablocks-world.pages.dev
Prompt: Write a code snippet to create a decaying NFT that burns itself over time using Meta Blocks.
Generated: DETERMINISTIC_dd806049bf647ae3
Batch ID: 20250612_163243
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
 * @title DecayingNFT
 * @dev This contract creates an NFT that decays and burns itself over time.
 * Decay is defined by a fixed time period after minting.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DecayingNFT is ERC721, Ownable {
    // Struct to store NFT data
    struct Metadata {
        uint256 mintTimestamp; // Timestamp when the NFT was minted
        uint256 lifetime;      // Lifetime of the NFT in seconds
    }

    // Mapping from token ID to metadata
    mapping(uint256 => Metadata) private _tokenMetadata;

    // Counter to generate unique token IDs
    uint256 private _nextTokenId;

    /**
     * @dev Constructor to initialize the NFT contract
     * @param name Name of the NFT collection
     * @param symbol Symbol of the NFT collection
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new decaying NFT
     * @param to Address of the recipient
     * @param lifetime Lifetime of the NFT in seconds
     */
    function mint(address to, uint256 lifetime) external onlyOwner {
        require(lifetime > 0, "Lifetime must be greater than 0");

        // Increment token ID counter
        uint256 tokenId = _nextTokenId++;
        
        // Mint the NFT to the recipient
        _mint(to, tokenId);
        
        // Store the metadata
        _tokenMetadata[tokenId] = Metadata({
            mintTimestamp: block.timestamp,
            lifetime: lifetime
        });
    }

    /**
     * @dev Check if an NFT is expired
     * @param tokenId ID of the token to check
     * @return bool True if the NFT is expired, false otherwise
     */
    function isExpired(uint256 tokenId) public view returns (bool) {
        require(_exists(tokenId), "Token does not exist");

        Metadata memory metadata = _tokenMetadata[tokenId];
        return block.timestamp >= (metadata.mintTimestamp + metadata.lifetime);
    }

    /**
     * @dev Trigger the burn of expired NFTs
     * @param tokenId ID of the token to burn
     */
    function burnIfExpired(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");

        // Check if the NFT is expired
        if (isExpired(tokenId)) {
            _burn(tokenId);
            delete _tokenMetadata[tokenId]; // Clean up metadata
        } else {
            revert("Token is not expired yet");
        }
    }

    /**
     * @dev Override _burn to ensure metadata cleanup
     * @param tokenId ID of the token to burn
     */
    function _burn(uint256 tokenId) internal override {
        super._burn(tokenId);
        delete _tokenMetadata[tokenId];
    }

    /**
     * @dev Retrieve metadata of a token
     * @param tokenId ID of the token to query
     * @return Metadata of the specified token
     */
    function getTokenMetadata(uint256 tokenId) external view returns (Metadata memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenMetadata[tokenId];
    }
}
```
