"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin.eu
Prompt: Create a smart contract template compatible with the Toncoin blockchain for token transfers.
Generated: DETERMINISTIC_15d2cfdc3f0b1431
Batch ID: 20250612_153915
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

// Importing the required libraries for Toncoin
import "@tonlabs/ton-core/contracts/interfaces/ITON.sol";
import "@tonlabs/ton-core/contracts/interfaces/ITONToken.sol";

/// @title Toncoin Token Transfer Smart Contract
/// @notice This contract allows users to transfer Toncoin tokens
contract ToncoinTokenTransfer {
    // State variable to hold the address of the token contract
    ITONToken public token;

    // Event to log token transfers
    event TokensTransferred(address indexed sender, address indexed receiver, uint256 amount);

    /// @notice Constructor to initialize the token contract
    /// @param _tokenAddress The address of the Toncoin token contract
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = ITONToken(_tokenAddress);
    }

    /// @notice Transfers a specified amount of tokens from the sender to the receiver
    /// @param _receiver The address of the receiver
    /// @param _amount The amount of tokens to transfer
    /// @dev This function handles the token transfer and emits an event upon success
    function transferTokens(address _receiver, uint256 _amount) external {
        require(_receiver != address(0), "Receiver address cannot be zero");
        require(_amount > 0, "Transfer amount must be greater than zero");

        // Call the transfer function of the token contract
        bool success = token.transferFrom(msg.sender, _receiver, _amount);
        require(success, "Token transfer failed");

        // Emit the event for the transfer
        emit TokensTransferred(msg.sender, _receiver, _amount);
    }

    /// @notice Allows the sender to approve the token transfer
    /// @param _spender The address of the spender
    /// @param _amount The amount of tokens to approve
    function approveTokens(address _spender, uint256 _amount) external {
        require(_spender != address(0), "Spender address cannot be zero");
        require(_amount > 0, "Approval amount must be greater than zero");

        // Approve the spender to spend the specified amount of tokens
        bool success = token.approve(_spender, _amount);
        require(success, "Token approval failed");
    }
}
```
