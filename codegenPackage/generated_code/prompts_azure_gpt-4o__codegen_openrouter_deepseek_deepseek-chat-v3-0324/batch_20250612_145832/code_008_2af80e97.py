"""
Generated Code Metadata:
========================
Original URL: https://okxouyigo.com
Prompt: Write a smart contract in Solidity for managing rare digital assets, inspired by OKX's discussion of scarcity and value in Web3.0.
Generated: DETERMINISTIC_2af80e9723bece47
Batch ID: 20250612_145832
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title RareDigitalAsset
 * @dev A smart contract for managing rare digital assets (NFTs) with scarcity features
 */
contract RareDigitalAsset is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Token ID counter
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of tokens
    uint256 public immutable MAX_SUPPLY;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Royalty information
    struct RoyaltyInfo {
        address recipient;
        uint24 amount; // basis points (10000 = 100%)
    }

    // Token ID to royalty info mapping
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Events
    event Minted(address indexed to, uint256 indexed tokenId, string tokenURI);
    event RoyaltySet(uint256 indexed tokenId, address recipient, uint256 amount);

    /**
     * @dev Constructor
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param maxSupply_ Maximum supply of tokens
     * @param baseTokenURI_ Base URI for token metadata
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 maxSupply_,
        string memory baseTokenURI_
    ) ERC721(name_, symbol_) {
        require(maxSupply_ > 0, "Max supply must be greater than zero");
        MAX_SUPPLY = maxSupply_;
        _baseTokenURI = baseTokenURI_;
    }

    /**
     * @dev Mints a new token with royalty information
     * @param to Address to mint the token to
     * @param tokenURI URI for the token's metadata
     * @param royaltyRecipient Address to receive royalties
     * @param royaltyBasisPoints Royalty amount in basis points
     */
    function safeMint(
        address to,
        string memory tokenURI,
        address royaltyRecipient,
        uint24 royaltyBasisPoints
    ) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(royaltyBasisPoints <= 10000, "Royalty exceeds max (10000 = 100%)");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _setRoyaltyInfo(tokenId, royaltyRecipient, royaltyBasisPoints);

        emit Minted(to, tokenId, tokenURI);
    }

    /**
     * @dev Sets royalty information for a token
     * @param tokenId ID of the token
     * @param recipient Address to receive royalties
     * @param basisPoints Royalty amount in basis points
     */
    function _setRoyaltyInfo(
        uint256 tokenId,
        address recipient,
        uint24 basisPoints
    ) internal {
        require(_exists(tokenId), "Nonexistent token");
        require(basisPoints <= 10000, "Royalty exceeds max (10000 = 100%)");

        _royalties[tokenId] = RoyaltyInfo(recipient, basisPoints);
        emit RoyaltySet(tokenId, recipient, basisPoints);
    }

    /**
     * @dev Gets royalty information for a token
     * @param tokenId ID of the token
     * @param salePrice Sale price of the token
     * @return recipient Address to receive royalties
     * @return royaltyAmount Royalty amount
     */
    function royaltyInfo(uint256 tokenId, uint256 salePrice)
        external
        view
        returns (address recipient, uint256 royaltyAmount)
    {
        require(_exists(tokenId), "Nonexistent token");
        
        RoyaltyInfo memory royalty = _royalties[tokenId];
        recipient = royalty.recipient;
        royaltyAmount = (salePrice * royalty.amount) / 10000;
    }

    /**
     * @dev Updates the base URI for all tokens
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Returns the base URI
     * @return Base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
