"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoin-dr-manager-bz23c2f5n-bootnode.vercel.app
Prompt: Create a smart contract in Solidity to interact with Gitcoin's Round Manager for distributing funds to multiple recipients based on predefined criteria.
Generated: DETERMINISTIC_df8c85ecca9fd55a
Batch ID: 20250612_154908
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

// Importing necessary interfaces for interacting with Gitcoin's Round Manager
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for distributing funds on Gitcoin platform
contract GitcoinFundDistributor is Ownable {
    // State variable to store the ERC20 token used for distributions
    IERC20 public token;

    // Struct to represent a recipient's details
    struct Recipient {
        address payable wallet; // Wallet address of the recipient
        uint256 amount; // Amount to be distributed
    }

    // Array to hold recipients
    Recipient[] public recipients;

    // Event to log fund distribution
    event FundsDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to add a recipient
    function addRecipient(address payable _wallet, uint256 _amount) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        require(_amount > 0, "Amount must be greater than zero");
        
        recipients.push(Recipient({
            wallet: _wallet,
            amount: _amount
        }));
    }

    // Function to remove a recipient by index
    function removeRecipient(uint256 index) external onlyOwner {
        require(index < recipients.length, "Index out of bounds");
        recipients[index] = recipients[recipients.length - 1]; // Replace with the last entry
        recipients.pop(); // Remove the last entry
    }

    // Function to distribute funds to all recipients
    function distributeFunds() external onlyOwner {
        uint256 totalAmount = 0;

        // Calculate total amount needed for distribution
        for (uint256 i = 0; i < recipients.length; i++) {
            totalAmount += recipients[i].amount;
        }

        // Check if contract has sufficient balance
        require(token.balanceOf(address(this)) >= totalAmount, "Insufficient contract balance");
        
        // Transfer funds to each recipient
        for (uint256 i = 0; i < recipients.length; i++) {
            require(token.transfer(recipients[i].wallet, recipients[i].amount), "Fund transfer failed");
            emit FundsDistributed(recipients[i].wallet, recipients[i].amount); // Emit event for each transfer
        }
    }

    // Function to withdraw remaining tokens from the contract
    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        require(token.transfer(owner(), balance), "Withdrawal failed");
    }

    // Function to view the number of recipients
    function recipientCount() external view returns (uint256) {
        return recipients.length;
    }
}
```
