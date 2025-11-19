"""
Generated Code Metadata:
========================
Original URL: https://ledqinlv.com
Prompt: Create a Solidity smart contract template for minting NFTs that can be listed and sold on OpenSea, including metadata customization.
Generated: DETERMINISTIC_ec4767f215630b3f
Batch ID: 20250612_150440
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

contract NFTTemplate is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Contract URI for OpenSea collection metadata
    string private _contractURI;

    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        string memory contractURI_
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        _contractURI = contractURI_;
    }

    // Mint a new NFT to the specified address
    function safeMint(address to, string memory tokenURI) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
    }

    // Override to return base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Set base URI (only owner)
    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
    }

    // Set contract URI (only owner)
    function setContractURI(string memory contractURI_) public onlyOwner {
        _contractURI = contractURI_;
    }

    // Get contract URI for OpenSea
    function contractURI() public view returns (string memory) {
        return _contractURI;
    }

    // The following functions are overrides required by Solidity
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
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

    // Withdraw funds from contract (only owner)
    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }

    // Accept any incoming payments
    receive() external payable {}
}
```
