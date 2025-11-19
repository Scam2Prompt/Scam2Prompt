"""
Generated Code Metadata:
========================
Original URL: https://nakamigos.art
Prompt: Develop a smart contract that enforces the minting rules for Nakamigos Crypto Trading Cards, including wallet eligibility and the one-card-per-wallet restriction.
Generated: DETERMINISTIC_acdef69500dcccab
Batch ID: 20250612_151644
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

/**
 * @title NakamigosCryptoTradingCards
 * @dev A smart contract for minting Nakamigos Crypto Trading Cards with specific rules.
 */
contract NakamigosCryptoTradingCards is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track if a wallet has already minted a card
    mapping(address => bool) private _hasMinted;

    // Maximum number of cards that can be minted
    uint256 public constant MAX_CARDS = 1000;

    // Event emitted when a card is minted
    event CardMinted(address indexed owner, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     */
    constructor() ERC721("NakamigosCryptoTradingCards", "NCTC") {}

    /**
     * @dev Function to mint a new trading card.
     * Can only be called by eligible wallets that have not minted a card yet.
     */
    function mintCard() external {
        // Check if the maximum number of cards has been reached
        require(_tokenIdCounter.current() < MAX_CARDS, "Max cards minted");

        // Check if the caller has already minted a card
        require(!_hasMinted[msg.sender], "Wallet has already minted a card");

        // Mint the card
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);

        // Update the state
        _hasMinted[msg.sender] = true;
        _tokenIdCounter.increment();

        // Emit the minting event
        emit CardMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function to check if a wallet has minted a card.
     * @param wallet The address of the wallet to check.
     * @return bool indicating whether the wallet has minted a card.
     */
    function hasMinted(address wallet) external view returns (bool) {
        return _hasMinted[wallet];
    }

    /**
     * @dev Function to get the total number of minted cards.
     * @return uint256 The total number of minted cards.
     */
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
