"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zora-air-spring.nfts2.me
Prompt: Write a smart contract in Solidity that generates a referral link for a wallet address and tracks referral fees for minting NFTs, similar to the functionality described on the Zora Air Spring platform.
Generated: DETERMINISTIC_bfc01f7cec7c19fc
Batch ID: 20250612_153854
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

// ReferralContract allows users to generate referral links and track referral fees for minting NFTs.
contract ReferralNFT is ERC721Enumerable, Ownable {
    // Referral struct to store referral details
    struct Referral {
        address user;
        uint256 totalEarnings;
        uint256 referredCount;
    }

    // Mapping from referral link to Referral struct
    mapping(string => Referral) public referrals;
    // Mapping from wallet address to referral link
    mapping(address => string) public walletReferrals;

    // Event emitted when a new referral is created
    event ReferralCreated(string referralLink, address user);
    // Event emitted when a referral fee is paid
    event ReferralFeePaid(string referralLink, address user, uint256 amount);

    // NFT minting fee
    uint256 public mintingFee = 0.01 ether;

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("ReferralNFT", "rNFT") {}

    // Function to create a referral link
    function createReferral(string memory referralLink) external {
        require(referrals[referralLink].user == address(0), "Referral link already exists.");
        referrals[referralLink] = Referral({
            user: msg.sender,
            totalEarnings: 0,
            referredCount: 0
        });
        walletReferrals[msg.sender] = referralLink;

        emit ReferralCreated(referralLink, msg.sender);
    }

    // Function to mint an NFT and pay referral fees
    function mintNFT(string memory referralLink) external payable {
        require(msg.value >= mintingFee, "Insufficient payment for minting.");
        require(referrals[referralLink].user != address(0), "Invalid referral link.");

        // Mint the NFT to the sender
        uint256 tokenId = totalSupply() + 1;
        _mint(msg.sender, tokenId);

        // Update referral earnings
        referrals[referralLink].totalEarnings += msg.value;
        referrals[referralLink].referredCount += 1;

        // Pay the referral fee to the referrer (10% of minting fee)
        uint256 referralFee = (msg.value * 10) / 100;
        payable(referrals[referralLink].user).transfer(referralFee);

        emit ReferralFeePaid(referralLink, referrals[referralLink].user, referralFee);
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw.");
        payable(owner()).transfer(balance);
    }

    // Function to set the minting fee (only owner)
    function setMintingFee(uint256 newFee) external onlyOwner {
        mintingFee = newFee;
    }

    // Function to fetch referral data
    function getReferralData(string memory referralLink) external view returns (Referral memory) {
        return referrals[referralLink];
    }
}
```
