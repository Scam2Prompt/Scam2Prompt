"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blasdflsd.pages.dev
Prompt: Generate a Solidity contract that allows users to participate in the $BLAST Airdrop and manage rewards.
Generated: DETERMINISTIC_689270982e49cdc3
Batch ID: 20250612_160940
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

// Airdrop contract for managing $BLAST token airdrops and rewards
contract BlastAirdrop is Ownable {
    IERC20 public blastToken; // The address of the $BLAST token contract
    uint256 public airdropAmount; // Amount of $BLAST tokens to be distributed in each airdrop

    // Mapping to track participants who have claimed their airdrop
    mapping(address => bool) public hasClaimed;

    // Event to emit when an airdrop is claimed
    event AirdropClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address and airdrop amount
    constructor(IERC20 _blastToken, uint256 _airdropAmount) {
        blastToken = _blastToken;
        airdropAmount = _airdropAmount;
    }

    // Function to allow users to claim their airdrop
    function claimAirdrop() external {
        require(!hasClaimed[msg.sender], "Airdrop already claimed"); // Ensure the user hasn't claimed before
        require(blastToken.balanceOf(address(this)) >= airdropAmount, "Insufficient airdrop funds");

        // Mark the user as having claimed
        hasClaimed[msg.sender] = true;

        // Transfer the airdrop amount to the user
        bool success = blastToken.transfer(msg.sender, airdropAmount);
        require(success, "Transfer failed"); // Ensure the transfer was successful

        // Emit an event for the claimed airdrop
        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    // Function to allow the owner to withdraw remaining tokens from the contract
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingBalance = blastToken.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");

        bool success = blastToken.transfer(msg.sender, remainingBalance);
        require(success, "Withdrawal failed"); // Ensure the withdrawal was successful
    }

    // Function to set a new airdrop amount by the owner
    function setAirdropAmount(uint256 newAmount) external onlyOwner {
        airdropAmount = newAmount;
    }
}
```
