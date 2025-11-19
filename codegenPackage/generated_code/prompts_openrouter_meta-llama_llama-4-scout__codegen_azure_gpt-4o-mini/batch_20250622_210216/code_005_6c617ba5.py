"""
Generated Code Metadata:
========================
Original URL: https://smogstoken.web.app
Prompt: Create a Solidity or Rust smart contract snippet for a basic airdrop distribution system similar to Smog Token's, focusing on security and fairness.
Generated: DETERMINISTIC_6c617ba5fa557345
Batch ID: 20250622_210216
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Airdrop
 * @dev A contract for distributing ERC20 tokens to multiple addresses
 */
contract Airdrop is Ownable {
    IERC20 public token; // The ERC20 token to be distributed

    event AirdropExecuted(address indexed recipient, uint256 amount);

    /**
     * @dev Sets the token to be used for the airdrop
     * @param _token The address of the ERC20 token contract
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Distributes tokens to a list of addresses
     * @param recipients The list of addresses to receive tokens
     * @param amounts The corresponding amounts of tokens to distribute
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit AirdropExecuted(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Allows the owner to withdraw any tokens sent to the contract
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = token.transfer(owner(), amount);
        require(success, "Token withdrawal failed");
    }
}
```
