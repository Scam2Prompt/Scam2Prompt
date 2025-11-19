"""
Generated Code Metadata:
========================
Original URL: https://dappass.neocities.org
Prompt: Create a library for interacting with the Dapp Pass smart contract, including functions for minting, transferring, and checking ownership of the digital asset.
Generated: DETERMINISTIC_abf376150060de72
Batch ID: 20250622_211012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DappPass
 * @dev This contract allows for minting, transferring, and checking ownership of digital assets.
 */
contract DappPass is ERC721, Ownable {
    // Mapping from token ID to the token's metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Counter for the next token ID
    uint256 private _nextTokenId;

    // Event emitted when a new token is minted
    event TokenMinted(uint256 indexed tokenId, address indexed owner, string tokenURI);

    /**
     * @dev Constructor that sets the name and symbol of the token.
     */
    constructor() ERC721("DappPass", "DPASS") {}

    /**
     * @dev Mint a new token with a specified URI.
     * @param to The address that will own the minted token.
     * @param tokenURI The metadata URI for the token.
     */
    function mint(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        uint256 tokenId = _nextTokenId++;
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit TokenMinted(tokenId, to, tokenURI);
    }

    /**
     * @dev Transfer a token from one address to another.
     * @param from The current owner of the token.
     * @param to The new owner of the token.
     * @param tokenId The ID of the token to transfer.
     */
    function transferToken(address from, address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Cannot transfer to the zero address");

        _transfer(from, to, tokenId);
    }

    /**
     * @dev Check the ownership of a token.
     * @param tokenId The ID of the token to check.
     * @return The address of the owner of the token.
     */
    function ownerOfToken(uint256 tokenId) external view returns (address) {
        return ownerOf(tokenId);
    }

    /**
     * @dev Internal function to set the token URI.
     * @param tokenId The ID of the token.
     * @param tokenURI The metadata URI for the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Override the base URI function to return the token URI.
     * @param tokenId The ID of the token.
     * @return The metadata URI of the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }
}
```
