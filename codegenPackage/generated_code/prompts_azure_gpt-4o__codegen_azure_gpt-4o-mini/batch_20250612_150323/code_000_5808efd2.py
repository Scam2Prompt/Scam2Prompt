"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Write a Solidity smart contract for an NFT charity project similar to CryptoTitties, ensuring it includes functionality for token minting, prize wallets, and donation tracking.
Generated: DETERMINISTIC_5808efd2742e66a2
Batch ID: 20250612_150323
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

// @title CharityNFT
// @dev A smart contract for an NFT charity project that allows minting of NFTs, tracking donations, and managing prize wallets.
contract CharityNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to donation amount
    mapping(uint256 => uint256) public donations;

    // Address for prize wallet
    address public prizeWallet;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, uint256 donationAmount);

    // Event emitted when a donation is made
    event DonationReceived(address indexed donor, uint256 indexed tokenId, uint256 amount);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, address _prizeWallet) ERC721(name, symbol) {
        require(_prizeWallet != address(0), "Invalid prize wallet address");
        prizeWallet = _prizeWallet;
    }

    // @dev Function to mint a new NFT with a donation
    // @param donationAmount The amount of donation for minting the NFT
    function mintNFT(uint256 donationAmount) external payable {
        require(msg.value == donationAmount, "Donation amount must match the sent value");
        require(donationAmount > 0, "Donation must be greater than zero");

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(msg.sender, tokenId);

        // Track the donation
        donations[tokenId] = donationAmount;

        // Emit the NFT minting event
        emit NFTMinted(msg.sender, tokenId, donationAmount);

        // Transfer the donation to the prize wallet
        (bool success, ) = prizeWallet.call{value: msg.value}("");
        require(success, "Transfer to prize wallet failed");
    }

    // @dev Function to donate to a specific NFT
    // @param tokenId The ID of the NFT to donate to
    function donateToNFT(uint256 tokenId) external payable {
        require(_exists(tokenId), "NFT does not exist");
        require(msg.value > 0, "Donation must be greater than zero");

        // Track the donation
        donations[tokenId] += msg.value;

        // Emit the donation event
        emit DonationReceived(msg.sender, tokenId, msg.value);

        // Transfer the donation to the prize wallet
        (bool success, ) = prizeWallet.call{value: msg.value}("");
        require(success, "Transfer to prize wallet failed");
    }

    // @dev Function to withdraw funds from the prize wallet (only owner)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    // @dev Function to get the donation amount for a specific NFT
    // @param tokenId The ID of the NFT
    // @return The total donation amount for the specified NFT
    function getDonationAmount(uint256 tokenId) external view returns (uint256) {
        return donations[tokenId];
    }
}
```
