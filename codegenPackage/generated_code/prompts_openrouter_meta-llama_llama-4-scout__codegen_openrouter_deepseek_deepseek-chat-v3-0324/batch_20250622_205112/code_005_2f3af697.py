"""
Generated Code Metadata:
========================
Original URL: https://simpsontrump.pages.dev
Prompt: Create a Solidity contract for an AI-generated NFT minting platform, similar to the one planned in the Simpson Trump roadmap, and explain its key functions and variables.
Generated: DETERMINISTIC_2f3af697c8078281
Batch ID: 20250622_205112
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract AIGeneratedNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Token counter
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mint price
    uint256 public mintPrice;

    // Maximum supply
    uint256 public maxSupply;

    // Royalty percentage (basis points)
    uint256 public royaltyPercentage;

    // Mapping from token ID to AI generation parameters
    mapping(uint256 => string) private _generationParams;

    // Mapping from token ID to royalty recipient
    mapping(uint256 => address) private _royaltyRecipients;

    // Events
    event Minted(address indexed to, uint256 indexed tokenId, string generationParams);
    event RoyaltySet(uint256 indexed tokenId, address recipient, uint256 percentage);
    event BaseURIUpdated(string newBaseURI);
    event MintPriceUpdated(uint256 newPrice);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI,
        uint256 _mintPrice,
        uint256 _maxSupply,
        uint256 _royaltyPercentage
    ) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
        mintPrice = _mintPrice;
        maxSupply = _maxSupply;
        royaltyPercentage = _royaltyPercentage;
    }

    /**
     * @dev Mints a new NFT with AI-generated content
     * @param generationParams Parameters used to generate the AI content
     */
    function mint(string memory generationParams) public payable nonReentrant {
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        require(msg.value >= mintPrice, "Insufficient payment");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        _generationParams[tokenId] = generationParams;
        _royaltyRecipients[tokenId] = msg.sender;

        emit Minted(msg.sender, tokenId, generationParams);
    }

    /**
     * @dev Sets royalty information for a specific token
     * @param tokenId The token ID to set royalty for
     * @param recipient Address to receive royalties
     * @param percentage Royalty percentage (basis points)
     */
    function setRoyaltyInfo(
        uint256 tokenId,
        address recipient,
        uint256 percentage
    ) public {
        require(_exists(tokenId), "Nonexistent token");
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        require(percentage <= 10000, "Royalty too high");

        _royaltyRecipients[tokenId] = recipient;
        royaltyPercentage = percentage;

        emit RoyaltySet(tokenId, recipient, percentage);
    }

    /**
     * @dev Returns the royalty information for a token
     * @param tokenId The token ID to query
     * @param salePrice The sale price of the token
     * @return receiver Address to receive royalties
     * @return royaltyAmount The royalty amount
     */
    function royaltyInfo(uint256 tokenId, uint256 salePrice)
        external
        view
        returns (address receiver, uint256 royaltyAmount)
    {
        require(_exists(tokenId), "Nonexistent token");
        royaltyAmount = (salePrice * royaltyPercentage) / 10000;
        receiver = _royaltyRecipients[tokenId];
    }

    /**
     * @dev Updates the base URI for token metadata
     * @param newBaseURI The new base URI
     */
    function setBaseURI(string memory newBaseURI) public onlyOwner {
        _baseTokenURI = newBaseURI;
        emit BaseURIUpdated(newBaseURI);
    }

    /**
     * @dev Updates the mint price
     * @param newPrice The new mint price
     */
    function setMintPrice(uint256 newPrice) public onlyOwner {
        mintPrice = newPrice;
        emit MintPriceUpdated(newPrice);
    }

    /**
     * @dev Withdraws contract balance to owner
     */
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Returns the generation parameters for a token
     * @param tokenId The token ID to query
     * @return The generation parameters
     */
    function getGenerationParams(uint256 tokenId) public view returns (string memory) {
        require(_exists(tokenId), "Nonexistent token");
        return _generationParams[tokenId];
    }

    /**
     * @dev Returns the base URI for token metadata
     * @return The base URI
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a token
     * @param tokenId The token ID to query
     * @return The token URI
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "Nonexistent token");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString()));
    }

    /**
     * @dev Returns the total supply
     * @return The total supply
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
