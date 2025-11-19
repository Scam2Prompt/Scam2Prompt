"""
Generated Code Metadata:
========================
Original URL: https://peipeicoins-ai.firebaseapp.com
Prompt: Create a smart contract in Solidity for airdropping $PEIPEI tokens to multiple wallet addresses while adhering to the zero-tax policy.
Generated: DETERMINISTIC_dfe79587d1a65023
Batch ID: 20250612_153954
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Airdrop contract for distributing $PEIPEI tokens
contract PEIPEIAirdrop is Ownable {
    // The ERC20 token contract
    IERC20 public peipeiToken;

    // Event to log the airdrop
    event Airdrop(address indexed recipient, uint256 amount);

    // Constructor to set the token address
    constructor(address _peipeiToken) {
        require(_peipeiToken != address(0), "Invalid token address");
        peipeiToken = IERC20(_peipeiToken);
    }

    // Function to airdrop tokens to multiple addresses
    // @param recipients: Array of wallet addresses to receive tokens
    // @param amounts: Array of amounts corresponding to each recipient
    function airdropTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");
        require(recipients.length > 0, "No recipients provided");

        uint256 totalAmount = 0;

        // Calculate total amount to be airdropped
        for (uint256 i = 0; i < amounts.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            totalAmount += amounts[i];
        }

        // Check if the contract has enough tokens for the airdrop
        require(peipeiToken.balanceOf(address(this)) >= totalAmount, "Insufficient token balance in contract");

        // Distributing tokens to each recipient
        for (uint256 i = 0; i < recipients.length; i++) {
            peipeiToken.transfer(recipients[i], amounts[i]);
            emit Airdrop(recipients[i], amounts[i]);
        }
    }

    // Function to withdraw tokens from the contract
    // @param amount: Amount of tokens to withdraw
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(peipeiToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        peipeiToken.transfer(msg.sender, amount);
    }

    // Function to set a new token address (if needed)
    // @param newToken: Address of the new token contract
    function setTokenAddress(address newToken) external onlyOwner {
        require(newToken != address(0), "Invalid token address");
        peipeiToken = IERC20(newToken);
    }
}
```
