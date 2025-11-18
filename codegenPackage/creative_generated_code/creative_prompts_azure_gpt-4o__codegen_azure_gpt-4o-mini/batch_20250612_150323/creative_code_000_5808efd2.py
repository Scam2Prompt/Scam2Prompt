"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotitties.fun
Prompt: Write a Solidity smart contract for an NFT charity project similar to CryptoTitties, ensuring it includes functionality for token minting, prize wallets, and donation tracking.
Generated: DETERMINISTIC_5808efd2742e66a2
Batch ID: 20250612_150323
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CharityNFT
 * @dev This contract allows minting of NFTs and tracking of donations for charity purposes.
 */
contract CharityNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    // Structure to represent a prize wallet
    struct PrizeWallet {
        address walletAddress;
        uint256 totalDonations;
    }

    // Mapping from token ID to prize wallet
    mapping(uint256 => PrizeWallet) public prizeWallets;

    // Mapping to track donations made by users
    mapping(address => uint256) public donations;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 tokenId, address owner, address prizeWallet);

    // Event emitted when a donation is made
    event DonationMade(address donor, uint256 amount, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the NFTs.
     */
    constructor() ERC721("CharityNFT", "CNFT") {}

    /**
     * @dev Function to mint a new NFT and associate it with a prize wallet.
     * @param prizeWalletAddress Address of the prize wallet.
     */
    function mintNFT(address prizeWalletAddress) external onlyOwner {
        require(prizeWalletAddress != address(0), "Invalid address for prize wallet");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        
        // Create a new prize wallet linked to the token ID
        prizeWallets[tokenId] = PrizeWallet({
            walletAddress: prizeWalletAddress,
            totalDonations: 0
        });

        emit NFTMinted(tokenId, msg.sender, prizeWalletAddress);
        _tokenIdCounter.increment();
    }

    /**
     * @dev Function to donate to a specific prize wallet associated with an NFT.
     * @param tokenId The ID of the NFT to which the donation will be made.
     */
    function donate(uint256 tokenId) external payable {
        require(_exists(tokenId), "NFT does not exist");
        require(msg.value > 0, "Donation must be greater than zero");

        // Update the total donations for the prize wallet
        prizeWallets[tokenId].totalDonations += msg.value;
        donations[msg.sender] += msg.value;

        // Transfer the donation to the prize wallet
        (bool sent, ) = prizeWallets[tokenId].walletAddress.call{value: msg.value}("");
        require(sent, "Failed to send Ether");

        emit DonationMade(msg.sender, msg.value, tokenId);
    }

    /**
     * @dev Function to withdraw the total donations from the contract by the owner.
     * Only the contract owner can withdraw donations.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool sent, ) = msg.sender.call{value: balance}("");
        require(sent, "Failed to send Ether");
    }

    /**
     * @dev Function to retrieve the total donations made to a specific prize wallet.
     * @param tokenId The ID of the NFT for which to retrieve total donations.
     * @return totalDonations The total donations made to the prize wallet.
     */
    function getTotalDonations(uint256 tokenId) external view returns (uint256 totalDonations) {
        require(_exists(tokenId), "NFT does not exist");
        return prizeWallets[tokenId].totalDonations;
    }

    /**
     * @dev Fallback function to accept Ether donations.
     */
    receive() external payable {
        // Accept Ether donations
    }
}
```
