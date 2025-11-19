"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.nfts2.me
Prompt: How can I implement a referral system for an NFT minting platform using Arbitrum that allows users to earn ETH for each mint through their referral link?
Generated: DETERMINISTIC_20277718ad1836d7
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTMintingWithReferral is ERC721, Ownable {
    using SafeMath for uint256;

    // Referral commission rate (e.g., 0.01 ETH = 10000000000000000 wei)
    uint256 public referralCommission = 0.01 ether;

    // Tracking referrals
    mapping(address => address) public referrals;
    mapping(address => uint256) public referralEarnings;

    // NFT minting price
    uint256 public mintPrice = 0.05 ether;

    // Counter for NFT tokens
    uint256 public tokenCounter;

    // Events for tracking
    event Minted(address indexed minter, uint256 tokenId, address indexed referrer);
    event ReferralEarningsPaid(address indexed referrer, uint256 amount);

    constructor() ERC721("NFTMintingWithReferral", "NFTMR") {
        tokenCounter = 0;
    }

    /**
     * @dev Mint a new NFT with an optional referral address.
     * @param referrer The address of the referrer if any.
     */
    function mintNFT(address referrer) external payable {
        require(msg.value >= mintPrice, "Insufficient ETH sent.");
        
        // If a valid referrer is provided and it's not the caller's address
        if (referrer != address(0) && referrer != msg.sender) {
            // Store the referrer if not already set
            if (referrals[msg.sender] == address(0)) {
                referrals[msg.sender] = referrer;
            }
        }

        // Mint the NFT
        uint256 newTokenId = tokenCounter;
        _mint(msg.sender, newTokenId);
        tokenCounter++;

        // Pay the referrer if applicable
        if (referrals[msg.sender] != address(0)) {
            referralEarnings[referrals[msg.sender]] = referralEarnings[referrals[msg.sender]].add(referralCommission);
            emit Minted(msg.sender, newTokenId, referrals[msg.sender]);
        } else {
            emit Minted(msg.sender, newTokenId, address(0));
        }
    }

    /**
     * @dev Withdraw referral earnings for the referrer.
     */
    function withdrawEarnings() external {
        uint256 earnings = referralEarnings[msg.sender];
        require(earnings > 0, "No earnings to withdraw.");

        // Reset earnings to zero before transfer to prevent re-entrancy attacks
        referralEarnings[msg.sender] = 0;

        // Transfer the earnings to the referrer
        (bool success, ) = msg.sender.call{value: earnings}("");
        require(success, "Transfer failed.");

        emit ReferralEarningsPaid(msg.sender, earnings);
    }

    /**
     * @dev Set the mint price.
     * @param newPrice The new mint price in wei.
     */
    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
    }

    /**
     * @dev Set referral commission.
     * @param newCommission The new referral commission in wei.
     */
    function setReferralCommission(uint256 newCommission) external onlyOwner {
        referralCommission = newCommission;
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}
}
```
