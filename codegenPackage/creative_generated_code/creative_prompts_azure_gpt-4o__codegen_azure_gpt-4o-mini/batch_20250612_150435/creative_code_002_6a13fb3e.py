"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ustddiststage.pages.dev
Prompt: Provide a step-by-step implementation in Solidity for a smart contract that handles FCFS token distribution similar to the $USDC airdrop described on the webpage.
Generated: DETERMINISTIC_6a13fb3e01a93ec5
Batch ID: 20250612_150435
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// FCFS Airdrop contract
contract FCFSDistribution is Ownable {
    // Token being distributed
    IERC20 public token;

    // Mapping to track claimed addresses
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are distributed
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Constructor to set the token address
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Invalid token address");
        token = IERC20(tokenAddress);
    }

    // Function to claim tokens
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Not enough tokens in contract");

        // Mark the address as having claimed
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the claimant
        token.transfer(msg.sender, amount);

        // Emit event for tracking
        emit TokensClaimed(msg.sender, amount);
    }

    // Function for the owner to withdraw remaining tokens
    function withdrawRemainingTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer tokens to the owner
        token.transfer(owner(), balance);
    }

    // Function to check if an address has claimed tokens
    function hasClaimedTokens(address claimant) external view returns (bool) {
        return hasClaimed[claimant];
    }
}
```
