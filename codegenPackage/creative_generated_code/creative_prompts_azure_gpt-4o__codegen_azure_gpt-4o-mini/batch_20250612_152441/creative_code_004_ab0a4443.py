"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signetfaucet1.pages.dev
Prompt: Write a smart contract function that interacts with the Signet Faucet to claim funds securely and verify the transaction.
Generated: DETERMINISTIC_ab0a44438b2949a4
Batch ID: 20250612_152441
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SignetFaucet is Ownable {
    // Address of the Signet Faucet token
    IERC20 public token;

    // Event emitted when funds are claimed
    event FundsClaimed(address indexed claimant, uint256 amount);

    // Error for insufficient balance
    error InsufficientBalance(uint256 requested, uint256 available);

    // Constructor to initialize the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to claim funds from the faucet
    function claimFunds(uint256 amount) external {
        // Ensure the amount requested is greater than zero
        require(amount > 0, "Amount must be greater than zero");

        // Check the contract's balance to ensure it has enough funds
        uint256 availableBalance = token.balanceOf(address(this));
        if (amount > availableBalance) {
            revert InsufficientBalance(amount, availableBalance);
        }

        // Transfer the requested amount of tokens to the claimant
        bool success = token.transfer(msg.sender, amount);
        require(success, "Transfer failed");

        // Emit an event for the claimed funds
        emit FundsClaimed(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract (owner only)
    function withdrawTokens(uint256 amount) external onlyOwner {
        uint256 contractBalance = token.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = token.transfer(msg.sender, amount);
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept ETH (if needed for future use)
    receive() external payable {}
}
```
