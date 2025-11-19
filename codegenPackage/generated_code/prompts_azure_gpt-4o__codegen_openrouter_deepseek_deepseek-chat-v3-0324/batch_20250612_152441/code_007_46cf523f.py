"""
Generated Code Metadata:
========================
Original URL: https://dee-lance.pages.dev
Prompt: Write a Solidity contract to tokenize freelancers' work as NFTs, including functionality for royalties and ownership verification, as described in DeeLance's NFT marketplace.
Generated: DETERMINISTIC_46cf523f97b43d69
Batch ID: 20250612_152441
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FreelancerNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIdCounter;

    struct RoyaltyInfo {
        address recipient;
        uint256 percentage; // Basis points (e.g., 1000 = 10%)
    }

    mapping(uint256 => RoyaltyInfo) private _royalties;
    mapping(uint256 => address) private _creators;
    mapping(uint256 => string) private _workDescriptions;

    event NFTMinted(
        uint256 indexed tokenId,
        address indexed creator,
        string tokenURI,
        string workDescription
    );
    event RoyaltySet(
        uint256 indexed tokenId,
        address indexed recipient,
        uint256 percentage
    );

    constructor() ERC721("FreelancerWorkToken", "FWT") {}

    /**
     * @dev Mints a new NFT representing freelancer's work
     * @param recipient The address receiving the NFT
     * @param tokenURI The metadata URI for the NFT
     * @param workDescription Description of the freelancer's work
     * @param royaltyRecipient Address to receive royalties
     * @param royaltyPercentage Royalty percentage in basis points
     */
    function mintNFT(
        address recipient,
        string memory tokenURI,
        string memory workDescription,
        address royaltyRecipient,
        uint256 royaltyPercentage
    ) external returns (uint256) {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");
        require(bytes(workDescription).length > 0, "Work description cannot be empty");
        require(royaltyPercentage <= 10000, "Royalty percentage exceeds maximum (100%)");

        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        _safeMint(recipient, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        _creators[newTokenId] = msg.sender;
        _workDescriptions[newTokenId] = workDescription;

        if (royaltyPercentage > 0) {
            _royalties[newTokenId] = RoyaltyInfo(royaltyRecipient, royaltyPercentage);
            emit RoyaltySet(newTokenId, royaltyRecipient, royaltyPercentage);
        }

        emit NFTMinted(newTokenId, msg.sender, tokenURI, workDescription);
        return newTokenId;
    }

    /**
     * @dev Returns the creator of a specific token
     * @param tokenId The NFT to query
     */
    function getCreator(uint256 tokenId) public view returns (address) {
        require(_exists(tokenId), "Token does not exist");
        return _creators[tokenId];
    }

    /**
     * @dev Returns the work description of a specific token
     * @param tokenId The NFT to query
     */
    function getWorkDescription(uint256 tokenId) public view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _workDescriptions[tokenId];
    }

    /**
     * @dev Returns royalty information for a specific token
     * @param tokenId The NFT to query
     * @param salePrice The sale price of the NFT
     */
    function royaltyInfo(uint256 tokenId, uint256 salePrice)
        external
        view
        returns (address receiver, uint256 royaltyAmount)
    {
        require(_exists(tokenId), "Token does not exist");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        if (royalty.percentage == 0) {
            return (address(0), 0);
        }
        royaltyAmount = salePrice.mul(royalty.percentage).div(10000);
        return (royalty.recipient, royaltyAmount);
    }

    /**
     * @dev Sets royalty information for a specific token
     * @param tokenId The NFT to update
     * @param recipient Address to receive royalties
     * @param percentage Royalty percentage in basis points
     */
    function setRoyaltyInfo(
        uint256 tokenId,
        address recipient,
        uint256 percentage
    ) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender || owner() == msg.sender, "Not authorized");
        require(percentage <= 10000, "Royalty percentage exceeds maximum (100%)");

        _royalties[tokenId] = RoyaltyInfo(recipient, percentage);
        emit RoyaltySet(tokenId, recipient, percentage);
    }

    // Override functions
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
        delete _royalties[tokenId];
        delete _creators[tokenId];
        delete _workDescriptions[tokenId];
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
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
