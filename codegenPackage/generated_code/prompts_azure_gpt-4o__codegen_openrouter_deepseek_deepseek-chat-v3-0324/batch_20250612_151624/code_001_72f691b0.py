"""
Generated Code Metadata:
========================
Original URL: https://test.fulviomenegozzo.com
Prompt: Create a smart contract in Solidity that limits NFT purchases to a maximum of 5 per wallet and includes functionality for setting a total price in ETH, based on the features of the Memeland pre-sale.
Generated: DETERMINISTIC_72f691b0efb09ad1
Batch ID: 20250612_151624
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

contract LimitedNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_PER_WALLET = 5;
    uint256 public price;
    bool public saleIsActive = false;

    mapping(address => uint256) private _walletMints;

    event PriceChanged(uint256 newPrice);
    event SaleStateChanged(bool newState);

    constructor(string memory name, string memory symbol, uint256 initialPrice) ERC721(name, symbol) {
        price = initialPrice;
    }

    function setPrice(uint256 newPrice) external onlyOwner {
        price = newPrice;
        emit PriceChanged(newPrice);
    }

    function toggleSaleState() external onlyOwner {
        saleIsActive = !saleIsActive;
        emit SaleStateChanged(saleIsActive);
    }

    function mintNFT(uint256 quantity) external payable {
        require(saleIsActive, "Sale is not active");
        require(quantity > 0, "Quantity must be greater than 0");
        require(_walletMints[msg.sender] + quantity <= MAX_PER_WALLET, "Exceeds max per wallet");
        require(msg.value >= price * quantity, "Insufficient ETH sent");

        _walletMints[msg.sender] += quantity;

        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(msg.sender, tokenId);
        }
    }

    function walletMints(address wallet) external view returns (uint256) {
        return _walletMints[wallet];
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
