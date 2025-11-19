"""
Generated Code Metadata:
========================
Original URL: https://chestme.com
Prompt: "Design a smart contract function in Solidity that handles the distribution of $ME tokens in exchange for NFT vouchers."
Generated: DETERMINISTIC_4ebe966e1bd0634e
Batch ID: 20250622_211123
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

// Importing the ERC20 interface for the $ME token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the NFT voucher
interface INFTVoucher {
    function isValidVoucher(address user) external view returns (bool);
}

contract TokenDistributor {
    // State variables
    IERC20 public meToken; // The $ME token contract
    INFTVoucher public nftVoucher; // The NFT voucher contract

    // Event to log the distribution of tokens
    event TokensDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token and voucher addresses
    constructor(address _meToken, address _nftVoucher) {
        require(_meToken != address(0), "Invalid $ME token address");
        require(_nftVoucher != address(0), "Invalid NFT voucher address");
        
        meToken = IERC20(_meToken);
        nftVoucher = INFTVoucher(_nftVoucher);
    }

    // Function to distribute $ME tokens in exchange for NFT vouchers
    function distributeTokens(uint256 amount) external {
        // Check if the user has a valid NFT voucher
        require(nftVoucher.isValidVoucher(msg.sender), "Invalid NFT voucher");

        // Check if the contract has enough $ME tokens to distribute
        require(meToken.balanceOf(address(this)) >= amount, "Insufficient $ME tokens in contract");

        // Transfer $ME tokens to the user
        bool success = meToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit an event for the distribution
        emit TokensDistributed(msg.sender, amount);
    }

    // Function to withdraw any remaining $ME tokens from the contract
    function withdrawTokens(uint256 amount) external {
        // Only the contract owner can withdraw tokens
        require(msg.sender == address(this), "Only contract owner can withdraw");

        // Check if the contract has enough tokens to withdraw
        require(meToken.balanceOf(address(this)) >= amount, "Insufficient $ME tokens in contract");

        // Transfer $ME tokens to the owner
        bool success = meToken.transfer(msg.sender, amount);
        require(success, "Token withdrawal failed");
    }
}
```
