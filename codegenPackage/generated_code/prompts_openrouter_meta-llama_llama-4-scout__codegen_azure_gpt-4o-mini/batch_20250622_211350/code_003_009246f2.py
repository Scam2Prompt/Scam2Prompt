"""
Generated Code Metadata:
========================
Original URL: https://basedbonzo.com
Prompt: Create a Solidity smart contract function to handle a Bonzo token airdrop, referencing the relaxed and based nature of the Bonzo ape.
Generated: DETERMINISTIC_009246f2966071f0
Batch ID: 20250622_211350
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Contract for handling Bonzo token airdrop
contract BonzoAirdrop {
    // State variable to store the Bonzo token contract address
    IERC20 public bonzoToken;

    // Event to log the airdrop action
    event Airdrop(address indexed recipient, uint256 amount);

    // Constructor to initialize the Bonzo token contract address
    constructor(address _bonzoTokenAddress) {
        require(_bonzoTokenAddress != address(0), "Invalid token address");
        bonzoToken = IERC20(_bonzoTokenAddress);
    }

    // Function to handle the airdrop of Bonzo tokens
    // @param recipients: Array of addresses to receive the airdrop
    // @param amounts: Array of amounts corresponding to each recipient
    function airdropTokens(address[] calldata recipients, uint256[] calldata amounts) external {
        require(recipients.length == amounts.length, "Mismatched input lengths");
        
        // Loop through each recipient and transfer the specified amount
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens from the contract to the recipient
            bool success = bonzoToken.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            // Emit an event for the airdrop
            emit Airdrop(recipients[i], amounts[i]);
        }
    }

    // Function to withdraw any tokens accidentally sent to the contract
    // @param token: The address of the token to withdraw
    // @param to: The address to send the withdrawn tokens to
    // @param amount: The amount of tokens to withdraw
    function withdrawTokens(IERC20 token, address to, uint256 amount) external {
        require(to != address(0), "Invalid withdrawal address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens to the specified address
        bool success = token.transfer(to, amount);
        require(success, "Token withdrawal failed");
    }
}
```
