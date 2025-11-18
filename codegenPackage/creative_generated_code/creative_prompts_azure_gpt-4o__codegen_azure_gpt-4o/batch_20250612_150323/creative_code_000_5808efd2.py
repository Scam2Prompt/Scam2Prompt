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

// Importing OpenZeppelin libraries for ERC721 and access control.
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CharityNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIds;

    // Address to hold the donations
    address public donationWallet;

    // Mapping to track the total donations for each token
    mapping(uint256 => uint256) public tokenDonations;

    // Event emitted when a new token is minted
    event TokenMinted(uint256 tokenId, address owner);

    // Event emitted when a donation is made
    event DonationReceived(uint256 tokenId, address donor, uint256 amount);

    // Constructor to initialize the NFT name, symbol, and donation wallet
    constructor(address _donationWallet) ERC721("CharityNFT", "CHNFT") {
        require(_donationWallet != address(0), "Invalid donation wallet address");
        donationWallet = _donationWallet;
    }

    // Function to mint new tokens
    function mintToken(address recipient) external onlyOwner returns (uint256) {
        require(recipient != address(0), "Invalid recipient address");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();
        _safeMint(recipient, newTokenId);

        emit TokenMinted(newTokenId, recipient);
        return newTokenId;
    }

    // Function to make a donation to a specific token
    function donateToToken(uint256 tokenId) external payable {
        require(_exists(tokenId), "Token does not exist");
        require(msg.value > 0, "Donation amount must be greater than zero");

        // Track the donation amount for this token
        tokenDonations[tokenId] += msg.value;

        // Transfer the donation to the donation wallet
        (bool success, ) = donationWallet.call{value: msg.value}("");
        require(success, "Transfer to donation wallet failed");

        emit DonationReceived(tokenId, msg.sender, msg.value);
    }

    // Function to update the donation wallet, only callable by the owner
    function updateDonationWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Invalid wallet address");
        donationWallet = newWallet;
    }

    // Function to withdraw contract balance (failsafe) – only callable by owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    // Fallback function to prevent accidental Ether submissions
    receive() external payable {
        revert("Direct payments not accepted");
    }
}
```
