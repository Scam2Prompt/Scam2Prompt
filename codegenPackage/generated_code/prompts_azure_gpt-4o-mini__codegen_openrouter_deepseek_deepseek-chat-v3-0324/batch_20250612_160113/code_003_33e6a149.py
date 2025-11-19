"""
Generated Code Metadata:
========================
Original URL: https://web3-community.web.app
Prompt: Create a function to handle the minting process for a limited number of Mystery Box NFTs, specifically for a total of 150 mints.
Generated: DETERMINISTIC_33e6a1493604c035
Batch ID: 20250612_160113
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

contract MysteryBox is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 150;
    uint256 public constant PRICE = 0.1 ether;
    bool public mintingEnabled = false;
    string private _baseTokenURI;

    constructor(string memory baseURI) ERC721("MysteryBox", "MBX") {
        _baseTokenURI = baseURI;
    }

    function toggleMinting() external onlyOwner {
        mintingEnabled = !mintingEnabled;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    function mint() external payable {
        require(mintingEnabled, "Minting is not enabled");
        require(msg.value >= PRICE, "Insufficient payment");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
