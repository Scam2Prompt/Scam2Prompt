"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Write a Solidity smart contract for minting NFTs that mimics the functionality described on KevinLand, including a maximum of 5 NFTs per transaction, the first 500 free, and a mint price of 0.03 ETH per NFT.
Generated: DETERMINISTIC_5a731c0c6645a2f6
Batch ID: 20250612_152827
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

/**
 * @title KevinLandNFT
 * @dev A smart contract for minting NFTs with specific functionality:
 *      - Max 5 NFTs per transaction
 *      - First 500 NFTs are free
 *      - Mint price is 0.03 ETH per NFT after the first 500
 */
contract KevinLandNFT is ERC721Enumerable, Ownable {
    uint256 public constant MAX_PER_TX = 5; // Maximum NFTs per transaction
    uint256 public constant FREE_NFTS = 500; // Number of free NFTs
    uint256 public constant MINT_PRICE = 0.03 ether; // Mint price per NFT
    uint256 public constant MAX_SUPPLY = 10000; // Maximum supply of NFTs
    uint256 public totalMinted; // Tracks the total number of NFTs minted

    constructor() ERC721("KevinLandNFT", "KLNFT") {}

    /**
     * @dev Mint NFTs
     * @param quantity The number of NFTs to mint
     */
    function mint(uint256 quantity) external payable {
        require(quantity > 0, "Must mint at least one NFT");
        require(quantity <= MAX_PER_TX, "Exceeds max NFTs per transaction");
        require(totalMinted + quantity <= MAX_SUPPLY, "Exceeds max supply");

        // Determine the cost based on the number of free NFTs remaining
        uint256 cost = 0;
        if (totalMinted >= FREE_NFTS) {
            cost = quantity * MINT_PRICE;
        } else if (totalMinted + quantity > FREE_NFTS) {
            uint256 paidQuantity = (totalMinted + quantity) - FREE_NFTS;
            cost = paidQuantity * MINT_PRICE;
        }

        // Ensure the correct payment is made
        require(msg.value >= cost, "Insufficient payment");

        // Mint the NFTs
        for (uint256 i = 0; i < quantity; i++) {
            _mint(msg.sender, totalMinted + 1);
            totalMinted++;
        }

        // Refund excess payment to the sender
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    /**
     * @dev Withdraw contract balance to owner
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}

    /**
     * @dev Fallback function if no function matches the call
     */
    fallback() external payable {}
}
```
