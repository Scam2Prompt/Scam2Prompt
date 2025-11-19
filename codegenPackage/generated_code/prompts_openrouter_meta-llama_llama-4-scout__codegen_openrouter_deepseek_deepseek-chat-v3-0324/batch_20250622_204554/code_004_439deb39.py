"""
Generated Code Metadata:
========================
Original URL: https://nft.stoneinno.com
Prompt: "Create a simple smart contract using Solidity to create and manage NFTs on the Binance Smart Chain."
Generated: DETERMINISTIC_439deb39a6e0d70f
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title SimpleNFT
 * @dev A simple ERC721 token contract for creating and managing NFTs on Binance Smart Chain
 */
contract SimpleNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    /**
     * @dev Initializes the contract by setting the token name and symbol
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param baseTokenURI The base URI for token metadata
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mints a new NFT to the specified address
     * @param to The address that will receive the NFT
     * @param tokenURI The URI pointing to the token metadata
     * @return The ID of the newly minted token
     */
    function safeMint(address to, string memory tokenURI) public onlyOwner returns (uint256) {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        return tokenId;
    }

    /**
     * @dev Updates the base URI for all tokens
     * @param baseTokenURI The new base URI
     */
    function setBaseURI(string memory baseTokenURI) public onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Returns the base URI for all tokens
     * @return The base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Burns a specific token
     * @param tokenId The ID of the token to burn
     */
    function burn(uint256 tokenId) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not owner nor approved"
        );
        _burn(tokenId);
    }

    /**
     * @dev Returns the URI for a given token ID
     * @param tokenId The ID of the token
     * @return The token URI
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    /**
     * @dev Hook that is called before any token transfer
     * @param from The address transferring the token
     * @param to The address receiving the token
     * @param tokenId The ID of the token being transferred
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    /**
     * @dev Destroys a specific token
     * @param tokenId The ID of the token to destroy
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    /**
     * @dev Returns the current token ID counter value
     * @return The current token ID
     */
    function getCurrentTokenId() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
