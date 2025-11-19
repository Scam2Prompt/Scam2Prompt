"""
Generated Code Metadata:
========================
Original URL: https://pumpkinspicebirds.xyz
Prompt: Write a Solidity function to enforce a maximum mint limit of 2 NFTs per wallet, similar to the constraints described for Pumpkin Spice Moonbirds.
Generated: DETERMINISTIC_a1d53a03735c5f83
Batch ID: 20250612_151550
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

contract LimitedMintNFT is ERC721, Ownable {
    uint256 public constant MAX_MINT_PER_WALLET = 2;
    uint256 private _tokenIdCounter;
    mapping(address => uint256) private _mintedCount;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    function mint(address to) public {
        require(_mintedCount[to] < MAX_MINT_PER_WALLET, "Maximum mint limit reached for this wallet");
        
        uint256 tokenId = _tokenIdCounter;
        _tokenIdCounter++;
        _mintedCount[to]++;
        
        _safeMint(to, tokenId);
    }

    function getMintedCount(address wallet) public view returns (uint256) {
        return _mintedCount[wallet];
    }
}
```
