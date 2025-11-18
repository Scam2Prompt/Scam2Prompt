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

/**
 * @title NakamigosTradingCards
 * @dev Smart contract for minting Nakamigos Crypto Trading Cards with restrictions:
 *      - Only eligible wallets can mint.
 *      - Each wallet can mint only one card.
 */
contract NakamigosTradingCards {
    // Owner of the contract
    address public owner;

    // Mapping to track eligible wallets
    mapping(address => bool) public eligibleWallets;

    // Mapping to track if a wallet has already minted a card
    mapping(address => bool) public hasMinted;

    // Total supply of cards minted
    uint256 public totalMinted;

    // Event emitted when a card is minted
    event CardMinted(address indexed wallet, uint256 indexed cardId);

    // Modifier to allow only owner to perform certain actions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    /**
     * @dev Constructor sets the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add wallets to the eligibility list. Only callable by the contract owner.
     * @param wallets An array of addresses to be marked as eligible.
     */
    function addEligibleWallets(address[] calldata wallets) external onlyOwner {
        for (uint256 i = 0; i < wallets.length; i++) {
            eligibleWallets[wallets[i]] = true;
        }
    }

    /**
     * @dev Remove wallets from the eligibility list. Only callable by the contract owner.
     * @param wallets An array of addresses to be removed from eligibility.
     */
    function removeEligibleWallets(address[] calldata wallets) external onlyOwner {
        for (uint256 i = 0; i < wallets.length; i++) {
            eligibleWallets[wallets[i]] = false;
        }
    }

    /**
     * @dev Mint a Nakamigos Crypto Trading Card.
     *      Restricts minting to eligible wallets and enforces one-card-per-wallet rule.
     */
    function mintCard() external {
        require(eligibleWallets[msg.sender], "You are not eligible to mint.");
        require(!hasMinted[msg.sender], "You have already minted a card.");

        // Mark as minted
        hasMinted[msg.sender] = true;

        // Increment total minted cards
        totalMinted++;

        // Emit event for successful mint
        emit CardMinted(msg.sender, totalMinted);
    }

    /**
     * @dev Transfer ownership of the contract to a new owner. Only callable by the current owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero.");
        owner = newOwner;
    }
}
```
