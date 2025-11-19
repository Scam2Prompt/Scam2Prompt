"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.nfts2.me
Prompt: Can you provide an example of how to track referral earnings for mints made through a referral link in an Arbitrum-based NFT project?
Generated: DETERMINISTIC_390bbbed7bab317f
Batch ID: 20250612_140414
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

// ReferralNFT is an ERC721 token that tracks referral earnings.
contract ReferralNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Token ID counter
    mapping(address => uint256) public referralEarnings; // Track earnings per referrer
    mapping(uint256 => address) public tokenReferral; // Mapping of token ID to referrer address
    uint256 public constant REFERRAL_REWARD = 0.01 ether; // Fixed reward for each referred mint

    // Events
    event Minted(uint256 indexed tokenId, address indexed owner, address indexed referrer);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("ReferralNFT", "rNFT") {}

    // Function to mint a new NFT with a referral link
    function mintNFT(address referrer) external payable {
        require(msg.value == REFERRAL_REWARD, "Incorrect Ether sent"); // Require correct payment
        require(referrer != address(0), "Invalid referrer address"); // Ensure referrer is valid

        _tokenIdCounter.increment(); // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current(); // Get the new token ID

        // Mint the NFT to the caller
        _safeMint(msg.sender, tokenId);

        // Track the referral
        tokenReferral[tokenId] = referrer; 
        referralEarnings[referrer] += REFERRAL_REWARD; // Update referrer earnings

        // Emit an event for the mint action
        emit Minted(tokenId, msg.sender, referrer);
    }

    // Function to withdraw referral earnings
    function withdrawEarnings() external {
        uint256 earnings = referralEarnings[msg.sender]; // Get earnings for the caller
        require(earnings > 0, "No earnings to withdraw"); // Check for positive earnings

        referralEarnings[msg.sender] = 0; // Reset earnings to prevent re-entrancy attacks
        payable(msg.sender).transfer(earnings); // Transfer earnings to the caller
    }

    // Function to get the referral earnings of a specific address
    function getReferralEarnings(address referrer) external view returns (uint256) {
        return referralEarnings[referrer];
    }

    // Function to get the referrer of a specific token ID
    function getTokenReferrer(uint256 tokenId) external view returns (address) {
        return tokenReferral[tokenId];
    }
}
```
