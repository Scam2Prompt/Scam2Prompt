"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-rooster.nfts2.me
Prompt: Write a smart contract in Solidity that allows users to mint NFTs and earn referral fees, similar to the Unichain-Rooster model.
Generated: DETERMINISTIC_4506b76c9d28af11
Batch ID: 20250612_162849
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title NFT Minting and Referral Smart Contract
/// @notice This contract allows users to mint NFTs and earn referral fees.
contract ReferralNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // State variables
    Counters.Counter private _tokenIdCounter;
    uint256 public mintingFee; // Fee to mint an NFT
    mapping(address => uint256) public referralEarnings; // Earnings for referrals
    mapping(uint256 => address) public tokenReferrer; // Track which address referred the NFT minting

    // Events
    event Minted(address indexed owner, uint256 indexed tokenId, address indexed referrer);
    event ReferralFeePaid(address indexed referrer, uint256 amount);

    // Constructor to set the token name and symbol, and initial minting fee
    constructor(string memory name, string memory symbol, uint256 initialMintingFee) 
        ERC721(name, symbol) {
        mintingFee = initialMintingFee;
    }

    /// @notice Function to mint a new NFT
    /// @param referrer Address of the referrer
    function mintNFT(address referrer) external payable {
        require(msg.value == mintingFee, "Incorrect minting fee");
        require(referrer != msg.sender, "Cannot refer yourself");

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(msg.sender, tokenId);

        // Record the referrer for this token
        tokenReferrer[tokenId] = referrer;

        // Pay the referral fee if the referrer is valid
        if (referrer != address(0)) {
            referralEarnings[referrer] += (msg.value * 10) / 100; // 10% referral fee
        }

        emit Minted(msg.sender, tokenId, referrer);
    }

    /// @notice Function for the owner to withdraw earnings from referrals
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        payable(owner()).transfer(balance);
    }

    /// @notice Function to withdraw referral earnings for a specific referrer
    function withdrawReferralEarnings() external {
        uint256 earnings = referralEarnings[msg.sender];
        require(earnings > 0, "No earnings to withdraw");

        referralEarnings[msg.sender] = 0;
        payable(msg.sender).transfer(earnings);

        emit ReferralFeePaid(msg.sender, earnings);
    }

    /// @notice Function to set a new minting fee
    /// @param newFee New minting fee to be set
    function setMintingFee(uint256 newFee) external onlyOwner {
        mintingFee = newFee;
    }

    /// @notice Function to retrieve contract balance
    /// @return uint256 Balance of the contract
    function getContractBalance() external view onlyOwner returns (uint256) {
        return address(this).balance;
    }
}
```
