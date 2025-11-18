"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-ico.pages.dev
Prompt: Generate a Solidity contract for distributing AirDrop rewards for $HMSTR tokens, ensuring it supports the largest-ever AirDrop as described in the roadmap.
Generated: DETERMINISTIC_28778c0279336f3d
Batch ID: 20250612_152240
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title Airdrop Contract for $HMSTR Tokens
/// @notice This contract allows the owner to distribute $HMSTR tokens as rewards through an airdrop mechanism
contract HMSTRAirdrop is Ownable {
    // Token to be distributed in the airdrop
    IERC20 public hmstrToken;

    // Event emitted when tokens are successfully airdropped
    event AirdropExecuted(address indexed recipient, uint256 amount);

    /// @notice Constructor to initialize the contract with the $HMSTR token address
    /// @param _hmstrToken Address of the $HMSTR token contract
    constructor(IERC20 _hmstrToken) {
        require(address(_hmstrToken) != address(0), "Invalid token address");
        hmstrToken = _hmstrToken;
    }

    /// @notice Function to distribute airdrop tokens to multiple addresses
    /// @param recipients List of addresses to receive the airdrop
    /// @param amounts List of amounts to airdrop corresponding to each address
    function executeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        
        uint256 totalAmount = 0;

        // Calculate the total amount to be sent to ensure sufficient balance
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount += amounts[i];
        }

        // Ensure the contract has enough tokens for the airdrop
        require(hmstrToken.balanceOf(address(this)) >= totalAmount, "Insufficient token balance in contract");

        // Distributing tokens to each recipient
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            // Ensure recipient is valid
            require(recipient != address(0), "Invalid recipient address");

            // Transfer the tokens to the recipient
            require(hmstrToken.transfer(recipient, amount), "Token transfer failed");

            // Emit event for each successful airdrop
            emit AirdropExecuted(recipient, amount);
        }
    }

    /// @notice Function to withdraw any tokens accidentally sent to the contract
    /// @param token Address of the token to withdraw
    /// @param amount Amount of the token to withdraw
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance to withdraw");

        // Transfer the tokens to the owner's address
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }

    /// @notice Function to view the balance of the contract for a specific token
    /// @param token Address of the token to check the balance
    /// @return uint256 The balance of the token in the contract
    function getTokenBalance(IERC20 token) external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
