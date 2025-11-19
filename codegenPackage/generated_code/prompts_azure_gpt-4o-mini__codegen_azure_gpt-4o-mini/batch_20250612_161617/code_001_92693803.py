"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.pages.dev
Prompt: How can I implement a referral bonus system for ERC721 NFT holders in a project like God Candle?
Generated: DETERMINISTIC_92693803c31b5647
Batch ID: 20250612_161617
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ReferralBonus is Ownable {
    using SafeMath for uint256;

    // Mapping to track referral bonuses for each address
    mapping(address => uint256) public referralBonuses;

    // Mapping to track if an address has already referred someone
    mapping(address => bool) public hasReferred;

    // The ERC721 token contract
    IERC721 public nftContract;

    // Event emitted when a referral bonus is claimed
    event ReferralBonusClaimed(address indexed referrer, uint256 amount);

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    // Function to set a referral bonus for a specific referrer
    function setReferralBonus(address referrer, uint256 amount) external onlyOwner {
        require(referrer != address(0), "Invalid referrer address");
        require(amount > 0, "Bonus amount must be greater than zero");
        referralBonuses[referrer] = amount;
    }

    // Function to refer a new user
    function refer(address newUser) external {
        require(newUser != address(0), "Invalid new user address");
        require(!hasReferred[newUser], "User has already been referred");

        // Check if the caller holds an NFT
        require(nftContract.balanceOf(msg.sender) > 0, "Caller must hold an NFT");

        // Mark the new user as referred
        hasReferred[newUser] = true;

        // Transfer the referral bonus to the referrer
        uint256 bonus = referralBonuses[msg.sender];
        require(bonus > 0, "No referral bonus set for this referrer");

        // Transfer the bonus (assuming the contract has enough balance)
        payable(msg.sender).transfer(bonus);

        emit ReferralBonusClaimed(msg.sender, bonus);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient balance");

        payable(owner()).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
