"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notrop.com
Prompt: How can I implement a smart contract to manage token airdrops like the Notcoin Airdrop?
Generated: DETERMINISTIC_35b648d3b60c9190
Batch ID: 20250612_162813
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

/// @title Airdrop Contract
/// @notice This contract manages token airdrops for a specific ERC20 token
contract Airdrop is Ownable {
    IERC20 public token; // The ERC20 token to be airdropped

    /// @param _token The address of the ERC20 token to be used for the airdrop
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    /// @notice Airdrop tokens to multiple recipients
    /// @param recipients List of addresses to receive the tokens
    /// @param amounts List of amounts to be sent to each recipient
    function airdropTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");
        require(recipients.length > 0, "No recipients provided");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens from the contract to the recipient
            bool success = token.transfer(recipients[i], amounts[i]);
            require(success, "Token transfer failed");
        }
    }

    /// @notice Allows the owner to withdraw any ERC20 tokens left in the contract
    /// @param _token Address of the token to withdraw
    /// @param amount Amount of the token to withdraw
    function withdrawTokens(IERC20 _token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(_token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        bool success = _token.transfer(owner(), amount);
        require(success, "Token withdrawal failed");
    }

    /// @notice Get the balance of the contract for the specific ERC20 token
    /// @return balance Contract's token balance
    function getTokenBalance() external view returns (uint256 balance) {
        return token.balanceOf(address(this));
    }
}
```
