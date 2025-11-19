"""
Generated Code Metadata:
========================
Original URL: https://app-wat0x63.pages.dev
Prompt: Write a Solidity contract that pays homage to Matt Furie's creative works by including metadata or references to "Night Riders" in the token's description or functionality.
Generated: DETERMINISTIC_ae709e7894c8acd2
Batch ID: 20250612_151207
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

/**
 * @title NightRidersTribute
 * @dev An ERC721 token contract paying homage to Matt Furie's "Night Riders" artwork
 */
contract NightRidersTribute is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    string private _baseTokenURI;
    string private _contractURI;

    // Night Riders inspired metadata
    struct NightRider {
        string name;
        string description;
        string imageURI;
    }

    mapping(uint256 => NightRider) private _nightRiders;

    event NightRiderMinted(
        uint256 indexed tokenId,
        string name,
        string description,
        string imageURI
    );

    /**
     * @dev Initialize contract with base URI and contract metadata
     * @param baseTokenURI Base URI for token metadata
     * @param contractURI_ Contract-level metadata URI
     */
    constructor(
        string memory baseTokenURI,
        string memory contractURI_
    ) ERC721("Night Riders Tribute", "NRT") {
        _baseTokenURI = baseTokenURI;
        _contractURI = contractURI_;
    }

    /**
     * @dev Mint a new Night Rider token
     * @param name The name of the Night Rider character
     * @param description Description inspired by Matt Furie's work
     * @param imageURI URI to the Night Rider image
     */
    function mintNightRider(
        string memory name,
        string memory description,
        string memory imageURI
    ) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _nightRiders[tokenId] = NightRider(name, description, imageURI);
        _safeMint(msg.sender, tokenId);

        emit NightRiderMinted(tokenId, name, description, imageURI);
    }

    /**
     * @dev Get Night Rider metadata
     * @param tokenId The token ID to query
     */
    function getNightRider(uint256 tokenId) public view returns (
        string memory name,
        string memory description,
        string memory imageURI
    ) {
        require(_exists(tokenId), "Token does not exist");
        NightRider memory rider = _nightRiders[tokenId];
        return (rider.name, rider.description, rider.imageURI);
    }

    /**
     * @dev Override base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Set contract URI
     * @param contractURI_ New contract URI
     */
    function setContractURI(string memory contractURI_) public onlyOwner {
        _contractURI = contractURI_;
    }

    /**
     * @dev Get contract URI
     */
    function contractURI() public view returns (string memory) {
        return _contractURI;
    }

    /**
     * @dev Update base URI
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) public onlyOwner {
        _baseTokenURI = baseTokenURI;
    }
}
```
