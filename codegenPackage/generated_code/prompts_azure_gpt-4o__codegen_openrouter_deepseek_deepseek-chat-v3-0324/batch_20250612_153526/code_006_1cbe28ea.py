"""
Generated Code Metadata:
========================
Original URL: https://disney-pinnacles.web.app
Prompt: Develop a smart contract that enables users to mint Disney-themed NFTs, referencing the collaboration between Disney and Dapper Labs.
Generated: DETERMINISTIC_1cbe28ea25759293
Batch ID: 20250612_153526
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

/**
 * @title DisneyNFT
 * @dev ERC721 token representing Disney-themed NFTs in collaboration with Dapper Labs
 */
contract DisneyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Price per NFT in wei
    uint256 public mintPrice = 0.1 ether;

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor sets the name and symbol of the token
     * @param baseURI The base URI for token metadata
     */
    constructor(string memory baseURI) ERC721("Disney x Dapper NFTs", "DXD") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new NFT to the specified address
     * @param to The address that will receive the NFT
     */
    function safeMint(address to) public payable {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(msg.value >= mintPrice, "Insufficient payment");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);

        emit Minted(to, tokenId);
    }

    /**
     * @dev Returns the total supply of minted NFTs
     * @return The total number of NFTs minted
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Sets the base URI for all token metadata
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for token metadata
     * @return The base URI string
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the URI for a given token ID
     * @param tokenId The token ID to query
     * @return The token URI string
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return string(abi.encodePacked(_baseURI(), tokenId.toString(), ".json"));
    }

    /**
     * @dev Updates the mint price
     * @param newPrice The new mint price in wei
     */
    function setMintPrice(uint256 newPrice) public onlyOwner {
        mintPrice = newPrice;
    }

    /**
     * @dev Withdraws contract balance to owner
     */
    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }
}
```
