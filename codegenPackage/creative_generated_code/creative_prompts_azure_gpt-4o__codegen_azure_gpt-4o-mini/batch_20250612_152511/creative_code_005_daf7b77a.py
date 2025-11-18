"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-coln.pages.dev
Prompt: Write a Solidity contract example for an airdrop system where tokens are automatically distributed to wallet addresses after the airdrop ends, similar to the $PORTAL token distribution process.
Generated: DETERMINISTIC_daf7b77a469bc007
Batch ID: 20250612_152511
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AirdropContract
 * @dev A contract for distributing ERC20 tokens to multiple addresses after an airdrop period ends.
 */
contract AirdropContract is Ownable {
    IERC20 public token; // The ERC20 token to be airdropped
    uint256 public airdropEndTime; // The end time of the airdrop
    mapping(address => uint256) public airdropBalances; // Balances of airdrop recipients
    bool public airdropClaimed; // Flag to ensure airdrop can only be claimed once

    event AirdropInitialized(uint256 endTime);
    event TokensClaimed(address indexed recipient, uint256 amount);

    /**
     * @dev Sets the token to be used for the airdrop.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Initializes the airdrop with an end time.
     * @param duration Duration of the airdrop in seconds.
     */
    function initializeAirdrop(uint256 duration) external onlyOwner {
        require(!airdropClaimed, "Airdrop already claimed");
        airdropEndTime = block.timestamp + duration;
        emit AirdropInitialized(airdropEndTime);
    }

    /**
     * @dev Allows the owner to add a recipient and their corresponding amount to the airdrop.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to airdrop to the recipient.
     */
    function addRecipient(address recipient, uint256 amount) external onlyOwner {
        require(block.timestamp < airdropEndTime, "Airdrop has ended");
        require(recipient != address(0), "Recipient cannot be zero address");
        require(amount > 0, "Amount must be greater than zero");
        
        airdropBalances[recipient] += amount;
    }

    /**
     * @dev Claims the airdropped tokens after the end of the airdrop period.
     */
    function claimTokens() external {
        require(block.timestamp >= airdropEndTime, "Airdrop still ongoing");
        require(!airdropClaimed, "Tokens have already been claimed");
        
        uint256 amount = airdropBalances[msg.sender];
        require(amount > 0, "No tokens to claim");

        // Reset the balance to prevent re-entrancy attacks
        airdropBalances[msg.sender] = 0;
        
        // Transfer tokens to the recipient
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw any leftover tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawLeftoverTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
