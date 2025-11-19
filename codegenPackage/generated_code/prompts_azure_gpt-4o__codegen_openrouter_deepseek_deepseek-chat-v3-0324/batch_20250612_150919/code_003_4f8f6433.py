"""
Generated Code Metadata:
========================
Original URL: https://meowworldsnft.pages.dev
Prompt: Create a Solidity smart contract for minting Meow Worlds NFTs, ensuring the total supply is capped at 10,000 and includes metadata for characters, environments, and artifacts.
Generated: DETERMINISTIC_4f8f64332dcc932b
Batch ID: 20250612_150919
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

contract MeowWorldsNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 10000;
    string public baseURI;

    struct MeowMetadata {
        string character;
        string environment;
        string artifact;
    }

    mapping(uint256 => MeowMetadata) private _tokenMetadata;

    constructor(string memory name, string memory symbol, string memory _baseURI) ERC721(name, symbol) {
        baseURI = _baseURI;
    }

    function safeMint(address to, string memory character, string memory environment, string memory artifact) public onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        
        _tokenMetadata[tokenId] = MeowMetadata(character, environment, artifact);
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        
        return string(abi.encodePacked(baseURI, Strings.toString(tokenId)));
    }

    function getMetadata(uint256 tokenId) public view returns (MeowMetadata memory) {
        require(_exists(tokenId), "Metadata query for nonexistent token");
        return _tokenMetadata[tokenId];
    }

    function setBaseURI(string memory _baseURI) public onlyOwner {
        baseURI = _baseURI;
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
