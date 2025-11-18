"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securedchainauth.pages.dev
Prompt: Generate a smart contract to handle airdrop distribution and fix related issues, inspired by the airdrop fixes offered by Secured Chain Auth.
Generated: DETERMINISTIC_e8d7fbaa2afbd71f
Batch ID: 20250612_152600
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

/**
 * @title AirdropContract
 * @dev This contract handles the distribution of airdrops to multiple recipients.
 */
contract AirdropContract is Ownable {
    IERC20 public token; // ERC20 token to be airdropped

    event AirdropDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to set the token contract address.
     * @param _token Address of the ERC20 token contract
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Function to distribute airdrop tokens to multiple recipients.
     * @param recipients Array of addresses to receive the airdrop
     * @param amounts Array of amounts corresponding to each recipient
     */
    function distributeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        require(recipients.length > 0, "No recipients to airdrop");

        for (uint256 i = 0; i < recipients.length; i++) {
            // Validate recipient address
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            emit AirdropDistributed(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to withdraw any remaining tokens from the contract.
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        uint256 balance = token.balanceOf(address(this));
        require(amount <= balance, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token withdrawal failed");
    }

    /**
     * @dev Function to check the contract balance of the token.
     * @return uint256 The balance of the contract in the specified ERC20 token
     */
    function contractBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
