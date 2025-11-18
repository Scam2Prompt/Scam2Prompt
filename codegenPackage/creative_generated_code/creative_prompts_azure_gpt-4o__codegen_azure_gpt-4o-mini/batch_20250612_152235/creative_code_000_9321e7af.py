"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintlama.pages.dev
Prompt: Write a smart contract in Solidity for minting NFTs with unique identifiers, inspired by the roadmap of the Cyber Lama NFT collection project. Ensure the contract includes mechanisms for limiting circulation and verifying uniqueness.
Generated: DETERMINISTIC_9321e7af94cf4825
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CyberLamaNFT
 * @dev A smart contract for minting unique NFTs with limited circulation.
 */
contract CyberLamaNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;
    
    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_SUPPLY = 10000;

    // Mapping to track if a token ID has been minted
    mapping(uint256 => bool) private _tokenExists;

    // Event emitted when a new NFT is minted
    event NFTMinted(address recipient, uint256 tokenId);

    /**
     * @dev Constructor that initializes the NFT collection name and symbol.
     */
    constructor() ERC721("Cyber Lama", "CLAMA") {}

    /**
     * @dev Mints a new NFT with a unique identifier.
     * @param recipient The address that will receive the NFT.
     * Requires that the total supply has not exceeded the maximum limit.
     */
    function mintNFT(address recipient) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        
        uint256 newTokenId = _tokenIdCounter.current();
        
        // Ensure uniqueness of the token ID
        require(!_tokenExists[newTokenId], "Token ID already exists");

        // Mint the NFT
        _safeMint(recipient, newTokenId);
        
        // Mark the token ID as minted
        _tokenExists[newTokenId] = true;

        // Increment the counter for the next token ID
        _tokenIdCounter.increment();

        // Emit the NFTMinted event
        emit NFTMinted(recipient, newTokenId);
    }

    /**
     * @dev Returns the total number of NFTs minted.
     * @return The total supply of minted NFTs.
     */
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Overrides the base class function to ensure that token IDs are unique.
     * @param tokenId The ID of the NFT to check for existence.
     * @return True if the token ID exists, false otherwise.
     */
    function _exists(uint256 tokenId) internal view virtual override returns (bool) {
        return super._exists(tokenId) && _tokenExists[tokenId];
    }
}
```
