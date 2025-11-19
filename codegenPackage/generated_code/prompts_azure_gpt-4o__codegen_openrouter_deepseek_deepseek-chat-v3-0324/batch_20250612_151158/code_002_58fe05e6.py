"""
Generated Code Metadata:
========================
Original URL: https://bobothebear.pages.dev
Prompt: Create a smart contract in Solidity for minting NFTs in the style of the Bobo Council NFT collection, ensuring the total supply is capped at 2,222 as specified on the website.
Generated: DETERMINISTIC_58fe05e6236b842a
Batch ID: 20250612_151158
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

contract BoboCouncilNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 2222;
    string public baseURI;

    constructor(string memory _initBaseURI) ERC721("Bobo Council NFT", "BOBO") {
        baseURI = _initBaseURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    function setBaseURI(string memory _newBaseURI) external onlyOwner {
        baseURI = _newBaseURI;
    }

    function safeMint(address to) external onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function remainingSupply() public view returns (uint256) {
        return MAX_SUPPLY - _tokenIdCounter.current();
    }
}
```
