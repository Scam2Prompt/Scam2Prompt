"""
Generated Code Metadata:
========================
Original URL: https://cryptotitties.fun
Prompt: Generate a Solidity contract for an NFT charity project similar to CryptOtitties, including features for donation tracking and ERC721 compliance.
Generated: DETERMINISTIC_832cb84233d8e55b
Batch ID: 20250612_135046
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

// Importing the ERC721 interface and the Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// CharityNFT contract inherits from ERC721 and Ownable
contract CharityNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to donation amount
    mapping(uint256 => uint256) private _donationAmounts;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, uint256 donationAmount);

    // Event emitted when a donation is made
    event DonationReceived(address indexed donor, uint256 indexed tokenId, uint256 amount);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("CharityNFT", "CNFT") {}

    // Function to mint a new NFT with a donation amount
    function mintNFT(uint256 donationAmount) external onlyOwner {
        require(donationAmount > 0, "Donation amount must be greater than zero");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the owner
        _mint(msg.sender, tokenId);

        // Record the donation amount for the minted NFT
        _donationAmounts[tokenId] = donationAmount;

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId, donationAmount);
    }

    // Function to donate to a specific NFT
    function donateToNFT(uint256 tokenId) external payable {
        require(_exists(tokenId), "NFT does not exist");
        require(msg.value > 0, "Donation amount must be greater than zero");

        // Update the donation amount for the NFT
        _donationAmounts[tokenId] += msg.value;

        // Emit the DonationReceived event
        emit DonationReceived(msg.sender, tokenId, msg.value);
    }

    // Function to retrieve the donation amount for a specific NFT
    function getDonationAmount(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "NFT does not exist");
        return _donationAmounts[tokenId];
    }

    // Function to withdraw the total donations to the owner's address
    function withdrawDonations() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    // Function to check if a token exists
    function _exists(uint256 tokenId) internal view override returns (bool) {
        return super._exists(tokenId);
    }
}
```
