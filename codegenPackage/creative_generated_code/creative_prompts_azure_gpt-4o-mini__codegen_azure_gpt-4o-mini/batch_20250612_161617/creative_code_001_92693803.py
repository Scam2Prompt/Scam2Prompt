"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.pages.dev
Prompt: How can I implement a referral bonus system for ERC721 NFT holders in a project like God Candle?
Generated: DETERMINISTIC_92693803c31b5647
Batch ID: 20250612_161617
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ReferralBonus is Ownable {
    // Mapping from NFT holder to their referrer
    mapping(address => address) public referrer;
    // Mapping to track bonuses for each referrer
    mapping(address => uint256) public referralBonus;
    // Base bonus amount for each successful referral
    uint256 public constant BASE_BONUS = 0.1 ether;
    // Reference to the ERC721 contract
    IERC721 public nftContract;

    // Event emitted when a new referral is registered
    event ReferralRegistered(address indexed referrer, address indexed referee);
    // Event emitted when a bonus is claimed
    event BonusClaimed(address indexed referrer, uint256 amount);

    /**
     * @dev Constructor to set the NFT contract address.
     * @param _nftContract Address of the ERC721 contract.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Register a referral.
     * @param _referrer Address of the referrer.
     */
    function registerReferral(address _referrer) external {
        // Ensure the caller is not already registered
        require(referrer[msg.sender] == address(0), "Already registered");
        // Ensure the referrer is a holder of the NFT
        require(nftContract.balanceOf(_referrer) > 0, "Referrer is not an NFT holder");

        // Register the referral
        referrer[msg.sender] = _referrer;
        // Increment the referrer's bonus
        referralBonus[_referrer] += BASE_BONUS;

        emit ReferralRegistered(_referrer, msg.sender);
    }

    /**
     * @dev Claim the referral bonus.
     */
    function claimBonus() external {
        uint256 bonus = referralBonus[msg.sender];
        require(bonus > 0, "No bonus to claim");

        // Reset the bonus after claiming
        referralBonus[msg.sender] = 0;

        // Transfer the bonus to the caller
        (bool success, ) = msg.sender.call{value: bonus}("");
        require(success, "Transfer failed");

        emit BonusClaimed(msg.sender, bonus);
    }

    /**
     * @dev Withdraw contract balance to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer the entire balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
