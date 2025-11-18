"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-wat0x63.pages.dev
Prompt: Write a Solidity contract that pays homage to Matt Furie's creative works by including metadata or references to "Night Riders" in the token's description or functionality.
Generated: DETERMINISTIC_ae709e7894c8acd2
Batch ID: 20250612_151207
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
 * @title NightRidersToken
 * @dev A simple ERC721 contract that pays homage to Matt Furie's "Night Riders"
 * by including references to it in metadata.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NightRidersToken is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Base URI for metadata reference
    string private _baseTokenURI;

    /**
     * @dev Constructor that initializes the contract with a name and symbol.
     * @param name - The name of the token collection.
     * @param symbol - The symbol for the token collection.
     * @param baseURI - The base URI for the token metadata.
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI
    ) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Sets the base URI for the token metadata.
     * @param baseURI - The new base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new token and assigns metadata that pays homage to "Night Riders".
     * @param recipient - The address of the recipient who will own the minted token.
     * @param tokenMetadataURI - The URI pointing to the specific metadata (e.g., "Night Riders" reference).
     */
    function mintToken(address recipient, string memory tokenMetadataURI) external onlyOwner {
        // Increment token ID counter
        _currentTokenId++;

        // Mint the token to the recipient
        _mint(recipient, _currentTokenId);

        // Set the token's metadata URI (e.g., contains "Night Riders" reference)
        _setTokenURI(_currentTokenId, string(abi.encodePacked(_baseTokenURI, tokenMetadataURI)));
    }

    /**
     * @dev Returns the base URI for the token metadata.
     * @return Base metadata URI for all tokens.
     */
    function baseURI() external view returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the current token ID counter.
     * @return Current token ID.
     */
    function currentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
