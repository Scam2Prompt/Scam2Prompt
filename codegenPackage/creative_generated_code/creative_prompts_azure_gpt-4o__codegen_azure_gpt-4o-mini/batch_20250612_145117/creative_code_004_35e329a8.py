"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gotchipus.top
Prompt: Write a smart contract for minting unique digital assets, inspired by the functionality described on Gotchipus Mint.
Generated: DETERMINISTIC_35e329a81404f4b3
Batch ID: 20250612_145117
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

/**
 * @title UniqueDigitalAsset
 * @dev A smart contract for minting unique digital assets (NFTs).
 */
contract UniqueDigitalAsset is ERC721Enumerable, Ownable {
    // Mapping from token ID to asset metadata (URI)
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new digital asset is minted
    event AssetMinted(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Counter for generating unique token IDs
    uint256 private _currentTokenId;

    /**
     * @dev Constructor that initializes the contract with a name and a symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        _currentTokenId = 0;
    }

    /**
     * @dev Mint a new unique digital asset.
     * @param tokenURI The metadata URI for the new asset.
     * Requirements:
     * - `tokenURI` must not be empty.
     */
    function mint(string memory tokenURI) external onlyOwner {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        _currentTokenId++;
        uint256 newTokenId = _currentTokenId;

        // Mint the NFT to the owner's address
        _mint(msg.sender, newTokenId);
        
        // Set the token's metadata URI
        _setTokenURI(newTokenId, tokenURI);

        emit AssetMinted(newTokenId, msg.sender, tokenURI);
    }

    /**
     * @dev Set the token URI for a given token ID.
     * @param tokenId The token ID for which to set the URI.
     * @param tokenURI The new token URI.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal virtual {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Retrieve the token URI for a given token ID.
     * @param tokenId The token ID for which to retrieve the URI.
     * @return The URI of the specified token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Get the current token ID. (For potential external use or tracking)
     * @return The current token ID.
     */
    function currentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
