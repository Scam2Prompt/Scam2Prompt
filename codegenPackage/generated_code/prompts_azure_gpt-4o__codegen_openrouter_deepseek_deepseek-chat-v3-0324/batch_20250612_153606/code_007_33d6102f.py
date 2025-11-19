"""
Generated Code Metadata:
========================
Original URL: https://t1-32y.pages.dev
Prompt: Write a function in Solidity to enforce a maximum mint limit per wallet, as described in the Blaze NFT collection's contract.
Generated: DETERMINISTIC_33d6102f95ea6502
Batch ID: 20250612_153606
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

contract BlazeNFT is ERC721, Ownable {
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MAX_MINT_PER_WALLET = 5;
    uint256 public totalSupply;
    mapping(address => uint256) public mintedPerWallet;

    constructor() ERC721("BlazeNFT", "BLAZE") {}

    function mint(address to, uint256 quantity) external {
        require(totalSupply + quantity <= MAX_SUPPLY, "Exceeds max supply");
        require(
            mintedPerWallet[msg.sender] + quantity <= MAX_MINT_PER_WALLET,
            "Exceeds max mint per wallet"
        );
        
        for (uint256 i = 0; i < quantity; i++) {
            _safeMint(to, totalSupply + i);
        }
        
        totalSupply += quantity;
        mintedPerWallet[msg.sender] += quantity;
    }
}
```
