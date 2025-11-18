"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimalvara.pages.dev
Prompt: Write a smart contract that uses the ERC-721 standard to represent ownership of ERC-7621 Basket Tokens, enabling transferability and management rights on-chain.
Generated: DETERMINISTIC_5f55c96b83570586
Batch ID: 20250612_154820
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
 * @title BasketToken721
 * @dev A smart contract implementing the ERC-721 standard to represent ownership 
 *      and management rights of Basket Tokens (ERC-7621). Fully compliant with 
 *      the ERC-721 specification.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract BasketToken721 is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Optional metadata URL for Basket Tokens
    mapping(uint256 => string) private _tokenURIs;

    // Events for important actions
    event BasketTokenMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);
    event BasketTokenBurned(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract.
     * @param name The name of the ERC-721 token collection.
     * @param symbol The symbol for the ERC-721 token collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new Basket Token (ERC-721).
     * @param to The address of the recipient.
     * @param tokenURI The metadata URI associated with the token.
     * @return The ID of the newly minted token.
     */
    function mintBasketToken(address to, string memory tokenURI) external onlyOwner returns (uint256) {
        require(to != address(0), "BasketToken721: Cannot mint to the zero address");

        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the token and set its metadata URI
        _mint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        emit BasketTokenMinted(to, newTokenId, tokenURI);

        return newTokenId;
    }

    /**
     * @dev Burn a Basket Token (destroy ownership rights).
     * @param tokenId The ID of the token to be burned.
     */
    function burnBasketToken(uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "BasketToken721: Caller is not owner nor approved");

        address owner = ownerOf(tokenId);

        // Burn the token
        _burn(tokenId);

        // Remove the metadata URI
        if (bytes(_tokenURIs[tokenId]).length > 0) {
            delete _tokenURIs[tokenId];
        }

        emit BasketTokenBurned(owner, tokenId);
    }

    /**
     * @dev Override the base function to return a specific token URI.
     * @param tokenId The ID of the token whose URI we want.
     * @return The metadata URI for the given token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "BasketToken721: URI query for nonexistent token");

        string memory uri = _tokenURIs[tokenId];
        return uri;
    }

    /**
     * @dev Internal function to set the token URI for a specific token ID.
     * @param tokenId The ID of the token.
     * @param uri The metadata URI to set.
     */
    function _setTokenURI(uint256 tokenId, string memory uri) internal {
        require(_exists(tokenId), "BasketToken721: URI set for nonexistent token");
        _tokenURIs[tokenId] = uri;
    }

    /**
     * @dev Override the base _burn function to clear metadata URI on token burn.
     * @param tokenId The ID of the token to be burned.
     */
    function _burn(uint256 tokenId) internal override {
        super._burn(tokenId);

        // Clear metadata URI
        if (bytes(_tokenURIs[tokenId]).length > 0) {
            delete _tokenURIs[tokenId];
        }
    }
}
```
