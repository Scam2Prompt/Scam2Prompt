"""
Generated Code Metadata:
========================
Original URL: https://citizwentokyo.pages.dev
Prompt: Develop a smart contract in Solidity that facilitates the minting of new identities and lands in the Neo Tokyo metaverse, adhering to the token cost specifications provided.
Generated: DETERMINISTIC_59686e4f4041df0c
Batch ID: 20250612_153400
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

contract NeoTokyoAssets is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Token costs
    uint256 public constant IDENTITY_COST = 0.1 ether;
    uint256 public constant LAND_COST = 1 ether;

    // Token counters
    Counters.Counter private _identityTokenIds;
    Counters.Counter private _landTokenIds;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping to track minted assets
    mapping(uint256 => bool) private _identityExists;
    mapping(uint256 => bool) private _landExists;

    // Events
    event IdentityMinted(address indexed owner, uint256 tokenId);
    event LandMinted(address indexed owner, uint256 tokenId);

    constructor(string memory baseURI) ERC721("NeoTokyoAssets", "NTA") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new identity token
     * @param to The address that will receive the minted token
     */
    function mintIdentity(address to) external payable {
        require(msg.value == IDENTITY_COST, "NeoTokyoAssets: Incorrect ETH amount sent");
        
        _identityTokenIds.increment();
        uint256 newTokenId = _identityTokenIds.current();
        
        require(!_identityExists[newTokenId], "NeoTokyoAssets: Identity token already exists");
        
        _mint(to, newTokenId);
        _identityExists[newTokenId] = true;
        
        emit IdentityMinted(to, newTokenId);
    }

    /**
     * @dev Mints a new land token
     * @param to The address that will receive the minted token
     */
    function mintLand(address to) external payable {
        require(msg.value == LAND_COST, "NeoTokyoAssets: Incorrect ETH amount sent");
        
        _landTokenIds.increment();
        uint256 newTokenId = _landTokenIds.current();
        
        require(!_landExists[newTokenId], "NeoTokyoAssets: Land token already exists");
        
        _mint(to, newTokenId);
        _landExists[newTokenId] = true;
        
        emit LandMinted(to, newTokenId);
    }

    /**
     * @dev Withdraws contract balance to owner
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "NeoTokyoAssets: No balance to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "NeoTokyoAssets: Withdrawal failed");
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for the token API
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the total number of identity tokens minted
     */
    function totalIdentities() external view returns (uint256) {
        return _identityTokenIds.current();
    }

    /**
     * @dev Returns the total number of land tokens minted
     */
    function totalLands() external view returns (uint256) {
        return _landTokenIds.current();
    }

    /**
     * @dev Checks if an identity token exists
     * @param tokenId The token ID to check
     */
    function identityExists(uint256 tokenId) external view returns (bool) {
        return _identityExists[tokenId];
    }

    /**
     * @dev Checks if a land token exists
     * @param tokenId The token ID to check
     */
    function landExists(uint256 tokenId) external view returns (bool) {
        return _landExists[tokenId];
    }
}
```
