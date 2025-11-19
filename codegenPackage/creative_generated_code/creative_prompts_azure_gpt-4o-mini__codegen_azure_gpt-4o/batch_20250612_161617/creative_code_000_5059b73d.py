"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Generate a smart contract in Solidity for minting NFTs on the Ethereum network, specifically for a project like KevinLand where users can adopt multiple NFTs at once.
Generated: DETERMINISTIC_5059b73d92ab3bc3
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract KevinLandNFT is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private baseURI;
    
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Price per NFT
    uint256 public constant PRICE = 0.05 ether;

    // Maximum NFTs that can be minted in one transaction
    uint256 public constant MAX_MINT_AMOUNT = 10;

    constructor(string memory _baseURI) ERC721("KevinLandNFT", "KEVIN") {
        baseURI = _baseURI;
    }

    /**
     * @dev Mint multiple NFTs at once.
     * @param _amount Number of NFTs to mint.
     */
    function adoptMultipleNFTs(uint256 _amount) external payable {
        require(_amount > 0, "Cannot mint 0 NFTs");
        require(_amount <= MAX_MINT_AMOUNT, "Exceeds maximum mint amount per transaction");
        require(totalSupply() + _amount <= MAX_SUPPLY, "Exceeds maximum supply");
        require(msg.value >= _amount * PRICE, "Insufficient ETH sent");

        for (uint256 i = 0; i < _amount; i++) {
            uint256 tokenId = totalSupply() + 1;
            _safeMint(msg.sender, tokenId);
        }
    }

    /**
     * @dev Override the base URI getter to return the set base URI.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Update the base URI for metadata.
     * Can only be called by the contract owner.
     * @param _newBaseURI New base URI string.
     */
    function setBaseURI(string memory _newBaseURI) external onlyOwner {
        baseURI = _newBaseURI;
    }

    /**
     * @dev Withdraw funds from the contract.
     * Can only be called by the contract owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }
}
```
