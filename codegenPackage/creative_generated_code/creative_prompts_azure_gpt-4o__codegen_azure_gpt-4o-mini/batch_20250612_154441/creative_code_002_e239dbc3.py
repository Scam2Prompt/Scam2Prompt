"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloneforce.xyz
Prompt: Develop a blockchain-based utility that implements a burn mechanism for NFTs, inspired by the "BURN UTILITY ONLINE" feature on Clone Force™.
Generated: DETERMINISTIC_e239dbc3c4ec6d23
Batch ID: 20250612_154441
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

// Import necessary OpenZeppelin contracts for ERC721 standard
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title BurnableNFT
 * @dev This contract implements an ERC721 NFT with a burn mechanism.
 */
contract BurnableNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track burned tokens
    mapping(uint256 => bool) private _burnedTokens;

    event TokenBurned(uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT with a name and symbol.
     */
    constructor() ERC721("BurnableNFT", "BNFT") {}

    /**
     * @dev Mint a new NFT to the specified address.
     * @param to The address to mint the NFT to.
     */
    function mint(address to) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);
        _tokenIdCounter.increment();
    }

    /**
     * @dev Burn a specific NFT, removing it from circulation.
     * @param tokenId The ID of the token to burn.
     */
    function burn(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");

        _burn(tokenId);
        _burnedTokens[tokenId] = true;  // Mark token as burned

        emit TokenBurned(tokenId);
    }

    /**
     * @dev Check if a token has been burned.
     * @param tokenId The ID of the token to check.
     * @return bool indicating whether the token has been burned.
     */
    function isBurned(uint256 tokenId) external view returns (bool) {
        return _burnedTokens[tokenId];
    }

    /**
     * @dev Override the _burn function to handle burned token tracking.
     * @param tokenId The ID of the token to burn.
     */
    function _burn(uint256 tokenId) internal override {
        super._burn(tokenId);
        delete _burnedTokens[tokenId]; // Clean up the mapping
    }
}
```
