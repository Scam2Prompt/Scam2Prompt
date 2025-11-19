"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://timcheese.pages.dev
Prompt: How can I create a smart contract to mint NFTs for a collection like Tim Cheese's 10,000 diverse tim?
Generated: DETERMINISTIC_5b94d6fc863f57ee
Batch ID: 20250612_161226
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

/**
 * @title TimCheeseNFTCollection
 * @dev A smart contract for minting NFTs for a 10,000-item collection. This contract follows ERC721 standards.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TimCheeseNFTCollection is ERC721Enumerable, Ownable {
    uint256 public constant MAX_SUPPLY = 10000; // Maximum number of NFTs
    uint256 public constant MINT_PRICE = 0.05 ether; // Price per NFT
    string private baseTokenURI; // Base URI for metadata

    constructor(string memory _baseTokenURI) ERC721("Tim Cheese Collection", "TCC") {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Mint a new NFT.
     * @param amount The number of NFTs to mint.
     */
    function mint(uint256 amount) external payable {
        require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds maximum supply");
        require(msg.value == amount * MINT_PRICE, "Incorrect Ether value");

        for (uint256 i = 0; i < amount; i++) {
            uint256 tokenId = totalSupply(); // Token ID starts at 0
            _safeMint(msg.sender, tokenId);
        }
    }

    /**
     * @dev Set the base URI for metadata.
     * @param _baseTokenURI The new base URI.
     */
    function setBaseURI(string memory _baseTokenURI) external onlyOwner {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Override the baseURI method to return the stored base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Withdraw the contract balance to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Ether cannot be sent directly to the contract");
    }
}
```
