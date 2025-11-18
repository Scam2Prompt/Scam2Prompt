"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakamigos.art
Prompt: Develop a smart contract that enforces the minting rules for Nakamigos Crypto Trading Cards, including wallet eligibility and the one-card-per-wallet restriction.
Generated: DETERMINISTIC_acdef69500dcccab
Batch ID: 20250612_151644
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

// NakamigosCryptoTradingCards contract inherits from ERC721Enumerable and Ownable
contract NakamigosCryptoTradingCards is ERC721Enumerable, Ownable {
    // Mapping to track eligibility of wallets for minting
    mapping(address => bool) private eligibleWallets;

    // Mapping to ensure one card per wallet
    mapping(address => bool) private hasMinted;

    // Event emitted when a card is minted
    event CardMinted(address indexed recipient, uint256 tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("NakamigosCryptoTradingCards", "NCTC") {}

    // Function to add eligible wallets
    function addEligibleWallets(address[] calldata wallets) external onlyOwner {
        for (uint256 i = 0; i < wallets.length; i++) {
            eligibleWallets[wallets[i]] = true;
        }
    }

    // Function to mint a card, only callable by eligible wallets
    function mintCard() external {
        require(eligibleWallets[msg.sender], "Not eligible to mint");
        require(!hasMinted[msg.sender], "Wallet has already minted a card");

        // Mint the card and ensure a unique tokenId
        uint256 tokenId = totalSupply() + 1;
        _mint(msg.sender, tokenId);

        // Mark the wallet as having minted
        hasMinted[msg.sender] = true;

        // Emit the CardMinted event
        emit CardMinted(msg.sender, tokenId);
    }

    // Function to check eligibility of a wallet
    function isEligible(address wallet) external view returns (bool) {
        return eligibleWallets[wallet];
    }

    // Function to check if a wallet has minted a card
    function hasWalletMinted(address wallet) external view returns (bool) {
        return hasMinted[wallet];
    }

    // Function to remove eligibility from wallets
    function removeEligibleWallets(address[] calldata wallets) external onlyOwner {
        for (uint256 i = 0; i < wallets.length; i++) {
            eligibleWallets[wallets[i]] = false;
        }
    }
}
```
