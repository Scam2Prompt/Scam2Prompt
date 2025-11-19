"""
Generated Code Metadata:
========================
Original URL: https://frame-i48.pages.dev
Prompt: "Generate a smart contract code to deploy an NFT project on Frame's Ethereum-based rollup, utilizing the Arbitrum Nitro stack for low fees and fast block times."
Generated: DETERMINISTIC_70b8a7dc4185ac5d
Batch ID: 20250622_204657
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title NFTProject
 * @author [Your Name]
 * @notice A smart contract for deploying an NFT project on Frame's Ethereum-based rollup,
 *         utilizing the Arbitrum Nitro stack for low fees and fast block times.
 */
contract NFTProject is SafeERC721, Ownable {
    // Mapping of token IDs to their owners
    mapping (address => mapping (uint256 => bool)) private _tokenOwners;

    // Mapping of token IDs to their URIs
    mapping (uint256 => string) private _tokenURIs;

    // Total supply of NFTs
    uint256 private _totalSupply;

    // Base URI for all NFTs
    string private _baseURI;

    /**
     * @dev Constructor
     * @param name The name of the NFT project
     * @param symbol The symbol of the NFT project
     */
    constructor(string memory name, string memory symbol) public SafeERC721(name, symbol) {
        _totalSupply = 0;
    }

    /**
     * @dev Mint an NFT
     * @param to The address to mint the NFT to
     * @param tokenId The ID of the NFT to mint
     * @param uri The URI of the NFT
     */
    function mint(address to, uint256 tokenId, string memory uri) public onlyOwner {
        _mint(to, tokenId);
        _tokenURIs[tokenId] = uri;
        _totalSupply++;
    }

    /**
     * @dev Burn an NFT
     * @param tokenId The ID of the NFT to burn
     */
    function burn(uint256 tokenId) public {
        require(_isApprovedOrOwner(msg.sender, tokenId), "NFTProject: caller is not owner nor approved");
        _burn(tokenId);
        _totalSupply--;
    }

    /**
     * @dev Get the URI of an NFT
     * @param tokenId The ID of the NFT
     * @return The URI of the NFT
     */
    function tokenURI(uint256 tokenId) public view returns (string memory) {
        require(_exists(tokenId), "NFTProject: URI query for nonexistent token");
        return string(abi.encodePacked(_baseURI, _tokenURIs[tokenId]));
    }

    /**
     * @dev Get the total supply of NFTs
     * @return The total supply of NFTs
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Set the base URI for all NFTs
     * @param baseURI The base URI
     */
    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseURI = baseURI;
    }

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal override {
        for (uint256 i = 0; i < ids.length; i++) {
            uint256 id = ids[i];
            require(_isApprovedOrOwner(msg.sender, id), "NFTProject: transfer caller is not owner nor approved");
        }
    }

    function _afterTokenTransfer(address from, address to, uint256[] memory ids) internal override {
        for (uint256 i = 0; i < ids.length; i++) {
            uint256 id = ids[i];
            if (_tokenOwners[to][id]) {
                _tokenOwners[to][id] = true;
            } else {
                _tokenOwners[from][id] = false;
            }
        }
    }
}
```
