"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tpaswapeth.pages.dev
Prompt: Write a smart contract that interacts with TapSwap's blockchain to facilitate token claims for eligible wallets.
Generated: DETERMINISTIC_89e0a46c3a468d29
Batch ID: 20250612_151100
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

// Importing the necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for TokenClaim
contract TokenClaim is Ownable {
    // Address of the TapSwap token
    IERC20 public tapSwapToken;

    // Mapping to keep track of eligible wallets
    mapping(address => bool) public eligibleWallets;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Constructor to set the TapSwap token address
    constructor(address _tapSwapToken) {
        require(_tapSwapToken != address(0), "Invalid token address");
        tapSwapToken = IERC20(_tapSwapToken);
    }

    // Function to mark a wallet as eligible for token claims
    function markAsEligible(address wallet) external onlyOwner {
        require(wallet != address(0), "Invalid address");
        eligibleWallets[wallet] = true;
    }

    // Function to claim tokens
    function claimTokens(uint256 amount) external {
        require(eligibleWallets[msg.sender], "Not eligible to claim tokens");
        require(amount > 0, "Amount must be greater than zero");
        require(tapSwapToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the claimant
        bool success = tapSwapToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit the token claimed event
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(tapSwapToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = tapSwapToken.transfer(owner(), amount);
        require(success, "Token withdrawal failed");
    }
}
```
