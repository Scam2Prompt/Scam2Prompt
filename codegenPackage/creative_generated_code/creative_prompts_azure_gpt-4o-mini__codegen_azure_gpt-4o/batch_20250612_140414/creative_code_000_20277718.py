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

/**
 * @title NFTMintWithReferral
 * @dev This contract implements an NFT minting platform with a referral system on Arbitrum.
 * Users can earn ETH rewards for each successful mint through their referral link.
 */
contract NFTMintWithReferral {
    // Events
    event NFTMinted(address indexed minter, uint256 tokenId, address indexed referrer);
    event ReferralPaid(address indexed referrer, uint256 amount);

    // State variables
    uint256 public mintPrice = 0.05 ether;               // Price to mint one NFT
    uint256 public referralReward = 0.01 ether;          // Reward for the referrer
    uint256 public nextTokenId = 1;                      // Tracks the next token ID
    address public owner;                                // Contract owner
    mapping(uint256 => address) public tokenOwners;      // Mapping of token IDs to their owners

    // Modifier to restrict access to the owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the deployer as the contract owner
    }

    /**
     * @dev Allows users to mint an NFT. Optionally accepts a referrer address.
     * @param referrer The address of the referrer (optional, can be zero address).
     */
    function mintNFT(address referrer) external payable {
        require(msg.value == mintPrice, "Incorrect ETH amount sent");

        // Assign the new NFT to the minter
        uint256 tokenId = nextTokenId;
        tokenOwners[tokenId] = msg.sender;
        nextTokenId++;

        emit NFTMinted(msg.sender, tokenId, referrer);

        // Pay the referral reward if the referrer is valid
        if (referrer != address(0) && referrer != msg.sender) {
            (bool success, ) = referrer.call{value: referralReward}("");
            if (success) {
                emit ReferralPaid(referrer, referralReward);
            }
        }

        // Send remaining funds to contract owner
        uint256 ownerAmount = msg.value - referralReward;
        (bool ownerTransferSuccess, ) = owner.call{value: ownerAmount}("");
        require(ownerTransferSuccess, "Failed to transfer funds to owner");
    }

    /**
     * @dev Allows the owner to withdraw the contract's balance.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Allows the owner to set a new mint price.
     * @param newPrice The new mint price in wei.
     */
    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
    }

    /**
     * @dev Allows the owner to set a new referral reward.
     * @param newReward The new referral reward in wei.
     */
    function setReferralReward(uint256 newReward) external onlyOwner {
        referralReward = newReward;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers directly to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
