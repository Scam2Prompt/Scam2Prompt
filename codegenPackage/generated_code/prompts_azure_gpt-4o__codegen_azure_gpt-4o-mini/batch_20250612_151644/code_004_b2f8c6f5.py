"""
Generated Code Metadata:
========================
Original URL: https://cknft.pages.dev
Prompt: Write a smart contract in Solidity to manage airdrops for NFT holders, ensuring eligibility for benefits like discounts, physical product claims, and WL spots as described in the Blvck Genesis membership phase.
Generated: DETERMINISTIC_b2f8c6f5387e3046
Batch ID: 20250612_151644
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

/**
 * @title AirdropManager
 * @dev Smart contract to manage airdrops for NFT holders
 */
contract AirdropManager is Ownable {
    // Mapping to track eligible addresses for airdrops
    mapping(address => bool) public eligibleAddresses;

    // Event emitted when an address is marked as eligible
    event AddressMarkedEligible(address indexed user);
    
    // Event emitted when an airdrop is claimed
    event AirdropClaimed(address indexed user, uint256 amount);

    // Reference to the NFT contract
    IERC721 public nftContract;

    // Airdrop amount for each eligible address
    uint256 public airdropAmount;

    // Constructor to initialize the NFT contract and airdrop amount
    constructor(IERC721 _nftContract, uint256 _airdropAmount) {
        nftContract = _nftContract;
        airdropAmount = _airdropAmount;
    }

    /**
     * @dev Marks an address as eligible for airdrop if they hold the NFT
     * @param user The address to mark as eligible
     */
    function markEligible(address user) external onlyOwner {
        require(nftContract.balanceOf(user) > 0, "User does not hold the NFT");
        eligibleAddresses[user] = true;
        emit AddressMarkedEligible(user);
    }

    /**
     * @dev Allows eligible addresses to claim their airdrop
     */
    function claimAirdrop() external {
        require(eligibleAddresses[msg.sender], "Not eligible for airdrop");
        
        // Reset eligibility to prevent double claiming
        eligibleAddresses[msg.sender] = false;

        // Transfer the airdrop amount to the user
        // Assuming the contract has enough balance to transfer
        (bool success, ) = msg.sender.call{value: airdropAmount}("");
        require(success, "Transfer failed");

        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    /**
     * @dev Allows the owner to withdraw any Ether from the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}
}
```
