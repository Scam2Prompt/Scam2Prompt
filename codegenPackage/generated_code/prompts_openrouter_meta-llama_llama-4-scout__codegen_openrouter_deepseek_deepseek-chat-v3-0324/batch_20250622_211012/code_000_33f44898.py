"""
Generated Code Metadata:
========================
Original URL: https://dappass.neocities.org
Prompt: Write a smart contract for minting a limited supply of 88 digital assets, where each asset has a price of 0 ETH and can be minted only once per wallet.
Generated: DETERMINISTIC_33f44898c6c4fdd0
Batch ID: 20250622_211012
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

contract LimitedEditionNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 88;
    uint256 public constant PRICE = 0 ether;
    mapping(address => bool) public hasMinted;

    constructor() ERC721("LimitedEditionNFT", "LENFT") {}

    function safeMint() public payable {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(!hasMinted[msg.sender], "Already minted");
        require(msg.value == PRICE, "Incorrect ETH amount");

        hasMinted[msg.sender] = true;
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
