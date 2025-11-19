"""
Generated Code Metadata:
========================
Original URL: https://molly-4uy.pages.dev
Prompt: Generate a smart contract code for creating and distributing NFTs on the Molly platform, similar to the "First Official NFT" offered for new signups.
Generated: DETERMINISTIC_356f9cb1401fa2d0
Batch ID: 20250622_210008
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

contract MollyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;
    string private _baseTokenURI;
    uint256 public constant MAX_SUPPLY = 10000;
    mapping(address => bool) private _hasClaimed;

    event NFTClaimed(address indexed recipient, uint256 tokenId);

    constructor(string memory baseURI) ERC721("MollyNFT", "MOL") {
        _baseTokenURI = baseURI;
    }

    function claimNFT() external {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        require(!_hasClaimed[msg.sender], "Address has already claimed NFT");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);
        _hasClaimed[msg.sender] = true;

        emit NFTClaimed(msg.sender, tokenId);
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString(), ".json"));
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function hasClaimed(address user) external view returns (bool) {
        return _hasClaimed[user];
    }

    function reserveNFTs(uint256 quantity, address recipient) external onlyOwner {
        require(_tokenIdCounter.current() + quantity <= MAX_SUPPLY, "Exceeds max supply");

        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(recipient, tokenId);
        }
    }
}
```
