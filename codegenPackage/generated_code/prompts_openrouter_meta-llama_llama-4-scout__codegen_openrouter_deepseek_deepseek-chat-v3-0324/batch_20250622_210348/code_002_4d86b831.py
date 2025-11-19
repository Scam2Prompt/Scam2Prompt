"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Generate a code snippet for a simple NFT minting process using Ethereum network, with a maximum of 5 NFTs per transaction and a fixed mint price.
Generated: DETERMINISTIC_4d86b831ed1d8dbd
Batch ID: 20250622_210348
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

contract SimpleNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_PER_TX = 5;
    uint256 public constant MINT_PRICE = 0.01 ether;
    string public baseURI;

    constructor(string memory _baseURI) ERC721("SimpleNFT", "SNFT") {
        baseURI = _baseURI;
    }

    function mintNFT(uint256 quantity) external payable {
        require(quantity > 0 && quantity <= MAX_PER_TX, "Invalid quantity");
        require(msg.value >= MINT_PRICE * quantity, "Insufficient payment");

        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(msg.sender, tokenId);
        }
    }

    function setBaseURI(string memory _newBaseURI) external onlyOwner {
        baseURI = _newBaseURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
