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

/**
 * @title DigitalAssetMinting
 * @dev A smart contract for minting unique digital assets (ERC721 tokens).
 * Inspired by minting functionality from Gotchipus Mint.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DigitalAssetMinting is ERC721Enumerable, Ownable {
    // Counter for unique token IDs
    uint256 private _currentTokenId;

    // Mapping to store metadata URIs for tokens
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new token is minted
    event TokenMinted(uint256 indexed tokenId, address indexed to, string tokenURI);

    /**
     * @dev Constructor to initialize the ERC721 token.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new unique digital asset to the specified address.
     * @param to Address of the recipient.
     * @param tokenURI Metadata URI associated with the token.
     */
    function mint(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "DigitalAssetMinting: Cannot mint to zero address");
        require(bytes(tokenURI).length > 0, "DigitalAssetMinting: Token URI cannot be empty");

        // Increment the token ID counter
        _currentTokenId++;

        // Mint the token
        _safeMint(to, _currentTokenId);

        // Set token URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit the minting event
        emit TokenMinted(_currentTokenId, to, tokenURI);
    }

    /**
     * @dev Get the URI of a specific token.
     * @param tokenId The ID of the token.
     * @return The URI of the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "DigitalAssetMinting: Query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Internal function to set the token URI.
     * @param tokenId The ID of the token.
     * @param tokenURI The URI to be set.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "DigitalAssetMinting: URI set for nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Override to include ERC721Enumerable's supportsInterface method.
     * @param interfaceId The interface identifier.
     * @return True if the contract supports the given interface.
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
