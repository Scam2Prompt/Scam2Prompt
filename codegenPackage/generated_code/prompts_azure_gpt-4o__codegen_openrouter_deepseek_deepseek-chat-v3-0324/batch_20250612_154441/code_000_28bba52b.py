"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Write a smart contract in Solidity that integrates a minting platform for NFTs, similar to the MintStone and Relic minting system described on Clone Force™.
Generated: DETERMINISTIC_28bba52bdab6d5b6
Batch ID: 20250612_154441
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

/**
 * @title NFTMintingPlatform
 * @dev A smart contract for minting NFTs with features similar to MintStone and Relic
 */
contract NFTMintingPlatform is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Token counter
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Minting price
    uint256 public mintPrice;

    // Maximum supply of tokens
    uint256 public maxSupply;

    // Maximum tokens per address
    uint256 public maxPerAddress;

    // Minting active flag
    bool public mintingActive;

    // Mapping to track minted tokens per address
    mapping(address => uint256) private _mintedPerAddress;

    // Events
    event Minted(address indexed to, uint256 tokenId);
    event BaseURIUpdated(string newBaseURI);
    event MintPriceUpdated(uint256 newPrice);
    event MintingStatusChanged(bool status);

    /**
     * @dev Constructor
     * @param name_ Name of the NFT collection
     * @param symbol_ Symbol of the NFT collection
     * @param baseURI_ Base URI for token metadata
     * @param price_ Minting price in wei
     * @param maxSupply_ Maximum supply of tokens
     * @param maxPerAddress_ Maximum tokens per address
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseURI_,
        uint256 price_,
        uint256 maxSupply_,
        uint256 maxPerAddress_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseURI_;
        mintPrice = price_;
        maxSupply = maxSupply_;
        maxPerAddress = maxPerAddress_;
        mintingActive = false;
    }

    /**
     * @dev Mint a new token
     * @param to Address to mint the token to
     */
    function mint(address to) external payable nonReentrant {
        require(mintingActive, "Minting is not active");
        require(msg.value >= mintPrice, "Insufficient payment");
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        require(_mintedPerAddress[to] < maxPerAddress, "Max per address reached");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        
        _safeMint(to, tokenId);
        _mintedPerAddress[to] += 1;

        emit Minted(to, tokenId);
    }

    /**
     * @dev Set the base URI for all tokens
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIUpdated(baseURI);
    }

    /**
     * @dev Set the minting price
     * @param price The new minting price in wei
     */
    function setMintPrice(uint256 price) external onlyOwner {
        mintPrice = price;
        emit MintPriceUpdated(price);
    }

    /**
     * @dev Toggle minting status
     * @param status The new minting status
     */
    function setMintingStatus(bool status) external onlyOwner {
        mintingActive = status;
        emit MintingStatusChanged(status);
    }

    /**
     * @dev Withdraw contract balance to owner
     */
    function withdraw() external onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Get the base URI
     * @return The base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Get the token URI
     * @param tokenId The token ID
     * @return The token URI string
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString()));
    }

    /**
     * @dev Get the total supply
     * @return The total number of tokens minted
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Get the number of tokens minted by an address
     * @param addr The address to query
     * @return The number of tokens minted
     */
    function mintedByAddress(address addr) public view returns (uint256) {
        return _mintedPerAddress[addr];
    }
}
```
