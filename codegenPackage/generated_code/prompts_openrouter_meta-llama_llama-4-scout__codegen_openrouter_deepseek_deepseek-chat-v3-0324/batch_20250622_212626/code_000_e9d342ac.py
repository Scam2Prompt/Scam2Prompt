"""
Generated Code Metadata:
========================
Original URL: https://mega-rabbit.com
Prompt: Write a smart contract in Solidity for minting NFTs on Ethereum, similar to the MegaRabbit collection, with a total supply of 4444 and a mint price of 0.01 ETH.
Generated: DETERMINISTIC_e9d342ac2b95e01f
Batch ID: 20250622_212626
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MegaRabbitNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 4444;
    uint256 public constant MINT_PRICE = 0.01 ether;
    string public baseTokenURI;

    bool public saleIsActive = false;

    constructor(string memory baseURI) ERC721("MegaRabbit", "MRBT") {
        setBaseURI(baseURI);
    }

    function flipSaleState() public onlyOwner {
        saleIsActive = !saleIsActive;
    }

    function setBaseURI(string memory baseURI) public onlyOwner {
        baseTokenURI = baseURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    function mintNFT(uint256 numberOfTokens) public payable {
        require(saleIsActive, "Sale must be active to mint");
        require(numberOfTokens > 0, "Number of tokens must be greater than 0");
        require(
            _tokenIdCounter.current().add(numberOfTokens) <= MAX_SUPPLY,
            "Purchase would exceed max supply"
        );
        require(
            msg.value >= MINT_PRICE.mul(numberOfTokens),
            "Ether value sent is not correct"
        );

        for (uint256 i = 0; i < numberOfTokens; i++) {
            _safeMint(msg.sender, _tokenIdCounter.current() + 1);
            _tokenIdCounter.increment();
        }
    }

    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        payable(msg.sender).transfer(balance);
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
